import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_ccr.api.ccr_client import CcrClient
from baiducloud_python_sdk_ccr import models as ccr_models


class CcrClientTest(unittest.TestCase):
    """CcrClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
        self.client = CcrClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_add_public_network_whitelist(self):
        self.client.add_public_network_whitelist(ccr_models.AddPublicNetworkWhitelistRequest())

    def test_add_vpc_link(self):
        self.client.add_vpc_link(ccr_models.AddVpcLinkRequest())

    def test_create_accelerator_filter(self):
        self.client.create_accelerator_filter(ccr_models.CreateAcceleratorFilterRequest())

    def test_create_image_migration_rule(self):
        self.client.create_image_migration_rule(ccr_models.CreateImageMigrationRuleRequest())

    def test_create_instance_sync(self):
        self.client.create_instance_sync(ccr_models.CreateInstanceSyncRequest())

    def test_create_robot_account(self):
        self.client.create_robot_account(ccr_models.CreateRobotAccountRequest())

    def test_create_temporary_password(self):
        self.client.create_temporary_password(ccr_models.CreateTemporaryPasswordRequest())

    def test_create_trigger(self):
        self.client.create_trigger(ccr_models.CreateTriggerRequest())

    def test_delete_accelerator_filter(self):
        self.client.delete_accelerator_filter(ccr_models.DeleteAcceleratorFilterRequest())

    def test_delete_accelerator_filters(self):
        self.client.delete_accelerator_filters(ccr_models.DeleteAcceleratorFiltersRequest())

    def test_delete_chart(self):
        self.client.delete_chart(ccr_models.DeleteChartRequest())

    def test_delete_chart_version(self):
        self.client.delete_chart_version(ccr_models.DeleteChartVersionRequest())

    def test_delete_chart_versions(self):
        self.client.delete_chart_versions(ccr_models.DeleteChartVersionsRequest())

    def test_delete_charts(self):
        self.client.delete_charts(ccr_models.DeleteChartsRequest())

    def test_delete_image_migration_rule(self):
        self.client.delete_image_migration_rule(ccr_models.DeleteImageMigrationRuleRequest())

    def test_delete_instance_sync(self):
        self.client.delete_instance_sync(ccr_models.DeleteInstanceSyncRequest())

    def test_delete_project(self):
        self.client.delete_project(ccr_models.DeleteProjectRequest())

    def test_delete_projects(self):
        self.client.delete_projects(ccr_models.DeleteProjectsRequest())

    def test_delete_public_network_whitelist(self):
        self.client.delete_public_network_whitelist(ccr_models.DeletePublicNetworkWhitelistRequest())

    def test_delete_repositories(self):
        self.client.delete_repositories(ccr_models.DeleteRepositoriesRequest())

    def test_delete_repository(self):
        self.client.delete_repository(ccr_models.DeleteRepositoryRequest())

    def test_delete_robot_account(self):
        self.client.delete_robot_account(ccr_models.DeleteRobotAccountRequest())

    def test_delete_tag(self):
        self.client.delete_tag(ccr_models.DeleteTagRequest())

    def test_delete_tags(self):
        self.client.delete_tags(ccr_models.DeleteTagsRequest())

    def test_delete_trigger(self):
        self.client.delete_trigger(ccr_models.DeleteTriggerRequest())

    def test_delete_triggers(self):
        self.client.delete_triggers(ccr_models.DeleteTriggersRequest())

    def test_delete_vpc_link(self):
        self.client.delete_vpc_link(ccr_models.DeleteVpcLinkRequest())

    def test_download_chart(self):
        self.client.download_chart(ccr_models.DownloadChartRequest())

    def test_execute_image_migration(self):
        self.client.execute_image_migration(ccr_models.ExecuteImageMigrationRequest())

    def test_execute_instance_sync(self):
        self.client.execute_instance_sync(ccr_models.ExecuteInstanceSyncRequest())

    def test_get_accelerator_filter_detail(self):
        self.client.get_accelerator_filter_detail(ccr_models.GetAcceleratorFilterDetailRequest())

    def test_get_image_migration_execution_record_detail(self):
        self.client.get_image_migration_execution_record_detail(
            ccr_models.GetImageMigrationExecutionRecordDetailRequest()
        )

    def test_get_image_migration_rule_detail(self):
        self.client.get_image_migration_rule_detail(ccr_models.GetImageMigrationRuleDetailRequest())

    def test_get_image_migration_task_logs(self):
        self.client.get_image_migration_task_logs(ccr_models.GetImageMigrationTaskLogsRequest())

    def test_get_instance_detail(self):
        self.client.get_instance_detail(ccr_models.GetInstanceDetailRequest())

    def test_get_instance_sync_detail(self):
        self.client.get_instance_sync_detail(ccr_models.GetInstanceSyncDetailRequest())

    def test_get_instance_sync_execution_detail(self):
        self.client.get_instance_sync_execution_detail(ccr_models.GetInstanceSyncExecutionDetailRequest())

    def test_get_instance_sync_task_logs(self):
        self.client.get_instance_sync_task_logs(ccr_models.GetInstanceSyncTaskLogsRequest())

    def test_get_public_network_config(self):
        self.client.get_public_network_config(ccr_models.GetPublicNetworkConfigRequest())

    def test_get_repository(self):
        self.client.get_repository(ccr_models.GetRepositoryRequest())

    def test_get_tag_build_history(self):
        self.client.get_tag_build_history(ccr_models.GetTagBuildHistoryRequest())

    def test_get_tag_detail(self):
        self.client.get_tag_detail(ccr_models.GetTagDetailRequest())

    def test_get_tags_scan_overview(self):
        self.client.get_tags_scan_overview(ccr_models.GetTagsScanOverviewRequest())

    def test_get_trigger_detail(self):
        self.client.get_trigger_detail(ccr_models.GetTriggerDetailRequest())

    def test_get_user_detail(self):
        self.client.get_user_detail(ccr_models.GetUserDetailRequest())

    def test_list_accelerator_filters(self):
        self.client.list_accelerator_filters(ccr_models.ListAcceleratorFiltersRequest())

    def test_list_chart_versions(self):
        self.client.list_chart_versions(ccr_models.ListChartVersionsRequest())

    def test_list_charts(self):
        self.client.list_charts(ccr_models.ListChartsRequest())

    def test_list_image_migration_records(self):
        self.client.list_image_migration_records(ccr_models.ListImageMigrationRecordsRequest())

    def test_list_image_migration_rules(self):
        self.client.list_image_migration_rules(ccr_models.ListImageMigrationRulesRequest())

    def test_list_image_migration_task_records(self):
        self.client.list_image_migration_task_records(ccr_models.ListImageMigrationTaskRecordsRequest())

    def test_list_instance_sync_records(self):
        self.client.list_instance_sync_records(ccr_models.ListInstanceSyncRecordsRequest())

    def test_list_instance_sync_task_records(self):
        self.client.list_instance_sync_task_records(ccr_models.ListInstanceSyncTaskRecordsRequest())

    def test_list_instance_syncs(self):
        self.client.list_instance_syncs(ccr_models.ListInstanceSyncsRequest())

    def test_list_instances(self):
        self.client.list_instances(ccr_models.ListInstancesRequest())

    def test_list_projects(self):
        self.client.list_projects(ccr_models.ListProjectsRequest())

    def test_list_repositories(self):
        self.client.list_repositories(ccr_models.ListRepositoriesRequest())

    def test_list_robot_accounts(self):
        self.client.list_robot_accounts(ccr_models.ListRobotAccountsRequest())

    def test_list_tags(self):
        self.client.list_tags(ccr_models.ListTagsRequest())

    def test_list_trigger_tasks(self):
        self.client.list_trigger_tasks(ccr_models.ListTriggerTasksRequest())

    def test_list_triggers(self):
        self.client.list_triggers(ccr_models.ListTriggersRequest())

    def test_list_vpc_links(self):
        self.client.list_vpc_links(ccr_models.ListVpcLinksRequest())

    def test_re_execute_trigger_task(self):
        self.client.re_execute_trigger_task(ccr_models.ReExecuteTriggerTaskRequest())

    def test_refresh_robot_account_key(self):
        self.client.refresh_robot_account_key(ccr_models.RefreshRobotAccountKeyRequest())

    def test_reset_password(self):
        self.client.reset_password(ccr_models.ResetPasswordRequest())

    def test_stop_image_migration(self):
        self.client.stop_image_migration(ccr_models.StopImageMigrationRequest())

    def test_stop_instance_sync(self):
        self.client.stop_instance_sync(ccr_models.StopInstanceSyncRequest())

    def test_test_accelerator_filter(self):
        self.client.test_accelerator_filter(ccr_models.TestAcceleratorFilterRequest())

    def test_test_trigger_target_address(self):
        self.client.test_trigger_target_address(ccr_models.TestTriggerTargetAddressRequest())

    def test_toggle_accelerator_filter(self):
        self.client.toggle_accelerator_filter(ccr_models.ToggleAcceleratorFilterRequest())

    def test_toggle_trigger(self):
        self.client.toggle_trigger(ccr_models.ToggleTriggerRequest())

    def test_trigger_tag_scan(self):
        self.client.trigger_tag_scan(ccr_models.TriggerTagScanRequest())

    def test_update_accelerator_filter(self):
        self.client.update_accelerator_filter(ccr_models.UpdateAcceleratorFilterRequest())

    def test_update_image_migration_rule(self):
        self.client.update_image_migration_rule(ccr_models.UpdateImageMigrationRuleRequest())

    def test_update_instance_name(self):
        self.client.update_instance_name(ccr_models.UpdateInstanceNameRequest())

    def test_update_instance_sync(self):
        self.client.update_instance_sync(ccr_models.UpdateInstanceSyncRequest())

    def test_update_instance_tags(self):
        self.client.update_instance_tags(ccr_models.UpdateInstanceTagsRequest())

    def test_update_public_network(self):
        self.client.update_public_network(ccr_models.UpdatePublicNetworkRequest())

    def test_update_repository(self):
        self.client.update_repository(ccr_models.UpdateRepositoryRequest())

    def test_update_robot_account(self):
        self.client.update_robot_account(ccr_models.UpdateRobotAccountRequest())

    def test_update_trigger(self):
        self.client.update_trigger(ccr_models.UpdateTriggerRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CcrClientTest("test_add_public_network_whitelist"))
    suite.addTest(CcrClientTest("test_add_vpc_link"))
    suite.addTest(CcrClientTest("test_create_accelerator_filter"))
    suite.addTest(CcrClientTest("test_create_image_migration_rule"))
    suite.addTest(CcrClientTest("test_create_instance_sync"))
    suite.addTest(CcrClientTest("test_create_robot_account"))
    suite.addTest(CcrClientTest("test_create_temporary_password"))
    suite.addTest(CcrClientTest("test_create_trigger"))
    suite.addTest(CcrClientTest("test_delete_accelerator_filter"))
    suite.addTest(CcrClientTest("test_delete_accelerator_filters"))
    suite.addTest(CcrClientTest("test_delete_chart"))
    suite.addTest(CcrClientTest("test_delete_chart_version"))
    suite.addTest(CcrClientTest("test_delete_chart_versions"))
    suite.addTest(CcrClientTest("test_delete_charts"))
    suite.addTest(CcrClientTest("test_delete_image_migration_rule"))
    suite.addTest(CcrClientTest("test_delete_instance_sync"))
    suite.addTest(CcrClientTest("test_delete_project"))
    suite.addTest(CcrClientTest("test_delete_projects"))
    suite.addTest(CcrClientTest("test_delete_public_network_whitelist"))
    suite.addTest(CcrClientTest("test_delete_repositories"))
    suite.addTest(CcrClientTest("test_delete_repository"))
    suite.addTest(CcrClientTest("test_delete_robot_account"))
    suite.addTest(CcrClientTest("test_delete_tag"))
    suite.addTest(CcrClientTest("test_delete_tags"))
    suite.addTest(CcrClientTest("test_delete_trigger"))
    suite.addTest(CcrClientTest("test_delete_triggers"))
    suite.addTest(CcrClientTest("test_delete_vpc_link"))
    suite.addTest(CcrClientTest("test_download_chart"))
    suite.addTest(CcrClientTest("test_execute_image_migration"))
    suite.addTest(CcrClientTest("test_execute_instance_sync"))
    suite.addTest(CcrClientTest("test_get_accelerator_filter_detail"))
    suite.addTest(CcrClientTest("test_get_image_migration_execution_record_detail"))
    suite.addTest(CcrClientTest("test_get_image_migration_rule_detail"))
    suite.addTest(CcrClientTest("test_get_image_migration_task_logs"))
    suite.addTest(CcrClientTest("test_get_instance_detail"))
    suite.addTest(CcrClientTest("test_get_instance_sync_detail"))
    suite.addTest(CcrClientTest("test_get_instance_sync_execution_detail"))
    suite.addTest(CcrClientTest("test_get_instance_sync_task_logs"))
    suite.addTest(CcrClientTest("test_get_public_network_config"))
    suite.addTest(CcrClientTest("test_get_repository"))
    suite.addTest(CcrClientTest("test_get_tag_build_history"))
    suite.addTest(CcrClientTest("test_get_tag_detail"))
    suite.addTest(CcrClientTest("test_get_tags_scan_overview"))
    suite.addTest(CcrClientTest("test_get_trigger_detail"))
    suite.addTest(CcrClientTest("test_get_user_detail"))
    suite.addTest(CcrClientTest("test_list_accelerator_filters"))
    suite.addTest(CcrClientTest("test_list_chart_versions"))
    suite.addTest(CcrClientTest("test_list_charts"))
    suite.addTest(CcrClientTest("test_list_image_migration_records"))
    suite.addTest(CcrClientTest("test_list_image_migration_rules"))
    suite.addTest(CcrClientTest("test_list_image_migration_task_records"))
    suite.addTest(CcrClientTest("test_list_instance_sync_records"))
    suite.addTest(CcrClientTest("test_list_instance_sync_task_records"))
    suite.addTest(CcrClientTest("test_list_instance_syncs"))
    suite.addTest(CcrClientTest("test_list_instances"))
    suite.addTest(CcrClientTest("test_list_projects"))
    suite.addTest(CcrClientTest("test_list_repositories"))
    suite.addTest(CcrClientTest("test_list_robot_accounts"))
    suite.addTest(CcrClientTest("test_list_tags"))
    suite.addTest(CcrClientTest("test_list_trigger_tasks"))
    suite.addTest(CcrClientTest("test_list_triggers"))
    suite.addTest(CcrClientTest("test_list_vpc_links"))
    suite.addTest(CcrClientTest("test_re_execute_trigger_task"))
    suite.addTest(CcrClientTest("test_refresh_robot_account_key"))
    suite.addTest(CcrClientTest("test_reset_password"))
    suite.addTest(CcrClientTest("test_stop_image_migration"))
    suite.addTest(CcrClientTest("test_stop_instance_sync"))
    suite.addTest(CcrClientTest("test_test_accelerator_filter"))
    suite.addTest(CcrClientTest("test_test_trigger_target_address"))
    suite.addTest(CcrClientTest("test_toggle_accelerator_filter"))
    suite.addTest(CcrClientTest("test_toggle_trigger"))
    suite.addTest(CcrClientTest("test_trigger_tag_scan"))
    suite.addTest(CcrClientTest("test_update_accelerator_filter"))
    suite.addTest(CcrClientTest("test_update_image_migration_rule"))
    suite.addTest(CcrClientTest("test_update_instance_name"))
    suite.addTest(CcrClientTest("test_update_instance_sync"))
    suite.addTest(CcrClientTest("test_update_instance_tags"))
    suite.addTest(CcrClientTest("test_update_public_network"))
    suite.addTest(CcrClientTest("test_update_repository"))
    suite.addTest(CcrClientTest("test_update_robot_account"))
    suite.addTest(CcrClientTest("test_update_trigger"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
