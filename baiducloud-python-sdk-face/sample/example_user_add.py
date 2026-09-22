"""
Example for face user_add method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.auth.api_key_credentials import ApiKeyCredentials
from baiducloud_python_sdk_core.auth.access_token_credentials import AccessTokenCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_face.api.face_client import FaceClient
from baiducloud_python_sdk_face import models as face_models

if __name__ == '__main__':
    try:
        endpoint = ""

        # ==== AK/SK 鉴权 ====
        # access_key_id = "Your Ak"
        # secret_access_key = "Your Sk"
        # bce_client_config = BceClientConfiguration(credentials=BceCredentials(access_key_id, secret_access_key),
        # endpoint=endpoint)

        # ==== AccessToken 鉴权（API Key / Secret Key 换取 AccessToken）====
        # api_key = "Your ApiKey"
        # secret_key = "Your SecretKey"
        # bce_client_config = BceClientConfiguration(credentials=AccessTokenCredentials(api_key, secret_key),
        # endpoint=endpoint)

        # ==== API Key 鉴权 ====
        api_key = "Your ApiKey"
        bce_client_config = BceClientConfiguration(credentials=ApiKeyCredentials(api_key), endpoint=endpoint)

        client = FaceClient(bce_client_config)
        request = face_models.UserAddRequest(
            image="",
            image_type="",
            group_id="",
            user_id="",
            user_info="",
            quality_control="",
            liveness_control="",
            spoofing_control="",
            action_type="",
            face_sort_type=0,
        )
        res = client.user_add(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
