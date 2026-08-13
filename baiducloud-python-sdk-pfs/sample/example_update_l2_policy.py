"""
Example for pfs update_l2_policy method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_pfs.api.pfs_client import PfsClient
from baiducloud_python_sdk_pfs import models as pfs_models

if __name__ == '__main__':
    try:
        endpoint = ""

        # ==== AK/SK 鉴权 ====
        access_key_id = "Your Ak"
        secret_access_key = "Your Sk"
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )

        client = PfsClient(bce_client_config)
        request = pfs_models.UpdateL2PolicyRequest(
            instance_id="",
            policy_id="",
            new_policy_name="",
            expired_time=0,
            execute_time=0,
            bucket_name="",
            bucket_prefix="",
        )
        res = client.update_l2_policy(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
