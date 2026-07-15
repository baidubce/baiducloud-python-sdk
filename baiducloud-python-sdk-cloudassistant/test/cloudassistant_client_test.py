import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_cloudassistant.api.cloudassistant_client import CloudassistantClient
from baiducloud_python_sdk_cloudassistant import models as cloudassistant_models


class CloudassistantClientTest(unittest.TestCase):
    """CloudassistantClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
        self.client = CloudassistantClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_action_list(self):
        self.client.action_list(cloudassistant_models.ActionListRequest())

    def test_action_log(self):
        self.client.action_log(cloudassistant_models.ActionLogRequest())

    def test_action_run(self):
        self.client.action_run(cloudassistant_models.ActionRunRequest())

    def test_action_run_list(self):
        self.client.action_run_list(cloudassistant_models.ActionRunListRequest())

    def test_batch_get_agent(self):
        self.client.batch_get_agent(cloudassistant_models.BatchGetAgentRequest())

    def test_create_action(self):
        self.client.create_action(cloudassistant_models.CreateActionRequest())

    def test_delete_action(self):
        self.client.delete_action(cloudassistant_models.DeleteActionRequest())

    def test_get_action(self):
        self.client.get_action(cloudassistant_models.GetActionRequest())

    def test_get_action_run(self):
        self.client.get_action_run(cloudassistant_models.GetActionRunRequest())

    def test_update_action(self):
        self.client.update_action(cloudassistant_models.UpdateActionRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CloudassistantClientTest("test_action_list"))
    suite.addTest(CloudassistantClientTest("test_action_log"))
    suite.addTest(CloudassistantClientTest("test_action_run"))
    suite.addTest(CloudassistantClientTest("test_action_run_list"))
    suite.addTest(CloudassistantClientTest("test_batch_get_agent"))
    suite.addTest(CloudassistantClientTest("test_create_action"))
    suite.addTest(CloudassistantClientTest("test_delete_action"))
    suite.addTest(CloudassistantClientTest("test_get_action"))
    suite.addTest(CloudassistantClientTest("test_get_action_run"))
    suite.addTest(CloudassistantClientTest("test_update_action"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
