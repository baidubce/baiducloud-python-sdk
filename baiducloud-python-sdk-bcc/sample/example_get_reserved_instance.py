"""
Example for bcc get_reserved_instance method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_bcc.api.bcc_client import BccClient
from baiducloud_python_sdk_bcc import models as bcc_models

if __name__ == '__main__':
    try:
        # 设置Client的Access Key ID和Secret Access Key，获取AKSK详见:https://cloud.baidu.com/doc/Reference/s/9jwvz2egb
        access_key_id = ""
        secret_access_key = ""
        endpoint = ""
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )
        client = BccClient(bce_client_config)
        request = bcc_models.GetReservedInstanceRequest(
            marker="",
            max_keys=0,
            reserved_instance_ids=[],
            reserved_instance_name="",
            zone_name="",
            reserved_instance_status="",
            spec="",
            offering_type="",
            os_type="",
            instance_id="",
            instance_name="",
            is_deduct=False,
            ehc_cluster_id="",
            sort_key="",
            sort_dir="",
            reserved_instance_source="",
            scope="",
        )
        res = client.get_reserved_instance(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
