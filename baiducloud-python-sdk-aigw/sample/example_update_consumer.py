"""
Example for aigw update_consumer method.
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
        credential_op = aigw_models.CredentialOp(operation="", credential_name="", value="")
        credential_location = aigw_models.ConsumerCredentialLocation(in_header=False, in_query=False, key_names=[])
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
        request = aigw_models.UpdateConsumerRequest(
            instance_id="",
            consumer_id="",
            x_region="",
            key_type="",
            description="",
            route_names=[],
            tags=[],
            credential_op=credential_op,
            credential_location=credential_location,
            iam_credential=iam_credential,
        )
        res = client.update_consumer(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
