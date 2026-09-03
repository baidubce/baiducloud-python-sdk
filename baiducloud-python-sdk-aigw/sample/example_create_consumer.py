"""
Example for aigw create_consumer method.
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
        credential = aigw_models.ConsumerCredentialSpec(
            name="", generate_mode="", value="", in_header=False, in_query=False, key_names=[], description=""
        )
        iam_credential = aigw_models.IAMCredentialSpec(
            name="",
            iam_api_key_id="",
            iam_token_id_masked="",
            iam_user_id="",
            iam_domain_id="",
            resource_ids=[],
            in_header=False,
            in_query=False,
            key_names=[],
            status="",
        )
        request = aigw_models.CreateConsumerRequest(
            instance_id="",
            x_region="",
            consumer_name="",
            auth_type="",
            credential_type="",
            description="",
            route_names=[],
            tags=[],
            credential=credential,
            iam_credential=iam_credential,
        )
        res = client.create_consumer(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
