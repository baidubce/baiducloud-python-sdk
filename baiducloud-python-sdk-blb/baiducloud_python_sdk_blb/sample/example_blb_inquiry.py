"""
Example for blb blb_inquiry method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_blb.api.blb_client import BlbClient
from baiducloud_python_sdk_blb.models.reservation import Reservation
from baiducloud_python_sdk_blb.models.billing import Billing
from baiducloud_python_sdk_blb.models.blb_inquiry_request import BlbInquiryRequest

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

        reservation = Reservation(reservation_length=0)
        billing = Billing(payment_timing="", billing_method="", reservation=reservation)
        request = BlbInquiryRequest(blb_type="", performance_level="", count=0, billing=billing)
        res = client.blb_inquiry(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
