"""
Example for vdb resize_instance_using_post method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_vdb.api.vdb_client import VdbClient
from baiducloud_python_sdk_vdb import models as vdb_models

if __name__ == '__main__':
    try:
        endpoint = ""

        # ==== AK/SK 鉴权 ====
        access_key_id = "Your Ak"
        secret_access_key = "Your Sk"
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )

        client = VdbClient(bce_client_config)
        request = vdb_models.ResizeInstanceUsingPOSTRequest(
            engine_type="",
            components=[],
            data_node_num=0,
            disk_flavor=0,
            disk_type="",
            env="",
            instance_id="",
            master_node_spec="",
            master_num=0,
            node_spec="",
            node_type="",
            order_id="",
            proxy_node_spec="",
            proxy_num=0,
        )
        res = client.resize_instance_using_post(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
