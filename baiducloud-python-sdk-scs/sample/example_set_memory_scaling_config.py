"""
Example for scs set_memory_scaling_config method.
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
        mem_spec = scs_models.MemSpec(
            mem_usage_upper_threshold=0,
            mem_usage_down_threshold=0,
            max_node_type="",
            min_node_type="",
            observation_window_size_for_upper="",
            observation_window_size_for_down="",
        )
        request = scs_models.SetMemoryScalingConfigRequest(instance_id="", mem_spec=mem_spec)
        res = client.set_memory_scaling_config(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
