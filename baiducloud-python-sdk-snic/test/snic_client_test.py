import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_snic.api.snic_client import SnicClient
from baiducloud_python_sdk_snic import models as snic_models


class SnicClientTest(unittest.TestCase):
    """SnicClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
        self.client = SnicClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_create_snic(self):
        self.client.create_snic(snic_models.CreateSnicRequest())

    def test_delete_snic(self):
        self.client.delete_snic(snic_models.DeleteSnicRequest())

    def test_describe_snic(self):
        self.client.describe_snic(snic_models.DescribeSnicRequest())

    def test_list_snic(self):
        self.client.list_snic(snic_models.ListSnicRequest())

    def test_query_available_public_services(self):
        self.client.query_available_public_services()

    def test_update_snic(self):
        self.client.update_snic(snic_models.UpdateSnicRequest())

    def test_update_snic_esg(self):
        self.client.update_snic_esg(snic_models.UpdateSnicEsgRequest())

    def test_update_snic_sg(self):
        self.client.update_snic_sg(snic_models.UpdateSnicSgRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(SnicClientTest("test_create_snic"))
    suite.addTest(SnicClientTest("test_delete_snic"))
    suite.addTest(SnicClientTest("test_describe_snic"))
    suite.addTest(SnicClientTest("test_list_snic"))
    suite.addTest(SnicClientTest("test_query_available_public_services"))
    suite.addTest(SnicClientTest("test_update_snic"))
    suite.addTest(SnicClientTest("test_update_snic_esg"))
    suite.addTest(SnicClientTest("test_update_snic_sg"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
