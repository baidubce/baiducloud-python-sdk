import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_as.api.as_client import AsClient
from baiducloud_python_sdk_as import models as as_models


class AsClientTest(unittest.TestCase):
    """AsClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
        self.client = AsClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_adjust_num_v2(self):
        self.client.adjust_num_v2(as_models.AdjustNumV2Request())

    def test_attach_node_v2(self):
        self.client.attach_node_v2(as_models.AttachNodeV2Request())

    def test_create_as_group_v2(self):
        self.client.create_as_group_v2(as_models.CreateAsGroupV2Request())

    def test_create_rule_v2(self):
        self.client.create_rule_v2(as_models.CreateRuleV2Request())

    def test_delete_as_group_v2(self):
        self.client.delete_as_group_v2(as_models.DeleteAsGroupV2Request())

    def test_delete_rule_v2(self):
        self.client.delete_rule_v2(as_models.DeleteRuleV2Request())

    def test_detach_node_v2(self):
        self.client.detach_node_v2(as_models.DetachNodeV2Request())

    def test_exec_rule_v2(self):
        self.client.exec_rule_v2(as_models.ExecRuleV2Request())

    def test_get_as_group_v2(self):
        self.client.get_as_group_v2(as_models.GetAsGroupV2Request())

    def test_get_rule_v2(self):
        self.client.get_rule_v2(as_models.GetRuleV2Request())

    def test_list_as_group_v2(self):
        self.client.list_as_group_v2(as_models.ListAsGroupV2Request())

    def test_list_as_node_v2(self):
        self.client.list_as_node_v2(as_models.ListAsNodeV2Request())

    def test_list_rule_v2(self):
        self.client.list_rule_v2(as_models.ListRuleV2Request())

    def test_list_task_v2(self):
        self.client.list_task_v2(as_models.ListTaskV2Request())

    def test_scaling_down_v2(self):
        self.client.scaling_down_v2(as_models.ScalingDownV2Request())

    def test_scaling_up_v2(self):
        self.client.scaling_up_v2(as_models.ScalingUpV2Request())

    def test_update_is_managed_v2(self):
        self.client.update_is_managed_v2(as_models.UpdateIsManagedV2Request())

    def test_update_protect_v2(self):
        self.client.update_protect_v2(as_models.UpdateProtectV2Request())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(AsClientTest("test_adjust_num_v2"))
    suite.addTest(AsClientTest("test_attach_node_v2"))
    suite.addTest(AsClientTest("test_create_as_group_v2"))
    suite.addTest(AsClientTest("test_create_rule_v2"))
    suite.addTest(AsClientTest("test_delete_as_group_v2"))
    suite.addTest(AsClientTest("test_delete_rule_v2"))
    suite.addTest(AsClientTest("test_detach_node_v2"))
    suite.addTest(AsClientTest("test_exec_rule_v2"))
    suite.addTest(AsClientTest("test_get_as_group_v2"))
    suite.addTest(AsClientTest("test_get_rule_v2"))
    suite.addTest(AsClientTest("test_list_as_group_v2"))
    suite.addTest(AsClientTest("test_list_as_node_v2"))
    suite.addTest(AsClientTest("test_list_rule_v2"))
    suite.addTest(AsClientTest("test_list_task_v2"))
    suite.addTest(AsClientTest("test_scaling_down_v2"))
    suite.addTest(AsClientTest("test_scaling_up_v2"))
    suite.addTest(AsClientTest("test_update_is_managed_v2"))
    suite.addTest(AsClientTest("test_update_protect_v2"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
