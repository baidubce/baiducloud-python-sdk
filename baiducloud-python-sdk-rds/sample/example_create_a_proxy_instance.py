"""
Example for rds create_a_proxy_instance method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_rds.api.rds_client import RdsClient
from baiducloud_python_sdk_rds import models as rds_models

if __name__ == '__main__':
    try:
        endpoint = ""

        # ==== AK/SK 鉴权 ====
        access_key_id = "Your Ak"
        secret_access_key = "Your Sk"
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )

        client = RdsClient(bce_client_config)
        billing = rds_models.Billing(payment_timing="", reservation=None)
        request = rds_models.CreateAProxyInstanceRequest(
            billing=billing,
            source_instance_id="",
            node_amount=0,
            client_token="",
            instance_name="",
            zone_names=[],
            vpc_id="",
            is_direct_pay=False,
            subnets=[],
            ovip="",
            entry_port=0,
            resource_group_id="",
        )
        res = client.create_a_proxy_instance(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
