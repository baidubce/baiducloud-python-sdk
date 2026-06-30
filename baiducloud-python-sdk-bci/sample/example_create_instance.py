"""
Example for bci create_instance method.
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
        volume = bci_models.Volume(nfs=[], empty_dir=[], config_file=[])
        request = bci_models.CreateInstanceRequest(
            name="",
            security_group_ids=[],
            subnet_ids=[],
            containers=[],
            volume=volume,
            client_token="",
            zone_name="",
            restart_policy="",
            eip_ip="",
            auto_create_eip=False,
            eip_name="",
            eip_route_type="",
            eip_bandwidth_in_mbps=0,
            eip_billing_method="",
            gpu_type="",
            termination_grace_period_seconds=0,
            host_name="",
            tags=[],
            image_registry_credentials=[],
            init_containers=[],
        )
        res = client.create_instance(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
