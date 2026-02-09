# Baidu Cloud Python SDK User Guide

## Overview

The Baidu Cloud Python SDK provides developers with a convenient way to access various services of Baidu Cloud. This SDK is built on top of Baidu Cloud APIs and supports Python 2.7 and Python 3.x versions.

## Installation

### Install via pip

It is recommended to install the SDK using pip:

```bash
pip install baiducloud-python-sdk-core
pip install baiducloud-python-sdk-vpc
```

### Install from Source

You can also install from source code:

```bash
git clone https://github.com/baidubce/baiducloud-python-sdk.git
cd baiducloud-python-sdk/baiducloud-python-sdk-core
python setup.py install

cd ../baiducloud-python-sdk-vpc
python setup.py install
```

### Requirements

- Python >= 2.7 or Python >= 3.4
- requests >= 2.20.0

## Quick Start

### 1. Obtain Access Key

Before using the SDK, you need to obtain the Access Key ID and Secret Access Key from Baidu Cloud.

Visit [Baidu Cloud Console](https://console.bce.baidu.com) to get your AKSK. For more details, see: https://cloud.baidu.com/doc/Reference/s/9jwvz2egb

### 2. Create Client

First, configure client credentials and create a service client:

```python
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_vpc.api.vpc_client import VpcClient

# Configure Access Key
access_key_id = "your-access-key-id"
secret_access_key = "your-secret-access-key"
endpoint = "bcc.bj.baidubce.com"

# Create configuration object
config = BceClientConfiguration(
    credentials=BceCredentials(access_key_id, secret_access_key),
    endpoint=endpoint
)

# Create VPC client
vpc_client = VpcClient(config)
```

### 3. Call Service APIs

#### Create VPC

```python
from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_vpc.models.create_vpc_request import CreateVpcRequest
from baiducloud_python_sdk_vpc.models.tag_model import TagModel

try:
    # Build create VPC request
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
    
    # Call create VPC API
    response = vpc_client.create_vpc(request)
    print(response.to_json_string())
    
except exception.BceHttpClientError as e:
    print(f"Error: {e.last_error}")
    print(f"Request ID: {e.request_id}")
    print(f"Error Code: {e.code}")
```

## Configuration

### BceClientConfiguration

`BceClientConfiguration` is the client configuration class that supports the following options:

```python
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials

config = BceClientConfiguration(
    credentials=BceCredentials(access_key_id, secret_access_key),
    endpoint="bcc.bj.baidubce.com",          # Service endpoint
    protocol="http",                          # Protocol: http or https, default is http
    region="bj",                              # Region, default is bj (Beijing)
    connection_timeout_in_mills=10000,        # Connection timeout (milliseconds), default 10000
    send_buf_size=1048576,                    # Send buffer size, default 1MB
    recv_buf_size=10485760                    # Receive buffer size, default 10MB
)
```

### Credentials Configuration

The SDK supports multiple credential configuration methods:

#### 1. Using Access Key

```python
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials

credentials = BceCredentials(
    access_key_id="your-access-key-id",
    secret_access_key="your-secret-access-key"
)
```

#### 2. Using STS Token (Temporary Credentials)

```python
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials

credentials = BceCredentials(
    access_key_id="your-access-key-id",
    secret_access_key="your-secret-access-key",
    security_token="your-sts-token"
)
```

### Endpoint Configuration

Different services and regions have different endpoints. Common endpoints are as follows:

| Service | Region | Endpoint |
|---------|--------|----------|
| VPC     | Beijing | bcc.bj.baidubce.com |
| VPC     | Guangzhou | bcc.gz.baidubce.com |
| VPC     | Suzhou | bcc.su.baidubce.com |

For more endpoint information, please refer to: https://cloud.baidu.com/doc/Reference/s/2jwvz23xx

### Retry Policy

The SDK supports configuring retry policies:

```python
from baiducloud_python_sdk_core.retry_policy import BackOffRetryPolicy

config = BceClientConfiguration(
    credentials=credentials,
    endpoint=endpoint
)

# Set retry policy
config.retry_policy = BackOffRetryPolicy(
    max_error_retry=3,           # Maximum number of retries
    max_delay_in_millis=20000    # Maximum delay time (milliseconds)
)
```

## Error Handling

The SDK uses an exception mechanism to handle errors. All exceptions inherit from `BceHttpClientError`.

### Exception Types

- `BceHttpClientError`: Base class for HTTP client errors
- `BceServerError`: Server error (HTTP 5xx)
- `BceClientError`: Client error (HTTP 4xx)

### Exception Attributes

- `last_error`: Detailed error information
- `request_id`: Request ID for issue tracking
- `code`: Error code
- `message`: Error message
- `status_code`: HTTP status code

### Error Handling Example

```python
from baiducloud_python_sdk_core import exception

try:
    response = vpc_client.create_vpc(request)
    print(response.to_json_string())
    
except exception.BceServerError as e:
    # Server error (5xx)
    print(f"Server Error: {e.message}")
    print(f"Request ID: {e.request_id}")
    print(f"Status Code: {e.status_code}")
    
except exception.BceClientError as e:
    # Client error (4xx)
    if e.code == "InvalidAccessKeyId":
        print("Invalid Access Key ID, please check configuration")
    elif e.code == "SignatureDoesNotMatch":
        print("Signature does not match, please check Secret Access Key")
    else:
        print(f"Client Error: {e.message}")
    print(f"Request ID: {e.request_id}")
    
except exception.BceHttpClientError as e:
    # Other HTTP errors
    print(f"HTTP Error: {e.last_error}")
    print(f"Request ID: {e.request_id}")
    print(f"Error Code: {e.code}")
    
except Exception as e:
    # Other exceptions
    print(f"Unexpected error: {str(e)}")
```

### Common Error Codes

| Error Code | Description | Solution |
|-----------|-------------|----------|
| InvalidAccessKeyId | Access Key ID does not exist | Check if Access Key ID is correct |
| SignatureDoesNotMatch | Signature does not match | Check if Secret Access Key is correct |
| RequestExpired | Request has expired | Check if local time is synchronized with server time |
| InvalidHTTPAuthHeader | Invalid HTTP authentication header | Check if request header format is correct |
| Forbidden | Insufficient permissions | Check if account has appropriate operation permissions |

## Logging Configuration

The SDK uses Python's standard library `logging` module to record logs.

### Configure Log Level

```python
import logging

# Configure root logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Configure SDK log level
sdk_logger = logging.getLogger('baiducloud_python_sdk')
sdk_logger.setLevel(logging.DEBUG)
```

### Log Level Description

- `DEBUG`: Detailed debugging information, including request/response content
- `INFO`: General information, such as request start/end
- `WARNING`: Warning information
- `ERROR`: Error information
- `CRITICAL`: Critical errors

### Output Logs to File

```python
import logging

# Create file handler
file_handler = logging.FileHandler('sdk.log')
file_handler.setLevel(logging.DEBUG)

# Set log format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add to SDK logger
sdk_logger = logging.getLogger('baiducloud_python_sdk')
sdk_logger.addHandler(file_handler)
```

## Complete Example

The following is a complete example program demonstrating how to use the SDK to create and query VPCs:

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

# Configure logging
logging.basicConfig(level=logging.INFO)

def main():
    # Configure Access Key
    access_key_id = "your-access-key-id"
    secret_access_key = "your-secret-access-key"
    endpoint = "bcc.bj.baidubce.com"
    
    # Create configuration object
    config = BceClientConfiguration(
        credentials=BceCredentials(access_key_id, secret_access_key),
        endpoint=endpoint
    )
    
    # Create VPC client
    vpc_client = VpcClient(config)
    
    try:
        # 1. Create VPC
        print("Creating VPC...")
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
        print("VPC created successfully:")
        print(create_response.to_json_string())
        
        # 2. Query VPC list
        print("\nQuerying VPC list...")
        query_request = QueryVpcListRequest(
            marker="",
            max_keys=100,
            is_default=False,
            vpc_ids=""
        )
        
        query_response = vpc_client.query_vpc_list(query_request)
        print("VPC list:")
        print(query_response.to_json_string())
        
    except exception.BceServerError as e:
        print(f"Server error: {e.message}")
        print(f"Request ID: {e.request_id}")
        print(f"Status Code: {e.status_code}")
        
    except exception.BceClientError as e:
        print(f"Client error: {e.message}")
        print(f"Request ID: {e.request_id}")
        print(f"Error Code: {e.code}")
        
    except exception.BceHttpClientError as e:
        print(f"HTTP error: {e.last_error}")
        print(f"Request ID: {e.request_id}")
        print(f"Error Code: {e.code}")
        
    except Exception as e:
        print(f"Unknown error: {str(e)}")

if __name__ == '__main__':
    main()
```

## Best Practices

### 1. Secure Credential Management

**Do not** hardcode Access Keys in your code:

```python
# Not recommended
access_key_id = "your-access-key-id"
secret_access_key = "your-secret-access-key"
```

**Recommended** to use environment variables or configuration files:

```python
import os

# Read from environment variables
access_key_id = os.environ.get('BCE_ACCESS_KEY_ID')
secret_access_key = os.environ.get('BCE_SECRET_ACCESS_KEY')

# Or read from configuration file
import configparser
config_parser = configparser.ConfigParser()
config_parser.read('config.ini')
access_key_id = config_parser.get('credentials', 'access_key_id')
secret_access_key = config_parser.get('credentials', 'secret_access_key')
```

### 2. Reuse Client Objects

Client objects are thread-safe and should be reused:

```python
# Recommended: Create once, use multiple times
vpc_client = VpcClient(config)

for i in range(10):
    response = vpc_client.query_vpc_list(request)
    # Process response
```

### 3. Properly Handle Exceptions

Always catch and handle exceptions, do not ignore errors:

```python
try:
    response = vpc_client.create_vpc(request)
    # Handle successful response
except exception.BceHttpClientError as e:
    # Log error
    logger.error(f"Failed to create VPC: {e.message}, Request ID: {e.request_id}")
    # Decide whether to retry or return error based on business requirements
    raise
```

### 4. Use Appropriate Timeout Configuration

Configure appropriate timeout based on your business scenario:

```python
config = BceClientConfiguration(
    credentials=credentials,
    endpoint=endpoint,
    connection_timeout_in_mills=30000  # 30 seconds timeout
)
```

### 5. Enable Logging for Debugging

Enable detailed logging during development and debugging:

```python
import logging

# Enable DEBUG level in development environment
if os.environ.get('ENV') == 'development':
    logging.getLogger('baiducloud_python_sdk').setLevel(logging.DEBUG)
else:
    logging.getLogger('baiducloud_python_sdk').setLevel(logging.INFO)
```

## Version Requirements

- Python 2.7 or Python 3.3+
- requests >= 2.20.0

## References

- [Baidu Cloud Official Documentation](https://cloud.baidu.com/doc/)
- [API Reference](https://cloud.baidu.com/doc/Reference/index.html)
- [SDK GitHub Repository](https://github.com/baidubce/baiducloud-python-sdk)
- [AKSK Acquisition Guide](https://cloud.baidu.com/doc/Reference/s/9jwvz2egb)

## FAQ

### Q: How to obtain Access Key?

A: Visit [Baidu Cloud Console](https://console.bce.baidu.com) and create an Access Key in "Security Authentication".

### Q: Which Python versions are supported?

A: The SDK supports Python 2.7 and Python 3.4 and above.

### Q: How to handle request timeouts?

A: You can set the timeout by configuring the `connection_timeout_in_mills` parameter in `BceClientConfiguration`.

### Q: How to enable HTTPS?

A: Set `protocol='https'` when creating the configuration object:

```python
config = BceClientConfiguration(
    credentials=credentials,
    endpoint=endpoint,
    protocol='https'
)
```

### Q: How to view request details for debugging?

A: Enable DEBUG level logging:

```python
import logging
logging.getLogger('baiducloud_python_sdk').setLevel(logging.DEBUG)
```

## Contributing

Contributions via Issues and Pull Requests are welcome to help improve the SDK.

## License

Apache License 2.0