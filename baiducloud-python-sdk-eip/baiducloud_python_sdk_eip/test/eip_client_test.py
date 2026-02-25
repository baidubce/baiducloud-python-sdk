import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_eip.api.eip_client import EipClient


class EipClientTest(unittest.TestCase):
    """EipClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK),
        endpoint=HOST)
        self.client = EipClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_activate_eip_automatic_renewal(self):
        self.client.activate_eip_automatic_renewal(None)

    def test_add_tbsp_area_blocking(self):
        self.client.add_tbsp_area_blocking(None)

    def test_add_tbsp_ip_whitelist(self):
        self.client.add_tbsp_ip_whitelist(None)

    def test_add_tbsp_protocol_blocking(self):
        self.client.add_tbsp_protocol_blocking(None)

    def test_apply_for_eip(self):
        self.client.apply_for_eip(None)

    def test_bandwidth_package_inquiry(self):
        self.client.bandwidth_package_inquiry(None)

    def test_bind_eip(self):
        self.client.bind_eip(None)

    def test_bind_tbsp_protection_object(self):
        self.client.bind_tbsp_protection_object(None)

    def test_cancel_eip_transfer(self):
        self.client.cancel_eip_transfer(None)

    def test_close_eip_direct_access(self):
        self.client.close_eip_direct_access(None)

    def test_create_eip_transfer(self):
        self.client.create_eip_transfer(None)

    def test_create_tbsp(self):
        self.client.create_tbsp(None)

    def test_detail_tbsp(self):
        self.client.detail_tbsp(None)

    def test_disable_tbsp_ip_clean(self):
        self.client.disable_tbsp_ip_clean(None)

    def test_eip_bandwidth_scaling_capacity(self):
        self.client.eip_bandwidth_scaling_capacity(None)

    def test_eip_inquiry(self):
        self.client.eip_inquiry(None)

    def test_eip_postpaid_to_prepaid(self):
        self.client.eip_postpaid_to_prepaid(None)

    def test_eip_renewal(self):
        self.client.eip_renewal(None)

    def test_enable_eip_direct_access(self):
        self.client.enable_eip_direct_access(None)

    def test_enable_tbsp_ip_clean(self):
        self.client.enable_tbsp_ip_clean(None)

    def test_list_eip_transfer(self):
        self.client.list_eip_transfer(None)

    def test_list_tbsp(self):
        self.client.list_tbsp(None)

    def test_list_tbsp_area_blocking(self):
        self.client.list_tbsp_area_blocking(None)

    def test_list_tbsp_ip_clean(self):
        self.client.list_tbsp_ip_clean(None)

    def test_list_tbsp_ip_whitelist(self):
        self.client.list_tbsp_ip_whitelist(None)

    def test_list_tbsp_protocol_blocking(self):
        self.client.list_tbsp_protocol_blocking(None)

    def test_modify_tbsp_ip_clean_threshold(self):
        self.client.modify_tbsp_ip_clean_threshold(None)

    def test_modify_tbsp_ip_protect_level(self):
        self.client.modify_tbsp_ip_protect_level(None)

    def test_prepaid_eip_unsubscribe(self):
        self.client.prepaid_eip_unsubscribe(None)

    def test_query_eip_list(self):
        self.client.query_eip_list(None)

    def test_query_the_list_of_eips_in_the_recycling_bin(self):
        self.client.query_the_list_of_eips_in_the_recycling_bin(None)

    def test_receive_eip_transfer(self):
        self.client.receive_eip_transfer(None)

    def test_reject_eip_transfer(self):
        self.client.reject_eip_transfer(None)

    def test_release_eip(self):
        self.client.release_eip(None)

    def test_release_the_eip_from_the_recycling_bin(self):
        self.client.release_the_eip_from_the_recycling_bin(None)

    def test_remove_tbsp_area_blocking(self):
        self.client.remove_tbsp_area_blocking(None)

    def test_remove_tbsp_ip_whitelist(self):
        self.client.remove_tbsp_ip_whitelist(None)

    def test_remove_tbsp_protocol_blocking(self):
        self.client.remove_tbsp_protocol_blocking(None)

    def test_renew_tbsp(self):
        self.client.renew_tbsp(None)

    def test_resize_tbsp(self):
        self.client.resize_tbsp(None)

    def test_restore_eip_in_recycle_bin(self):
        self.client.restore_eip_in_recycle_bin(None)

    def test_selective_release_of_eip(self):
        self.client.selective_release_of_eip(None)

    def test_shared_bandwidth_inquiry(self):
        self.client.shared_bandwidth_inquiry(None)

    def test_shared_data_package_inquiry(self):
        self.client.shared_data_package_inquiry(None)

    def test_turn_off_eip_automatic_renewal(self):
        self.client.turn_off_eip_automatic_renewal(None)

    def test_unbind_eip(self):
        self.client.unbind_eip(None)

    def test_unbind_tbsp_protection_object(self):
        self.client.unbind_tbsp_protection_object(None)

    def test_update_eip_release_protection_switch(self):
        self.client.update_eip_release_protection_switch(None)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(EipClientTest("test_activate_eip_automatic_renewal"))
    suite.addTest(EipClientTest("test_add_tbsp_area_blocking"))
    suite.addTest(EipClientTest("test_add_tbsp_ip_whitelist"))
    suite.addTest(EipClientTest("test_add_tbsp_protocol_blocking"))
    suite.addTest(EipClientTest("test_apply_for_eip"))
    suite.addTest(EipClientTest("test_bandwidth_package_inquiry"))
    suite.addTest(EipClientTest("test_bind_eip"))
    suite.addTest(EipClientTest("test_bind_tbsp_protection_object"))
    suite.addTest(EipClientTest("test_cancel_eip_transfer"))
    suite.addTest(EipClientTest("test_close_eip_direct_access"))
    suite.addTest(EipClientTest("test_create_eip_transfer"))
    suite.addTest(EipClientTest("test_create_tbsp"))
    suite.addTest(EipClientTest("test_detail_tbsp"))
    suite.addTest(EipClientTest("test_disable_tbsp_ip_clean"))
    suite.addTest(EipClientTest("test_eip_bandwidth_scaling_capacity"))
    suite.addTest(EipClientTest("test_eip_inquiry"))
    suite.addTest(EipClientTest("test_eip_postpaid_to_prepaid"))
    suite.addTest(EipClientTest("test_eip_renewal"))
    suite.addTest(EipClientTest("test_enable_eip_direct_access"))
    suite.addTest(EipClientTest("test_enable_tbsp_ip_clean"))
    suite.addTest(EipClientTest("test_list_eip_transfer"))
    suite.addTest(EipClientTest("test_list_tbsp"))
    suite.addTest(EipClientTest("test_list_tbsp_area_blocking"))
    suite.addTest(EipClientTest("test_list_tbsp_ip_clean"))
    suite.addTest(EipClientTest("test_list_tbsp_ip_whitelist"))
    suite.addTest(EipClientTest("test_list_tbsp_protocol_blocking"))
    suite.addTest(EipClientTest("test_modify_tbsp_ip_clean_threshold"))
    suite.addTest(EipClientTest("test_modify_tbsp_ip_protect_level"))
    suite.addTest(EipClientTest("test_prepaid_eip_unsubscribe"))
    suite.addTest(EipClientTest("test_query_eip_list"))
    suite.addTest(EipClientTest("test_query_the_list_of_eips_in_the_recycling_bin"))
    suite.addTest(EipClientTest("test_receive_eip_transfer"))
    suite.addTest(EipClientTest("test_reject_eip_transfer"))
    suite.addTest(EipClientTest("test_release_eip"))
    suite.addTest(EipClientTest("test_release_the_eip_from_the_recycling_bin"))
    suite.addTest(EipClientTest("test_remove_tbsp_area_blocking"))
    suite.addTest(EipClientTest("test_remove_tbsp_ip_whitelist"))
    suite.addTest(EipClientTest("test_remove_tbsp_protocol_blocking"))
    suite.addTest(EipClientTest("test_renew_tbsp"))
    suite.addTest(EipClientTest("test_resize_tbsp"))
    suite.addTest(EipClientTest("test_restore_eip_in_recycle_bin"))
    suite.addTest(EipClientTest("test_selective_release_of_eip"))
    suite.addTest(EipClientTest("test_shared_bandwidth_inquiry"))
    suite.addTest(EipClientTest("test_shared_data_package_inquiry"))
    suite.addTest(EipClientTest("test_turn_off_eip_automatic_renewal"))
    suite.addTest(EipClientTest("test_unbind_eip"))
    suite.addTest(EipClientTest("test_unbind_tbsp_protection_object"))
    suite.addTest(EipClientTest("test_update_eip_release_protection_switch"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
