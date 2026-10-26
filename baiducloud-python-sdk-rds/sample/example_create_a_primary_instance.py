"""
Example for rds create_a_primary_instance method.
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
        initial_data_reference = rds_models.InitialDataReference(
            instance_id="", reference_type="", datetime="", snapshot_id=""
        )
        request = rds_models.CreateAPrimaryInstanceRequest(
            billing=billing,
            engine="",
            engine_version="",
            cpu_count=0,
            memory_capacity=0,
            volume_capacity=0,
            disk_io_type="",
            vpc_id="",
            client_token="",
            purchase_count=0,
            instance_name="",
            category="",
            zone_names=[],
            bcm_group_name="",
            is_direct_pay=False,
            subnets=[],
            tags=[],
            bgw_group_id="",
            bgw_group_exclusive=False,
            character_set_name="",
            auto_renew_time_unit="",
            auto_renew_time=0,
            lower_case_table_names=0,
            parameter_template_id="",
            ovip="",
            entry_port=0,
            replication_type="",
            resource_group_id="",
            initial_data_reference=initial_data_reference,
            data=[],
            leader_instance_id="",
            resource_type="",
        )
        res = client.create_a_primary_instance(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
