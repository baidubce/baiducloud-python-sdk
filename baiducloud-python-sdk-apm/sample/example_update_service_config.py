"""
Example for apm update_service_config method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_apm.api.apm_client import ApmClient
from baiducloud_python_sdk_apm import models as apm_models

if __name__ == '__main__':
    try:
        # 设置Client的Access Key ID和Secret Access Key，获取AKSK详见:https://cloud.baidu.com/doc/Reference/s/9jwvz2egb
        access_key_id = ""
        secret_access_key = ""
        endpoint = ""
        config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )
        client = ApmClient(config)
        sample_config = apm_models.SampleConfig(enabled=False, processors=[])
        logging_config = apm_models.LoggingConfig(
            enabled=False,
            region="",
            project="",
            log_store_name="",
            trace_id_index="",
            trace_id_key="",
            span_id_index="",
            span_id_key="",
        )
        request_config = apm_models.ServiceRequestConfig(
            apm_global=False,
            server_slow_request_threshold_seconds=0.0,
            db_slow_request_threshold_seconds=0.0,
            ok_http_status=[],
        )
        topo_config = apm_models.ServiceTopoConfig(
            apm_global=False, request_seconds_threshold=0.0, error_rate_threshold=0.0
        )
        mllm_resource_dump_config = apm_models.MllmResourceDumpConfig(retention_days=0, bucket="")
        request = apm_models.UpdateServiceConfigRequest(
            service_names=[],
            sample_config=sample_config,
            logging_config=logging_config,
            request_config=request_config,
            topo_config=topo_config,
            mllm_resource_dump_config=mllm_resource_dump_config,
        )
        res = client.update_service_config(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
