"""
Example for rds create_read_only_instance method.
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

        reservation = rds_models.Reservation(reservation_length=0, reservation_time_unit="")
        billing = rds_models.Billing(payment_timing="", reservation=reservation)
        request = rds_models.CreateReadOnlyInstanceRequest(
            billing=billing,
            source_instance_id="",
            cpu_count=0,
            memory_capacity=0,
            volume_capacity=0,
            client_token="",
            instance_name="",
            disk_io_type="",
            zone_names=[],
            vpc_id="",
            bcm_group_name="",
            is_direct_pay=False,
            subnets=[],
            ovip="",
            entry_port=0,
            resource_group_id="",
            replica_type="",
            is_inherit_master_authip=False,
            purchase_count=0,
            resource_type="",
            auto_renew_time_unit="",
            auto_renew_time=0,
        )
        res = client.create_read_only_instance(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
