"""
Example for bls create_task method.
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

        process_config = bls_models.ProcessConfig(
            regex="",
            separator="",
            custom_separator="",
            quote="",
            kv_key_index=0,
            kv_value_index=0,
            sample_log="",
            keys="",
            data_type="",
            discard_on_failure=False,
            keep_original=False,
        )
        src_config = bls_models.SrcConfig(
            src_type="",
            log_type="",
            src_dir="",
            matched_pattern="",
            ignore_pattern="",
            time_format="",
            ttl=0,
            use_multiline=False,
            multiline_regex="",
            recursive_dir=False,
            process_type="",
            process_config=process_config,
            log_time="",
            timestamp_key="",
            date_format="",
            filter_expr="",
            addition_config=None,
            meta_env=[],
            meta_label=[],
            meta_container=[],
            meta_to_fields=False,
            harvester_limit=0,
        )

        dest_config = bls_models.DestConfig(
            bos_path="",
            partition_format_ts="",
            partition_format_log_stream=False,
            max_object_size=0,
            compress_type="",
            deliver_interval=0,
            storage_format="",
            csv_headline=False,
            csv_delimiter="",
            csv_quote="",
            null_identifier="",
            selected_column_name="",
            selected_column_type="",
            fields_name=[],
            fields_type=[],
            shipper_type="",
            kafka_config="",
            dest_type="",
            log_store="",
            rate_limit=0,
            client_count=0,
        )
        config = bls_models.TaskConfig(src_config=src_config, dest_config=dest_config)
        request = bls_models.CreateTaskRequest(name="", config=config, hosts=[], tags=[])
        res = client.create_task(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
