import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_rds.api.rds_client import RdsClient
from baiducloud_python_sdk_rds import models as rds_models


class RdsClientTest(unittest.TestCase):
    """RdsClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''

        # ==== AK/SK 鉴权 ====
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)

        self.client = RdsClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_add_account_api_at_table_granularity(self):
        self.client.add_account_api_at_table_granularity(rds_models.AddAccountApiAtTableGranularityRequest())

    def test_batch_configuration_of_instances(self):
        self.client.batch_configuration_of_instances(rds_models.BatchConfigurationOfInstancesRequest())

    def test_binding_tags(self):
        self.client.binding_tags(rds_models.BindingTagsRequest())

    def test_change_account_password(self):
        self.client.change_account_password(rds_models.ChangeAccountPasswordRequest())

    def test_check_the_whitelist(self):
        self.client.check_the_whitelist(rds_models.CheckTheWhitelistRequest())

    def test_cluster_status_check(self):
        self.client.cluster_status_check(rds_models.ClusterStatusCheckRequest())

    def test_copy_parameter_template(self):
        self.client.copy_parameter_template(rds_models.CopyParameterTemplateRequest())

    def test_create_a_database(self):
        self.client.create_a_database(rds_models.CreateADatabaseRequest())

    def test_create_a_primary_instance(self):
        self.client.create_a_primary_instance(rds_models.CreateAPrimaryInstanceRequest())

    def test_create_a_proxy_instance(self):
        self.client.create_a_proxy_instance(rds_models.CreateAProxyInstanceRequest())

    def test_create_account(self):
        self.client.create_account(rds_models.CreateAccountRequest())

    def test_create_read_only_instance(self):
        self.client.create_read_only_instance(rds_models.CreateReadOnlyInstanceRequest())

    def test_delete_account(self):
        self.client.delete_account(rds_models.DeleteAccountRequest())

    def test_delete_the_database(self):
        self.client.delete_the_database(rds_models.DeleteTheDatabaseRequest())

    def test_delete_the_specified_backup_set(self):
        self.client.delete_the_specified_backup_set(rds_models.DeleteTheSpecifiedBackupSetRequest())

    def test_dial_test_interface(self):
        self.client.dial_test_interface(rds_models.DialTestInterfaceRequest())

    def test_does_the_instance_support_enabling_automatic_expansion(self):
        self.client.does_the_instance_support_enabling_automatic_expansion(
            rds_models.DoesTheInstanceSupportEnablingAutomaticExpansionRequest()
        )

    def test_error_log_download_details(self):
        self.client.error_log_download_details(rds_models.ErrorLogDownloadDetailsRequest())

    def test_error_log_list(self):
        self.client.error_log_list(rds_models.ErrorLogListRequest())

    def test_get_parameter_template_details(self):
        self.client.get_parameter_template_details(rds_models.GetParameterTemplateDetailsRequest())

    def test_get_parameter_template_list(self):
        self.client.get_parameter_template_list(rds_models.GetParameterTemplateListRequest())

    def test_get_pg_log_details(self):
        self.client.get_pg_log_details(rds_models.GetPgLogDetailsRequest())

    def test_get_pg_log_list(self):
        self.client.get_pg_log_list(rds_models.GetPgLogListRequest())

    def test_instance_enables_automatic_renewal(self):
        self.client.instance_enables_automatic_renewal(rds_models.InstanceEnablesAutomaticRenewalRequest())

    def test_manually_initiate_full_physical_backup(self):
        self.client.manually_initiate_full_physical_backup(rds_models.ManuallyInitiateFullPhysicalBackupRequest())

    def test_modify_account_notes(self):
        self.client.modify_account_notes(rds_models.ModifyAccountNotesRequest())

    def test_modify_account_permissions(self):
        self.client.modify_account_permissions(rds_models.ModifyAccountPermissionsRequest())

    def test_modify_backup_strategy(self):
        self.client.modify_backup_strategy(rds_models.ModifyBackupStrategyRequest())

    def test_modify_configuration_parameters(self):
        self.client.modify_configuration_parameters(rds_models.ModifyConfigurationParametersRequest())

    def test_modify_database_port(self):
        self.client.modify_database_port(rds_models.ModifyDatabasePortRequest())

    def test_modify_description_information(self):
        self.client.modify_description_information(rds_models.ModifyDescriptionInformationRequest())

    def test_obtain_binlog_information(self):
        self.client.obtain_binlog_information(rds_models.ObtainBinlogInformationRequest())

    def test_obtain_ssl_encryption_certificate(self):
        self.client.obtain_ssl_encryption_certificate()

    def test_obtain_ssl_encryption_information(self):
        self.client.obtain_ssl_encryption_information(rds_models.ObtainSslEncryptionInformationRequest())

    def test_query_account_details(self):
        self.client.query_account_details(rds_models.QueryAccountDetailsRequest())

    def test_query_account_list(self):
        self.client.query_account_list(rds_models.QueryAccountListRequest())

    def test_query_and_modify_history(self):
        self.client.query_and_modify_history(rds_models.QueryAndModifyHistoryRequest())

    def test_query_backup_details(self):
        self.client.query_backup_details(rds_models.QueryBackupDetailsRequest())

    def test_query_backup_list(self):
        self.client.query_backup_list(rds_models.QueryBackupListRequest())

    def test_query_instance_list(self):
        self.client.query_instance_list(rds_models.QueryInstanceListRequest())

    def test_query_parameter_list(self):
        self.client.query_parameter_list(rds_models.QueryParameterListRequest())

    def test_query_subnet_list(self):
        self.client.query_subnet_list(rds_models.QuerySubnetListRequest())

    def test_query_task_list(self):
        self.client.query_task_list(rds_models.QueryTaskListRequest())

    def test_query_the_details_of_the_specified_instance(self):
        self.client.query_the_details_of_the_specified_instance(
            rds_models.QueryTheDetailsOfTheSpecifiedInstanceRequest()
        )

    def test_query_the_list_of_available_zones(self):
        self.client.query_the_list_of_available_zones()

    def test_release_instance(self):
        self.client.release_instance(rds_models.ReleaseInstanceRequest())

    def test_renewal_example(self):
        self.client.renewal_example(rds_models.RenewalExampleRequest())

    def test_restart_the_instance(self):
        self.client.restart_the_instance(rds_models.RestartTheInstanceRequest())

    def test_restore_library_tables_based_on_backup_sets(self):
        self.client.restore_library_tables_based_on_backup_sets(
            rds_models.RestoreLibraryTablesBasedOnBackupSetsRequest()
        )

    def test_restore_the_database_table_by_time_point(self):
        self.client.restore_the_database_table_by_time_point(rds_models.RestoreTheDatabaseTableByTimePointRequest())

    def test_retrieve_database_list(self):
        self.client.retrieve_database_list(rds_models.RetrieveDatabaseListRequest())

    def test_retrieve_instance_auto_scaling_config(self):
        self.client.retrieve_instance_auto_scaling_config(rds_models.RetrieveInstanceAutoScalingConfigRequest())

    def test_retrieve_the_binlog_list(self):
        self.client.retrieve_the_binlog_list(rds_models.RetrieveTheBinlogListRequest())

    def test_set_encryption_policy_api(self):
        self.client.set_encryption_policy_api(rds_models.SetEncryptionPolicyApiRequest())

    def test_slow_log_download_details(self):
        self.client.slow_log_download_details(rds_models.SlowLogDownloadDetailsRequest())

    def test_slow_log_list(self):
        self.client.slow_log_list(rds_models.SlowLogListRequest())

    def test_table_granularity_query_user_details_api(self):
        self.client.table_granularity_query_user_details_api(rds_models.TableGranularityQueryUserDetailsApiRequest())

    def test_table_granularity_query_user_list_api(self):
        self.client.table_granularity_query_user_list_api(rds_models.TableGranularityQueryUserListApiRequest())

    def test_table_granularity_update_user_description_api(self):
        self.client.table_granularity_update_user_description_api(
            rds_models.TableGranularityUpdateUserDescriptionApiRequest()
        )

    def test_target_region_mapping_list_api(self):
        self.client.target_region_mapping_list_api(rds_models.TargetRegionMappingListApiRequest())

    def test_transformation_example(self):
        self.client.transformation_example(rds_models.TransformationExampleRequest())

    def test_update_automatic_storage_expansion_configuration(self):
        self.client.update_automatic_storage_expansion_configuration(
            rds_models.UpdateAutomaticStorageExpansionConfigurationRequest()
        )

    def test_update_instance_connection_information(self):
        self.client.update_instance_connection_information(rds_models.UpdateInstanceConnectionInformationRequest())

    def test_update_instance_name(self):
        self.client.update_instance_name(rds_models.UpdateInstanceNameRequest())

    def test_update_instance_public_network_access_status(self):
        self.client.update_instance_public_network_access_status(
            rds_models.UpdateInstancePublicNetworkAccessStatusRequest()
        )

    def test_update_instance_synchronization_mode(self):
        self.client.update_instance_synchronization_mode(rds_models.UpdateInstanceSynchronizationModeRequest())

    def test_update_time_window(self):
        self.client.update_time_window(rds_models.UpdateTimeWindowRequest())

    def test_update_whitelist(self):
        self.client.update_whitelist(rds_models.UpdateWhitelistRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(RdsClientTest("test_add_account_api_at_table_granularity"))
    suite.addTest(RdsClientTest("test_batch_configuration_of_instances"))
    suite.addTest(RdsClientTest("test_binding_tags"))
    suite.addTest(RdsClientTest("test_change_account_password"))
    suite.addTest(RdsClientTest("test_check_the_whitelist"))
    suite.addTest(RdsClientTest("test_cluster_status_check"))
    suite.addTest(RdsClientTest("test_copy_parameter_template"))
    suite.addTest(RdsClientTest("test_create_a_database"))
    suite.addTest(RdsClientTest("test_create_a_primary_instance"))
    suite.addTest(RdsClientTest("test_create_a_proxy_instance"))
    suite.addTest(RdsClientTest("test_create_account"))
    suite.addTest(RdsClientTest("test_create_read_only_instance"))
    suite.addTest(RdsClientTest("test_delete_account"))
    suite.addTest(RdsClientTest("test_delete_the_database"))
    suite.addTest(RdsClientTest("test_delete_the_specified_backup_set"))
    suite.addTest(RdsClientTest("test_dial_test_interface"))
    suite.addTest(RdsClientTest("test_does_the_instance_support_enabling_automatic_expansion"))
    suite.addTest(RdsClientTest("test_error_log_download_details"))
    suite.addTest(RdsClientTest("test_error_log_list"))
    suite.addTest(RdsClientTest("test_get_parameter_template_details"))
    suite.addTest(RdsClientTest("test_get_parameter_template_list"))
    suite.addTest(RdsClientTest("test_get_pg_log_details"))
    suite.addTest(RdsClientTest("test_get_pg_log_list"))
    suite.addTest(RdsClientTest("test_instance_enables_automatic_renewal"))
    suite.addTest(RdsClientTest("test_manually_initiate_full_physical_backup"))
    suite.addTest(RdsClientTest("test_modify_account_notes"))
    suite.addTest(RdsClientTest("test_modify_account_permissions"))
    suite.addTest(RdsClientTest("test_modify_backup_strategy"))
    suite.addTest(RdsClientTest("test_modify_configuration_parameters"))
    suite.addTest(RdsClientTest("test_modify_database_port"))
    suite.addTest(RdsClientTest("test_modify_description_information"))
    suite.addTest(RdsClientTest("test_obtain_binlog_information"))
    suite.addTest(RdsClientTest("test_obtain_ssl_encryption_certificate"))
    suite.addTest(RdsClientTest("test_obtain_ssl_encryption_information"))
    suite.addTest(RdsClientTest("test_query_account_details"))
    suite.addTest(RdsClientTest("test_query_account_list"))
    suite.addTest(RdsClientTest("test_query_and_modify_history"))
    suite.addTest(RdsClientTest("test_query_backup_details"))
    suite.addTest(RdsClientTest("test_query_backup_list"))
    suite.addTest(RdsClientTest("test_query_instance_list"))
    suite.addTest(RdsClientTest("test_query_parameter_list"))
    suite.addTest(RdsClientTest("test_query_subnet_list"))
    suite.addTest(RdsClientTest("test_query_task_list"))
    suite.addTest(RdsClientTest("test_query_the_details_of_the_specified_instance"))
    suite.addTest(RdsClientTest("test_query_the_list_of_available_zones"))
    suite.addTest(RdsClientTest("test_release_instance"))
    suite.addTest(RdsClientTest("test_renewal_example"))
    suite.addTest(RdsClientTest("test_restart_the_instance"))
    suite.addTest(RdsClientTest("test_restore_library_tables_based_on_backup_sets"))
    suite.addTest(RdsClientTest("test_restore_the_database_table_by_time_point"))
    suite.addTest(RdsClientTest("test_retrieve_database_list"))
    suite.addTest(RdsClientTest("test_retrieve_instance_auto_scaling_config"))
    suite.addTest(RdsClientTest("test_retrieve_the_binlog_list"))
    suite.addTest(RdsClientTest("test_set_encryption_policy_api"))
    suite.addTest(RdsClientTest("test_slow_log_download_details"))
    suite.addTest(RdsClientTest("test_slow_log_list"))
    suite.addTest(RdsClientTest("test_table_granularity_query_user_details_api"))
    suite.addTest(RdsClientTest("test_table_granularity_query_user_list_api"))
    suite.addTest(RdsClientTest("test_table_granularity_update_user_description_api"))
    suite.addTest(RdsClientTest("test_target_region_mapping_list_api"))
    suite.addTest(RdsClientTest("test_transformation_example"))
    suite.addTest(RdsClientTest("test_update_automatic_storage_expansion_configuration"))
    suite.addTest(RdsClientTest("test_update_instance_connection_information"))
    suite.addTest(RdsClientTest("test_update_instance_name"))
    suite.addTest(RdsClientTest("test_update_instance_public_network_access_status"))
    suite.addTest(RdsClientTest("test_update_instance_synchronization_mode"))
    suite.addTest(RdsClientTest("test_update_time_window"))
    suite.addTest(RdsClientTest("test_update_whitelist"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
