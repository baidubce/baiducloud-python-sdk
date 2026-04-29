import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_privatezone.api.privatezone_client import PrivatezoneClient


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

    def test_add_parsing_records(self):
        self.client.add_parsing_records(None)

    def test_associate_vpc(self):
        self.client.associate_vpc(None)

    def test_create_a_private_zone(self):
        self.client.create_a_private_zone(None)

    def test_delete_parsing_records(self):
        self.client.delete_parsing_records(None)

    def test_delete_private_zone(self):
        self.client.delete_private_zone(None)

    def test_disassociate_vpc(self):
        self.client.disassociate_vpc(None)

    def test_modify_parsing_records(self):
        self.client.modify_parsing_records(None)

    def test_query_and_parse_record_list(self):
        self.client.query_and_parse_record_list(None)

    def test_query_the_list_of_private_zones(self):
        self.client.query_the_list_of_private_zones(None)

    def test_search_for_details_of_privatzone(self):
        self.client.search_for_details_of_privatzone(None)

    def test_set_parsing_record_status(self):
        self.client.set_parsing_record_status(None)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(PrivatezoneClientTest("test_add_parsing_records"))
    suite.addTest(PrivatezoneClientTest("test_associate_vpc"))
    suite.addTest(PrivatezoneClientTest("test_create_a_private_zone"))
    suite.addTest(PrivatezoneClientTest("test_delete_parsing_records"))
    suite.addTest(PrivatezoneClientTest("test_delete_private_zone"))
    suite.addTest(PrivatezoneClientTest("test_disassociate_vpc"))
    suite.addTest(PrivatezoneClientTest("test_modify_parsing_records"))
    suite.addTest(PrivatezoneClientTest("test_query_and_parse_record_list"))
    suite.addTest(PrivatezoneClientTest("test_query_the_list_of_private_zones"))
    suite.addTest(PrivatezoneClientTest("test_search_for_details_of_privatzone"))
    suite.addTest(PrivatezoneClientTest("test_set_parsing_record_status"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
