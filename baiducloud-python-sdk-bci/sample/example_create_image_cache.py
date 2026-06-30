"""
Example for bci create_image_cache method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_bci.api.bci_client import BciClient
from baiducloud_python_sdk_bci import models as bci_models

if __name__ == '__main__':
    try:
        # 设置Client的Access Key ID和Secret Access Key，获取AKSK详见:https://cloud.baidu.com/doc/Reference/s/9jwvz2egb
        access_key_id = ""
        secret_access_key = ""
        endpoint = ""
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )
        client = BciClient(bce_client_config)
        request = bci_models.CreateImageCacheRequest(
            image_cache_name="",
            origin_images=[],
            subnet_id="",
            security_group_id="",
            zone_name="",
            temporary_storage_size=0,
            need_eip=False,
            eip_ip="",
            auto_match_image_cache=False,
            image_registry_secrets=[],
        )
        res = client.create_image_cache(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
