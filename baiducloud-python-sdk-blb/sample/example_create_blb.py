"""
Example for blb create_blb method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_blb.api.blb_client import BlbClient
from baiducloud_python_sdk_blb import models as blb_models

if __name__ == '__main__':
    try:
        endpoint = ""

        # ==== AK/SK 鉴权 ====
        access_key_id = "Your Ak"
        secret_access_key = "Your Sk"
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )

        client = BlbClient(bce_client_config)

        reservation = blb_models.ReservationForCreate(reservation_length=0)
        billing = blb_models.BillingForCreate(payment_timing="", billing_method="", reservation=reservation)
        request = blb_models.CreateBlbRequest(
            vpc_id="",
            subnet_id="",
            client_token="",
            name="",
            desc="",
            address="",
            type="",
            eip="",
            tags=[],
            billing=billing,
            performance_level="",
            auto_renew_length=0,
            auto_renew_time_unit="",
            resource_group_id="",
            allow_delete=False,
            allow_modify=False,
            modification_protection_reason="",
            allocate_ipv6=False,
        )
        res = client.create_blb(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
