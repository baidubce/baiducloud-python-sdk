"""
Example for rds get_new_purchase_price method.
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

        endpoint = rds_models.Endpoint(port=0, vnet_ip="", inet_ip="", address="", inet_ip_v6="", vnet_ip_v6="")

        encrypt_strategy = rds_models.EncryptStrategy(
            encrypt_enable=False, key_management_service_name="", key_management_type="", secret_key_id=""
        )
        backup_policy = rds_models.SnapshotPolicy(
            backup_time="",
            backup_days="",
            persistent=False,
            expire_in_days=0,
            log_backup_retain_days=0,
            free_space_in_gb=0,
            data_backup_type="",
            free_space=0,
            incremental_data_backup_enable=False,
            time_unit="",
            data_backup_copy_enable=False,
            incremental_data_backup_interval=0,
            latest_data_backup_retain_days=0,
            retention_period=0,
            data_backup_retain_strategys=[],
            encrypt_strategy=encrypt_strategy,
        )

        blb_service = rds_models.BlbService(status="", service="")

        master_id_mapping = rds_models.MasterIdMapping(
            app_id="",
            app_id_short="",
            status="",
            allocated_memory_in_mb=0,
            cpu_count=0,
            allocated_storage_in_gb=0,
            used_storage_in_gb=0.0,
        )
        rdsproxy_id_mapping = rds_models.ReadReplicaIdMapping(
            app_id="",
            app_id_short="",
            status="",
            allocated_memory_in_mb=0,
            cpu_count=0,
            allocated_storage_in_gb=0,
            used_storage_in_gb=0.0,
        )
        topology = rds_models.Topology(
            master=[],
            read_replica=[],
            rdsproxy=[],
            read_replica_id_mapping=[],
            master_id_mapping=master_id_mapping,
            rdsproxy_id_mapping=rdsproxy_id_mapping,
            rdsproxy_id_mappings=[],
        )

        master = rds_models.DccHostId(host_id="", azone="")
        backup = rds_models.DccHostId(host_id="", azone="")
        dcc_host_ids = rds_models.DccHostInfo(master=master, backup=backup)

        node_read_replica = rds_models.RoleInfo(id="", azone="", subnet_id="", name="", vpc_cidr="", short_id="")

        node_master = rds_models.RoleInfo(id="", azone="", subnet_id="", name="", vpc_cidr="", short_id="")

        node_slave = rds_models.RoleInfo(id="", azone="", subnet_id="", name="", vpc_cidr="", short_id="")

        node_proxy = rds_models.RoleInfo(id="", azone="", subnet_id="", name="", vpc_cidr="", short_id="")

        node_master_read_replica = rds_models.RoleInfo(
            id="", azone="", subnet_id="", name="", vpc_cidr="", short_id=""
        )

        node_backup_read_replica = rds_models.RoleInfo(
            id="", azone="", subnet_id="", name="", vpc_cidr="", short_id=""
        )

        resource_group = rds_models.ResourceGroupsDetailFull(
            groups=[],
            name="",
            type="",
            region="",
            id="",
            uuid="",
            summary="",
            url="",
            account_id="",
            user_id="",
            tags=[],
            res_uuid="",
        )
        instance = rds_models.Instance(
            instance_id="",
            instance_short_id="",
            instance_name="",
            engine="",
            engine_version="",
            rds_minor_version="",
            character_set_name="",
            endpoint=endpoint,
            instance_class="",
            allocated_memory_in_mb=0,
            allocated_memory_in_gb=0,
            memory_capacity=0.0,
            allocated_storage_in_gb=0,
            volume_capacity=0,
            total_storage_in_gb=0,
            used_storage_in_mb=0,
            used_storage_in_gb=0.0,
            used_storage=0.0,
            cpu_count=0,
            instance_type="",
            source_instance_id="",
            read_replica_num=0,
            read_replica=[],
            instance_status="",
            lock_mode="",
            eip_status="",
            public_access_status="",
            super_user_flag="",
            replication_type="",
            sync_mode="",
            sqlserver_br_type="",
            backup_policy=backup_policy,
            blb_service=blb_service,
            publicly_accessible=False,
            instance_create_time="",
            instance_expire_time="",
            product_type="",
            payment_timing="",
            topology=topology,
            azone="",
            vpc_id="",
            subnet_id=None,
            physical_zone=None,
            region="",
            source_region="",
            billing_status="",
            application_type="",
            node_amount=0,
            old_instance=0,
            online_status=0,
            is_single=False,
            dcc_host_ids=dcc_host_ids,
            machine_type=0,
            weight=0,
            node_type="",
            repair_start_time="",
            repair_end_time="",
            quot_status="",
            node_read_replica=node_read_replica,
            node_master=node_master,
            node_slave=node_slave,
            node_proxy=node_proxy,
            disk_io_type="",
            group_id="",
            group_name="",
            tde_status="",
            user_id="",
            bgw_group_id="",
            bgw_group_exclusive=False,
            ro_group_list=[],
            ro_group_abnormal=False,
            disk_type="",
            cds_type="",
            maintain_start_time="",
            maintain_duration=0,
            maintain_period="",
            instance_sub_status="",
            bcm_send_cycle="",
            auto_resize_disk=0,
            auto_resize_cpu=0,
            edge_region="",
            edge_region_name="",
            edge_vpc_id="",
            edge_subnet_id="",
            gtid_type=0,
            node_master_read_replica=node_master_read_replica,
            node_backup_read_replica=node_backup_read_replica,
            ha_strategy=0,
            is_dbrs_enable=False,
            replica_type="",
            resource_type="",
            cds_encrypt=0,
            cds_encrypt_key="",
            resource_platform="",
            location="",
            has_slave=False,
            expire_date=0,
            has_proxy=False,
            vpc_name="",
            resource_uuid="",
            tags=[],
            task="",
            order_status="",
            vpc_cidr="",
            zone_names=[],
            dcc_hosts=[],
            category="",
            name="",
            resource_group=resource_group,
            resource_group_id="",
            resource_group_name="",
            is_charge_proxy=False,
            single=False,
        )
        request = rds_models.GetNewPurchasePriceRequest(instance=instance, product_type="", duration=0, number=0)
        res = client.get_new_purchase_price(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
