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
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
        self.client = VpcClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_batch_create_ssl_vpn_users(self):
        self.client.batch_create_ssl_vpn_users(None)

    def test_bind_eip(self):
        self.client.bind_eip(None)

    def test_close_vpc_relay(self):
        self.client.close_vpc_relay(None)

    def test_create_ip_reserved(self):
        self.client.create_ip_reserved(None)

    def test_create_ssl_vpn_server(self):
        self.client.create_ssl_vpn_server(None)

    def test_create_subnet(self):
        self.client.create_subnet(None)

    def test_create_user_gateway(self):
        self.client.create_user_gateway(None)

    def test_create_vpc(self):
        self.client.create_vpc(None)

    def test_create_vpn(self):
        self.client.create_vpn(None)

    def test_create_vpn_tunnel(self):
        self.client.create_vpn_tunnel(None)

    def test_delete_ip_reserve(self):
        self.client.delete_ip_reserve(None)

    def test_delete_ssl_vpn_server(self):
        self.client.delete_ssl_vpn_server(None)

    def test_delete_ssl_vpn_user(self):
        self.client.delete_ssl_vpn_user(None)

    def test_delete_subnet(self):
        self.client.delete_subnet(None)

    def test_delete_user_gateway(self):
        self.client.delete_user_gateway(None)

    def test_delete_vpc(self):
        self.client.delete_vpc(None)

    def test_delete_vpn_tunnel(self):
        self.client.delete_vpn_tunnel(None)

    def test_get_vpc_resource_ip_info(self):
        self.client.get_vpc_resource_ip_info(None)

    def test_list_ip_reserve(self):
        self.client.list_ip_reserve(None)

    def test_open_vpc_relay(self):
        self.client.open_vpc_relay(None)

    def test_query_specified_subnet(self):
        self.client.query_specified_subnet(None)

    def test_query_specified_vpc(self):
        self.client.query_specified_vpc(None)

    def test_query_ssl_vpn_server(self):
        self.client.query_ssl_vpn_server(None)

    def test_query_ssl_vpn_users(self):
        self.client.query_ssl_vpn_users(None)

    def test_query_subnet_list(self):
        self.client.query_subnet_list(None)

    def test_query_vpc_intranet_ip(self):
        self.client.query_vpc_intranet_ip(None)

    def test_query_vpc_list(self):
        self.client.query_vpc_list(None)

    def test_query_vpn_list(self):
        self.client.query_vpn_list(None)

    def test_release_vpn(self):
        self.client.release_vpn(None)

    def test_renew_vpn(self):
        self.client.renew_vpn(None)

    def test_search_for_vpn_details(self):
        self.client.search_for_vpn_details(None)

    def test_search_vpn_tunnel(self):
        self.client.search_vpn_tunnel(None)

    def test_unbind_eip(self):
        self.client.unbind_eip(None)

    def test_update_ssl_vpn_server(self):
        self.client.update_ssl_vpn_server(None)

    def test_update_ssl_vpn_users(self):
        self.client.update_ssl_vpn_users(None)

    def test_update_subnet(self):
        self.client.update_subnet(None)

    def test_update_user_gateway(self):
        self.client.update_user_gateway(None)

    def test_update_vpc(self):
        self.client.update_vpc(None)

    def test_update_vpn(self):
        self.client.update_vpn(None)

    def test_update_vpn_release_protection(self):
        self.client.update_vpn_release_protection(None)

    def test_update_vpn_tunnel(self):
        self.client.update_vpn_tunnel(None)

    def test_user_gateway_details(self):
        self.client.user_gateway_details(None)

    def test_user_gateway_list(self):
        self.client.user_gateway_list(None)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(VpcClientTest("test_batch_create_ssl_vpn_users"))
    suite.addTest(VpcClientTest("test_bind_eip"))
    suite.addTest(VpcClientTest("test_close_vpc_relay"))
    suite.addTest(VpcClientTest("test_create_ip_reserved"))
    suite.addTest(VpcClientTest("test_create_ssl_vpn_server"))
    suite.addTest(VpcClientTest("test_create_subnet"))
    suite.addTest(VpcClientTest("test_create_user_gateway"))
    suite.addTest(VpcClientTest("test_create_vpc"))
    suite.addTest(VpcClientTest("test_create_vpn"))
    suite.addTest(VpcClientTest("test_create_vpn_tunnel"))
    suite.addTest(VpcClientTest("test_delete_ip_reserve"))
    suite.addTest(VpcClientTest("test_delete_ssl_vpn_server"))
    suite.addTest(VpcClientTest("test_delete_ssl_vpn_user"))
    suite.addTest(VpcClientTest("test_delete_subnet"))
    suite.addTest(VpcClientTest("test_delete_user_gateway"))
    suite.addTest(VpcClientTest("test_delete_vpc"))
    suite.addTest(VpcClientTest("test_delete_vpn_tunnel"))
    suite.addTest(VpcClientTest("test_get_vpc_resource_ip_info"))
    suite.addTest(VpcClientTest("test_list_ip_reserve"))
    suite.addTest(VpcClientTest("test_open_vpc_relay"))
    suite.addTest(VpcClientTest("test_query_specified_subnet"))
    suite.addTest(VpcClientTest("test_query_specified_vpc"))
    suite.addTest(VpcClientTest("test_query_ssl_vpn_server"))
    suite.addTest(VpcClientTest("test_query_ssl_vpn_users"))
    suite.addTest(VpcClientTest("test_query_subnet_list"))
    suite.addTest(VpcClientTest("test_query_vpc_intranet_ip"))
    suite.addTest(VpcClientTest("test_query_vpc_list"))
    suite.addTest(VpcClientTest("test_query_vpn_list"))
    suite.addTest(VpcClientTest("test_release_vpn"))
    suite.addTest(VpcClientTest("test_renew_vpn"))
    suite.addTest(VpcClientTest("test_search_for_vpn_details"))
    suite.addTest(VpcClientTest("test_search_vpn_tunnel"))
    suite.addTest(VpcClientTest("test_unbind_eip"))
    suite.addTest(VpcClientTest("test_update_ssl_vpn_server"))
    suite.addTest(VpcClientTest("test_update_ssl_vpn_users"))
    suite.addTest(VpcClientTest("test_update_subnet"))
    suite.addTest(VpcClientTest("test_update_user_gateway"))
    suite.addTest(VpcClientTest("test_update_vpc"))
    suite.addTest(VpcClientTest("test_update_vpn"))
    suite.addTest(VpcClientTest("test_update_vpn_release_protection"))
    suite.addTest(VpcClientTest("test_update_vpn_tunnel"))
    suite.addTest(VpcClientTest("test_user_gateway_details"))
    suite.addTest(VpcClientTest("test_user_gateway_list"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
