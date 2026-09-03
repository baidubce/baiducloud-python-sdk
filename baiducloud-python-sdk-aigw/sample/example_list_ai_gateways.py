"""
Example for aigw list_ai_gateways method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_aigw.api.aigw_client import AigwClient
from baiducloud_python_sdk_aigw import models as aigw_models

if __name__ == '__main__':
    try:
        endpoint = ""

        # ==== AK/SK 鉴权 ====
        access_key_id = "Your Ak"
        secret_access_key = "Your Sk"
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )

        client = AigwClient(bce_client_config)
        request = aigw_models.ListAiGatewaysRequest(
            x_region="",
            keyword="",
            keyword_type="",
            status="",
            src_product="",
            tag_key="",
            tag_value="",
            resource_group_id="",
            page_no=0,
            page_size=0,
            order_by="",
            order="",
        )
        res = client.list_ai_gateways(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
