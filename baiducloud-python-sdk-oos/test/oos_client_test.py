import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_oos.api.oos_client import OosClient
from baiducloud_python_sdk_oos import models as oos_models


class OosClientTest(unittest.TestCase):
    """OosClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
        self.client = OosClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_check_template_v2(self):
        self.client.check_template_v2(oos_models.CheckTemplateV2Request())

    def test_create_execution_v2(self):
        self.client.create_execution_v2(oos_models.CreateExecutionV2Request())

    def test_create_template_v2(self):
        self.client.create_template_v2(oos_models.CreateTemplateV2Request())

    def test_delete_template_v2(self):
        self.client.delete_template_v2(oos_models.DeleteTemplateV2Request())

    def test_get_execution_detail_v2(self):
        self.client.get_execution_detail_v2(oos_models.GetExecutionDetailV2Request())

    def test_get_execution_list_v2(self):
        self.client.get_execution_list_v2(oos_models.GetExecutionListV2Request())

    def test_get_operator_list_v2(self):
        self.client.get_operator_list_v2(oos_models.GetOperatorListV2Request())

    def test_get_task_children_list_v2(self):
        self.client.get_task_children_list_v2(oos_models.GetTaskChildrenListV2Request())

    def test_get_task_detail_v2(self):
        self.client.get_task_detail_v2(oos_models.GetTaskDetailV2Request())

    def test_get_template_detail_v2(self):
        self.client.get_template_detail_v2(oos_models.GetTemplateDetailV2Request())

    def test_get_template_list_v2(self):
        self.client.get_template_list_v2(oos_models.GetTemplateListV2Request())

    def test_update_template_v2(self):
        self.client.update_template_v2(oos_models.UpdateTemplateV2Request())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(OosClientTest("test_check_template_v2"))
    suite.addTest(OosClientTest("test_create_execution_v2"))
    suite.addTest(OosClientTest("test_create_template_v2"))
    suite.addTest(OosClientTest("test_delete_template_v2"))
    suite.addTest(OosClientTest("test_get_execution_detail_v2"))
    suite.addTest(OosClientTest("test_get_execution_list_v2"))
    suite.addTest(OosClientTest("test_get_operator_list_v2"))
    suite.addTest(OosClientTest("test_get_task_children_list_v2"))
    suite.addTest(OosClientTest("test_get_task_detail_v2"))
    suite.addTest(OosClientTest("test_get_template_detail_v2"))
    suite.addTest(OosClientTest("test_get_template_list_v2"))
    suite.addTest(OosClientTest("test_update_template_v2"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
