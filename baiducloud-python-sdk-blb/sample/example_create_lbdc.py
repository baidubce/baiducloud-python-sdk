"""
Example for blb create_lbdc method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_blb.api.blb_client import BlbClient
from baiducloud_python_sdk_blb import models as blb_models

if __name__ == '__main__':
    try:
        # 设置Client的Access Key ID和Secret Access Key，获取AKSK详见:https://cloud.baidu.com/doc/Reference/s/9jwvz2egb
        access_key_id = ""
        secret_access_key = ""
        endpoint = ""
        config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )
        client = BlbClient(config)

        reservation = blb_models.ReservationForCreate(reservation_length=0)
        billing = blb_models.BillingForCreate(payment_timing="", billing_method="", reservation=reservation)
        renew_reservation = blb_models.ReservationForCreate(reservation_length=0)
        request = blb_models.CreateLbdcRequest(
            name="",
            type="",
            ccu_count=0,
            billing=billing,
            client_token="",
            desc="",
            renew_reservation=renew_reservation,
            tags=[],
        )
        res = client.create_lbdc(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
