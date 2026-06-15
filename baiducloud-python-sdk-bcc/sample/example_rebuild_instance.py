"""
Example for bcc rebuild_instance method.
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
        request = bcc_models.RebuildInstanceRequest(
            instance_id="",
            image_id="",
            keep_image_login=False,
            is_preserve_data=False,
            admin_pass="",
            is_open_host_eye=False,
            sys_root_size=0,
            keypair_id="",
            data_partition_type="",
            root_partition_type="",
            raid_id="",
            user_data="",
            use_last_user_data=False,
            clean_last_user_data=False,
        )
        res = client.rebuild_instance(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
