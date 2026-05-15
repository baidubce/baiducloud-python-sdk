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
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
        self.client = CfwClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_query_cfw_list(self):
        self.client.query_cfw_list(cfw_models.QueryCfwListRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CfwClientTest("test_query_cfw_list"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
