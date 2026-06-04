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

    def test_bind_vpc_to_rule(self):
        self.client.bind_vpc_to_rule(privatezone_models.BindVpcToRuleRequest())

    def test_create_private_zone(self):
        self.client.create_private_zone(privatezone_models.CreatePrivateZoneRequest())

    def test_create_resolver(self):
        self.client.create_resolver(privatezone_models.CreateResolverRequest())

    def test_create_resolver_rule(self):
        self.client.create_resolver_rule(privatezone_models.CreateResolverRuleRequest())

    def test_delete_private_zone(self):
        self.client.delete_private_zone(privatezone_models.DeletePrivateZoneRequest())

    def test_delete_record(self):
        self.client.delete_record(privatezone_models.DeleteRecordRequest())

    def test_delete_resolver(self):
        self.client.delete_resolver(privatezone_models.DeleteResolverRequest())

    def test_delete_resolver_rule(self):
        self.client.delete_resolver_rule(privatezone_models.DeleteResolverRuleRequest())

    def test_disable_record(self):
        self.client.disable_record(privatezone_models.DisableRecordRequest())

    def test_enable_record(self):
        self.client.enable_record(privatezone_models.EnableRecordRequest())

    def test_get_dns_resolver_detail(self):
        self.client.get_dns_resolver_detail(privatezone_models.GetDnsResolverDetailRequest())

    def test_get_dns_resolver_list(self):
        self.client.get_dns_resolver_list(privatezone_models.GetDnsResolverListRequest())

    def test_get_dns_resolver_rule_detail(self):
        self.client.get_dns_resolver_rule_detail(privatezone_models.GetDnsResolverRuleDetailRequest())

    def test_get_dns_resolver_rule_list(self):
        self.client.get_dns_resolver_rule_list(privatezone_models.GetDnsResolverRuleListRequest())

    def test_get_private_zone(self):
        self.client.get_private_zone(privatezone_models.GetPrivateZoneRequest())

    def test_list_private_zone(self):
        self.client.list_private_zone(privatezone_models.ListPrivateZoneRequest())

    def test_list_record(self):
        self.client.list_record(privatezone_models.ListRecordRequest())

    def test_unbind_vpc(self):
        self.client.unbind_vpc(privatezone_models.UnbindVpcRequest())

    def test_unbind_vpc_to_rule(self):
        self.client.unbind_vpc_to_rule(privatezone_models.UnbindVpcToRuleRequest())

    def test_update_dns_parser(self):
        self.client.update_dns_parser(privatezone_models.UpdateDnsParserRequest())

    def test_update_record(self):
        self.client.update_record(privatezone_models.UpdateRecordRequest())

    def test_update_resolver_rule(self):
        self.client.update_resolver_rule(privatezone_models.UpdateResolverRuleRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(PrivatezoneClientTest("test_add_record"))
    suite.addTest(PrivatezoneClientTest("test_bind_vpc"))
    suite.addTest(PrivatezoneClientTest("test_bind_vpc_to_rule"))
    suite.addTest(PrivatezoneClientTest("test_create_private_zone"))
    suite.addTest(PrivatezoneClientTest("test_create_resolver"))
    suite.addTest(PrivatezoneClientTest("test_create_resolver_rule"))
    suite.addTest(PrivatezoneClientTest("test_delete_private_zone"))
    suite.addTest(PrivatezoneClientTest("test_delete_record"))
    suite.addTest(PrivatezoneClientTest("test_delete_resolver"))
    suite.addTest(PrivatezoneClientTest("test_delete_resolver_rule"))
    suite.addTest(PrivatezoneClientTest("test_disable_record"))
    suite.addTest(PrivatezoneClientTest("test_enable_record"))
    suite.addTest(PrivatezoneClientTest("test_get_dns_resolver_detail"))
    suite.addTest(PrivatezoneClientTest("test_get_dns_resolver_list"))
    suite.addTest(PrivatezoneClientTest("test_get_dns_resolver_rule_detail"))
    suite.addTest(PrivatezoneClientTest("test_get_dns_resolver_rule_list"))
    suite.addTest(PrivatezoneClientTest("test_get_private_zone"))
    suite.addTest(PrivatezoneClientTest("test_list_private_zone"))
    suite.addTest(PrivatezoneClientTest("test_list_record"))
    suite.addTest(PrivatezoneClientTest("test_unbind_vpc"))
    suite.addTest(PrivatezoneClientTest("test_unbind_vpc_to_rule"))
    suite.addTest(PrivatezoneClientTest("test_update_dns_parser"))
    suite.addTest(PrivatezoneClientTest("test_update_record"))
    suite.addTest(PrivatezoneClientTest("test_update_resolver_rule"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
