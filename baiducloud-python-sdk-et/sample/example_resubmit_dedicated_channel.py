"""
Example for et resubmit_dedicated_channel method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_et.api.et_client import EtClient
from baiducloud_python_sdk_et import models as et_models

if __name__ == '__main__':
    try:
        # 设置Client的Access Key ID和Secret Access Key，获取AKSK详见:https://cloud.baidu.com/doc/Reference/s/9jwvz2egb
        access_key_id = ""
        secret_access_key = ""
        endpoint = ""
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )
        client = EtClient(bce_client_config)
        request = et_models.ResubmitDedicatedChannelRequest(
            et_id="",
            et_channel_id="",
            baidu_address="",
            name="",
            networks=[],
            customer_address="",
            route_type="",
            vlan_id=0,
            client_token="",
            authorized_users=[],
            description="",
            enable_ipv6=0,
            baidu_ipv6_address="",
            customer_ipv6_address="",
            ipv6_networks=[],
        )
        res = client.resubmit_dedicated_channel(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
