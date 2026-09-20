import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_scs.api.scs_client import ScsClient
from baiducloud_python_sdk_scs import models as scs_models


class ScsClientTest(unittest.TestCase):
    """ScsClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''

        # ==== AK/SK 鉴权 ====
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)

        self.client = ScsClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_instance_list(self):
        self.client.instance_list(scs_models.InstanceListRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ScsClientTest("test_instance_list"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
