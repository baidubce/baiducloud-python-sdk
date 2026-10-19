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

    def test_batch_configuration_of_instances(self):
        self.client.batch_configuration_of_instances(rds_models.BatchConfigurationOfInstancesRequest())

    def test_binding_tags(self):
        self.client.binding_tags(rds_models.BindingTagsRequest())

    def test_cluster_status_check(self):
        self.client.cluster_status_check(rds_models.ClusterStatusCheckRequest())

    def test_create_a_primary_instance(self):
        self.client.create_a_primary_instance(rds_models.CreateAPrimaryInstanceRequest())

    def test_create_a_proxy_instance(self):
        self.client.create_a_proxy_instance(rds_models.CreateAProxyInstanceRequest())

    def test_create_read_only_instance(self):
        self.client.create_read_only_instance(rds_models.CreateReadOnlyInstanceRequest())

    def test_dial_test_interface(self):
        self.client.dial_test_interface(rds_models.DialTestInterfaceRequest())

    def test_does_the_instance_support_enabling_automatic_expansion(self):
        self.client.does_the_instance_support_enabling_automatic_expansion(
            rds_models.DoesTheInstanceSupportEnablingAutomaticExpansionRequest()
        )

    def test_get_new_purchase_price(self):
        self.client.get_new_purchase_price(rds_models.GetNewPurchasePriceRequest())

    def test_obtain_the_price_difference_of_prepaid_transformer(self):
        self.client.obtain_the_price_difference_of_prepaid_transformer(
            rds_models.ObtainThePriceDifferenceOfPrepaidTransformerRequest()
        )

    def test_query_instance_list(self):
        self.client.query_instance_list(rds_models.QueryInstanceListRequest())

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

    def test_restart_the_instance(self):
        self.client.restart_the_instance(rds_models.RestartTheInstanceRequest())

    def test_retrieve_instance_auto_scaling_config(self):
        self.client.retrieve_instance_auto_scaling_config(rds_models.RetrieveInstanceAutoScalingConfigRequest())

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

    def test_zone_migration(self):
        self.client.zone_migration(rds_models.ZoneMigrationRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(RdsClientTest("test_batch_configuration_of_instances"))
    suite.addTest(RdsClientTest("test_binding_tags"))
    suite.addTest(RdsClientTest("test_cluster_status_check"))
    suite.addTest(RdsClientTest("test_create_a_primary_instance"))
    suite.addTest(RdsClientTest("test_create_a_proxy_instance"))
    suite.addTest(RdsClientTest("test_create_read_only_instance"))
    suite.addTest(RdsClientTest("test_dial_test_interface"))
    suite.addTest(RdsClientTest("test_does_the_instance_support_enabling_automatic_expansion"))
    suite.addTest(RdsClientTest("test_get_new_purchase_price"))
    suite.addTest(RdsClientTest("test_obtain_the_price_difference_of_prepaid_transformer"))
    suite.addTest(RdsClientTest("test_query_instance_list"))
    suite.addTest(RdsClientTest("test_query_subnet_list"))
    suite.addTest(RdsClientTest("test_query_task_list"))
    suite.addTest(RdsClientTest("test_query_the_details_of_the_specified_instance"))
    suite.addTest(RdsClientTest("test_query_the_list_of_available_zones"))
    suite.addTest(RdsClientTest("test_release_instance"))
    suite.addTest(RdsClientTest("test_restart_the_instance"))
    suite.addTest(RdsClientTest("test_retrieve_instance_auto_scaling_config"))
    suite.addTest(RdsClientTest("test_transformation_example"))
    suite.addTest(RdsClientTest("test_update_automatic_storage_expansion_configuration"))
    suite.addTest(RdsClientTest("test_update_instance_connection_information"))
    suite.addTest(RdsClientTest("test_update_instance_name"))
    suite.addTest(RdsClientTest("test_update_instance_public_network_access_status"))
    suite.addTest(RdsClientTest("test_update_instance_synchronization_mode"))
    suite.addTest(RdsClientTest("test_update_time_window"))
    suite.addTest(RdsClientTest("test_zone_migration"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
