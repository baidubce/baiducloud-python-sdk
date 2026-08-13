import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_cfw.api.cfw_client import CfwClient
from baiducloud_python_sdk_cfw import models as cfw_models


class CfwClientTest(unittest.TestCase):
    """CfwClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''

        # ==== AK/SK 鉴权 ====
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)

        self.client = CfwClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_bind_cfw(self):
        self.client.bind_cfw(cfw_models.BindCfwRequest())

    def test_create_cfw(self):
        self.client.create_cfw(cfw_models.CreateCfwRequest())

    def test_create_cfw_rule(self):
        self.client.create_cfw_rule(cfw_models.CreateCfwRuleRequest())

    def test_create_stateless_cfw(self):
        self.client.create_stateless_cfw(cfw_models.CreateStatelessCfwRequest())

    def test_delete_cfw(self):
        self.client.delete_cfw(cfw_models.DeleteCfwRequest())

    def test_delete_cfw_rule(self):
        self.client.delete_cfw_rule(cfw_models.DeleteCfwRuleRequest())

    def test_disable_cfw_protect(self):
        self.client.disable_cfw_protect(cfw_models.DisableCfwProtectRequest())

    def test_enable_cfw_protect(self):
        self.client.enable_cfw_protect(cfw_models.EnableCfwProtectRequest())

    def test_get_cfw(self):
        self.client.get_cfw(cfw_models.GetCfwRequest())

    def test_get_stateless_cfw(self):
        self.client.get_stateless_cfw(cfw_models.GetStatelessCfwRequest())

    def test_list_cfw(self):
        self.client.list_cfw(cfw_models.ListCfwRequest())

    def test_list_protect_instances(self):
        self.client.list_protect_instances(cfw_models.ListProtectInstancesRequest())

    def test_list_stateless_cfw(self):
        self.client.list_stateless_cfw(cfw_models.ListStatelessCfwRequest())

    def test_unbind_cfw(self):
        self.client.unbind_cfw(cfw_models.UnbindCfwRequest())

    def test_update_cfw(self):
        self.client.update_cfw(cfw_models.UpdateCfwRequest())

    def test_update_cfw_rule(self):
        self.client.update_cfw_rule(cfw_models.UpdateCfwRuleRequest())

    def test_update_stateless_cfw(self):
        self.client.update_stateless_cfw(cfw_models.UpdateStatelessCfwRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CfwClientTest("test_bind_cfw"))
    suite.addTest(CfwClientTest("test_create_cfw"))
    suite.addTest(CfwClientTest("test_create_cfw_rule"))
    suite.addTest(CfwClientTest("test_create_stateless_cfw"))
    suite.addTest(CfwClientTest("test_delete_cfw"))
    suite.addTest(CfwClientTest("test_delete_cfw_rule"))
    suite.addTest(CfwClientTest("test_disable_cfw_protect"))
    suite.addTest(CfwClientTest("test_enable_cfw_protect"))
    suite.addTest(CfwClientTest("test_get_cfw"))
    suite.addTest(CfwClientTest("test_get_stateless_cfw"))
    suite.addTest(CfwClientTest("test_list_cfw"))
    suite.addTest(CfwClientTest("test_list_protect_instances"))
    suite.addTest(CfwClientTest("test_list_stateless_cfw"))
    suite.addTest(CfwClientTest("test_unbind_cfw"))
    suite.addTest(CfwClientTest("test_update_cfw"))
    suite.addTest(CfwClientTest("test_update_cfw_rule"))
    suite.addTest(CfwClientTest("test_update_stateless_cfw"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
