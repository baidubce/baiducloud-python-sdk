"""
Example for pfs upd_per_l2_bkt_lnk_info method.
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
        request = pfs_models.UpdPerL2BktLnkInfoRequest(
            instance_id="",
            bucket_link_id="",
            new_cron="",
            new_bucket_link_name="",
            new_conflict_policy=0,
            new_throughput_limit_bytes=0,
            new_scope=0,
        )
        res = client.upd_per_l2_bkt_lnk_info(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
