"""
Example for vpc create_vpn method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_vpc.api.vpc_client import VpcClient
from baiducloud_python_sdk_vpc import models as vpc_models

if __name__ == '__main__':
    try:
        endpoint = ""

        # ==== AK/SK 鉴权 ====
        access_key_id = "Your Ak"
        secret_access_key = "Your Sk"
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )

        client = VpcClient(bce_client_config)

        reservation = vpc_models.Reservation(reservation_length=0, reservation_time_unit="")
        billing = vpc_models.Billing(payment_timing="", reservation=reservation)
        request = vpc_models.CreateVpnRequest(
            vpc_id="",
            vpn_name="",
            billing=billing,
            client_token="",
            subnet_id="",
            type="",
            description="",
            eip="",
            tags=[],
            resource_group_id="",
            max_connection=0,
            delete_protect=False,
        )
        res = client.create_vpn(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
