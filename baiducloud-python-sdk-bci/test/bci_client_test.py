import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_bci.api.bci_client import BciClient
from baiducloud_python_sdk_bci import models as bci_models


class BciClientTest(unittest.TestCase):
    """BciClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
        self.client = BciClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_batch_delete_image_caches(self):
        self.client.batch_delete_image_caches(bci_models.BatchDeleteImageCachesRequest())

    def test_batch_delete_instances(self):
        self.client.batch_delete_instances(bci_models.BatchDeleteInstancesRequest())

    def test_create_image_cache(self):
        self.client.create_image_cache(bci_models.CreateImageCacheRequest())

    def test_create_instance(self):
        self.client.create_instance(bci_models.CreateInstanceRequest())

    def test_delete_instance(self):
        self.client.delete_instance(bci_models.DeleteInstanceRequest())

    def test_get_instance(self):
        self.client.get_instance(bci_models.GetInstanceRequest())

    def test_list_image_caches(self):
        self.client.list_image_caches(bci_models.ListImageCachesRequest())

    def test_list_instances(self):
        self.client.list_instances(bci_models.ListInstancesRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(BciClientTest("test_batch_delete_image_caches"))
    suite.addTest(BciClientTest("test_batch_delete_instances"))
    suite.addTest(BciClientTest("test_create_image_cache"))
    suite.addTest(BciClientTest("test_create_instance"))
    suite.addTest(BciClientTest("test_delete_instance"))
    suite.addTest(BciClientTest("test_get_instance"))
    suite.addTest(BciClientTest("test_list_image_caches"))
    suite.addTest(BciClientTest("test_list_instances"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
