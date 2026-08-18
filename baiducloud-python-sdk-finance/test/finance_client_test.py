import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_finance.api.finance_client import FinanceClient
from baiducloud_python_sdk_finance import models as finance_models


class FinanceClientTest(unittest.TestCase):
    """FinanceClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''

        # ==== AK/SK 鉴权 ====
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)

        self.client = FinanceClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_create_renew_resource_rule(self):
        self.client.create_renew_resource_rule(finance_models.CreateRenewResourceRuleRequest())

    def test_get_renew_resource_list(self):
        self.client.get_renew_resource_list(finance_models.GetRenewResourceListRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(FinanceClientTest("test_create_renew_resource_rule"))
    suite.addTest(FinanceClientTest("test_get_renew_resource_list"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
