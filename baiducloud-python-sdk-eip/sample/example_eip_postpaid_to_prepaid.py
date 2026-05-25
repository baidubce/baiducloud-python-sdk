"""
Example for eip eip_postpaid_to_prepaid method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_eip.api.eip_client import EipClient
from baiducloud_python_sdk_eip.models.eip_postpaid_to_prepaid_request import EipPostpaidToPrepaidRequest

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
        request = EipPostpaidToPrepaidRequest(eip="", purchase_length=0, band_width=0, client_token="")
        res = client.eip_postpaid_to_prepaid(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
