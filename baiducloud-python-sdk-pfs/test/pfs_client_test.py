import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_pfs.api.pfs_client import PfsClient
from baiducloud_python_sdk_pfs import models as pfs_models


class PfsClientTest(unittest.TestCase):
    """PfsClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
        self.client = PfsClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_create_pfs(self):
        self.client.create_pfs(pfs_models.CreatePfsRequest())

    def test_delete_pfs(self):
        self.client.delete_pfs(pfs_models.DeletePfsRequest())

    def test_desc_pfs(self):
        self.client.desc_pfs(pfs_models.DescPfsRequest())

    def test_list_pfs(self):
        self.client.list_pfs(pfs_models.ListPfsRequest())

    def test_update_pfs_tag(self):
        self.client.update_pfs_tag(pfs_models.UpdatePFSTagRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(PfsClientTest("test_create_pfs"))
    suite.addTest(PfsClientTest("test_delete_pfs"))
    suite.addTest(PfsClientTest("test_desc_pfs"))
    suite.addTest(PfsClientTest("test_list_pfs"))
    suite.addTest(PfsClientTest("test_update_pfs_tag"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
