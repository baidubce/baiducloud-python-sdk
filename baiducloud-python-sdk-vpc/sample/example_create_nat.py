"""
Example for vpc create_nat method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_vpc.api.vpc_client import VpcClient
from baiducloud_python_sdk_vpc import models as vpc_models

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

        reservation = vpc_models.Reservation(reservation_length=0, reservation_time_unit="")
        billing = vpc_models.Billing(payment_timing="", reservation=reservation)
        session_config = vpc_models.SessionConfig(tcp_timeout=0, udp_timeout=0, icmp_timeout=0)
        request = vpc_models.CreateNatRequest(
            name="",
            vpc_id="",
            cu_num=0,
            billing=billing,
            client_token="",
            ip_version="",
            bind_eips=[],
            session_config=session_config,
            tags=[],
            resource_group_id="",
            delete_protect=False,
        )
        res = client.create_nat(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
