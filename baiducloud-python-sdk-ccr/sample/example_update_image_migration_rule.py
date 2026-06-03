"""
Example for ccr update_image_migration_rule method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_ccr.api.ccr_client import CcrClient
from baiducloud_python_sdk_ccr import models as ccr_models

if __name__ == '__main__':
    try:
        # 设置Client的Access Key ID和Secret Access Key，获取AKSK详见:https://cloud.baidu.com/doc/Reference/s/9jwvz2egb
        access_key_id = ""
        secret_access_key = ""
        endpoint = ""
        config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )
        client = CcrClient(config)
        src_registry = ccr_models.ReplicationRegistryRequest(id=0)
        trigger = ccr_models.ReplicationTriggerRequest(type="")
        request = ccr_models.UpdateImageMigrationRuleRequest(
            instance_id="",
            policy_id="",
            dest_project_name="",
            filters=[],
            name="",
            override=False,
            src_registry=src_registry,
            trigger=trigger,
            description="",
        )
        res = client.update_image_migration_rule(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
