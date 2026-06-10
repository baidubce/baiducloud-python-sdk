"""
Example for bcc create_volume method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_bcc.api.bcc_client import BccClient
from baiducloud_python_sdk_bcc import models as bcc_models

if __name__ == '__main__':
    try:
        # 设置Client的Access Key ID和Secret Access Key，获取AKSK详见:https://cloud.baidu.com/doc/Reference/s/9jwvz2egb
        access_key_id = ""
        secret_access_key = ""
        endpoint = ""
        config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )
        client = BccClient(config)

        reservation = bcc_models.Reservation(reservation_length=0, reservation_time_unit="")
        billing = bcc_models.Billing(payment_timing="", reservation=reservation)
        auto_snapshot_policy = bcc_models.AutoSnapshotPolicyModel(
            id="",
            name="",
            time_points=[],
            repeat_weekdays=[],
            status="",
            retention_days=0,
            created_time="",
            updated_time="",
            deleted_time="",
            last_execute_time="",
            volume_count=0,
        )
        request = bcc_models.CreateVolumeRequest(
            billing=billing,
            zone_name="",
            storage_type="",
            cds_size_in_gb=0,
            cds_extra_io=0,
            snapshot_id="",
            share_snapshot_id="",
            enable_delete_protection="",
            instance_id="",
            encrypt_key="",
            name="",
            description="",
            renew_time_unit="",
            renew_time=0,
            relation_tag=False,
            tags=[],
            res_group_id="",
            cluster_id="",
            charge_type="",
            auto_snapshot_policy=auto_snapshot_policy,
            delete_with_instance=False,
            delete_auto_snapshot=False,
            purchase_count=0,
        )
        res = client.create_volume(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
