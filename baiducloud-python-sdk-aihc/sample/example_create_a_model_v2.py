"""
Example for aihc create_a_model_v2 method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_aihc.api.aihc_client import AihcClient
from baiducloud_python_sdk_aihc import models as aihc_models

if __name__ == '__main__':
    try:
        # 设置Client的Access Key ID和Secret Access Key，获取AKSK详见:https://cloud.baidu.com/doc/Reference/s/9jwvz2egb
        access_key_id = ""
        secret_access_key = ""
        endpoint = ""
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )
        client = AihcClient(bce_client_config)
        init_version_entry = aihc_models.ModelVersionEntry(
            id="", version="", source="", storage_bucket="", storage_path="", model_metrics="", description=""
        )
        request = aihc_models.CreateAModelV2Request(
            name="",
            model_format="",
            init_version_entry=init_version_entry,
            description="",
            owner="",
            visibility_scope="",
        )
        res = client.create_a_model_v2(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
