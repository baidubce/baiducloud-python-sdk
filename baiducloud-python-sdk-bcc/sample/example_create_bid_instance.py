"""
Example for bcc create_bid_instance method.
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
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )
        client = BccClient(bce_client_config)

        reservation = bcc_models.Reservation(reservation_length=0, reservation_time_unit="")
        billing = bcc_models.Billing(payment_timing="", reservation=reservation)
        request = bcc_models.CreateBidInstanceRequest(
            spec="",
            image_id="",
            billing=billing,
            bid_model="",
            bid_price="",
            cpu_count=0,
            memory_capacity_in_gb=0,
            root_disk_size_in_gb=0,
            root_disk_storage_type="",
            create_cds_list=[],
            ephemeral_disks=[],
            network_capacity_in_mbps=0,
            internet_charge_type="",
            eip_name="",
            purchase_count=0,
            name="",
            hostname="",
            auto_seq_suffix=False,
            is_open_hostname_domain=False,
            admin_pass="",
            keypair_id="",
            user_data="",
            zone_name="",
            subnet_id="",
            security_group_id="",
            enterprise_security_group_id="",
            isomerism_card="",
            deletion_protection=0,
            relation_tag=False,
            is_open_ipv6=False,
            tags=[],
            asp_id="",
            file_systems=[],
            is_eip_auto_related_delete=False,
            res_group_id="",
        )
        res = client.create_bid_instance(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
