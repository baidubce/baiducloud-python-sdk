import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_eip.api.eip_client import EipClient
from baiducloud_python_sdk_eip import models as eip_models


class EipClientTest(unittest.TestCase):
    """EipClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
        self.client = EipClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_add_eip_group_count(self):
        self.client.add_eip_group_count(eip_models.AddEipGroupCountRequest())

    def test_add_tbsp_area_blocking(self):
        self.client.add_tbsp_area_blocking(eip_models.AddTbspAreaBlockingRequest())

    def test_add_tbsp_ip_whitelist(self):
        self.client.add_tbsp_ip_whitelist(eip_models.AddTbspIpWhitelistRequest())

    def test_add_tbsp_protocol_blocking(self):
        self.client.add_tbsp_protocol_blocking(eip_models.AddTbspProtocolBlockingRequest())

    def test_apply_for_eip(self):
        self.client.apply_for_eip(eip_models.ApplyForEipRequest())

    def test_bandwidth_package_inquiry(self):
        self.client.bandwidth_package_inquiry(eip_models.BandwidthPackageInquiryRequest())

    def test_bind_eip(self):
        self.client.bind_eip(eip_models.BindEipRequest())

    def test_bind_tbsp_protection_object(self):
        self.client.bind_tbsp_protection_object(eip_models.BindTbspProtectionObjectRequest())

    def test_cancel_eip_transfer(self):
        self.client.cancel_eip_transfer(eip_models.CancelEipTransferRequest())

    def test_create_a_shared_traffic_package(self):
        self.client.create_a_shared_traffic_package(eip_models.CreateASharedTrafficPackageRequest())

    def test_create_eip_bp(self):
        self.client.create_eip_bp(eip_models.CreateEipBpRequest())

    def test_create_eip_group(self):
        self.client.create_eip_group(eip_models.CreateEipGroupRequest())

    def test_create_eip_transfer(self):
        self.client.create_eip_transfer(eip_models.CreateEipTransferRequest())

    def test_create_tbsp(self):
        self.client.create_tbsp(eip_models.CreateTbspRequest())

    def test_detail_tbsp(self):
        self.client.detail_tbsp(eip_models.DetailTbspRequest())

    def test_direct_eip(self):
        self.client.direct_eip(eip_models.DirectEipRequest())

    def test_disable_tbsp_ip_clean(self):
        self.client.disable_tbsp_ip_clean(eip_models.DisableTbspIpCleanRequest())

    def test_eip_bandwidth_scaling_capacity(self):
        self.client.eip_bandwidth_scaling_capacity(eip_models.EipBandwidthScalingCapacityRequest())

    def test_eip_inquiry(self):
        self.client.eip_inquiry(eip_models.EipInquiryRequest())

    def test_eip_postpaid_to_prepaid(self):
        self.client.eip_postpaid_to_prepaid(eip_models.EipPostpaidToPrepaidRequest())

    def test_eip_renewal(self):
        self.client.eip_renewal(eip_models.EipRenewalRequest())

    def test_enable_tbsp_ip_clean(self):
        self.client.enable_tbsp_ip_clean(eip_models.EnableTbspIpCleanRequest())

    def test_get_eip_bp(self):
        self.client.get_eip_bp(eip_models.GetEipBpRequest())

    def test_get_eip_group(self):
        self.client.get_eip_group(eip_models.GetEipGroupRequest())

    def test_list_base_ddos(self):
        self.client.list_base_ddos(eip_models.ListBaseDdosRequest())

    def test_list_base_ddos_attack_record(self):
        self.client.list_base_ddos_attack_record(eip_models.ListBaseDdosAttackRecordRequest())

    def test_list_eip_bp(self):
        self.client.list_eip_bp(eip_models.ListEipBpRequest())

    def test_list_eip_group(self):
        self.client.list_eip_group(eip_models.ListEipGroupRequest())

    def test_list_eip_transfer(self):
        self.client.list_eip_transfer(eip_models.ListEipTransferRequest())

    def test_list_recycle_eips(self):
        self.client.list_recycle_eips(eip_models.ListRecycleEipsRequest())

    def test_list_tbsp(self):
        self.client.list_tbsp(eip_models.ListTbspRequest())

    def test_list_tbsp_area_blocking(self):
        self.client.list_tbsp_area_blocking(eip_models.ListTbspAreaBlockingRequest())

    def test_list_tbsp_ip_clean(self):
        self.client.list_tbsp_ip_clean(eip_models.ListTbspIpCleanRequest())

    def test_list_tbsp_ip_whitelist(self):
        self.client.list_tbsp_ip_whitelist(eip_models.ListTbspIpWhitelistRequest())

    def test_list_tbsp_protocol_blocking(self):
        self.client.list_tbsp_protocol_blocking(eip_models.ListTbspProtocolBlockingRequest())

    def test_list_unban(self):
        self.client.list_unban(eip_models.ListUnbanRequest())

    def test_modify_tbsp_ip_clean_threshold(self):
        self.client.modify_tbsp_ip_clean_threshold(eip_models.ModifyTbspIpCleanThresholdRequest())

    def test_modify_tbsp_ip_protect_level(self):
        self.client.modify_tbsp_ip_protect_level(eip_models.ModifyTbspIpProtectLevelRequest())

    def test_move_in_eips(self):
        self.client.move_in_eips(eip_models.MoveInEipsRequest())

    def test_move_out_eips(self):
        self.client.move_out_eips(eip_models.MoveOutEipsRequest())

    def test_optional_release_eip(self):
        self.client.optional_release_eip(eip_models.OptionalReleaseEipRequest())

    def test_purchase_reserved_eip_group(self):
        self.client.purchase_reserved_eip_group(eip_models.PurchaseReservedEipGroupRequest())

    def test_query_eip_list(self):
        self.client.query_eip_list(eip_models.QueryEipListRequest())

    def test_query_the_details_of_shared_traffic_packages(self):
        self.client.query_the_details_of_shared_traffic_packages(
            eip_models.QueryTheDetailsOfSharedTrafficPackagesRequest()
        )

    def test_query_the_list_of_shared_traffic_packages(self):
        self.client.query_the_list_of_shared_traffic_packages(eip_models.QueryTheListOfSharedTrafficPackagesRequest())

    def test_receive_eip_transfer(self):
        self.client.receive_eip_transfer(eip_models.ReceiveEipTransferRequest())

    def test_refund_eip(self):
        self.client.refund_eip(eip_models.RefundEipRequest())

    def test_refund_eip_group(self):
        self.client.refund_eip_group(eip_models.RefundEipGroupRequest())

    def test_reject_eip_transfer(self):
        self.client.reject_eip_transfer(eip_models.RejectEipTransferRequest())

    def test_release_eip(self):
        self.client.release_eip(eip_models.ReleaseEipRequest())

    def test_release_eip_bp(self):
        self.client.release_eip_bp(eip_models.ReleaseEipBpRequest())

    def test_release_eip_from_recycle(self):
        self.client.release_eip_from_recycle(eip_models.ReleaseEipFromRecycleRequest())

    def test_release_eip_group(self):
        self.client.release_eip_group(eip_models.ReleaseEipGroupRequest())

    def test_remove_tbsp_area_blocking(self):
        self.client.remove_tbsp_area_blocking(eip_models.RemoveTbspAreaBlockingRequest())

    def test_remove_tbsp_ip_whitelist(self):
        self.client.remove_tbsp_ip_whitelist(eip_models.RemoveTbspIpWhitelistRequest())

    def test_remove_tbsp_protocol_blocking(self):
        self.client.remove_tbsp_protocol_blocking(eip_models.RemoveTbspProtocolBlockingRequest())

    def test_renew_tbsp(self):
        self.client.renew_tbsp(eip_models.RenewTbspRequest())

    def test_resize_eip_bp_bandwidth(self):
        self.client.resize_eip_bp_bandwidth(eip_models.ResizeEipBpBandwidthRequest())

    def test_resize_eip_group_bandwidth(self):
        self.client.resize_eip_group_bandwidth(eip_models.ResizeEipGroupBandwidthRequest())

    def test_resize_tbsp(self):
        self.client.resize_tbsp(eip_models.ResizeTbspRequest())

    def test_restore_eip_from_recycle(self):
        self.client.restore_eip_from_recycle(eip_models.RestoreEipFromRecycleRequest())

    def test_shared_bandwidth_inquiry(self):
        self.client.shared_bandwidth_inquiry(eip_models.SharedBandwidthInquiryRequest())

    def test_shared_data_package_inquiry(self):
        self.client.shared_data_package_inquiry(eip_models.SharedDataPackageInquiryRequest())

    def test_start_eip_auto_renew(self):
        self.client.start_eip_auto_renew(eip_models.StartEipAutoRenewRequest())

    def test_stop_eip_auto_renew(self):
        self.client.stop_eip_auto_renew(eip_models.StopEipAutoRenewRequest())

    def test_un_direct_eip(self):
        self.client.un_direct_eip(eip_models.UnDirectEipRequest())

    def test_unbind_eip(self):
        self.client.unbind_eip(eip_models.UnbindEipRequest())

    def test_unbind_tbsp_protection_object(self):
        self.client.unbind_tbsp_protection_object(eip_models.UnbindTbspProtectionObjectRequest())

    def test_update_base_ddos_threshold(self):
        self.client.update_base_ddos_threshold(eip_models.UpdateBaseDdosThresholdRequest())

    def test_update_eip_bp_auto_release_time(self):
        self.client.update_eip_bp_auto_release_time(eip_models.UpdateEipBpAutoReleaseTimeRequest())

    def test_update_eip_bp_name(self):
        self.client.update_eip_bp_name(eip_models.UpdateEipBpNameRequest())

    def test_update_eip_delete_protect(self):
        self.client.update_eip_delete_protect(eip_models.UpdateEipDeleteProtectRequest())

    def test_update_eip_group(self):
        self.client.update_eip_group(eip_models.UpdateEipGroupRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(EipClientTest("test_add_eip_group_count"))
    suite.addTest(EipClientTest("test_add_tbsp_area_blocking"))
    suite.addTest(EipClientTest("test_add_tbsp_ip_whitelist"))
    suite.addTest(EipClientTest("test_add_tbsp_protocol_blocking"))
    suite.addTest(EipClientTest("test_apply_for_eip"))
    suite.addTest(EipClientTest("test_bandwidth_package_inquiry"))
    suite.addTest(EipClientTest("test_bind_eip"))
    suite.addTest(EipClientTest("test_bind_tbsp_protection_object"))
    suite.addTest(EipClientTest("test_cancel_eip_transfer"))
    suite.addTest(EipClientTest("test_create_a_shared_traffic_package"))
    suite.addTest(EipClientTest("test_create_eip_bp"))
    suite.addTest(EipClientTest("test_create_eip_group"))
    suite.addTest(EipClientTest("test_create_eip_transfer"))
    suite.addTest(EipClientTest("test_create_tbsp"))
    suite.addTest(EipClientTest("test_detail_tbsp"))
    suite.addTest(EipClientTest("test_direct_eip"))
    suite.addTest(EipClientTest("test_disable_tbsp_ip_clean"))
    suite.addTest(EipClientTest("test_eip_bandwidth_scaling_capacity"))
    suite.addTest(EipClientTest("test_eip_inquiry"))
    suite.addTest(EipClientTest("test_eip_postpaid_to_prepaid"))
    suite.addTest(EipClientTest("test_eip_renewal"))
    suite.addTest(EipClientTest("test_enable_tbsp_ip_clean"))
    suite.addTest(EipClientTest("test_get_eip_bp"))
    suite.addTest(EipClientTest("test_get_eip_group"))
    suite.addTest(EipClientTest("test_list_base_ddos"))
    suite.addTest(EipClientTest("test_list_base_ddos_attack_record"))
    suite.addTest(EipClientTest("test_list_eip_bp"))
    suite.addTest(EipClientTest("test_list_eip_group"))
    suite.addTest(EipClientTest("test_list_eip_transfer"))
    suite.addTest(EipClientTest("test_list_recycle_eips"))
    suite.addTest(EipClientTest("test_list_tbsp"))
    suite.addTest(EipClientTest("test_list_tbsp_area_blocking"))
    suite.addTest(EipClientTest("test_list_tbsp_ip_clean"))
    suite.addTest(EipClientTest("test_list_tbsp_ip_whitelist"))
    suite.addTest(EipClientTest("test_list_tbsp_protocol_blocking"))
    suite.addTest(EipClientTest("test_list_unban"))
    suite.addTest(EipClientTest("test_modify_tbsp_ip_clean_threshold"))
    suite.addTest(EipClientTest("test_modify_tbsp_ip_protect_level"))
    suite.addTest(EipClientTest("test_move_in_eips"))
    suite.addTest(EipClientTest("test_move_out_eips"))
    suite.addTest(EipClientTest("test_optional_release_eip"))
    suite.addTest(EipClientTest("test_purchase_reserved_eip_group"))
    suite.addTest(EipClientTest("test_query_eip_list"))
    suite.addTest(EipClientTest("test_query_the_details_of_shared_traffic_packages"))
    suite.addTest(EipClientTest("test_query_the_list_of_shared_traffic_packages"))
    suite.addTest(EipClientTest("test_receive_eip_transfer"))
    suite.addTest(EipClientTest("test_refund_eip"))
    suite.addTest(EipClientTest("test_refund_eip_group"))
    suite.addTest(EipClientTest("test_reject_eip_transfer"))
    suite.addTest(EipClientTest("test_release_eip"))
    suite.addTest(EipClientTest("test_release_eip_bp"))
    suite.addTest(EipClientTest("test_release_eip_from_recycle"))
    suite.addTest(EipClientTest("test_release_eip_group"))
    suite.addTest(EipClientTest("test_remove_tbsp_area_blocking"))
    suite.addTest(EipClientTest("test_remove_tbsp_ip_whitelist"))
    suite.addTest(EipClientTest("test_remove_tbsp_protocol_blocking"))
    suite.addTest(EipClientTest("test_renew_tbsp"))
    suite.addTest(EipClientTest("test_resize_eip_bp_bandwidth"))
    suite.addTest(EipClientTest("test_resize_eip_group_bandwidth"))
    suite.addTest(EipClientTest("test_resize_tbsp"))
    suite.addTest(EipClientTest("test_restore_eip_from_recycle"))
    suite.addTest(EipClientTest("test_shared_bandwidth_inquiry"))
    suite.addTest(EipClientTest("test_shared_data_package_inquiry"))
    suite.addTest(EipClientTest("test_start_eip_auto_renew"))
    suite.addTest(EipClientTest("test_stop_eip_auto_renew"))
    suite.addTest(EipClientTest("test_un_direct_eip"))
    suite.addTest(EipClientTest("test_unbind_eip"))
    suite.addTest(EipClientTest("test_unbind_tbsp_protection_object"))
    suite.addTest(EipClientTest("test_update_base_ddos_threshold"))
    suite.addTest(EipClientTest("test_update_eip_bp_auto_release_time"))
    suite.addTest(EipClientTest("test_update_eip_bp_name"))
    suite.addTest(EipClientTest("test_update_eip_delete_protect"))
    suite.addTest(EipClientTest("test_update_eip_group"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
