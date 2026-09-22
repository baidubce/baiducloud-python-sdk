import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_scs.api.scs_client import ScsClient
from baiducloud_python_sdk_scs import models as scs_models


class ScsClientTest(unittest.TestCase):
    """ScsClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''

        # ==== AK/SK 鉴权 ====
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)

        self.client = ScsClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_account_list(self):
        self.client.account_list(scs_models.AccountListRequest())

    def test_add_ip_whitelist(self):
        self.client.add_ip_whitelist(scs_models.AddIpWhitelistRequest())

    def test_add_parameters_to_parameter_template(self):
        self.client.add_parameters_to_parameter_template(scs_models.AddParametersToParameterTemplateRequest())

    def test_application_parameter_template(self):
        self.client.application_parameter_template(scs_models.ApplicationParameterTemplateRequest())

    def test_audit_log_switch(self):
        self.client.audit_log_switch(scs_models.AuditLogSwitchRequest())

    def test_batch_restore_instances(self):
        self.client.batch_restore_instances(scs_models.BatchRestoreInstancesRequest())

    def test_bind_security_group(self):
        self.client.bind_security_group(scs_models.BindSecurityGroupRequest())

    def test_bind_tags(self):
        self.client.bind_tags(scs_models.BindTagsRequest())

    def test_cancel_prepaid_to_postpaid(self):
        self.client.cancel_prepaid_to_postpaid(scs_models.CancelPrepaidToPostpaidRequest())

    def test_change_access_password(self):
        self.client.change_access_password(scs_models.ChangeAccessPasswordRequest())

    def test_change_account_password(self):
        self.client.change_account_password(scs_models.ChangeAccountPasswordRequest())

    def test_change_configuration(self):
        self.client.change_configuration(scs_models.ChangeConfigurationRequest())

    def test_clear_instance(self):
        self.client.clear_instance(scs_models.ClearInstanceRequest())

    def test_cluster_status_check(self):
        self.client.cluster_status_check(scs_models.ClusterStatusCheckRequest())

    def test_cluster_type_upgrade(self):
        self.client.cluster_type_upgrade(scs_models.ClusterTypeUpgradeRequest())

    def test_create_account(self):
        self.client.create_account(scs_models.CreateAccountRequest())

    def test_create_an_instance(self):
        self.client.create_an_instance(scs_models.CreateAnInstanceRequest())

    def test_create_deployment_set(self):
        self.client.create_deployment_set(scs_models.CreateDeploymentSetRequest())

    def test_create_entrance(self):
        self.client.create_entrance(scs_models.CreateEntranceRequest())

    def test_create_hot_group(self):
        self.client.create_hot_group(scs_models.CreateHotGroupRequest())

    def test_create_instance_white_group(self):
        self.client.create_instance_white_group(scs_models.CreateInstanceWhiteGroupRequest())

    def test_create_parameter_template(self):
        self.client.create_parameter_template(scs_models.CreateParameterTemplateRequest())

    def test_create_sync_group(self):
        self.client.create_sync_group(scs_models.CreateSyncGroupRequest())

    def test_delete_account(self):
        self.client.delete_account(scs_models.DeleteAccountRequest())

    def test_delete_deployment_set(self):
        self.client.delete_deployment_set(scs_models.DeleteDeploymentSetRequest())

    def test_delete_instance_white_group(self):
        self.client.delete_instance_white_group(scs_models.DeleteInstanceWhiteGroupRequest())

    def test_delete_instances(self):
        self.client.delete_instances(scs_models.DeleteInstancesRequest())

    def test_delete_ip_whitelist(self):
        self.client.delete_ip_whitelist(scs_models.DeleteIpWhitelistRequest())

    def test_delete_manual_backup(self):
        self.client.delete_manual_backup(scs_models.DeleteManualBackupRequest())

    def test_delete_memory_scaling_config(self):
        self.client.delete_memory_scaling_config(scs_models.DeleteMemoryScalingConfigRequest())

    def test_delete_parameter_template(self):
        self.client.delete_parameter_template(scs_models.DeleteParameterTemplateRequest())

    def test_delete_sync_group(self):
        self.client.delete_sync_group(scs_models.DeleteSyncGroupRequest())

    def test_disconnect_entrance(self):
        self.client.disconnect_entrance(scs_models.DisconnectEntranceRequest())

    def test_domain_name_exchange(self):
        self.client.domain_name_exchange(scs_models.DomainNameExchangeRequest())

    def test_ge_price_for_resize_instance(self):
        self.client.ge_price_for_resize_instance(scs_models.GePriceForResizeInstanceRequest())

    def test_get_application_parameter_template_records(self):
        self.client.get_application_parameter_template_records(
            scs_models.GetApplicationParameterTemplateRecordsRequest()
        )

    def test_get_available_zones(self):
        self.client.get_available_zones()

    def test_get_back_up_url(self):
        self.client.get_back_up_url(scs_models.GetBackUpUrlRequest())

    def test_get_back_up_usage(self):
        self.client.get_back_up_usage(scs_models.GetBackUpUsageRequest())

    def test_get_backup_list(self):
        self.client.get_backup_list(scs_models.GetBackupListRequest())

    def test_get_backup_strategy(self):
        self.client.get_backup_strategy(scs_models.GetBackupStrategyRequest())

    def test_get_cluster_blb_status(self):
        self.client.get_cluster_blb_status(scs_models.GetClusterBlbStatusRequest())

    def test_get_deployment_set_list(self):
        self.client.get_deployment_set_list(scs_models.GetDeploymentSetListRequest())

    def test_get_hot_group_detail(self):
        self.client.get_hot_group_detail(scs_models.GetHotGroupDetailRequest())

    def test_get_hot_group_list(self):
        self.client.get_hot_group_list(scs_models.GetHotGroupListRequest())

    def test_get_instance_detail(self):
        self.client.get_instance_detail(scs_models.GetInstanceDetailRequest())

    def test_get_instance_list(self):
        self.client.get_instance_list(scs_models.GetInstanceListRequest())

    def test_get_instance_spec_list(self):
        self.client.get_instance_spec_list()

    def test_get_instance_white_group(self):
        self.client.get_instance_white_group(scs_models.GetInstanceWhiteGroupRequest())

    def test_get_parameter_list(self):
        self.client.get_parameter_list(scs_models.GetParameterListRequest())

    def test_get_parameter_template_list(self):
        self.client.get_parameter_template_list(scs_models.GetParameterTemplateListRequest())

    def test_get_price_for_create_instance(self):
        self.client.get_price_for_create_instance(scs_models.GetPriceForCreateInstanceRequest())

    def test_get_recycle_list(self):
        self.client.get_recycle_list(scs_models.GetRecycleListRequest())

    def test_get_subnet_list(self):
        self.client.get_subnet_list(scs_models.GetSubnetListRequest())

    def test_get_sync_group_status(self):
        self.client.get_sync_group_status(scs_models.GetSyncGroupStatusRequest())

    def test_get_system_parameter_list(self):
        self.client.get_system_parameter_list(scs_models.GetSystemParameterListRequest())

    def test_get_time_window(self):
        self.client.get_time_window(scs_models.GetTimeWindowRequest())

    def test_get_tls_cert(self):
        self.client.get_tls_cert(scs_models.GetTlsCertRequest())

    def test_hot_group_add_cluster(self):
        self.client.hot_group_add_cluster(scs_models.HotGroupAddClusterRequest())

    def test_hot_group_change_master_role(self):
        self.client.hot_group_change_master_role(scs_models.HotGroupChangeMasterRoleRequest())

    def test_hot_group_forbid_write(self):
        self.client.hot_group_forbid_write(scs_models.HotGroupForbidWriteRequest())

    def test_hot_group_modify_name(self):
        self.client.hot_group_modify_name(scs_models.HotGroupModifyNameRequest())

    def test_hot_group_pre_check(self):
        self.client.hot_group_pre_check(scs_models.HotGroupPreCheckRequest())

    def test_hot_group_remove_cluster(self):
        self.client.hot_group_remove_cluster(scs_models.HotGroupRemoveClusterRequest())

    def test_hot_group_set_flow_control_rules(self):
        self.client.hot_group_set_flow_control_rules(scs_models.HotGroupSetFlowControlRulesRequest())

    def test_hot_group_stale_readable(self):
        self.client.hot_group_stale_readable(scs_models.HotGroupStaleReadableRequest())

    def test_hot_group_sync_status(self):
        self.client.hot_group_sync_status(scs_models.HotGroupSyncStatusRequest())

    def test_instance_version_upgrade(self):
        self.client.instance_version_upgrade(scs_models.InstanceVersionUpgradeRequest())

    def test_log_details(self):
        self.client.log_details(scs_models.LogDetailsRequest())

    def test_log_list(self):
        self.client.log_list(scs_models.LogListRequest())

    def test_manual_backup(self):
        self.client.manual_backup(scs_models.ManualBackupRequest())

    def test_manually_modify_bandwidth(self):
        self.client.manually_modify_bandwidth(scs_models.ManuallyModifyBandwidthRequest())

    def test_master_slave_switch(self):
        self.client.master_slave_switch(scs_models.MasterSlaveSwitchRequest())

    def test_modify_backup_comment(self):
        self.client.modify_backup_comment(scs_models.ModifyBackupCommentRequest())

    def test_modify_deployment_set(self):
        self.client.modify_deployment_set(scs_models.ModifyDeploymentSetRequest())

    def test_modify_entrance(self):
        self.client.modify_entrance(scs_models.ModifyEntranceRequest())

    def test_modify_instance_domain_name(self):
        self.client.modify_instance_domain_name(scs_models.ModifyInstanceDomainNameRequest())

    def test_modify_instance_name(self):
        self.client.modify_instance_name(scs_models.ModifyInstanceNameRequest())

    def test_modify_parameter_template_name(self):
        self.client.modify_parameter_template_name(scs_models.ModifyParameterTemplateNameRequest())

    def test_modify_parameters(self):
        self.client.modify_parameters(scs_models.ModifyParametersRequest())

    def test_modify_replication_zone(self):
        self.client.modify_replication_zone(scs_models.ModifyReplicationZoneRequest())

    def test_modify_sync_group_name(self):
        self.client.modify_sync_group_name(scs_models.ModifySyncGroupNameRequest())

    def test_modify_time_window(self):
        self.client.modify_time_window(scs_models.ModifyTimeWindowRequest())

    def test_parameter_template_delete_parameters(self):
        self.client.parameter_template_delete_parameters(scs_models.ParameterTemplateDeleteParametersRequest())

    def test_parameter_template_details(self):
        self.client.parameter_template_details(scs_models.ParameterTemplateDetailsRequest())

    def test_parameter_template_modify_parameters(self):
        self.client.parameter_template_modify_parameters(scs_models.ParameterTemplateModifyParametersRequest())

    def test_post_paid_to_prepaid(self):
        self.client.post_paid_to_prepaid(scs_models.PostPaidToPrepaidRequest())

    def test_prepaid_to_postpaid(self):
        self.client.prepaid_to_postpaid(scs_models.PrepaidToPostpaidRequest())

    def test_proxy_node_replace(self):
        self.client.proxy_node_replace(scs_models.ProxyNodeReplaceRequest())

    def test_proxy_version_upgrade_or_restart(self):
        self.client.proxy_version_upgrade_or_restart(scs_models.ProxyVersionUpgradeOrRestartRequest())

    def test_query_ip_whitelist(self):
        self.client.query_ip_whitelist(scs_models.QueryIpWhitelistRequest())

    def test_query_memory_scaling_config(self):
        self.client.query_memory_scaling_config(scs_models.QueryMemoryScalingConfigRequest())

    def test_release_hot_group(self):
        self.client.release_hot_group(scs_models.ReleaseHotGroupRequest())

    def test_release_instance(self):
        self.client.release_instance(scs_models.ReleaseInstanceRequest())

    def test_renew_instance(self):
        self.client.renew_instance(scs_models.RenewInstanceRequest())

    def test_restart_instance(self):
        self.client.restart_instance(scs_models.RestartInstanceRequest())

    def test_set_backup_policy(self):
        self.client.set_backup_policy(scs_models.SetBackupPolicyRequest())

    def test_set_cluster_as_master(self):
        self.client.set_cluster_as_master(scs_models.SetClusterAsMasterRequest())

    def test_set_cluster_as_slave(self):
        self.client.set_cluster_as_slave(scs_models.SetClusterAsSlaveRequest())

    def test_set_memory_scaling_config(self):
        self.client.set_memory_scaling_config(scs_models.SetMemoryScalingConfigRequest())

    def test_set_permissions(self):
        self.client.set_permissions(scs_models.SetPermissionsRequest())

    def test_sync_group_add_instance(self):
        self.client.sync_group_add_instance(scs_models.SyncGroupAddInstanceRequest())

    def test_sync_group_delay_info(self):
        self.client.sync_group_delay_info(scs_models.SyncGroupDelayInfoRequest())

    def test_sync_group_detail(self):
        self.client.sync_group_detail(scs_models.SyncGroupDetailRequest())

    def test_sync_group_list(self):
        self.client.sync_group_list(scs_models.SyncGroupListRequest())

    def test_sync_group_modify_bnsgroup(self):
        self.client.sync_group_modify_bnsgroup(scs_models.SyncGroupModifyBnsgroupRequest())

    def test_sync_group_pre_check(self):
        self.client.sync_group_pre_check(scs_models.SyncGroupPreCheckRequest())

    def test_sync_group_remove_instance(self):
        self.client.sync_group_remove_instance(scs_models.SyncGroupRemoveInstanceRequest())

    def test_tde_encryption(self):
        self.client.tde_encryption(scs_models.TdeEncryptionRequest())

    def test_unbind_security_group(self):
        self.client.unbind_security_group(scs_models.UnbindSecurityGroupRequest())

    def test_unbind_tags(self):
        self.client.unbind_tags(scs_models.UnbindTagsRequest())

    def test_update_instance_white_group(self):
        self.client.update_instance_white_group(scs_models.UpdateInstanceWhiteGroupRequest())

    def test_update_security_group(self):
        self.client.update_security_group(scs_models.UpdateSecurityGroupRequest())

    def test_update_tls_encryption(self):
        self.client.update_tls_encryption(scs_models.UpdateTlsEncryptionRequest())

    def test_view_security_group(self):
        self.client.view_security_group(scs_models.ViewSecurityGroupRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ScsClientTest("test_account_list"))
    suite.addTest(ScsClientTest("test_add_ip_whitelist"))
    suite.addTest(ScsClientTest("test_add_parameters_to_parameter_template"))
    suite.addTest(ScsClientTest("test_application_parameter_template"))
    suite.addTest(ScsClientTest("test_audit_log_switch"))
    suite.addTest(ScsClientTest("test_batch_restore_instances"))
    suite.addTest(ScsClientTest("test_bind_security_group"))
    suite.addTest(ScsClientTest("test_bind_tags"))
    suite.addTest(ScsClientTest("test_cancel_prepaid_to_postpaid"))
    suite.addTest(ScsClientTest("test_change_access_password"))
    suite.addTest(ScsClientTest("test_change_account_password"))
    suite.addTest(ScsClientTest("test_change_configuration"))
    suite.addTest(ScsClientTest("test_clear_instance"))
    suite.addTest(ScsClientTest("test_cluster_status_check"))
    suite.addTest(ScsClientTest("test_cluster_type_upgrade"))
    suite.addTest(ScsClientTest("test_create_account"))
    suite.addTest(ScsClientTest("test_create_an_instance"))
    suite.addTest(ScsClientTest("test_create_deployment_set"))
    suite.addTest(ScsClientTest("test_create_entrance"))
    suite.addTest(ScsClientTest("test_create_hot_group"))
    suite.addTest(ScsClientTest("test_create_instance_white_group"))
    suite.addTest(ScsClientTest("test_create_parameter_template"))
    suite.addTest(ScsClientTest("test_create_sync_group"))
    suite.addTest(ScsClientTest("test_delete_account"))
    suite.addTest(ScsClientTest("test_delete_deployment_set"))
    suite.addTest(ScsClientTest("test_delete_instance_white_group"))
    suite.addTest(ScsClientTest("test_delete_instances"))
    suite.addTest(ScsClientTest("test_delete_ip_whitelist"))
    suite.addTest(ScsClientTest("test_delete_manual_backup"))
    suite.addTest(ScsClientTest("test_delete_memory_scaling_config"))
    suite.addTest(ScsClientTest("test_delete_parameter_template"))
    suite.addTest(ScsClientTest("test_delete_sync_group"))
    suite.addTest(ScsClientTest("test_disconnect_entrance"))
    suite.addTest(ScsClientTest("test_domain_name_exchange"))
    suite.addTest(ScsClientTest("test_ge_price_for_resize_instance"))
    suite.addTest(ScsClientTest("test_get_application_parameter_template_records"))
    suite.addTest(ScsClientTest("test_get_available_zones"))
    suite.addTest(ScsClientTest("test_get_back_up_url"))
    suite.addTest(ScsClientTest("test_get_back_up_usage"))
    suite.addTest(ScsClientTest("test_get_backup_list"))
    suite.addTest(ScsClientTest("test_get_backup_strategy"))
    suite.addTest(ScsClientTest("test_get_cluster_blb_status"))
    suite.addTest(ScsClientTest("test_get_deployment_set_list"))
    suite.addTest(ScsClientTest("test_get_hot_group_detail"))
    suite.addTest(ScsClientTest("test_get_hot_group_list"))
    suite.addTest(ScsClientTest("test_get_instance_detail"))
    suite.addTest(ScsClientTest("test_get_instance_list"))
    suite.addTest(ScsClientTest("test_get_instance_spec_list"))
    suite.addTest(ScsClientTest("test_get_instance_white_group"))
    suite.addTest(ScsClientTest("test_get_parameter_list"))
    suite.addTest(ScsClientTest("test_get_parameter_template_list"))
    suite.addTest(ScsClientTest("test_get_price_for_create_instance"))
    suite.addTest(ScsClientTest("test_get_recycle_list"))
    suite.addTest(ScsClientTest("test_get_subnet_list"))
    suite.addTest(ScsClientTest("test_get_sync_group_status"))
    suite.addTest(ScsClientTest("test_get_system_parameter_list"))
    suite.addTest(ScsClientTest("test_get_time_window"))
    suite.addTest(ScsClientTest("test_get_tls_cert"))
    suite.addTest(ScsClientTest("test_hot_group_add_cluster"))
    suite.addTest(ScsClientTest("test_hot_group_change_master_role"))
    suite.addTest(ScsClientTest("test_hot_group_forbid_write"))
    suite.addTest(ScsClientTest("test_hot_group_modify_name"))
    suite.addTest(ScsClientTest("test_hot_group_pre_check"))
    suite.addTest(ScsClientTest("test_hot_group_remove_cluster"))
    suite.addTest(ScsClientTest("test_hot_group_set_flow_control_rules"))
    suite.addTest(ScsClientTest("test_hot_group_stale_readable"))
    suite.addTest(ScsClientTest("test_hot_group_sync_status"))
    suite.addTest(ScsClientTest("test_instance_version_upgrade"))
    suite.addTest(ScsClientTest("test_log_details"))
    suite.addTest(ScsClientTest("test_log_list"))
    suite.addTest(ScsClientTest("test_manual_backup"))
    suite.addTest(ScsClientTest("test_manually_modify_bandwidth"))
    suite.addTest(ScsClientTest("test_master_slave_switch"))
    suite.addTest(ScsClientTest("test_modify_backup_comment"))
    suite.addTest(ScsClientTest("test_modify_deployment_set"))
    suite.addTest(ScsClientTest("test_modify_entrance"))
    suite.addTest(ScsClientTest("test_modify_instance_domain_name"))
    suite.addTest(ScsClientTest("test_modify_instance_name"))
    suite.addTest(ScsClientTest("test_modify_parameter_template_name"))
    suite.addTest(ScsClientTest("test_modify_parameters"))
    suite.addTest(ScsClientTest("test_modify_replication_zone"))
    suite.addTest(ScsClientTest("test_modify_sync_group_name"))
    suite.addTest(ScsClientTest("test_modify_time_window"))
    suite.addTest(ScsClientTest("test_parameter_template_delete_parameters"))
    suite.addTest(ScsClientTest("test_parameter_template_details"))
    suite.addTest(ScsClientTest("test_parameter_template_modify_parameters"))
    suite.addTest(ScsClientTest("test_post_paid_to_prepaid"))
    suite.addTest(ScsClientTest("test_prepaid_to_postpaid"))
    suite.addTest(ScsClientTest("test_proxy_node_replace"))
    suite.addTest(ScsClientTest("test_proxy_version_upgrade_or_restart"))
    suite.addTest(ScsClientTest("test_query_ip_whitelist"))
    suite.addTest(ScsClientTest("test_query_memory_scaling_config"))
    suite.addTest(ScsClientTest("test_release_hot_group"))
    suite.addTest(ScsClientTest("test_release_instance"))
    suite.addTest(ScsClientTest("test_renew_instance"))
    suite.addTest(ScsClientTest("test_restart_instance"))
    suite.addTest(ScsClientTest("test_set_backup_policy"))
    suite.addTest(ScsClientTest("test_set_cluster_as_master"))
    suite.addTest(ScsClientTest("test_set_cluster_as_slave"))
    suite.addTest(ScsClientTest("test_set_memory_scaling_config"))
    suite.addTest(ScsClientTest("test_set_permissions"))
    suite.addTest(ScsClientTest("test_sync_group_add_instance"))
    suite.addTest(ScsClientTest("test_sync_group_delay_info"))
    suite.addTest(ScsClientTest("test_sync_group_detail"))
    suite.addTest(ScsClientTest("test_sync_group_list"))
    suite.addTest(ScsClientTest("test_sync_group_modify_bnsgroup"))
    suite.addTest(ScsClientTest("test_sync_group_pre_check"))
    suite.addTest(ScsClientTest("test_sync_group_remove_instance"))
    suite.addTest(ScsClientTest("test_tde_encryption"))
    suite.addTest(ScsClientTest("test_unbind_security_group"))
    suite.addTest(ScsClientTest("test_unbind_tags"))
    suite.addTest(ScsClientTest("test_update_instance_white_group"))
    suite.addTest(ScsClientTest("test_update_security_group"))
    suite.addTest(ScsClientTest("test_update_tls_encryption"))
    suite.addTest(ScsClientTest("test_view_security_group"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
