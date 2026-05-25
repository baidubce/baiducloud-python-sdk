"""
Example for eip create_eip_group method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_eip.api.eip_client import EipClient
from baiducloud_python_sdk_eip import models as eip_models

if __name__ == '__main__':
    try:
        # 设置Client的Access Key ID和Secret Access Key，获取AKSK详见:https://cloud.baidu.com/doc/Reference/s/9jwvz2egb
        access_key_id = ""
        secret_access_key = ""
        endpoint = ""
        config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )
        client = EipClient(config)

        reservation = eip_models.Reservation(reservation_length=0, reservation_time_unit="")
        billing = eip_models.Billing(payment_timing="", billing_method="", reservation=reservation)
        request = eip_models.CreateEipGroupRequest(
            bandwidth_in_mbps=0,
            billing=billing,
            client_token="",
            route_type="",
            eip_count=0,
            eipv6_count=0,
            name="",
            tags=[],
            resource_group_id="",
        )
        res = client.create_eip_group(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
