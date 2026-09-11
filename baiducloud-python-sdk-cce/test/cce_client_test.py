import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_cce.api.cce_client import CceClient
from baiducloud_python_sdk_cce import models as cce_models


class CceClientTest(unittest.TestCase):
    """CceClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''

        # ==== AK/SK 鉴权 ====
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)

        self.client = CceClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_create_a_shrinking_node_group_task_v2(self):
        self.client.create_a_shrinking_node_group_task_v2(cce_models.CreateAShrinkingNodeGroupTaskV2Request())

    def test_create_an_autoscaler_v2(self):
        self.client.create_an_autoscaler_v2(cce_models.CreateAnAutoscalerV2Request())

    def test_create_expansion_node_group_task_v2(self):
        self.client.create_expansion_node_group_task_v2(cce_models.CreateExpansionNodeGroupTaskV2Request())

    def test_create_node_group_v2(self):
        self.client.create_node_group_v2(cce_models.CreateNodeGroupV2Request())

    def test_delete_node_group_v2(self):
        self.client.delete_node_group_v2(cce_models.DeleteNodeGroupV2Request())

    def test_delete_nodes_cluster_scaling_v2(self):
        self.client.delete_nodes_cluster_scaling_v2(cce_models.DeleteNodesClusterScalingV2Request())

    def test_get_node_details_v2(self):
        self.client.get_node_details_v2(cce_models.GetNodeDetailsV2Request())

    def test_get_node_group_details_v2(self):
        self.client.get_node_group_details_v2(cce_models.GetNodeGroupDetailsV2Request())

    def test_get_package_list_v2(self):
        self.client.get_package_list_v2(cce_models.GetPackageListV2Request())

    def test_get_task_list_v2(self):
        self.client.get_task_list_v2(cce_models.GetTaskListV2Request())

    def test_get_the_list_of_cluster_node_groups_v2(self):
        self.client.get_the_list_of_cluster_node_groups_v2(cce_models.GetTheListOfClusterNodeGroupsV2Request())

    def test_get_the_list_of_cluster_nodes_v2(self):
        self.client.get_the_list_of_cluster_nodes_v2(cce_models.GetTheListOfClusterNodesV2Request())

    def test_modify_ig_auto_scaler(self):
        self.client.modify_ig_auto_scaler(cce_models.ModifyIGAutoScalerRequest())

    def test_modify_node_group_node_shrink_protection_status_v2(self):
        self.client.modify_node_group_node_shrink_protection_status_v2(
            cce_models.ModifyNodeGroupNodeShrinkProtectionStatusV2Request()
        )

    def test_modify_the_number_of_node_replicas_in_a_node_group_v2(self):
        self.client.modify_the_number_of_node_replicas_in_a_node_group_v2(
            cce_models.ModifyTheNumberOfNodeReplicasInANodeGroupV2Request()
        )

    def test_move_into_an_existing_node_v2(self):
        self.client.move_into_an_existing_node_v2(cce_models.MoveIntoAnExistingNodeV2Request())

    def test_query_the_configuration_of_autoscaler_v2(self):
        self.client.query_the_configuration_of_autoscaler_v2(cce_models.QueryTheConfigurationOfAutoscalerV2Request())

    def test_retrieve_the_node_group_node_list_v2(self):
        self.client.retrieve_the_node_group_node_list_v2(cce_models.RetrieveTheNodeGroupNodeListV2Request())

    def test_steps_to_obtain_node_events_v2(self):
        self.client.steps_to_obtain_node_events_v2(cce_models.StepsToObtainNodeEventsV2Request())

    def test_synchronize_node_metadata_v2(self):
        self.client.synchronize_node_metadata_v2(cce_models.SynchronizeNodeMetadataV2Request())

    def test_update_autoscaler_configuration_v2(self):
        self.client.update_autoscaler_configuration_v2(cce_models.UpdateAutoscalerConfigurationV2Request())

    def test_update_node_attributes_v2(self):
        self.client.update_node_attributes_v2(cce_models.UpdateNodeAttributesV2Request())

    def test_view_task_details_v2(self):
        self.client.view_task_details_v2(cce_models.ViewTaskDetailsV2Request())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CceClientTest("test_create_a_shrinking_node_group_task_v2"))
    suite.addTest(CceClientTest("test_create_an_autoscaler_v2"))
    suite.addTest(CceClientTest("test_create_expansion_node_group_task_v2"))
    suite.addTest(CceClientTest("test_create_node_group_v2"))
    suite.addTest(CceClientTest("test_delete_node_group_v2"))
    suite.addTest(CceClientTest("test_delete_nodes_cluster_scaling_v2"))
    suite.addTest(CceClientTest("test_get_node_details_v2"))
    suite.addTest(CceClientTest("test_get_node_group_details_v2"))
    suite.addTest(CceClientTest("test_get_package_list_v2"))
    suite.addTest(CceClientTest("test_get_task_list_v2"))
    suite.addTest(CceClientTest("test_get_the_list_of_cluster_node_groups_v2"))
    suite.addTest(CceClientTest("test_get_the_list_of_cluster_nodes_v2"))
    suite.addTest(CceClientTest("test_modify_ig_auto_scaler"))
    suite.addTest(CceClientTest("test_modify_node_group_node_shrink_protection_status_v2"))
    suite.addTest(CceClientTest("test_modify_the_number_of_node_replicas_in_a_node_group_v2"))
    suite.addTest(CceClientTest("test_move_into_an_existing_node_v2"))
    suite.addTest(CceClientTest("test_query_the_configuration_of_autoscaler_v2"))
    suite.addTest(CceClientTest("test_retrieve_the_node_group_node_list_v2"))
    suite.addTest(CceClientTest("test_steps_to_obtain_node_events_v2"))
    suite.addTest(CceClientTest("test_synchronize_node_metadata_v2"))
    suite.addTest(CceClientTest("test_update_autoscaler_configuration_v2"))
    suite.addTest(CceClientTest("test_update_node_attributes_v2"))
    suite.addTest(CceClientTest("test_view_task_details_v2"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
