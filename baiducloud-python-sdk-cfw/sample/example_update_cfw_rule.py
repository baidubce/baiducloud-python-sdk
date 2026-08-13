"""
Example for cfw update_cfw_rule method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_cfw.api.cfw_client import CfwClient
from baiducloud_python_sdk_cfw import models as cfw_models

if __name__ == '__main__':
    try:
        endpoint = ""

        # ==== AK/SK 鉴权 ====
        access_key_id = "Your Ak"
        secret_access_key = "Your Sk"
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )

        client = CfwClient(bce_client_config)
        request = cfw_models.UpdateCfwRuleRequest(
            cfw_id="",
            cfw_rule_id="",
            ip_version=0,
            priority=0,
            protocol="",
            direction="",
            source_address="",
            dest_address="",
            source_port="",
            dest_port="",
            action="",
            description="",
        )
        res = client.update_cfw_rule(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
