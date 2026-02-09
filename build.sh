#!/bin/bash

# 多模块构建脚本

mkdir -p output/dist
export LC_ALL="en_US.UTF-8"

# Detect Python
PYTHON=python
[ -f /home/cmc/opt/pyenv/versions/2.7.14/bin/python2.7 ] && PYTHON=/home/cmc/opt/pyenv/versions/2.7.14/bin/python2.7

echo "Using Python: $PYTHON"
$PYTHON --version || true
echo ""

#######################################
# Load modules
#######################################

MODULES=()
# 自动扫描目录
echo "Auto-scanning for modules..."
# 自动扫描当前目录下所有符合命名规范的模块
for dir in baiducloud-python-sdk-*; do
    if [ -d "$dir" ] && [ -f "$dir/setup.py" ]; then
        MODULES+=("$dir")
        echo "  Found module: $dir"
    fi
done

# 如果没有找到模块，提示错误
if [ ${#MODULES[@]} -eq 0 ]; then
    echo "Error: No modules found matching pattern 'baiducloud-python-sdk-*'"
    echo "Please ensure:"
    echo "  1. Module directories exist"
    echo "  2. Each has a setup.py file"
    echo "  3. Names follow pattern: baiducloud-python-sdk-<service>"
    exit 1
fi

echo ""
echo "Total modules loaded: ${#MODULES[@]}"
for m in "${MODULES[@]}"; do 
    echo "  - $m"
done
echo ""

# 如果指定了参数，只构建指定模块
if [ -n "$1" ]; then
    if [[ " ${MODULES[@]} " =~ " $1 " ]]; then
        MODULES=("$1")
        echo "Building only: $1"
    else
        echo "Error: Module '$1' not found in discovered modules"
        exit 1
    fi
fi

echo "Modules to build: ${#MODULES[@]}"
for m in "${MODULES[@]}"; do echo "  - $m"; done
echo ""

SUCCESS=0
FAILED=0

#######################################
# Build each module
#######################################

for MODULE in "${MODULES[@]}"; do
    echo "========================================="
    echo "Building: $MODULE"
    echo "========================================="
    
    [ ! -d "$MODULE" ] && echo "✗ Directory not found" && FAILED=$((FAILED+1)) && continue
    [ ! -f "$MODULE/setup.py" ] && echo "✗ setup.py not found" && FAILED=$((FAILED+1)) && continue
    
    # 自动检测包名和版本
    PKG="${MODULE//-/_}"
    INIT="$MODULE/$PKG/__init__.py"
    [ ! -f "$INIT" ] && PKG="${MODULE#baiducloud-python-sdk-}" && PKG="${PKG//-/_}" && INIT="$MODULE/$PKG/__init__.py"
    [ ! -f "$INIT" ] && echo "✗ __init__.py not found" && FAILED=$((FAILED+1)) && continue
    
    VERSION=$(awk -F"'" '$1 ~ /SDK_VERSION/ {print $2}' "$INIT")
    [ -z "$VERSION" ] && echo "✗ Cannot read version" && FAILED=$((FAILED+1)) && continue
    
    echo "Version: $VERSION"
    TARGET="${MODULE}-${VERSION}"
    
    # 清理
    rm -rf "$TARGET" "$MODULE/dist" "$MODULE/build" "$MODULE"/*.egg-info
    
    # 创建源码包
    mkdir -p "$TARGET"
    cp -rf "$MODULE"/* "$TARGET"/
    zip -r "${TARGET}.zip" "$TARGET" -x "*.pyc" "*.pyo" "*__pycache__*" "*/\.*" > /dev/null
    cp "${TARGET}.zip" output/
    
    # 构建
    cd "$MODULE"
    
    # 检查 setuptools 是否可用
    if ! $PYTHON -c "import setuptools" 2>/dev/null; then
        echo "✗ setuptools not available"
        cd ..
        rm -rf "$TARGET"
        FAILED=$((FAILED+1))
        echo ""
        continue
    fi
    
    # 构建 wheel，显示错误输出
    echo "Building wheel..."
    if ! $PYTHON setup.py bdist_wheel --universal 2>&1 | tail -20; then
        echo "✗ Wheel build failed"
        cd ..
        rm -rf "$TARGET"
        FAILED=$((FAILED+1))
        echo ""
        continue
    fi
    
    # 构建 sdist，显示错误输出
    echo "Building sdist..."
    if ! $PYTHON setup.py sdist 2>&1 | tail -20; then
        echo "✗ Sdist build failed"
        cd ..
        rm -rf "$TARGET"
        FAILED=$((FAILED+1))
        echo ""
        continue
    fi
    
    cd ..
    
    # 检查并移动构建产物
    if [ -d "$MODULE/dist" ]; then
        DIST_FILES=$(ls "$MODULE/dist" 2>/dev/null | wc -l)
        if [ "$DIST_FILES" -gt 0 ]; then
            echo "Moving $DIST_FILES file(s) to output/dist/..."
            mv -v "$MODULE/dist"/* output/dist/
            echo "✓ Files moved successfully"
        else
            echo "⚠️  Warning: dist directory is empty"
        fi
    else
        echo "⚠️  Warning: dist directory not found"
    fi
    
    rm -rf "$TARGET"
    echo "✓ Success"
    SUCCESS=$((SUCCESS+1))
    echo ""
done

#######################################
# Summary
#######################################

echo "========================================="
echo "Summary: ✓ $SUCCESS  ✗ $FAILED"
echo "========================================="
ls -lh output/*.zip 2>/dev/null || true
echo ""
ls -lh output/dist/ 2>/dev/null || true
echo "========================================="

[ $FAILED -eq 0 ] && exit 0 || exit 1