from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_eip.api.eip_client import EipClient
from baiducloud_python_sdk_eip.models.reservation import Reservation
from baiducloud_python_sdk_eip.models.apply_for_eip_request import ApplyForEipRequest
from baiducloud_python_sdk_eip.models.billing import Billing
from baiducloud_python_sdk_eip.models.tag_model import TagModel

if __name__ == '__main__':
    try:
        # 设置Client的Access Key ID和Secret Access Key，获取AKSK详见:https://cloud.baidu.com/doc/Reference/s/9jwvz2egb
        access_key_id = ""
        secret_access_key = ""
        endpoint = ""
        config = BceClientConfiguration(credentials=BceCredentials(access_key_id, secret_access_key), endpoint = endpoint)
        EipClient = EipClient(config)
        
        reservation = Reservation(reservation_length=0, reservation_time_unit="")
        billing = Billing(payment_timing="", billing_method="", reservation = reservation)
        request = ApplyForEipRequest(
            client_token = "", 
            bandwidth_in_mbps = 0, 
            billing = billing, 
            ip_version = "", 
            route_type = "", 
            name = "", 
            tags = [], 
            resource_group_id = "", 
            auto_renew_time_unit = "", 
            auto_renew_time = 0, 
            delete_protect = False
        )
        res = EipClient.apply_for_eip(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)