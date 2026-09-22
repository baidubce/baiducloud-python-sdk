"""
Example for scs create_hot_group method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_scs.api.scs_client import ScsClient
from baiducloud_python_sdk_scs import models as scs_models

if __name__ == '__main__':
    try:
        endpoint = ""

        # ==== AK/SK 鉴权 ====
        access_key_id = "Your Ak"
        secret_access_key = "Your Sk"
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )

        client = ScsClient(bce_client_config)
        leader = scs_models.Leader(
            group_name="",
            leader_id="",
            leader_region="",
            cluster_name="",
            cluster_show_id="",
            region="",
            status="",
            total_capacity_in_gb=0.0,
            used_capacity_in_gb=0,
            shard_num=0,
            flavor=0,
            qps_write=0,
            qps_read=0,
            stale_readable=False,
            forbid_write=0,
            availability_zone="",
            expired_time="",
        )
        request = scs_models.CreateHotGroupRequest(leader=leader)
        res = client.create_hot_group(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
