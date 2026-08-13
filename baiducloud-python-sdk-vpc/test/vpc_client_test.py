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

        # ==== AK/SK 鉴权 ====
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

    def test_add_eni_ip(self):
        self.client.add_eni_ip(vpc_models.AddEniIpRequest())

    def test_add_ip_address_to_ip_group(self):
        self.client.add_ip_address_to_ip_group(vpc_models.AddIpAddressToIpGroupRequest())

    def test_add_ip_group_to_ip_set(self):
        self.client.add_ip_group_to_ip_set(vpc_models.AddIpGroupToIpSetRequest())

    def test_attach_eni_instance(self):
        self.client.attach_eni_instance(vpc_models.AttachEniInstanceRequest())

    def test_authorize_enterprise_security_group_rules(self):
        self.client.authorize_enterprise_security_group_rules(
            vpc_models.AuthorizeEnterpriseSecurityGroupRulesRequest()
        )

    def test_authorize_security_group_rules(self):
        self.client.authorize_security_group_rules(vpc_models.AuthorizeSecurityGroupRulesRequest())

    def test_batch_add_dnat_rules(self):
        self.client.batch_add_dnat_rules(vpc_models.BatchAddDnatRulesRequest())

    def test_batch_add_eni_ip(self):
        self.client.batch_add_eni_ip(vpc_models.BatchAddEniIpRequest())

    def test_batch_add_snat_rules(self):
        self.client.batch_add_snat_rules(vpc_models.BatchAddSnatRulesRequest())

    def test_batch_create_ssl_vpn_users(self):
        self.client.batch_create_ssl_vpn_users(vpc_models.BatchCreateSslVpnUsersRequest())

    def test_batch_delete_eni_ip(self):
        self.client.batch_delete_eni_ip(vpc_models.BatchDeleteEniIpRequest())

    def test_bind_eip(self):
        self.client.bind_eip(vpc_models.BindEipRequest())

    def test_bind_eni_eip(self):
        self.client.bind_eni_eip(vpc_models.BindEniEipRequest())

    def test_bind_ha_vip_eip(self):
        self.client.bind_ha_vip_eip(vpc_models.BindHaVipEipRequest())

    def test_bind_ha_vip_instance(self):
        self.client.bind_ha_vip_instance(vpc_models.BindHaVipInstanceRequest())

    def test_bind_physical_dedicated_line(self):
        self.client.bind_physical_dedicated_line(vpc_models.BindPhysicalDedicatedLineRequest())

    def test_close_peer_conn_sync_dns(self):
        self.client.close_peer_conn_sync_dns(vpc_models.ClosePeerConnSyncDnsRequest())

    def test_close_vpc_relay(self):
        self.client.close_vpc_relay(vpc_models.CloseVpcRelayRequest())

    def test_create_dedicated_gateway(self):
        self.client.create_dedicated_gateway(vpc_models.CreateDedicatedGatewayRequest())

    def test_create_dedicated_gateway_health_check(self):
        self.client.create_dedicated_gateway_health_check(vpc_models.CreateDedicatedGatewayHealthCheckRequest())

    def test_create_dnat_rule(self):
        self.client.create_dnat_rule(vpc_models.CreateDnatRuleRequest())

    def test_create_egress_only_rule(self):
        self.client.create_egress_only_rule(vpc_models.CreateEgressOnlyRuleRequest())

    def test_create_eni(self):
        self.client.create_eni(vpc_models.CreateEniRequest())

    def test_create_enterprise_security_group(self):
        self.client.create_enterprise_security_group(vpc_models.CreateEnterpriseSecurityGroupRequest())

    def test_create_gateway_limit_rules(self):
        self.client.create_gateway_limit_rules(vpc_models.CreateGatewayLimitRulesRequest())

    def test_create_ha_vip(self):
        self.client.create_ha_vip(vpc_models.CreateHaVipRequest())

    def test_create_ip_group(self):
        self.client.create_ip_group(vpc_models.CreateIpGroupRequest())

    def test_create_ip_reserved(self):
        self.client.create_ip_reserved(vpc_models.CreateIpReservedRequest())

    def test_create_ip_set(self):
        self.client.create_ip_set(vpc_models.CreateIpSetRequest())

    def test_create_ipv6_gateway(self):
        self.client.create_ipv6_gateway(vpc_models.CreateIpv6GatewayRequest())

    def test_create_nat(self):
        self.client.create_nat(vpc_models.CreateNatRequest())

    def test_create_peer_conn(self):
        self.client.create_peer_conn(vpc_models.CreatePeerConnRequest())

    def test_create_probe(self):
        self.client.create_probe(vpc_models.CreateProbeRequest())

    def test_create_rate_limit_rule(self):
        self.client.create_rate_limit_rule(vpc_models.CreateRateLimitRuleRequest())

    def test_create_routing_rules(self):
        self.client.create_routing_rules(vpc_models.CreateRoutingRulesRequest())

    def test_create_security_group(self):
        self.client.create_security_group(vpc_models.CreateSecurityGroupRequest())

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

    def test_delete_eni_ip(self):
        self.client.delete_eni_ip(vpc_models.DeleteEniIpRequest())

    def test_delete_enterprise_security_group(self):
        self.client.delete_enterprise_security_group(vpc_models.DeleteEnterpriseSecurityGroupRequest())

    def test_delete_enterprise_security_group_rules(self):
        self.client.delete_enterprise_security_group_rules(vpc_models.DeleteEnterpriseSecurityGroupRulesRequest())

    def test_delete_gateway_limit_rule(self):
        self.client.delete_gateway_limit_rule(vpc_models.DeleteGatewayLimitRuleRequest())

    def test_delete_ha_vip(self):
        self.client.delete_ha_vip(vpc_models.DeleteHaVipRequest())

    def test_delete_ip_group(self):
        self.client.delete_ip_group(vpc_models.DeleteIpGroupRequest())

    def test_delete_ip_reserve(self):
        self.client.delete_ip_reserve(vpc_models.DeleteIpReserveRequest())

    def test_delete_ip_set(self):
        self.client.delete_ip_set(vpc_models.DeleteIpSetRequest())

    def test_delete_ipv6_gateway(self):
        self.client.delete_ipv6_gateway(vpc_models.DeleteIpv6GatewayRequest())

    def test_delete_ipv6_gateway_egress_only_rule(self):
        self.client.delete_ipv6_gateway_egress_only_rule(vpc_models.DeleteIpv6GatewayEgressOnlyRuleRequest())

    def test_delete_ipv6_gateway_rate_limit_rule(self):
        self.client.delete_ipv6_gateway_rate_limit_rule(vpc_models.DeleteIpv6GatewayRateLimitRuleRequest())

    def test_delete_probe(self):
        self.client.delete_probe(vpc_models.DeleteProbeRequest())

    def test_delete_routing_rules(self):
        self.client.delete_routing_rules(vpc_models.DeleteRoutingRulesRequest())

    def test_delete_security_group(self):
        self.client.delete_security_group(vpc_models.DeleteSecurityGroupRequest())

    def test_delete_security_group_rules(self):
        self.client.delete_security_group_rules(vpc_models.DeleteSecurityGroupRulesRequest())

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

    def test_detach_eni_instance(self):
        self.client.detach_eni_instance(vpc_models.DetachEniInstanceRequest())

    def test_get_eni_detail(self):
        self.client.get_eni_detail(vpc_models.GetEniDetailRequest())

    def test_get_eni_status(self):
        self.client.get_eni_status(vpc_models.GetEniStatusRequest())

    def test_get_ha_vip_detail(self):
        self.client.get_ha_vip_detail(vpc_models.GetHaVipDetailRequest())

    def test_get_nat(self):
        self.client.get_nat(vpc_models.GetNatRequest())

    def test_get_peer_conn(self):
        self.client.get_peer_conn(vpc_models.GetPeerConnRequest())

    def test_get_probe_detail(self):
        self.client.get_probe_detail(vpc_models.GetProbeDetailRequest())

    def test_get_security_group_details(self):
        self.client.get_security_group_details(vpc_models.GetSecurityGroupDetailsRequest())

    def test_get_vpc_resource_ip_info(self):
        self.client.get_vpc_resource_ip_info(vpc_models.GetVpcResourceIpInfoRequest())

    def test_list_dnat_rule(self):
        self.client.list_dnat_rule(vpc_models.ListDnatRuleRequest())

    def test_list_egress_only_rule(self):
        self.client.list_egress_only_rule(vpc_models.ListEgressOnlyRuleRequest())

    def test_list_eni(self):
        self.client.list_eni(vpc_models.ListEniRequest())

    def test_list_ha_vip(self):
        self.client.list_ha_vip(vpc_models.ListHaVipRequest())

    def test_list_ip_reserve(self):
        self.client.list_ip_reserve(vpc_models.ListIpReserveRequest())

    def test_list_nat(self):
        self.client.list_nat(vpc_models.ListNatRequest())

    def test_list_peer_conn(self):
        self.client.list_peer_conn(vpc_models.ListPeerConnRequest())

    def test_list_probes(self):
        self.client.list_probes(vpc_models.ListProbesRequest())

    def test_list_rate_limit_rule(self):
        self.client.list_rate_limit_rule(vpc_models.ListRateLimitRuleRequest())

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

    def test_query_enterprise_security_group_list(self):
        self.client.query_enterprise_security_group_list(vpc_models.QueryEnterpriseSecurityGroupListRequest())

    def test_query_ip_group_detail(self):
        self.client.query_ip_group_detail(vpc_models.QueryIpGroupDetailRequest())

    def test_query_ip_group_list(self):
        self.client.query_ip_group_list(vpc_models.QueryIpGroupListRequest())

    def test_query_ip_set_detail(self):
        self.client.query_ip_set_detail(vpc_models.QueryIpSetDetailRequest())

    def test_query_ip_set_list(self):
        self.client.query_ip_set_list(vpc_models.QueryIpSetListRequest())

    def test_query_ipv6_gateway(self):
        self.client.query_ipv6_gateway(vpc_models.QueryIpv6GatewayRequest())

    def test_query_routing_rules(self):
        self.client.query_routing_rules(vpc_models.QueryRoutingRulesRequest())

    def test_query_routing_table(self):
        self.client.query_routing_table(vpc_models.QueryRoutingTableRequest())

    def test_query_security_groups_list(self):
        self.client.query_security_groups_list(vpc_models.QuerySecurityGroupsListRequest())

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

    def test_query_vpc_intranet_ip(self):
        self.client.query_vpc_intranet_ip(vpc_models.QueryVpcIntranetIpRequest())

    def test_query_vpc_list(self):
        self.client.query_vpc_list(vpc_models.QueryVpcListRequest())

    def test_query_vpn_list(self):
        self.client.query_vpn_list(vpc_models.QueryVpnListRequest())

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

    def test_remove_eni(self):
        self.client.remove_eni(vpc_models.RemoveEniRequest())

    def test_remove_ip_address_from_ip_group(self):
        self.client.remove_ip_address_from_ip_group(vpc_models.RemoveIpAddressFromIpGroupRequest())

    def test_remove_ip_group_from_ip_set(self):
        self.client.remove_ip_group_from_ip_set(vpc_models.RemoveIpGroupFromIpSetRequest())

    def test_renew_peer_conn(self):
        self.client.renew_peer_conn(vpc_models.RenewPeerConnRequest())

    def test_renew_vpn(self):
        self.client.renew_vpn(vpc_models.RenewVpnRequest())

    def test_resize_ipv6_gateway(self):
        self.client.resize_ipv6_gateway(vpc_models.ResizeIpv6GatewayRequest())

    def test_resize_nat(self):
        self.client.resize_nat(vpc_models.ResizeNatRequest())

    def test_revoke_security_group_rules(self):
        self.client.revoke_security_group_rules(vpc_models.RevokeSecurityGroupRulesRequest())

    def test_search_for_vpn_details(self):
        self.client.search_for_vpn_details(vpc_models.SearchForVpnDetailsRequest())

    def test_search_vpn_tunnel(self):
        self.client.search_vpn_tunnel(vpc_models.SearchVpnTunnelRequest())

    def test_unbind_eip(self):
        self.client.unbind_eip(vpc_models.UnbindEipRequest())

    def test_unbind_eni_eip(self):
        self.client.unbind_eni_eip(vpc_models.UnbindEniEipRequest())

    def test_unbind_ha_vip_eip(self):
        self.client.unbind_ha_vip_eip(vpc_models.UnbindHaVipEipRequest())

    def test_unbind_ha_vip_instance(self):
        self.client.unbind_ha_vip_instance(vpc_models.UnbindHaVipInstanceRequest())

    def test_unbind_physical_dedicated_line(self):
        self.client.unbind_physical_dedicated_line(vpc_models.UnbindPhysicalDedicatedLineRequest())

    def test_update_acl_rules(self):
        self.client.update_acl_rules(vpc_models.UpdateAclRulesRequest())

    def test_update_dedicated_gateway(self):
        self.client.update_dedicated_gateway(vpc_models.UpdateDedicatedGatewayRequest())

    def test_update_delete_protect(self):
        self.client.update_delete_protect(vpc_models.UpdateDeleteProtectRequest())

    def test_update_dnat_rule(self):
        self.client.update_dnat_rule(vpc_models.UpdateDnatRuleRequest())

    def test_update_eni(self):
        self.client.update_eni(vpc_models.UpdateEniRequest())

    def test_update_eni_enterprise_security_group(self):
        self.client.update_eni_enterprise_security_group(vpc_models.UpdateEniEnterpriseSecurityGroupRequest())

    def test_update_eni_security_group(self):
        self.client.update_eni_security_group(vpc_models.UpdateEniSecurityGroupRequest())

    def test_update_enterprise_security_group_rules(self):
        self.client.update_enterprise_security_group_rules(vpc_models.UpdateEnterpriseSecurityGroupRulesRequest())

    def test_update_ha_vip(self):
        self.client.update_ha_vip(vpc_models.UpdateHaVipRequest())

    def test_update_ip_group(self):
        self.client.update_ip_group(vpc_models.UpdateIpGroupRequest())

    def test_update_ip_set(self):
        self.client.update_ip_set(vpc_models.UpdateIpSetRequest())

    def test_update_nat_release_protection_switch(self):
        self.client.update_nat_release_protection_switch(vpc_models.UpdateNatReleaseProtectionSwitchRequest())

    def test_update_peer_conn(self):
        self.client.update_peer_conn(vpc_models.UpdatePeerConnRequest())

    def test_update_peer_conn_bandwidth(self):
        self.client.update_peer_conn_bandwidth(vpc_models.UpdatePeerConnBandwidthRequest())

    def test_update_peer_conn_delete_protect(self):
        self.client.update_peer_conn_delete_protect(vpc_models.UpdatePeerConnDeleteProtectRequest())

    def test_update_probe(self):
        self.client.update_probe(vpc_models.UpdateProbeRequest())

    def test_update_rate_limit_rule(self):
        self.client.update_rate_limit_rule(vpc_models.UpdateRateLimitRuleRequest())

    def test_update_routing_rules(self):
        self.client.update_routing_rules(vpc_models.UpdateRoutingRulesRequest())

    def test_update_security_group_rules(self):
        self.client.update_security_group_rules(vpc_models.UpdateSecurityGroupRulesRequest())

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


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(VpcClientTest("test_accept_peer_conn"))
    suite.addTest(VpcClientTest("test_active_standby_switchover"))
    suite.addTest(VpcClientTest("test_add_acl_rule"))
    suite.addTest(VpcClientTest("test_add_eni_ip"))
    suite.addTest(VpcClientTest("test_add_ip_address_to_ip_group"))
    suite.addTest(VpcClientTest("test_add_ip_group_to_ip_set"))
    suite.addTest(VpcClientTest("test_attach_eni_instance"))
    suite.addTest(VpcClientTest("test_authorize_enterprise_security_group_rules"))
    suite.addTest(VpcClientTest("test_authorize_security_group_rules"))
    suite.addTest(VpcClientTest("test_batch_add_dnat_rules"))
    suite.addTest(VpcClientTest("test_batch_add_eni_ip"))
    suite.addTest(VpcClientTest("test_batch_add_snat_rules"))
    suite.addTest(VpcClientTest("test_batch_create_ssl_vpn_users"))
    suite.addTest(VpcClientTest("test_batch_delete_eni_ip"))
    suite.addTest(VpcClientTest("test_bind_eip"))
    suite.addTest(VpcClientTest("test_bind_eni_eip"))
    suite.addTest(VpcClientTest("test_bind_ha_vip_eip"))
    suite.addTest(VpcClientTest("test_bind_ha_vip_instance"))
    suite.addTest(VpcClientTest("test_bind_physical_dedicated_line"))
    suite.addTest(VpcClientTest("test_close_peer_conn_sync_dns"))
    suite.addTest(VpcClientTest("test_close_vpc_relay"))
    suite.addTest(VpcClientTest("test_create_dedicated_gateway"))
    suite.addTest(VpcClientTest("test_create_dedicated_gateway_health_check"))
    suite.addTest(VpcClientTest("test_create_dnat_rule"))
    suite.addTest(VpcClientTest("test_create_egress_only_rule"))
    suite.addTest(VpcClientTest("test_create_eni"))
    suite.addTest(VpcClientTest("test_create_enterprise_security_group"))
    suite.addTest(VpcClientTest("test_create_gateway_limit_rules"))
    suite.addTest(VpcClientTest("test_create_ha_vip"))
    suite.addTest(VpcClientTest("test_create_ip_group"))
    suite.addTest(VpcClientTest("test_create_ip_reserved"))
    suite.addTest(VpcClientTest("test_create_ip_set"))
    suite.addTest(VpcClientTest("test_create_ipv6_gateway"))
    suite.addTest(VpcClientTest("test_create_nat"))
    suite.addTest(VpcClientTest("test_create_peer_conn"))
    suite.addTest(VpcClientTest("test_create_probe"))
    suite.addTest(VpcClientTest("test_create_rate_limit_rule"))
    suite.addTest(VpcClientTest("test_create_routing_rules"))
    suite.addTest(VpcClientTest("test_create_security_group"))
    suite.addTest(VpcClientTest("test_create_snat_rule"))
    suite.addTest(VpcClientTest("test_create_ssl_vpn_server"))
    suite.addTest(VpcClientTest("test_create_subnet"))
    suite.addTest(VpcClientTest("test_create_user_gateway"))
    suite.addTest(VpcClientTest("test_create_vpc"))
    suite.addTest(VpcClientTest("test_create_vpn"))
    suite.addTest(VpcClientTest("test_create_vpn_tunnel"))
    suite.addTest(VpcClientTest("test_delete_acl_rule"))
    suite.addTest(VpcClientTest("test_delete_dnat_rule"))
    suite.addTest(VpcClientTest("test_delete_eni_ip"))
    suite.addTest(VpcClientTest("test_delete_enterprise_security_group"))
    suite.addTest(VpcClientTest("test_delete_enterprise_security_group_rules"))
    suite.addTest(VpcClientTest("test_delete_gateway_limit_rule"))
    suite.addTest(VpcClientTest("test_delete_ha_vip"))
    suite.addTest(VpcClientTest("test_delete_ip_group"))
    suite.addTest(VpcClientTest("test_delete_ip_reserve"))
    suite.addTest(VpcClientTest("test_delete_ip_set"))
    suite.addTest(VpcClientTest("test_delete_ipv6_gateway"))
    suite.addTest(VpcClientTest("test_delete_ipv6_gateway_egress_only_rule"))
    suite.addTest(VpcClientTest("test_delete_ipv6_gateway_rate_limit_rule"))
    suite.addTest(VpcClientTest("test_delete_probe"))
    suite.addTest(VpcClientTest("test_delete_routing_rules"))
    suite.addTest(VpcClientTest("test_delete_security_group"))
    suite.addTest(VpcClientTest("test_delete_security_group_rules"))
    suite.addTest(VpcClientTest("test_delete_snat_rule"))
    suite.addTest(VpcClientTest("test_delete_ssl_vpn_server"))
    suite.addTest(VpcClientTest("test_delete_ssl_vpn_user"))
    suite.addTest(VpcClientTest("test_delete_subnet"))
    suite.addTest(VpcClientTest("test_delete_user_gateway"))
    suite.addTest(VpcClientTest("test_delete_vpc"))
    suite.addTest(VpcClientTest("test_delete_vpn_tunnel"))
    suite.addTest(VpcClientTest("test_detach_eni_instance"))
    suite.addTest(VpcClientTest("test_get_eni_detail"))
    suite.addTest(VpcClientTest("test_get_eni_status"))
    suite.addTest(VpcClientTest("test_get_ha_vip_detail"))
    suite.addTest(VpcClientTest("test_get_nat"))
    suite.addTest(VpcClientTest("test_get_peer_conn"))
    suite.addTest(VpcClientTest("test_get_probe_detail"))
    suite.addTest(VpcClientTest("test_get_security_group_details"))
    suite.addTest(VpcClientTest("test_get_vpc_resource_ip_info"))
    suite.addTest(VpcClientTest("test_list_dnat_rule"))
    suite.addTest(VpcClientTest("test_list_egress_only_rule"))
    suite.addTest(VpcClientTest("test_list_eni"))
    suite.addTest(VpcClientTest("test_list_ha_vip"))
    suite.addTest(VpcClientTest("test_list_ip_reserve"))
    suite.addTest(VpcClientTest("test_list_nat"))
    suite.addTest(VpcClientTest("test_list_peer_conn"))
    suite.addTest(VpcClientTest("test_list_probes"))
    suite.addTest(VpcClientTest("test_list_rate_limit_rule"))
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
    suite.addTest(VpcClientTest("test_query_enterprise_security_group_list"))
    suite.addTest(VpcClientTest("test_query_ip_group_detail"))
    suite.addTest(VpcClientTest("test_query_ip_group_list"))
    suite.addTest(VpcClientTest("test_query_ip_set_detail"))
    suite.addTest(VpcClientTest("test_query_ip_set_list"))
    suite.addTest(VpcClientTest("test_query_ipv6_gateway"))
    suite.addTest(VpcClientTest("test_query_routing_rules"))
    suite.addTest(VpcClientTest("test_query_routing_table"))
    suite.addTest(VpcClientTest("test_query_security_groups_list"))
    suite.addTest(VpcClientTest("test_query_specified_subnet"))
    suite.addTest(VpcClientTest("test_query_specified_vpc"))
    suite.addTest(VpcClientTest("test_query_ssl_vpn_server"))
    suite.addTest(VpcClientTest("test_query_ssl_vpn_users"))
    suite.addTest(VpcClientTest("test_query_subnet_list"))
    suite.addTest(VpcClientTest("test_query_the_details_of_the_dedicated_gateway"))
    suite.addTest(VpcClientTest("test_query_the_list_of_dedicated_line_gateways"))
    suite.addTest(VpcClientTest("test_query_vpc_intranet_ip"))
    suite.addTest(VpcClientTest("test_query_vpc_list"))
    suite.addTest(VpcClientTest("test_query_vpn_list"))
    suite.addTest(VpcClientTest("test_refund_peer_conn"))
    suite.addTest(VpcClientTest("test_reject_peer_conn"))
    suite.addTest(VpcClientTest("test_release_dedicated_gateway"))
    suite.addTest(VpcClientTest("test_release_nat"))
    suite.addTest(VpcClientTest("test_release_peer_conn"))
    suite.addTest(VpcClientTest("test_release_vpn"))
    suite.addTest(VpcClientTest("test_remove_eni"))
    suite.addTest(VpcClientTest("test_remove_ip_address_from_ip_group"))
    suite.addTest(VpcClientTest("test_remove_ip_group_from_ip_set"))
    suite.addTest(VpcClientTest("test_renew_peer_conn"))
    suite.addTest(VpcClientTest("test_renew_vpn"))
    suite.addTest(VpcClientTest("test_resize_ipv6_gateway"))
    suite.addTest(VpcClientTest("test_resize_nat"))
    suite.addTest(VpcClientTest("test_revoke_security_group_rules"))
    suite.addTest(VpcClientTest("test_search_for_vpn_details"))
    suite.addTest(VpcClientTest("test_search_vpn_tunnel"))
    suite.addTest(VpcClientTest("test_unbind_eip"))
    suite.addTest(VpcClientTest("test_unbind_eni_eip"))
    suite.addTest(VpcClientTest("test_unbind_ha_vip_eip"))
    suite.addTest(VpcClientTest("test_unbind_ha_vip_instance"))
    suite.addTest(VpcClientTest("test_unbind_physical_dedicated_line"))
    suite.addTest(VpcClientTest("test_update_acl_rules"))
    suite.addTest(VpcClientTest("test_update_dedicated_gateway"))
    suite.addTest(VpcClientTest("test_update_delete_protect"))
    suite.addTest(VpcClientTest("test_update_dnat_rule"))
    suite.addTest(VpcClientTest("test_update_eni"))
    suite.addTest(VpcClientTest("test_update_eni_enterprise_security_group"))
    suite.addTest(VpcClientTest("test_update_eni_security_group"))
    suite.addTest(VpcClientTest("test_update_enterprise_security_group_rules"))
    suite.addTest(VpcClientTest("test_update_ha_vip"))
    suite.addTest(VpcClientTest("test_update_ip_group"))
    suite.addTest(VpcClientTest("test_update_ip_set"))
    suite.addTest(VpcClientTest("test_update_nat_release_protection_switch"))
    suite.addTest(VpcClientTest("test_update_peer_conn"))
    suite.addTest(VpcClientTest("test_update_peer_conn_bandwidth"))
    suite.addTest(VpcClientTest("test_update_peer_conn_delete_protect"))
    suite.addTest(VpcClientTest("test_update_probe"))
    suite.addTest(VpcClientTest("test_update_rate_limit_rule"))
    suite.addTest(VpcClientTest("test_update_routing_rules"))
    suite.addTest(VpcClientTest("test_update_security_group_rules"))
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
    runner = unittest.TextTestRunner()
    runner.run(suite)
