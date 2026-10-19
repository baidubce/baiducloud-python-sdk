"""
Example for rds transformation_example method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_rds.api.rds_client import RdsClient
from baiducloud_python_sdk_rds import models as rds_models

if __name__ == '__main__':
    try:
        endpoint = ""

        # ==== AK/SK 鉴权 ====
        access_key_id = "Your Ak"
        secret_access_key = "Your Sk"
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )

        client = RdsClient(bce_client_config)
        request = rds_models.TransformationExampleRequest(
            instance_id="",
            cpu_count=0,
            memory_capacity=0,
            volume_capacity=0,
            allocated_memory_in_mb=0,
            node_amount=0,
            is_direct_pay=False,
            is_enhanced=False,
            effective_time="",
            master_azone="",
            backup_azone="",
            disk_io_type="",
            subnet_id="",
            edge_subnet_id="",
            subnets=[],
        )
        res = client.transformation_example(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
