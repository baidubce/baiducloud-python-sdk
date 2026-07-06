"""
Example for aihc create_job method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_aihc.api.aihc_client import AihcClient
from baiducloud_python_sdk_aihc import models as aihc_models

if __name__ == '__main__':
    try:
        # 设置Client的Access Key ID和Secret Access Key，获取AKSK详见:https://cloud.baidu.com/doc/Reference/s/9jwvz2egb
        access_key_id = ""
        secret_access_key = ""
        endpoint = ""
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )
        client = AihcClient(bce_client_config)

        image_config = aihc_models.ImageConfig(username="", password="")
        job_spec = aihc_models.JobSpec(
            image="",
            image_config=image_config,
            replicas=0,
            resources=[],
            envs=[],
            enable_rdma=False,
            host_network=False,
        )
        tensorboard_config = aihc_models.TensorboardConfig(enable=False, log_path="")
        alert_config = aihc_models.AlertConfig(instance_id="", alert_items=[], aihc_for="", notify_rule_id="")
        advanced_settings = aihc_models.AdvancedSettings(runtime_env="", submitter_backoff_limit=0)
        request = aihc_models.CreateJobRequest(
            resource_pool_id="",
            queue_id="",
            name="",
            queue="",
            job_spec=job_spec,
            command="",
            job_type="",
            labels=[],
            priority="",
            datasources=[],
            enable_bccl=False,
            fault_tolerance=False,
            fault_tolerance_args="",
            tensorboard_config=tensorboard_config,
            alert_config=alert_config,
            retention_period="",
            advanced_settings=advanced_settings,
        )
        res = client.create_job(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
