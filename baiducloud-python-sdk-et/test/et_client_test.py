import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_et.api.et_client import EtClient
from baiducloud_python_sdk_et import models as et_models


class EtClientTest(unittest.TestCase):
    """EtClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
        self.client = EtClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_apply_physical_dedicated_line(self):
        self.client.apply_physical_dedicated_line(et_models.ApplyPhysicalDedicatedLineRequest())

    def test_associated_dedicated_channel(self):
        self.client.associated_dedicated_channel(et_models.AssociatedDedicatedChannelRequest())

    def test_create_dedicated_channel(self):
        self.client.create_dedicated_channel(et_models.CreateDedicatedChannelRequest())

    def test_create_dedicated_channel_bfd(self):
        self.client.create_dedicated_channel_bfd(et_models.CreateDedicatedChannelBfdRequest())

    def test_create_dedicated_channel_route_parameters(self):
        self.client.create_dedicated_channel_route_parameters(et_models.CreateDedicatedChannelRouteParametersRequest())

    def test_create_dedicated_channel_route_rules(self):
        self.client.create_dedicated_channel_route_rules(et_models.CreateDedicatedChannelRouteRulesRequest())

    def test_create_dedicated_channel_user_object(self):
        self.client.create_dedicated_channel_user_object(et_models.CreateDedicatedChannelUserObjectRequest())

    def test_delete_dedicated_channel(self):
        self.client.delete_dedicated_channel(et_models.DeleteDedicatedChannelRequest())

    def test_delete_dedicated_channel_bfd(self):
        self.client.delete_dedicated_channel_bfd(et_models.DeleteDedicatedChannelBfdRequest())

    def test_delete_dedicated_channel_route_rules(self):
        self.client.delete_dedicated_channel_route_rules(et_models.DeleteDedicatedChannelRouteRulesRequest())

    def test_disable_dedicated_channel_ipv6(self):
        self.client.disable_dedicated_channel_ipv6(et_models.DisableDedicatedChannelIpv6Request())

    def test_enable_dedicated_channel_ipv6(self):
        self.client.enable_dedicated_channel_ipv6(et_models.EnableDedicatedChannelIpv6Request())

    def test_query_dedicated_channel(self):
        self.client.query_dedicated_channel(et_models.QueryDedicatedChannelRequest())

    def test_query_dedicated_channel_route_rules(self):
        self.client.query_dedicated_channel_route_rules(et_models.QueryDedicatedChannelRouteRulesRequest())

    def test_query_dedicated_line_detail(self):
        self.client.query_dedicated_line_detail(et_models.QueryDedicatedLineDetailRequest())

    def test_query_dedicated_lines(self):
        self.client.query_dedicated_lines(et_models.QueryDedicatedLinesRequest())

    def test_remove_dedicated_channel_route_parameters(self):
        self.client.remove_dedicated_channel_route_parameters(et_models.RemoveDedicatedChannelRouteParametersRequest())

    def test_remove_dedicated_channel_user_object(self):
        self.client.remove_dedicated_channel_user_object(et_models.RemoveDedicatedChannelUserObjectRequest())

    def test_resubmit_dedicated_channel(self):
        self.client.resubmit_dedicated_channel(et_models.ResubmitDedicatedChannelRequest())

    def test_unrelated_dedicated_line_channel(self):
        self.client.unrelated_dedicated_line_channel(et_models.UnrelatedDedicatedLineChannelRequest())

    def test_update_dedicated_channel(self):
        self.client.update_dedicated_channel(et_models.UpdateDedicatedChannelRequest())

    def test_update_dedicated_channel_bfd(self):
        self.client.update_dedicated_channel_bfd(et_models.UpdateDedicatedChannelBfdRequest())

    def test_update_dedicated_channel_route_rules(self):
        self.client.update_dedicated_channel_route_rules(et_models.UpdateDedicatedChannelRouteRulesRequest())

    def test_update_physical_dedicated_line(self):
        self.client.update_physical_dedicated_line(et_models.UpdatePhysicalDedicatedLineRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(EtClientTest("test_apply_physical_dedicated_line"))
    suite.addTest(EtClientTest("test_associated_dedicated_channel"))
    suite.addTest(EtClientTest("test_create_dedicated_channel"))
    suite.addTest(EtClientTest("test_create_dedicated_channel_bfd"))
    suite.addTest(EtClientTest("test_create_dedicated_channel_route_parameters"))
    suite.addTest(EtClientTest("test_create_dedicated_channel_route_rules"))
    suite.addTest(EtClientTest("test_create_dedicated_channel_user_object"))
    suite.addTest(EtClientTest("test_delete_dedicated_channel"))
    suite.addTest(EtClientTest("test_delete_dedicated_channel_bfd"))
    suite.addTest(EtClientTest("test_delete_dedicated_channel_route_rules"))
    suite.addTest(EtClientTest("test_disable_dedicated_channel_ipv6"))
    suite.addTest(EtClientTest("test_enable_dedicated_channel_ipv6"))
    suite.addTest(EtClientTest("test_query_dedicated_channel"))
    suite.addTest(EtClientTest("test_query_dedicated_channel_route_rules"))
    suite.addTest(EtClientTest("test_query_dedicated_line_detail"))
    suite.addTest(EtClientTest("test_query_dedicated_lines"))
    suite.addTest(EtClientTest("test_remove_dedicated_channel_route_parameters"))
    suite.addTest(EtClientTest("test_remove_dedicated_channel_user_object"))
    suite.addTest(EtClientTest("test_resubmit_dedicated_channel"))
    suite.addTest(EtClientTest("test_unrelated_dedicated_line_channel"))
    suite.addTest(EtClientTest("test_update_dedicated_channel"))
    suite.addTest(EtClientTest("test_update_dedicated_channel_bfd"))
    suite.addTest(EtClientTest("test_update_dedicated_channel_route_rules"))
    suite.addTest(EtClientTest("test_update_physical_dedicated_line"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
