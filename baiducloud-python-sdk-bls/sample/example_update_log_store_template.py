"""
Example for bls update_log_store_template method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_bls.api.bls_client import BlsClient
from baiducloud_python_sdk_bls import models as bls_models

if __name__ == '__main__':
    try:
        # 设置Client的Access Key ID和Secret Access Key，获取AKSK详见:https://cloud.baidu.com/doc/Reference/s/9jwvz2egb
        access_key_id = ""
        secret_access_key = ""
        endpoint = ""
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )
        client = BlsClient(bce_client_config)

        index = bls_models.Index(fulltext=False, case_sensitive=False, include_chinese=False, separators="", fields={})
        template = bls_models.Template(
            retention=0,
            shard_count=0,
            disable_shard_auto_split=False,
            max_shard_count=0,
            enable_hot_retention=False,
            hot_retention=0,
            index=index,
            name="",
            project_patterns=[],
            logstore_patterns=[],
            priority=0,
            created_timestamp="",
            updated_timestamp="",
        )
        request = bls_models.UpdateLogStoreTemplateRequest(
            name="", project_patterns=[], logstore_patterns=[], priority=0, template=template
        )
        res = client.update_log_store_template(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
