"""
Example for cloudassistant update_action method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_cloudassistant.api.cloudassistant_client import CloudassistantClient
from baiducloud_python_sdk_cloudassistant import models as cloudassistant_models

if __name__ == '__main__':
    try:
        # 设置Client的Access Key ID和Secret Access Key，获取AKSK详见:https://cloud.baidu.com/doc/Reference/s/9jwvz2egb
        access_key_id = ""
        secret_access_key = ""
        endpoint = ""
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )
        client = CloudassistantClient(bce_client_config)

        command = cloudassistant_models.Command(
            type="",
            content="",
            scope="",
            enable_parameter=False,
            parameters=[],
            user="",
            work_dir="",
            exec_params=None,
            wait_on_agent_milli=0,
        )

        file_upload = cloudassistant_models.FileUpload(
            os="",
            content="",
            filename="",
            filepath="",
            bos_bucket_name="",
            bos_file_path="",
            bos_etag="",
            user="",
            group="",
            mode="",
            overwrite=False,
        )
        action = cloudassistant_models.Action(
            id="",
            ref="",
            type="",
            name="",
            alias="",
            description="",
            timeout_second=0,
            command=command,
            file_upload=file_upload,
            supported_instance_types=[],
            created_timestamp=0,
            updated_timestamp=0,
        )

        import_instances = cloudassistant_models.TargetImport(keyword_type="", instances=[])
        target_selector = cloudassistant_models.TargetSelector(
            instance_type="", tags=[], import_instances=import_instances
        )
        request = cloudassistant_models.UpdateActionRequest(
            execution="",
            action=action,
            parameters=None,
            target_selector_type="",
            targets=[],
            target_selector=target_selector,
        )
        res = client.update_action(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
