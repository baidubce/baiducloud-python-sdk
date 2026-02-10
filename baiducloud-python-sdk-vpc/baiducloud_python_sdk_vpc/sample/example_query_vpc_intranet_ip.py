from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_vpc.api.vpc_client import VpcClient
from baiducloud_python_sdk_vpc.models.query_vpc_intranet_ip_request import QueryVpcIntranetIpRequest

if __name__ == '__main__':
    try:
        # 设置Client的Access Key ID和Secret Access Key，获取AKSK详见:https://cloud.baidu.com/doc/Reference/s/9jwvz2egb
        access_key_id = ""
        secret_access_key = ""
        endpoint = ""
        config = BceClientConfiguration(credentials=BceCredentials(access_key_id, secret_access_key), endpoint = endpoint)
        VpcClient = VpcClient(config)
        request = QueryVpcIntranetIpRequest(
            vpc_id = "", 
            private_ip_addresses = [], 
            private_ip_range = ""
        )
        res = VpcClient.query_vpc_intranet_ip(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)