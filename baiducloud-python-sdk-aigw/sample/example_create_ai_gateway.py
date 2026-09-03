"""
Example for aigw create_ai_gateway method.
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
        aihc_args = aigw_models.AihcArgs(
            account_id="", subnet_id="", security_group_ids="", vpc_cidr="", domain_prefix=""
        )
        request = aigw_models.CreateAIGatewayRequest(
            x_region="",
            name="",
            vpc_id="",
            vpc_cidr="",
            subnet_id="",
            gateway_type="",
            is_internal="",
            network_types=[],
            replicas=0,
            install_mode="",
            description="",
            delete_protection=False,
            src_product="",
            account_id="",
            workspace_id="",
            workspace_name="",
            blb_id="",
            blb_ip="",
            clusters=[],
            cprom_instance_id="",
            cprom_bearer_token="",
            bls_enabled=False,
            log_store_name="",
            version="",
            tags=[],
            resource_group_id="",
            aihc_args=aihc_args,
        )
        res = client.create_ai_gateway(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
