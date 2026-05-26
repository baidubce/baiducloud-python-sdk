import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_vpc.api.vpc_client import VpcClient
from baiducloud_python_sdk_vpc import models as vpc_models


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

    def test_accept_peer_conn(self):
        self.client.accept_peer_conn(vpc_models.AcceptPeerConnRequest())

    def test_active_standby_switchover(self):
        self.client.active_standby_switchover(vpc_models.ActiveStandbySwitchoverRequest())

    def test_add_acl_rule(self):
        self.client.add_acl_rule(vpc_models.AddAclRuleRequest())

    def test_add_elastic_network_card_auxiliary_ip(self):
        self.client.add_elastic_network_card_auxiliary_ip(vpc_models.AddElasticNetworkCardAuxiliaryIpRequest())

    def test_add_ip_address_group_to_ip_address_family(self):
        self.client.add_ip_address_group_to_ip_address_family(vpc_models.AddIpAddressGroupToIpAddressFamilyRequest())

    def test_add_ip_addresses_to_the_ip_address_group(self):
        self.client.add_ip_addresses_to_the_ip_address_group(vpc_models.AddIpAddressesToTheIpAddressGroupRequest())

    def test_add_ipv6_only_outbound_and_no_inbound_policy(self):
        self.client.add_ipv6_only_outbound_and_no_inbound_policy(
            vpc_models.AddIpv6OnlyOutboundAndNoInboundPolicyRequest()
        )

    def test_authorize_regular_security_group_rules_v2(self):
        self.client.authorize_regular_security_group_rules_v2(vpc_models.AuthorizeRegularSecurityGroupRulesV2Request())

    def test_authorized_enterprise_security_group_rules(self):
        self.client.authorized_enterprise_security_group_rules(
            vpc_models.AuthorizedEnterpriseSecurityGroupRulesRequest()
        )

    def test_batch_add_dnat_rules(self):
        self.client.batch_add_dnat_rules(vpc_models.BatchAddDnatRulesRequest())

    def test_batch_add_snat_rules(self):
        self.client.batch_add_snat_rules(vpc_models.BatchAddSnatRulesRequest())

    def test_batch_create_ssl_vpn_users(self):
        self.client.batch_create_ssl_vpn_users(vpc_models.BatchCreateSslVpnUsersRequest())

    def test_batch_delete_elastic_network_card_intranet_ip(self):
        self.client.batch_delete_elastic_network_card_intranet_ip(
            vpc_models.BatchDeleteElasticNetworkCardIntranetIpRequest()
        )

    def test_batch_increase_elastic_network_card_intranet_ip(self):
        self.client.batch_increase_elastic_network_card_intranet_ip(
            vpc_models.BatchIncreaseElasticNetworkCardIntranetIpRequest()
        )

    def test_bind_eip(self):
        self.client.bind_eip(vpc_models.BindEipRequest())

    def test_bind_physical_dedicated_line(self):
        self.client.bind_physical_dedicated_line(vpc_models.BindPhysicalDedicatedLineRequest())

    def test_close_peer_conn_sync_dns(self):
        self.client.close_peer_conn_sync_dns(vpc_models.ClosePeerConnSyncDnsRequest())

    def test_close_vpc_relay(self):
        self.client.close_vpc_relay(vpc_models.CloseVpcRelayRequest())

    def test_create_a_highly_available_virtual_ip(self):
        self.client.create_a_highly_available_virtual_ip(vpc_models.CreateAHighlyAvailableVirtualIpRequest())

    def test_create_a_regular_security_group_v2(self):
        self.client.create_a_regular_security_group_v2(vpc_models.CreateARegularSecurityGroupV2Request())

    def test_create_an_ipv6_gateway(self):
        self.client.create_an_ipv6_gateway(vpc_models.CreateAnIpv6GatewayRequest())

    def test_create_dedicated_gateway(self):
        self.client.create_dedicated_gateway(vpc_models.CreateDedicatedGatewayRequest())

    def test_create_dedicated_gateway_health_check(self):
        self.client.create_dedicated_gateway_health_check(vpc_models.CreateDedicatedGatewayHealthCheckRequest())

    def test_create_dnat_rule(self):
        self.client.create_dnat_rule(vpc_models.CreateDnatRuleRequest())

    def test_create_elastic_network_card(self):
        self.client.create_elastic_network_card(vpc_models.CreateElasticNetworkCardRequest())

    def test_create_enterprise_security_group(self):
        self.client.create_enterprise_security_group(vpc_models.CreateEnterpriseSecurityGroupRequest())

    def test_create_gateway_limit_rules(self):
        self.client.create_gateway_limit_rules(vpc_models.CreateGatewayLimitRulesRequest())

    def test_create_ip_address_family(self):
        self.client.create_ip_address_family(vpc_models.CreateIpAddressFamilyRequest())

    def test_create_ip_address_group(self):
        self.client.create_ip_address_group(vpc_models.CreateIpAddressGroupRequest())

    def test_create_ip_reserved(self):
        self.client.create_ip_reserved(vpc_models.CreateIpReservedRequest())

    def test_create_ipv6_gateway_speed_limit_policy(self):
        self.client.create_ipv6_gateway_speed_limit_policy(vpc_models.CreateIpv6GatewaySpeedLimitPolicyRequest())

    def test_create_nat(self):
        self.client.create_nat(vpc_models.CreateNatRequest())

    def test_create_network_detection(self):
        self.client.create_network_detection(vpc_models.CreateNetworkDetectionRequest())

    def test_create_peer_conn(self):
        self.client.create_peer_conn(vpc_models.CreatePeerConnRequest())

    def test_create_routing_rules(self):
        self.client.create_routing_rules(vpc_models.CreateRoutingRulesRequest())

    def test_create_snat_rule(self):
        self.client.create_snat_rule(vpc_models.CreateSnatRuleRequest())

    def test_create_ssl_vpn_server(self):
        self.client.create_ssl_vpn_server(vpc_models.CreateSslVpnServerRequest())

    def test_create_subnet(self):
        self.client.create_subnet(vpc_models.CreateSubnetRequest())

    def test_create_user_gateway(self):
        self.client.create_user_gateway(vpc_models.CreateUserGatewayRequest())

    def test_create_vpc(self):
        self.client.create_vpc(vpc_models.CreateVpcRequest())

    def test_create_vpn(self):
        self.client.create_vpn(vpc_models.CreateVpnRequest())

    def test_create_vpn_tunnel(self):
        self.client.create_vpn_tunnel(vpc_models.CreateVpnTunnelRequest())

    def test_delete_acl_rule(self):
        self.client.delete_acl_rule(vpc_models.DeleteAclRuleRequest())

    def test_delete_dnat_rule(self):
        self.client.delete_dnat_rule(vpc_models.DeleteDnatRuleRequest())

    def test_delete_elastic_network_card_auxiliary_ip(self):
        self.client.delete_elastic_network_card_auxiliary_ip(vpc_models.DeleteElasticNetworkCardAuxiliaryIpRequest())

    def test_delete_enterprise_security_group(self):
        self.client.delete_enterprise_security_group(vpc_models.DeleteEnterpriseSecurityGroupRequest())

    def test_delete_enterprise_security_group_rules(self):
        self.client.delete_enterprise_security_group_rules(vpc_models.DeleteEnterpriseSecurityGroupRulesRequest())

    def test_delete_gateway_limit_rule(self):
        self.client.delete_gateway_limit_rule(vpc_models.DeleteGatewayLimitRuleRequest())

    def test_delete_highly_available_virtual_ip(self):
        self.client.delete_highly_available_virtual_ip(vpc_models.DeleteHighlyAvailableVirtualIpRequest())

    def test_delete_ip_address_family(self):
        self.client.delete_ip_address_family(vpc_models.DeleteIpAddressFamilyRequest())

    def test_delete_ip_address_from_ip_address_group(self):
        self.client.delete_ip_address_from_ip_address_group(vpc_models.DeleteIpAddressFromIpAddressGroupRequest())

    def test_delete_ip_address_group(self):
        self.client.delete_ip_address_group(vpc_models.DeleteIpAddressGroupRequest())

    def test_delete_ip_reserve(self):
        self.client.delete_ip_reserve(vpc_models.DeleteIpReserveRequest())

    def test_delete_ipv6_gateway(self):
        self.client.delete_ipv6_gateway(vpc_models.DeleteIpv6GatewayRequest())

    def test_delete_ipv6_gateway_speed_limit_policy(self):
        self.client.delete_ipv6_gateway_speed_limit_policy(vpc_models.DeleteIpv6GatewaySpeedLimitPolicyRequest())

    def test_delete_ipv6_only_access_policy(self):
        self.client.delete_ipv6_only_access_policy(vpc_models.DeleteIpv6OnlyAccessPolicyRequest())

    def test_delete_network_detection(self):
        self.client.delete_network_detection(vpc_models.DeleteNetworkDetectionRequest())

    def test_delete_regular_security_group_rules_v2(self):
        self.client.delete_regular_security_group_rules_v2(vpc_models.DeleteRegularSecurityGroupRulesV2Request())

    def test_delete_regular_security_group_v2(self):
        self.client.delete_regular_security_group_v2(vpc_models.DeleteRegularSecurityGroupV2Request())

    def test_delete_routing_rules(self):
        self.client.delete_routing_rules(vpc_models.DeleteRoutingRulesRequest())

    def test_delete_snat_rule(self):
        self.client.delete_snat_rule(vpc_models.DeleteSnatRuleRequest())

    def test_delete_ssl_vpn_server(self):
        self.client.delete_ssl_vpn_server(vpc_models.DeleteSslVpnServerRequest())

    def test_delete_ssl_vpn_user(self):
        self.client.delete_ssl_vpn_user(vpc_models.DeleteSslVpnUserRequest())

    def test_delete_subnet(self):
        self.client.delete_subnet(vpc_models.DeleteSubnetRequest())

    def test_delete_user_gateway(self):
        self.client.delete_user_gateway(vpc_models.DeleteUserGatewayRequest())

    def test_delete_vpc(self):
        self.client.delete_vpc(vpc_models.DeleteVpcRequest())

    def test_delete_vpn_tunnel(self):
        self.client.delete_vpn_tunnel(vpc_models.DeleteVpnTunnelRequest())

    def test_elastic_network_card_binding_eip(self):
        self.client.elastic_network_card_binding_eip(vpc_models.ElasticNetworkCardBindingEipRequest())

    def test_elastic_network_card_mounted_cloud_product_instance(self):
        self.client.elastic_network_card_mounted_cloud_product_instance(
            vpc_models.ElasticNetworkCardMountedCloudProductInstanceRequest()
        )

    def test_elastic_network_card_unbinding_eip(self):
        self.client.elastic_network_card_unbinding_eip(vpc_models.ElasticNetworkCardUnbindingEipRequest())

    def test_elastic_network_card_uninstallation_cloud_product_instance(self):
        self.client.elastic_network_card_uninstallation_cloud_product_instance(
            vpc_models.ElasticNetworkCardUninstallationCloudProductInstanceRequest()
        )

    def test_elastic_network_card_update_enterprise_security_group(self):
        self.client.elastic_network_card_update_enterprise_security_group(
            vpc_models.ElasticNetworkCardUpdateEnterpriseSecurityGroupRequest()
        )

    def test_elastic_network_card_updates_regular_security_group(self):
        self.client.elastic_network_card_updates_regular_security_group(
            vpc_models.ElasticNetworkCardUpdatesRegularSecurityGroupRequest()
        )

    def test_get_nat(self):
        self.client.get_nat(vpc_models.GetNatRequest())

    def test_get_peer_conn(self):
        self.client.get_peer_conn(vpc_models.GetPeerConnRequest())

    def test_get_vpc_resource_ip_info(self):
        self.client.get_vpc_resource_ip_info(vpc_models.GetVpcResourceIpInfoRequest())

    def test_high_availability_virtual_ip_unbinding_eip(self):
        self.client.high_availability_virtual_ip_unbinding_eip(
            vpc_models.HighAvailabilityVirtualIpUnbindingEipRequest()
        )

    def test_high_availability_virtual_ip_unbinding_instance(self):
        self.client.high_availability_virtual_ip_unbinding_instance(
            vpc_models.HighAvailabilityVirtualIpUnbindingInstanceRequest()
        )

    def test_highly_available_virtual_ip_binding_eip(self):
        self.client.highly_available_virtual_ip_binding_eip(vpc_models.HighlyAvailableVirtualIpBindingEipRequest())

    def test_highly_available_virtual_ip_binding_instance(self):
        self.client.highly_available_virtual_ip_binding_instance(
            vpc_models.HighlyAvailableVirtualIpBindingInstanceRequest()
        )

    def test_ipv6_gateway_bandwidth_upgrade_and_downgrade(self):
        self.client.ipv6_gateway_bandwidth_upgrade_and_downgrade(
            vpc_models.Ipv6GatewayBandwidthUpgradeAndDowngradeRequest()
        )

    def test_list_dnat_rule(self):
        self.client.list_dnat_rule(vpc_models.ListDnatRuleRequest())

    def test_list_ip_reserve(self):
        self.client.list_ip_reserve(vpc_models.ListIpReserveRequest())

    def test_list_nat(self):
        self.client.list_nat(vpc_models.ListNatRequest())

    def test_list_peer_conn(self):
        self.client.list_peer_conn(vpc_models.ListPeerConnRequest())

    def test_list_snat_rule(self):
        self.client.list_snat_rule(vpc_models.ListSnatRuleRequest())

    def test_modify_gateway_limit_rules(self):
        self.client.modify_gateway_limit_rules(vpc_models.ModifyGatewayLimitRulesRequest())

    def test_modify_nat(self):
        self.client.modify_nat(vpc_models.ModifyNatRequest())

    def test_nat_bind_eip(self):
        self.client.nat_bind_eip(vpc_models.NatBindEipRequest())

    def test_nat_un_bind_eip(self):
        self.client.nat_un_bind_eip(vpc_models.NatUnBindEipRequest())

    def test_open_peer_conn_sync_dns(self):
        self.client.open_peer_conn_sync_dns(vpc_models.OpenPeerConnSyncDnsRequest())

    def test_open_vpc_relay(self):
        self.client.open_vpc_relay(vpc_models.OpenVpcRelayRequest())

    def test_purchase_reserved_nat(self):
        self.client.purchase_reserved_nat(vpc_models.PurchaseReservedNatRequest())

    def test_query_acl(self):
        self.client.query_acl(vpc_models.QueryAclRequest())

    def test_query_acl_rules(self):
        self.client.query_acl_rules(vpc_models.QueryAclRulesRequest())

    def test_query_ip_address_family_list(self):
        self.client.query_ip_address_family_list(vpc_models.QueryIpAddressFamilyListRequest())

    def test_query_ipv6_gateway(self):
        self.client.query_ipv6_gateway(vpc_models.QueryIpv6GatewayRequest())

    def test_query_network_detection_details(self):
        self.client.query_network_detection_details(vpc_models.QueryNetworkDetectionDetailsRequest())

    def test_query_network_detection_list(self):
        self.client.query_network_detection_list(vpc_models.QueryNetworkDetectionListRequest())

    def test_query_routing_rules(self):
        self.client.query_routing_rules(vpc_models.QueryRoutingRulesRequest())

    def test_query_routing_table(self):
        self.client.query_routing_table(vpc_models.QueryRoutingTableRequest())

    def test_query_specified_subnet(self):
        self.client.query_specified_subnet(vpc_models.QuerySpecifiedSubnetRequest())

    def test_query_specified_vpc(self):
        self.client.query_specified_vpc(vpc_models.QuerySpecifiedVpcRequest())

    def test_query_ssl_vpn_server(self):
        self.client.query_ssl_vpn_server(vpc_models.QuerySslVpnServerRequest())

    def test_query_ssl_vpn_users(self):
        self.client.query_ssl_vpn_users(vpc_models.QuerySslVpnUsersRequest())

    def test_query_subnet_list(self):
        self.client.query_subnet_list(vpc_models.QuerySubnetListRequest())

    def test_query_the_details_of_the_dedicated_gateway(self):
        self.client.query_the_details_of_the_dedicated_gateway(
            vpc_models.QueryTheDetailsOfTheDedicatedGatewayRequest()
        )

    def test_query_the_list_of_dedicated_line_gateways(self):
        self.client.query_the_list_of_dedicated_line_gateways(vpc_models.QueryTheListOfDedicatedLineGatewaysRequest())

    def test_query_the_list_of_elastic_network_cards(self):
        self.client.query_the_list_of_elastic_network_cards(vpc_models.QueryTheListOfElasticNetworkCardsRequest())

    def test_query_the_list_of_enterprise_security_groups(self):
        self.client.query_the_list_of_enterprise_security_groups(
            vpc_models.QueryTheListOfEnterpriseSecurityGroupsRequest()
        )

    def test_query_the_list_of_highly_available_virtual_ips(self):
        self.client.query_the_list_of_highly_available_virtual_ips(
            vpc_models.QueryTheListOfHighlyAvailableVirtualIpsRequest()
        )

    def test_query_the_list_of_ip_address_groups(self):
        self.client.query_the_list_of_ip_address_groups(vpc_models.QueryTheListOfIpAddressGroupsRequest())

    def test_query_the_list_of_regular_security_groups_v2(self):
        self.client.query_the_list_of_regular_security_groups_v2(
            vpc_models.QueryTheListOfRegularSecurityGroupsV2Request()
        )

    def test_query_the_list_of_speed_limit_policies_for_ipv6_gateway(self):
        self.client.query_the_list_of_speed_limit_policies_for_ipv6_gateway(
            vpc_models.QueryTheListOfSpeedLimitPoliciesForIpv6GatewayRequest()
        )

    def test_query_the_specified_elastic_network_card(self):
        self.client.query_the_specified_elastic_network_card(vpc_models.QueryTheSpecifiedElasticNetworkCardRequest())

    def test_query_the_specified_highly_available_virtual_ip(self):
        self.client.query_the_specified_highly_available_virtual_ip(
            vpc_models.QueryTheSpecifiedHighlyAvailableVirtualIpRequest()
        )

    def test_query_the_specified_ip_address_family(self):
        self.client.query_the_specified_ip_address_family(vpc_models.QueryTheSpecifiedIpAddressFamilyRequest())

    def test_query_the_specified_ip_address_group(self):
        self.client.query_the_specified_ip_address_group(vpc_models.QueryTheSpecifiedIpAddressGroupRequest())

    def test_query_the_status_of_the_elastic_network_card(self):
        self.client.query_the_status_of_the_elastic_network_card(
            vpc_models.QueryTheStatusOfTheElasticNetworkCardRequest()
        )

    def test_query_vpc_intranet_ip(self):
        self.client.query_vpc_intranet_ip(vpc_models.QueryVpcIntranetIpRequest())

    def test_query_vpc_list(self):
        self.client.query_vpc_list(vpc_models.QueryVpcListRequest())

    def test_query_vpn_list(self):
        self.client.query_vpn_list(vpc_models.QueryVpnListRequest())

    def test_querying_the_ipv6_policy_list_with_only_output_and_no_inclusion(self):
        self.client.querying_the_ipv6_policy_list_with_only_output_and_no_inclusion(
            vpc_models.QueryingTheIpv6PolicyListWithOnlyOutputAndNoInclusionRequest()
        )

    def test_refund_peer_conn(self):
        self.client.refund_peer_conn(vpc_models.RefundPeerConnRequest())

    def test_reject_peer_conn(self):
        self.client.reject_peer_conn(vpc_models.RejectPeerConnRequest())

    def test_release_dedicated_gateway(self):
        self.client.release_dedicated_gateway(vpc_models.ReleaseDedicatedGatewayRequest())

    def test_release_nat(self):
        self.client.release_nat(vpc_models.ReleaseNatRequest())

    def test_release_peer_conn(self):
        self.client.release_peer_conn(vpc_models.ReleasePeerConnRequest())

    def test_release_vpn(self):
        self.client.release_vpn(vpc_models.ReleaseVpnRequest())

    def test_remove_elastic_network_card(self):
        self.client.remove_elastic_network_card(vpc_models.RemoveElasticNetworkCardRequest())

    def test_remove_ip_address_group_from_ip_address_family(self):
        self.client.remove_ip_address_group_from_ip_address_family(
            vpc_models.RemoveIpAddressGroupFromIpAddressFamilyRequest()
        )

    def test_renew_peer_conn(self):
        self.client.renew_peer_conn(vpc_models.RenewPeerConnRequest())

    def test_renew_vpn(self):
        self.client.renew_vpn(vpc_models.RenewVpnRequest())

    def test_resize_nat(self):
        self.client.resize_nat(vpc_models.ResizeNatRequest())

    def test_revoke_regular_security_group_rules_v2(self):
        self.client.revoke_regular_security_group_rules_v2(vpc_models.RevokeRegularSecurityGroupRulesV2Request())

    def test_search_for_vpn_details(self):
        self.client.search_for_vpn_details(vpc_models.SearchForVpnDetailsRequest())

    def test_search_vpn_tunnel(self):
        self.client.search_vpn_tunnel(vpc_models.SearchVpnTunnelRequest())

    def test_unbind_eip(self):
        self.client.unbind_eip(vpc_models.UnbindEipRequest())

    def test_unbind_physical_dedicated_line(self):
        self.client.unbind_physical_dedicated_line(vpc_models.UnbindPhysicalDedicatedLineRequest())

    def test_update_acl_rules(self):
        self.client.update_acl_rules(vpc_models.UpdateAclRulesRequest())

    def test_update_dedicated_gateway(self):
        self.client.update_dedicated_gateway(vpc_models.UpdateDedicatedGatewayRequest())

    def test_update_dnat_rule(self):
        self.client.update_dnat_rule(vpc_models.UpdateDnatRuleRequest())

    def test_update_elastic_network_card(self):
        self.client.update_elastic_network_card(vpc_models.UpdateElasticNetworkCardRequest())

    def test_update_enterprise_security_group_rules(self):
        self.client.update_enterprise_security_group_rules(vpc_models.UpdateEnterpriseSecurityGroupRulesRequest())

    def test_update_highly_available_virtual_ip(self):
        self.client.update_highly_available_virtual_ip(vpc_models.UpdateHighlyAvailableVirtualIpRequest())

    def test_update_ip_address_family(self):
        self.client.update_ip_address_family(vpc_models.UpdateIpAddressFamilyRequest())

    def test_update_ip_address_group(self):
        self.client.update_ip_address_group(vpc_models.UpdateIpAddressGroupRequest())

    def test_update_ipv6_gateway_release_protection_switch(self):
        self.client.update_ipv6_gateway_release_protection_switch(
            vpc_models.UpdateIpv6GatewayReleaseProtectionSwitchRequest()
        )

    def test_update_ipv6_gateway_speed_limit_policy(self):
        self.client.update_ipv6_gateway_speed_limit_policy(vpc_models.UpdateIpv6GatewaySpeedLimitPolicyRequest())

    def test_update_nat_release_protection_switch(self):
        self.client.update_nat_release_protection_switch(vpc_models.UpdateNatReleaseProtectionSwitchRequest())

    def test_update_network_detection(self):
        self.client.update_network_detection(vpc_models.UpdateNetworkDetectionRequest())

    def test_update_peer_conn(self):
        self.client.update_peer_conn(vpc_models.UpdatePeerConnRequest())

    def test_update_peer_conn_bandwidth(self):
        self.client.update_peer_conn_bandwidth(vpc_models.UpdatePeerConnBandwidthRequest())

    def test_update_peer_conn_delete_protect(self):
        self.client.update_peer_conn_delete_protect(vpc_models.UpdatePeerConnDeleteProtectRequest())

    def test_update_regular_security_group_rules_v2(self):
        self.client.update_regular_security_group_rules_v2(vpc_models.UpdateRegularSecurityGroupRulesV2Request())

    def test_update_routing_rules(self):
        self.client.update_routing_rules(vpc_models.UpdateRoutingRulesRequest())

    def test_update_snat_rule(self):
        self.client.update_snat_rule(vpc_models.UpdateSnatRuleRequest())

    def test_update_ssl_vpn_server(self):
        self.client.update_ssl_vpn_server(vpc_models.UpdateSslVpnServerRequest())

    def test_update_ssl_vpn_users(self):
        self.client.update_ssl_vpn_users(vpc_models.UpdateSslVpnUsersRequest())

    def test_update_subnet(self):
        self.client.update_subnet(vpc_models.UpdateSubnetRequest())

    def test_update_user_gateway(self):
        self.client.update_user_gateway(vpc_models.UpdateUserGatewayRequest())

    def test_update_vpc(self):
        self.client.update_vpc(vpc_models.UpdateVpcRequest())

    def test_update_vpn(self):
        self.client.update_vpn(vpc_models.UpdateVpnRequest())

    def test_update_vpn_release_protection(self):
        self.client.update_vpn_release_protection(vpc_models.UpdateVpnReleaseProtectionRequest())

    def test_update_vpn_tunnel(self):
        self.client.update_vpn_tunnel(vpc_models.UpdateVpnTunnelRequest())

    def test_user_gateway_details(self):
        self.client.user_gateway_details(vpc_models.UserGatewayDetailsRequest())

    def test_user_gateway_list(self):
        self.client.user_gateway_list(vpc_models.UserGatewayListRequest())

    def test_view_gateway_limit_rules(self):
        self.client.view_gateway_limit_rules(vpc_models.ViewGatewayLimitRulesRequest())

    def test_view_security_group_details_v2(self):
        self.client.view_security_group_details_v2(vpc_models.ViewSecurityGroupDetailsV2Request())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(VpcClientTest("test_accept_peer_conn"))
    suite.addTest(VpcClientTest("test_active_standby_switchover"))
    suite.addTest(VpcClientTest("test_add_acl_rule"))
    suite.addTest(VpcClientTest("test_add_elastic_network_card_auxiliary_ip"))
    suite.addTest(VpcClientTest("test_add_ip_address_group_to_ip_address_family"))
    suite.addTest(VpcClientTest("test_add_ip_addresses_to_the_ip_address_group"))
    suite.addTest(VpcClientTest("test_add_ipv6_only_outbound_and_no_inbound_policy"))
    suite.addTest(VpcClientTest("test_authorize_regular_security_group_rules_v2"))
    suite.addTest(VpcClientTest("test_authorized_enterprise_security_group_rules"))
    suite.addTest(VpcClientTest("test_batch_add_dnat_rules"))
    suite.addTest(VpcClientTest("test_batch_add_snat_rules"))
    suite.addTest(VpcClientTest("test_batch_create_ssl_vpn_users"))
    suite.addTest(VpcClientTest("test_batch_delete_elastic_network_card_intranet_ip"))
    suite.addTest(VpcClientTest("test_batch_increase_elastic_network_card_intranet_ip"))
    suite.addTest(VpcClientTest("test_bind_eip"))
    suite.addTest(VpcClientTest("test_bind_physical_dedicated_line"))
    suite.addTest(VpcClientTest("test_close_peer_conn_sync_dns"))
    suite.addTest(VpcClientTest("test_close_vpc_relay"))
    suite.addTest(VpcClientTest("test_create_a_highly_available_virtual_ip"))
    suite.addTest(VpcClientTest("test_create_a_regular_security_group_v2"))
    suite.addTest(VpcClientTest("test_create_an_ipv6_gateway"))
    suite.addTest(VpcClientTest("test_create_dedicated_gateway"))
    suite.addTest(VpcClientTest("test_create_dedicated_gateway_health_check"))
    suite.addTest(VpcClientTest("test_create_dnat_rule"))
    suite.addTest(VpcClientTest("test_create_elastic_network_card"))
    suite.addTest(VpcClientTest("test_create_enterprise_security_group"))
    suite.addTest(VpcClientTest("test_create_gateway_limit_rules"))
    suite.addTest(VpcClientTest("test_create_ip_address_family"))
    suite.addTest(VpcClientTest("test_create_ip_address_group"))
    suite.addTest(VpcClientTest("test_create_ip_reserved"))
    suite.addTest(VpcClientTest("test_create_ipv6_gateway_speed_limit_policy"))
    suite.addTest(VpcClientTest("test_create_nat"))
    suite.addTest(VpcClientTest("test_create_network_detection"))
    suite.addTest(VpcClientTest("test_create_peer_conn"))
    suite.addTest(VpcClientTest("test_create_routing_rules"))
    suite.addTest(VpcClientTest("test_create_snat_rule"))
    suite.addTest(VpcClientTest("test_create_ssl_vpn_server"))
    suite.addTest(VpcClientTest("test_create_subnet"))
    suite.addTest(VpcClientTest("test_create_user_gateway"))
    suite.addTest(VpcClientTest("test_create_vpc"))
    suite.addTest(VpcClientTest("test_create_vpn"))
    suite.addTest(VpcClientTest("test_create_vpn_tunnel"))
    suite.addTest(VpcClientTest("test_delete_acl_rule"))
    suite.addTest(VpcClientTest("test_delete_dnat_rule"))
    suite.addTest(VpcClientTest("test_delete_elastic_network_card_auxiliary_ip"))
    suite.addTest(VpcClientTest("test_delete_enterprise_security_group"))
    suite.addTest(VpcClientTest("test_delete_enterprise_security_group_rules"))
    suite.addTest(VpcClientTest("test_delete_gateway_limit_rule"))
    suite.addTest(VpcClientTest("test_delete_highly_available_virtual_ip"))
    suite.addTest(VpcClientTest("test_delete_ip_address_family"))
    suite.addTest(VpcClientTest("test_delete_ip_address_from_ip_address_group"))
    suite.addTest(VpcClientTest("test_delete_ip_address_group"))
    suite.addTest(VpcClientTest("test_delete_ip_reserve"))
    suite.addTest(VpcClientTest("test_delete_ipv6_gateway"))
    suite.addTest(VpcClientTest("test_delete_ipv6_gateway_speed_limit_policy"))
    suite.addTest(VpcClientTest("test_delete_ipv6_only_access_policy"))
    suite.addTest(VpcClientTest("test_delete_network_detection"))
    suite.addTest(VpcClientTest("test_delete_regular_security_group_rules_v2"))
    suite.addTest(VpcClientTest("test_delete_regular_security_group_v2"))
    suite.addTest(VpcClientTest("test_delete_routing_rules"))
    suite.addTest(VpcClientTest("test_delete_snat_rule"))
    suite.addTest(VpcClientTest("test_delete_ssl_vpn_server"))
    suite.addTest(VpcClientTest("test_delete_ssl_vpn_user"))
    suite.addTest(VpcClientTest("test_delete_subnet"))
    suite.addTest(VpcClientTest("test_delete_user_gateway"))
    suite.addTest(VpcClientTest("test_delete_vpc"))
    suite.addTest(VpcClientTest("test_delete_vpn_tunnel"))
    suite.addTest(VpcClientTest("test_elastic_network_card_binding_eip"))
    suite.addTest(VpcClientTest("test_elastic_network_card_mounted_cloud_product_instance"))
    suite.addTest(VpcClientTest("test_elastic_network_card_unbinding_eip"))
    suite.addTest(VpcClientTest("test_elastic_network_card_uninstallation_cloud_product_instance"))
    suite.addTest(VpcClientTest("test_elastic_network_card_update_enterprise_security_group"))
    suite.addTest(VpcClientTest("test_elastic_network_card_updates_regular_security_group"))
    suite.addTest(VpcClientTest("test_get_nat"))
    suite.addTest(VpcClientTest("test_get_peer_conn"))
    suite.addTest(VpcClientTest("test_get_vpc_resource_ip_info"))
    suite.addTest(VpcClientTest("test_high_availability_virtual_ip_unbinding_eip"))
    suite.addTest(VpcClientTest("test_high_availability_virtual_ip_unbinding_instance"))
    suite.addTest(VpcClientTest("test_highly_available_virtual_ip_binding_eip"))
    suite.addTest(VpcClientTest("test_highly_available_virtual_ip_binding_instance"))
    suite.addTest(VpcClientTest("test_ipv6_gateway_bandwidth_upgrade_and_downgrade"))
    suite.addTest(VpcClientTest("test_list_dnat_rule"))
    suite.addTest(VpcClientTest("test_list_ip_reserve"))
    suite.addTest(VpcClientTest("test_list_nat"))
    suite.addTest(VpcClientTest("test_list_peer_conn"))
    suite.addTest(VpcClientTest("test_list_snat_rule"))
    suite.addTest(VpcClientTest("test_modify_gateway_limit_rules"))
    suite.addTest(VpcClientTest("test_modify_nat"))
    suite.addTest(VpcClientTest("test_nat_bind_eip"))
    suite.addTest(VpcClientTest("test_nat_un_bind_eip"))
    suite.addTest(VpcClientTest("test_open_peer_conn_sync_dns"))
    suite.addTest(VpcClientTest("test_open_vpc_relay"))
    suite.addTest(VpcClientTest("test_purchase_reserved_nat"))
    suite.addTest(VpcClientTest("test_query_acl"))
    suite.addTest(VpcClientTest("test_query_acl_rules"))
    suite.addTest(VpcClientTest("test_query_ip_address_family_list"))
    suite.addTest(VpcClientTest("test_query_ipv6_gateway"))
    suite.addTest(VpcClientTest("test_query_network_detection_details"))
    suite.addTest(VpcClientTest("test_query_network_detection_list"))
    suite.addTest(VpcClientTest("test_query_routing_rules"))
    suite.addTest(VpcClientTest("test_query_routing_table"))
    suite.addTest(VpcClientTest("test_query_specified_subnet"))
    suite.addTest(VpcClientTest("test_query_specified_vpc"))
    suite.addTest(VpcClientTest("test_query_ssl_vpn_server"))
    suite.addTest(VpcClientTest("test_query_ssl_vpn_users"))
    suite.addTest(VpcClientTest("test_query_subnet_list"))
    suite.addTest(VpcClientTest("test_query_the_details_of_the_dedicated_gateway"))
    suite.addTest(VpcClientTest("test_query_the_list_of_dedicated_line_gateways"))
    suite.addTest(VpcClientTest("test_query_the_list_of_elastic_network_cards"))
    suite.addTest(VpcClientTest("test_query_the_list_of_enterprise_security_groups"))
    suite.addTest(VpcClientTest("test_query_the_list_of_highly_available_virtual_ips"))
    suite.addTest(VpcClientTest("test_query_the_list_of_ip_address_groups"))
    suite.addTest(VpcClientTest("test_query_the_list_of_regular_security_groups_v2"))
    suite.addTest(VpcClientTest("test_query_the_list_of_speed_limit_policies_for_ipv6_gateway"))
    suite.addTest(VpcClientTest("test_query_the_specified_elastic_network_card"))
    suite.addTest(VpcClientTest("test_query_the_specified_highly_available_virtual_ip"))
    suite.addTest(VpcClientTest("test_query_the_specified_ip_address_family"))
    suite.addTest(VpcClientTest("test_query_the_specified_ip_address_group"))
    suite.addTest(VpcClientTest("test_query_the_status_of_the_elastic_network_card"))
    suite.addTest(VpcClientTest("test_query_vpc_intranet_ip"))
    suite.addTest(VpcClientTest("test_query_vpc_list"))
    suite.addTest(VpcClientTest("test_query_vpn_list"))
    suite.addTest(VpcClientTest("test_querying_the_ipv6_policy_list_with_only_output_and_no_inclusion"))
    suite.addTest(VpcClientTest("test_refund_peer_conn"))
    suite.addTest(VpcClientTest("test_reject_peer_conn"))
    suite.addTest(VpcClientTest("test_release_dedicated_gateway"))
    suite.addTest(VpcClientTest("test_release_nat"))
    suite.addTest(VpcClientTest("test_release_peer_conn"))
    suite.addTest(VpcClientTest("test_release_vpn"))
    suite.addTest(VpcClientTest("test_remove_elastic_network_card"))
    suite.addTest(VpcClientTest("test_remove_ip_address_group_from_ip_address_family"))
    suite.addTest(VpcClientTest("test_renew_peer_conn"))
    suite.addTest(VpcClientTest("test_renew_vpn"))
    suite.addTest(VpcClientTest("test_resize_nat"))
    suite.addTest(VpcClientTest("test_revoke_regular_security_group_rules_v2"))
    suite.addTest(VpcClientTest("test_search_for_vpn_details"))
    suite.addTest(VpcClientTest("test_search_vpn_tunnel"))
    suite.addTest(VpcClientTest("test_unbind_eip"))
    suite.addTest(VpcClientTest("test_unbind_physical_dedicated_line"))
    suite.addTest(VpcClientTest("test_update_acl_rules"))
    suite.addTest(VpcClientTest("test_update_dedicated_gateway"))
    suite.addTest(VpcClientTest("test_update_dnat_rule"))
    suite.addTest(VpcClientTest("test_update_elastic_network_card"))
    suite.addTest(VpcClientTest("test_update_enterprise_security_group_rules"))
    suite.addTest(VpcClientTest("test_update_highly_available_virtual_ip"))
    suite.addTest(VpcClientTest("test_update_ip_address_family"))
    suite.addTest(VpcClientTest("test_update_ip_address_group"))
    suite.addTest(VpcClientTest("test_update_ipv6_gateway_release_protection_switch"))
    suite.addTest(VpcClientTest("test_update_ipv6_gateway_speed_limit_policy"))
    suite.addTest(VpcClientTest("test_update_nat_release_protection_switch"))
    suite.addTest(VpcClientTest("test_update_network_detection"))
    suite.addTest(VpcClientTest("test_update_peer_conn"))
    suite.addTest(VpcClientTest("test_update_peer_conn_bandwidth"))
    suite.addTest(VpcClientTest("test_update_peer_conn_delete_protect"))
    suite.addTest(VpcClientTest("test_update_regular_security_group_rules_v2"))
    suite.addTest(VpcClientTest("test_update_routing_rules"))
    suite.addTest(VpcClientTest("test_update_snat_rule"))
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
    suite.addTest(VpcClientTest("test_view_gateway_limit_rules"))
    suite.addTest(VpcClientTest("test_view_security_group_details_v2"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
