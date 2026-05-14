"""
Example for snic create_snic method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_snic.api.snic_client import SnicClient
from baiducloud_python_sdk_snic import models as snic_models

if __name__ == '__main__':
    try:
        # 设置Client的Access Key ID和Secret Access Key，获取AKSK详见:https://cloud.baidu.com/doc/Reference/s/9jwvz2egb
        access_key_id = ""
        secret_access_key = ""
        endpoint = ""
        config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )
        client = SnicClient(config)

        reservation = snic_models.Reservation(reservation_length=0, reservation_time_unit="")
        billing = snic_models.Billing(payment_timing="", reservation=reservation)
        request = snic_models.CreateSnicRequest(
            vpc_id="",
            name="",
            subnet_id="",
            service="",
            bandwidth=0,
            billing=billing,
            client_token="",
            description="",
            ip_address="",
            tags=[],
            resource_group_id="",
        )
        res = client.create_snic(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
