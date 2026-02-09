# 百度智能云 Python SDK 使用文档

## 概述

百度智能云 Python SDK 为开发者提供了便捷的方式来访问百度智能云的各项服务。本 SDK 基于百度智能云 API 构建，支持 Python 2.7 及 Python 3.x 版本。

## 安装

### 使用 pip 安装

推荐使用 pip 安装 SDK：

```bash
pip install baiducloud-python-sdk-core
pip install baiducloud-python-sdk-vpc
```

### 从源码安装

你也可以从源码安装：

```bash
git clone https://github.com/baidubce/baiducloud-python-sdk.git
cd baiducloud-python-sdk/baiducloud-python-sdk-core
python setup.py install

cd ../baiducloud-python-sdk-vpc
python setup.py install
```

### 依赖要求

- Python >= 2.7 或 Python >= 3.4
- requests >= 2.20.0

## 快速开始

### 1. 获取 Access Key

在使用 SDK 之前，你需要先获取百度智能云的 Access Key ID 和 Secret Access Key。

访问 [百度智能云控制台](https://console.bce.baidu.com) 获取 AKSK，详见：https://cloud.baidu.com/doc/Reference/s/9jwvz2egb

### 2. 创建客户端

首先需要配置客户端凭证和创建服务客户端：

```python
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_vpc.api.vpc_client import VpcClient

# 配置 Access Key
access_key_id = "your-access-key-id"
secret_access_key = "your-secret-access-key"
endpoint = "bcc.bj.baidubce.com"

# 创建配置对象
config = BceClientConfiguration(
    credentials=BceCredentials(access_key_id, secret_access_key),
    endpoint=endpoint
)

# 创建 VPC 客户端
vpc_client = VpcClient(config)
```

### 3. 调用服务接口

#### 创建 VPC

```python
from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_vpc.models.create_vpc_request import CreateVpcRequest
from baiducloud_python_sdk_vpc.models.tag_model import TagModel

try:
    # 构建创建 VPC 请求
    request = CreateVpcRequest(
        name="my-vpc",
        cidr="192.168.0.0/16",
        description="My VPC for testing",
        enable_ipv6=False,
        tags=[
            TagModel(tag_key="project", tag_value="test"),
            TagModel(tag_key="env", tag_value="dev")
        ]
    )
    
    # 调用创建 VPC 接口
    response = vpc_client.create_vpc(request)
    print(response.to_json_string())
    
except exception.BceHttpClientError as e:
    print(f"Error: {e.last_error}")
    print(f"Request ID: {e.request_id}")
    print(f"Error Code: {e.code}")
```

## 配置说明

### BceClientConfiguration

`BceClientConfiguration` 是客户端配置类，支持以下配置项：

```python
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials

config = BceClientConfiguration(
    credentials=BceCredentials(access_key_id, secret_access_key),
    endpoint="bcc.bj.baidubce.com",          # 服务端点
    protocol="http",                          # 协议：http 或 https，默认 http
    region="bj",                              # 区域，默认 bj（北京）
    connection_timeout_in_mills=10000,        # 连接超时时间（毫秒），默认 10000
    send_buf_size=1048576,                    # 发送缓冲区大小，默认 1MB
    recv_buf_size=10485760                    # 接收缓冲区大小，默认 10MB
)
```

### 凭证配置

SDK 支持多种凭证配置方式：

#### 1. 使用 Access Key

```python
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials

credentials = BceCredentials(
    access_key_id="your-access-key-id",
    secret_access_key="your-secret-access-key"
)
```

#### 2. 使用 STS Token（临时凭证）

```python
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials

credentials = BceCredentials(
    access_key_id="your-access-key-id",
    secret_access_key="your-secret-access-key",
    security_token="your-sts-token"
)
```

### 端点（Endpoint）配置

不同服务和不同地域有不同的端点，常用端点如下：

| 服务 | 地域 | 端点 |
|------|------|------|
| VPC  | 北京 | bcc.bj.baidubce.com |
| VPC  | 广州 | bcc.gz.baidubce.com |
| VPC  | 苏州 | bcc.su.baidubce.com |

更多端点信息请参考：https://cloud.baidu.com/doc/Reference/s/2jwvz23xx

### 重试策略

SDK 支持配置重试策略：

```python
from baiducloud_python_sdk_core.retry_policy import BackOffRetryPolicy

config = BceClientConfiguration(
    credentials=credentials,
    endpoint=endpoint
)

# 设置重试策略
config.retry_policy = BackOffRetryPolicy(
    max_error_retry=3,           # 最大重试次数
    max_delay_in_millis=20000    # 最大延迟时间（毫秒）
)
```

## 错误处理

SDK 使用异常机制处理错误，所有异常都继承自 `BceHttpClientError`。

### 异常类型

- `BceHttpClientError`: HTTP 客户端错误基类
- `BceServerError`: 服务端错误（HTTP 5xx）
- `BceClientError`: 客户端错误（HTTP 4xx）

### 异常属性

- `last_error`: 错误详细信息
- `request_id`: 请求 ID，用于问题追踪
- `code`: 错误代码
- `message`: 错误消息
- `status_code`: HTTP 状态码

### 错误处理示例

```python
from baiducloud_python_sdk_core import exception

try:
    response = vpc_client.create_vpc(request)
    print(response.to_json_string())
    
except exception.BceServerError as e:
    # 服务端错误（5xx）
    print(f"Server Error: {e.message}")
    print(f"Request ID: {e.request_id}")
    print(f"Status Code: {e.status_code}")
    
except exception.BceClientError as e:
    # 客户端错误（4xx）
    if e.code == "InvalidAccessKeyId":
        print("Access Key ID 无效，请检查配置")
    elif e.code == "SignatureDoesNotMatch":
        print("签名不匹配，请检查 Secret Access Key")
    else:
        print(f"Client Error: {e.message}")
    print(f"Request ID: {e.request_id}")
    
except exception.BceHttpClientError as e:
    # 其他 HTTP 错误
    print(f"HTTP Error: {e.last_error}")
    print(f"Request ID: {e.request_id}")
    print(f"Error Code: {e.code}")
    
except Exception as e:
    # 其他异常
    print(f"Unexpected error: {str(e)}")
```

### 常见错误代码

| 错误代码 | 说明 | 解决方案 |
|---------|------|---------|
| InvalidAccessKeyId | Access Key ID 不存在 | 检查 Access Key ID 是否正确 |
| SignatureDoesNotMatch | 签名不匹配 | 检查 Secret Access Key 是否正确 |
| RequestExpired | 请求已过期 | 检查本地时间是否与服务器时间同步 |
| InvalidHTTPAuthHeader | HTTP 认证头无效 | 检查请求头格式是否正确 |
| Forbidden | 权限不足 | 检查账号是否有相应操作权限 |

## 日志配置

SDK 使用 Python 标准库 `logging` 模块记录日志。

### 配置日志级别

```python
import logging

# 配置根日志记录器
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# 配置 SDK 日志级别
sdk_logger = logging.getLogger('baiducloud_python_sdk')
sdk_logger.setLevel(logging.DEBUG)
```

### 日志级别说明

- `DEBUG`: 详细的调试信息，包括请求/响应内容
- `INFO`: 一般信息，如请求开始/结束
- `WARNING`: 警告信息
- `ERROR`: 错误信息
- `CRITICAL`: 严重错误

### 日志输出到文件

```python
import logging

# 创建文件处理器
file_handler = logging.FileHandler('sdk.log')
file_handler.setLevel(logging.DEBUG)

# 设置日志格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# 添加到 SDK 日志记录器
sdk_logger = logging.getLogger('baiducloud_python_sdk')
sdk_logger.addHandler(file_handler)
```

## 完整示例

以下是一个完整的示例程序，演示如何使用 SDK 创建和查询 VPC：

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_vpc.api.vpc_client import VpcClient
from baiducloud_python_sdk_vpc.models.create_vpc_request import CreateVpcRequest
from baiducloud_python_sdk_vpc.models.query_vpc_list_request import QueryVpcListRequest
from baiducloud_python_sdk_vpc.models.tag_model import TagModel

# 配置日志
logging.basicConfig(level=logging.INFO)

def main():
    # 配置 Access Key
    access_key_id = "your-access-key-id"
    secret_access_key = "your-secret-access-key"
    endpoint = "bcc.bj.baidubce.com"
    
    # 创建配置对象
    config = BceClientConfiguration(
        credentials=BceCredentials(access_key_id, secret_access_key),
        endpoint=endpoint
    )
    
    # 创建 VPC 客户端
    vpc_client = VpcClient(config)
    
    try:
        # 1. 创建 VPC
        print("创建 VPC...")
        create_request = CreateVpcRequest(
            name="my-vpc",
            cidr="192.168.0.0/16",
            description="My VPC for testing",
            enable_ipv6=False,
            tags=[
                TagModel(tag_key="project", tag_value="test"),
                TagModel(tag_key="env", tag_value="dev")
            ]
        )
        
        create_response = vpc_client.create_vpc(create_request)
        print("VPC 创建成功:")
        print(create_response.to_json_string())
        
        # 2. 查询 VPC 列表
        print("\n查询 VPC 列表...")
        query_request = QueryVpcListRequest(
            marker="",
            max_keys=100,
            is_default=False,
            vpc_ids=""
        )
        
        query_response = vpc_client.query_vpc_list(query_request)
        print("VPC 列表:")
        print(query_response.to_json_string())
        
    except exception.BceServerError as e:
        print(f"服务端错误: {e.message}")
        print(f"Request ID: {e.request_id}")
        print(f"Status Code: {e.status_code}")
        
    except exception.BceClientError as e:
        print(f"客户端错误: {e.message}")
        print(f"Request ID: {e.request_id}")
        print(f"Error Code: {e.code}")
        
    except exception.BceHttpClientError as e:
        print(f"HTTP 错误: {e.last_error}")
        print(f"Request ID: {e.request_id}")
        print(f"Error Code: {e.code}")
        
    except Exception as e:
        print(f"未知错误: {str(e)}")

if __name__ == '__main__':
    main()
```

## 最佳实践

### 1. 安全管理凭证

**不要**在代码中硬编码 Access Key：

```python
# 不推荐
access_key_id = "your-access-key-id"
secret_access_key = "your-secret-access-key"
```

**推荐**使用环境变量或配置文件：

```python
import os

# 从环境变量读取
access_key_id = os.environ.get('BCE_ACCESS_KEY_ID')
secret_access_key = os.environ.get('BCE_SECRET_ACCESS_KEY')

# 或从配置文件读取
import configparser
config_parser = configparser.ConfigParser()
config_parser.read('config.ini')
access_key_id = config_parser.get('credentials', 'access_key_id')
secret_access_key = config_parser.get('credentials', 'secret_access_key')
```

### 2. 复用客户端对象

客户端对象是线程安全的，建议复用：

```python
# 推荐：创建一次，多次使用
vpc_client = VpcClient(config)

for i in range(10):
    response = vpc_client.query_vpc_list(request)
    # 处理响应
```

### 3. 正确处理异常

始终捕获并处理异常，不要忽略错误：

```python
try:
    response = vpc_client.create_vpc(request)
    # 处理成功响应
except exception.BceHttpClientError as e:
    # 记录错误日志
    logger.error(f"Failed to create VPC: {e.message}, Request ID: {e.request_id}")
    # 根据业务需求决定是否重试或返回错误
    raise
```

### 4. 使用合适的超时配置

根据业务场景配置合适的超时时间：

```python
config = BceClientConfiguration(
    credentials=credentials,
    endpoint=endpoint,
    connection_timeout_in_mills=30000  # 30秒超时
)
```

### 5. 启用日志用于调试

在开发和调试阶段启用详细日志：

```python
import logging

# 开发环境启用 DEBUG 级别
if os.environ.get('ENV') == 'development':
    logging.getLogger('baiducloud_python_sdk').setLevel(logging.DEBUG)
else:
    logging.getLogger('baiducloud_python_sdk').setLevel(logging.INFO)
```

## 版本要求

- Python 2.7 或 Python 3.3+
- requests >= 2.20.0

## 参考资料

- [百度智能云官方文档](https://cloud.baidu.com/doc/)
- [API 参考](https://cloud.baidu.com/doc/Reference/index.html)
- [SDK GitHub 仓库](https://github.com/baidubce/baiducloud-python-sdk)
- [AKSK 获取指南](https://cloud.baidu.com/doc/Reference/s/9jwvz2egb)

## 常见问题

### Q: 如何获取 Access Key？

A: 访问 [百度智能云控制台](https://console.bce.baidu.com)，在"安全认证"中创建 Access Key。

### Q: 支持哪些 Python 版本？

A: SDK 支持 Python 2.7 和 Python 3.4 及以上版本。

### Q: 如何处理请求超时？

A: 可以通过 `BceClientConfiguration` 配置 `connection_timeout_in_mills` 参数来设置超时时间。

### Q: 如何启用 HTTPS？

A: 在创建配置对象时设置 `protocol='https'`：

```python
config = BceClientConfiguration(
    credentials=credentials,
    endpoint=endpoint,
    protocol='https'
)
```

### Q: 如何查看请求详情用于调试？

A: 启用 DEBUG 级别日志：

```python
import logging
logging.getLogger('baiducloud_python_sdk').setLevel(logging.DEBUG)
```

## 贡献

欢迎提交 Issue 和 Pull Request 来帮助改进 SDK。

## 许可证

Apache License 2.0