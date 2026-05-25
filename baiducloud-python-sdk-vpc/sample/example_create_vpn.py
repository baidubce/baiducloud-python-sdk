"""
Example for vpc create_vpn method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_vpc.api.vpc_client import VpcClient
from baiducloud_python_sdk_vpc.models.create_vpn_request import CreateVpnRequest
from baiducloud_python_sdk_vpc.models.reservation import Reservation
from baiducloud_python_sdk_vpc.models.billing import Billing

if __name__ == '__main__':
    try:
        # 设置Client的Access Key ID和Secret Access Key，获取AKSK详见:https://cloud.baidu.com/doc/Reference/s/9jwvz2egb
        access_key_id = ""
        secret_access_key = ""
        endpoint = ""
        config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )
        client = VpcClient(config)

        reservation = Reservation(reservation_length=0, reservation_time_unit="")
        billing = Billing(payment_timing="", reservation=reservation)
        request = CreateVpnRequest(
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
