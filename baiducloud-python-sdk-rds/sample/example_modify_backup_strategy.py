"""
Example for rds modify_backup_strategy method.
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
        request = rds_models.ModifyBackupStrategyRequest(
            instance_id="",
            backup_days="",
            backup_time="",
            persistent=False,
            expire_in_days=0,
            log_backup_retain_days=0,
            data_backup_type="",
            incremental_data_backup_enable=False,
            incremental_data_backup_interval=0,
            latest_data_backup_retain_days=0,
            retention_period=0,
            time_unit="",
            data_backup_copy_enable=False,
            data_backup_copy_storages_regions=[],
            data_backup_copy_retain_days=0,
        )
        res = client.modify_backup_strategy(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
