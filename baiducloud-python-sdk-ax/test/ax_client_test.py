import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_ax.api.ax_client import AxClient
from baiducloud_python_sdk_ax import models as ax_models


class AxClientTest(unittest.TestCase):
    """AxClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
        self.client = AxClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_query_sandboxes(self):
        self.client.query_sandboxes(ax_models.QuerySandboxesRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(AxClientTest("test_query_sandboxes"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
