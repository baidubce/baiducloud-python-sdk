"""
Example for cce modify_node_group_node_shrink_protection_status_v2 method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_cce.api.cce_client import CceClient
from baiducloud_python_sdk_cce import models as cce_models

if __name__ == '__main__':
    try:
        endpoint = ""

        # ==== AK/SK 鉴权 ====
        access_key_id = "Your Ak"
        secret_access_key = "Your Sk"
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )

        client = CceClient(bce_client_config)
        request = cce_models.ModifyNodeGroupNodeShrinkProtectionStatusV2Request(
            cluster_id="", instance_ids=[], scale_down_disabled=False
        )
        res = client.modify_node_group_node_shrink_protection_status_v2(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
