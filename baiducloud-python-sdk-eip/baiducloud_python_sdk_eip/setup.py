# Copyright 2014 Baidu, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file
# except in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the
# License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.

"""
The setup script to install BCE SDK for python
"""

from __future__ import absolute_import
import io
import os
import re
from setuptools import setup, find_packages


with io.open(os.path.join("baiducloud_python_sdk_eip", "__init__.py"), "rt") as f:
    SDK_VERSION = re.search(r"SDK_VERSION = b'(.*?)'", f.read()).group(1)

LONG_DESCRIPTION = ''
if os.path.exists('./README.md'):
    with io.open("README.md", encoding='utf-8') as fp:
        LONG_DESCRIPTION = fp.read()

setup(
    name='baiducloud-python-sdk-eip',
    version=SDK_VERSION,
    description='Baidu Cloud eipApi SDK Library for Python',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    install_requires=['pycryptodome>=3.8.0', 'future>=0.6.0', 'six>=1.4.0'],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, <4',
    packages=find_packages(exclude=["tests*"]),
    url='https://github.com/baidubce/baiducloud-python-sdk',
    keywords=["baiducloud", "eip"],
    license='Apache License 2.0',
    author='Baidu Cloud SDK',
    author_email='',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    project_urls={
        'Source': 'https://github.com/baidubce/baiducloud-python-sdk',
        'Documentation': 'https://github.com/baidubce/baiducloud-python-sdk/tree/master/docs',
        'Changelog': (
            'https://github.com/baidubce/baiducloud-python-sdk/blob/master/baiducloud-python-sdk-eip/ChangeLog.md'
        ),
    },
)
