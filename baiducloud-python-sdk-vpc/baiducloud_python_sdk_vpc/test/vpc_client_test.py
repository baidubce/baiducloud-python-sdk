import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_vpc.api.vpc_client import VpcClient


class VpcClientTest(unittest.TestCase):
    """VpcClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK),
        endpoint=HOST)
        self.client = VpcClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_close_vpc_relay(self):
        self.client.close_vpc_relay(None)

    def test_create_a_reserved_network_segment(self):
        self.client.create_a_reserved_network_segment(None)

    def test_create_subnet(self):
        self.client.create_subnet(None)

    def test_create_vpc(self):
        self.client.create_vpc(None)

    def test_delete_reserved_network_segment(self):
        self.client.delete_reserved_network_segment(None)

    def test_delete_subnet(self):
        self.client.delete_subnet(None)

    def test_delete_vpc(self):
        self.client.delete_vpc(None)

    def test_enable_vpc_relay(self):
        self.client.enable_vpc_relay(None)

    def test_query_specified_subnet(self):
        self.client.query_specified_subnet(None)

    def test_query_specified_vpc(self):
        self.client.query_specified_vpc(None)

    def test_query_subnet_list(self):
        self.client.query_subnet_list(None)

    def test_query_the_ip_addresses_occupied_by_products_within_vpc(self):
        self.client.query_the_ip_addresses_occupied_by_products_within_vpc(None)

    def test_query_the_reserved_network_segment_list(self):
        self.client.query_the_reserved_network_segment_list(None)

    def test_query_vpc_intranet_ip(self):
        self.client.query_vpc_intranet_ip(None)

    def test_query_vpc_list(self):
        self.client.query_vpc_list(None)

    def test_update_subnet(self):
        self.client.update_subnet(None)

    def test_update_vpc(self):
        self.client.update_vpc(None)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(VpcClientTest("test_close_vpc_relay"))
    suite.addTest(VpcClientTest("test_create_a_reserved_network_segment"))
    suite.addTest(VpcClientTest("test_create_subnet"))
    suite.addTest(VpcClientTest("test_create_vpc"))
    suite.addTest(VpcClientTest("test_delete_reserved_network_segment"))
    suite.addTest(VpcClientTest("test_delete_subnet"))
    suite.addTest(VpcClientTest("test_delete_vpc"))
    suite.addTest(VpcClientTest("test_enable_vpc_relay"))
    suite.addTest(VpcClientTest("test_query_specified_subnet"))
    suite.addTest(VpcClientTest("test_query_specified_vpc"))
    suite.addTest(VpcClientTest("test_query_subnet_list"))
    suite.addTest(VpcClientTest("test_query_the_ip_addresses_occupied_by_products_within_vpc"))
    suite.addTest(VpcClientTest("test_query_the_reserved_network_segment_list"))
    suite.addTest(VpcClientTest("test_query_vpc_intranet_ip"))
    suite.addTest(VpcClientTest("test_query_vpc_list"))
    suite.addTest(VpcClientTest("test_update_subnet"))
    suite.addTest(VpcClientTest("test_update_vpc"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
