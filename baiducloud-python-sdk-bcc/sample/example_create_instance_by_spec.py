"""
Example for bcc create_instance_by_spec method.
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
        request = bcc_models.CreateInstanceBySpecRequest(
            image_id="",
            spec="",
            zone_name="",
            billing=billing,
            keep_image_login=False,
            bcc_create_with_script="",
            name="",
            cpu_thread_config="",
            numa_config="",
            enable_delete_protection=False,
            hostname="",
            auto_seq_suffix=False,
            is_open_hostname_domain=False,
            admin_pass="",
            keypair_id="",
            asp_id="",
            spec_id="",
            enable_jumbo_frame=False,
            user_data="",
            deletion_protection="",
            auto_renew_time_unit="",
            auto_renew_time=0,
            hosteye_type="",
            enable_numa=False,
            data_partition_type="",
            root_partition_type="",
            cds_auto_renew=False,
            create_cds_list=[],
            role_name="",
            bid_model="",
            bid_price="",
            root_disk_size_in_gb=0,
            root_disk_extra_io="",
            root_disk_storage_type="",
            network_capacity_in_mbps=0,
            ehc_cluster_id="",
            purchase_count=0,
            purchase_min_count=0,
            dedicated_host_id="",
            relation_tag=False,
            tags=[],
            file_systems=[],
            ephemeral_disks=[],
            security_group_id="",
            enterprise_security_group_id="",
            security_group_ids=[],
            enterprise_security_group_ids=[],
            subnet_id="",
            deploy_id="",
            deploy_id_list=[],
            eni_ids=[],
            disable_root_disk_serial="",
            internal_ips=[],
            res_group_id="",
            is_eip_auto_related_delete=False,
            network_purchase_type="",
            instance_type="",
            internet_charge_type="",
            eip_name="",
            is_open_host_eye=False,
            enable_ht=False,
            is_open_ipv6=False,
        )
        res = client.create_instance_by_spec(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
