import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_privatezone.api.privatezone_client import PrivatezoneClient
from baiducloud_python_sdk_privatezone import models as privatezone_models


class PrivatezoneClientTest(unittest.TestCase):
    """PrivatezoneClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
        self.client = PrivatezoneClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_add_record(self):
        self.client.add_record(privatezone_models.AddRecordRequest())

    def test_bind_vpc(self):
        self.client.bind_vpc(privatezone_models.BindVpcRequest())

    def test_create_private_zone(self):
        self.client.create_private_zone(privatezone_models.CreatePrivateZoneRequest())

    def test_delete_private_zone(self):
        self.client.delete_private_zone(privatezone_models.DeletePrivateZoneRequest())

    def test_delete_record(self):
        self.client.delete_record(privatezone_models.DeleteRecordRequest())

    def test_disable_record(self):
        self.client.disable_record(privatezone_models.DisableRecordRequest())

    def test_enable_record(self):
        self.client.enable_record(privatezone_models.EnableRecordRequest())

    def test_get_private_zone(self):
        self.client.get_private_zone(privatezone_models.GetPrivateZoneRequest())

    def test_list_private_zone(self):
        self.client.list_private_zone(privatezone_models.ListPrivateZoneRequest())

    def test_list_record(self):
        self.client.list_record(privatezone_models.ListRecordRequest())

    def test_unbind_vpc(self):
        self.client.unbind_vpc(privatezone_models.UnbindVpcRequest())

    def test_update_record(self):
        self.client.update_record(privatezone_models.UpdateRecordRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(PrivatezoneClientTest("test_add_record"))
    suite.addTest(PrivatezoneClientTest("test_bind_vpc"))
    suite.addTest(PrivatezoneClientTest("test_create_private_zone"))
    suite.addTest(PrivatezoneClientTest("test_delete_private_zone"))
    suite.addTest(PrivatezoneClientTest("test_delete_record"))
    suite.addTest(PrivatezoneClientTest("test_disable_record"))
    suite.addTest(PrivatezoneClientTest("test_enable_record"))
    suite.addTest(PrivatezoneClientTest("test_get_private_zone"))
    suite.addTest(PrivatezoneClientTest("test_list_private_zone"))
    suite.addTest(PrivatezoneClientTest("test_list_record"))
    suite.addTest(PrivatezoneClientTest("test_unbind_vpc"))
    suite.addTest(PrivatezoneClientTest("test_update_record"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
