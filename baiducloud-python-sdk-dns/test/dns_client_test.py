import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_dns.api.dns_client import DnsClient
from baiducloud_python_sdk_dns import models as dns_models


class DnsClientTest(unittest.TestCase):
    """DnsClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
        self.client = DnsClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_add_domain_name(self):
        self.client.add_domain_name(dns_models.AddDomainNameRequest())

    def test_add_line_group(self):
        self.client.add_line_group(dns_models.AddLineGroupRequest())

    def test_add_parsing_records(self):
        self.client.add_parsing_records(dns_models.AddParsingRecordsRequest())

    def test_delete_line_group(self):
        self.client.delete_line_group(dns_models.DeleteLineGroupRequest())

    def test_delete_parsing_records(self):
        self.client.delete_parsing_records(dns_models.DeleteParsingRecordsRequest())

    def test_domain_name_renewal(self):
        self.client.domain_name_renewal(dns_models.DomainNameRenewalRequest())

    def test_modify_parsing_records(self):
        self.client.modify_parsing_records(dns_models.ModifyParsingRecordsRequest())

    def test_modify_the_parsing_record_status(self):
        self.client.modify_the_parsing_record_status(dns_models.ModifyTheParsingRecordStatusRequest())

    def test_purchase_a_paid_domain_name(self):
        self.client.purchase_a_paid_domain_name(dns_models.PurchaseAPaidDomainNameRequest())

    def test_query_and_parse_record_list(self):
        self.client.query_and_parse_record_list(dns_models.QueryAndParseRecordListRequest())

    def test_query_domain_name_list(self):
        self.client.query_domain_name_list(dns_models.QueryDomainNameListRequest())

    def test_query_the_list_of_line_groups(self):
        self.client.query_the_list_of_line_groups(dns_models.QueryTheListOfLineGroupsRequest())

    def test_remove_domain_name(self):
        self.client.remove_domain_name(dns_models.RemoveDomainNameRequest())

    def test_update_line_group(self):
        self.client.update_line_group(dns_models.UpdateLineGroupRequest())

    def test_upgrade_the_free_domain_name_to_the_universal_version(self):
        self.client.upgrade_the_free_domain_name_to_the_universal_version(
            dns_models.UpgradeTheFreeDomainNameToTheUniversalVersionRequest()
        )


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(DnsClientTest("test_add_domain_name"))
    suite.addTest(DnsClientTest("test_add_line_group"))
    suite.addTest(DnsClientTest("test_add_parsing_records"))
    suite.addTest(DnsClientTest("test_delete_line_group"))
    suite.addTest(DnsClientTest("test_delete_parsing_records"))
    suite.addTest(DnsClientTest("test_domain_name_renewal"))
    suite.addTest(DnsClientTest("test_modify_parsing_records"))
    suite.addTest(DnsClientTest("test_modify_the_parsing_record_status"))
    suite.addTest(DnsClientTest("test_purchase_a_paid_domain_name"))
    suite.addTest(DnsClientTest("test_query_and_parse_record_list"))
    suite.addTest(DnsClientTest("test_query_domain_name_list"))
    suite.addTest(DnsClientTest("test_query_the_list_of_line_groups"))
    suite.addTest(DnsClientTest("test_remove_domain_name"))
    suite.addTest(DnsClientTest("test_update_line_group"))
    suite.addTest(DnsClientTest("test_upgrade_the_free_domain_name_to_the_universal_version"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
