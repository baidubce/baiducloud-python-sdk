"""
Example for bls create_log_shipper method.
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
        request = bls_models.CreateLogShipperRequest(
            log_store_name="", log_shipper_name="", dest_config=dest_config, project="", start_time="", dest_type=""
        )
        res = client.create_log_shipper(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
