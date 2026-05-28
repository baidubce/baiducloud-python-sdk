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

    def test_add_line_group(self):
        self.client.add_line_group(dns_models.AddLineGroupRequest())

    def test_create_paid_zone(self):
        self.client.create_paid_zone(dns_models.CreatePaidZoneRequest())

    def test_create_record(self):
        self.client.create_record(dns_models.CreateRecordRequest())

    def test_create_zone(self):
        self.client.create_zone(dns_models.CreateZoneRequest())

    def test_delete_line_group(self):
        self.client.delete_line_group(dns_models.DeleteLineGroupRequest())

    def test_delete_record(self):
        self.client.delete_record(dns_models.DeleteRecordRequest())

    def test_delete_zone(self):
        self.client.delete_zone(dns_models.DeleteZoneRequest())

    def test_list_line_group(self):
        self.client.list_line_group(dns_models.ListLineGroupRequest())

    def test_list_record(self):
        self.client.list_record(dns_models.ListRecordRequest())

    def test_list_zone(self):
        self.client.list_zone(dns_models.ListZoneRequest())

    def test_renew_zone(self):
        self.client.renew_zone(dns_models.RenewZoneRequest())

    def test_update_line_group(self):
        self.client.update_line_group(dns_models.UpdateLineGroupRequest())

    def test_update_record(self):
        self.client.update_record(dns_models.UpdateRecordRequest())

    def test_update_record_disable(self):
        self.client.update_record_disable(dns_models.UpdateRecordDisableRequest())

    def test_update_record_enable(self):
        self.client.update_record_enable(dns_models.UpdateRecordEnableRequest())

    def test_upgrade_zone(self):
        self.client.upgrade_zone(dns_models.UpgradeZoneRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(DnsClientTest("test_add_line_group"))
    suite.addTest(DnsClientTest("test_create_paid_zone"))
    suite.addTest(DnsClientTest("test_create_record"))
    suite.addTest(DnsClientTest("test_create_zone"))
    suite.addTest(DnsClientTest("test_delete_line_group"))
    suite.addTest(DnsClientTest("test_delete_record"))
    suite.addTest(DnsClientTest("test_delete_zone"))
    suite.addTest(DnsClientTest("test_list_line_group"))
    suite.addTest(DnsClientTest("test_list_record"))
    suite.addTest(DnsClientTest("test_list_zone"))
    suite.addTest(DnsClientTest("test_renew_zone"))
    suite.addTest(DnsClientTest("test_update_line_group"))
    suite.addTest(DnsClientTest("test_update_record"))
    suite.addTest(DnsClientTest("test_update_record_disable"))
    suite.addTest(DnsClientTest("test_update_record_enable"))
    suite.addTest(DnsClientTest("test_upgrade_zone"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
