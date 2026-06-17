import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_sts.api.sts_client import StsClient
from baiducloud_python_sdk_sts import models as sts_models


class StsClientTest(unittest.TestCase):
    """StsClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
        self.client = StsClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_assume_role(self):
        self.client.assume_role(sts_models.AssumeRoleRequest())

    def test_get_session_token(self):
        self.client.get_session_token(sts_models.GetSessionTokenRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(StsClientTest("test_assume_role"))
    suite.addTest(StsClientTest("test_get_session_token"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
