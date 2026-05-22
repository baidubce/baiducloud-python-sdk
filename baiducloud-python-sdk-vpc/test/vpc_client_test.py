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

    def test_accept_peer_to_peer_connection_applications(self):
        self.client.accept_peer_to_peer_connection_applications(
            vpc_models.AcceptPeerToPeerConnectionApplicationsRequest()
        )

    def test_active_standby_switchover(self):
        self.client.active_standby_switchover(vpc_models.ActiveStandbySwitchoverRequest())

    def test_authorize_regular_security_group_rules_v2(self):
        self.client.authorize_regular_security_group_rules_v2(vpc_models.AuthorizeRegularSecurityGroupRulesV2Request())

    def test_authorized_enterprise_security_group_rules(self):
        self.client.authorized_enterprise_security_group_rules(
            vpc_models.AuthorizedEnterpriseSecurityGroupRulesRequest()
        )

    def test_batch_create_ssl_vpn_users(self):
        self.client.batch_create_ssl_vpn_users(vpc_models.BatchCreateSslVpnUsersRequest())

    def test_bind_eip(self):
        self.client.bind_eip(vpc_models.BindEipRequest())

    def test_bind_physical_dedicated_line(self):
        self.client.bind_physical_dedicated_line(vpc_models.BindPhysicalDedicatedLineRequest())

    def test_close_peer_to_peer_connection_to_synchronize_dns(self):
        self.client.close_peer_to_peer_connection_to_synchronize_dns(
            vpc_models.ClosePeerToPeerConnectionToSynchronizeDnsRequest()
        )

    def test_close_vpc_relay(self):
        self.client.close_vpc_relay(vpc_models.CloseVpcRelayRequest())

    def test_create_a_peer_to_peer_connection(self):
        self.client.create_a_peer_to_peer_connection(vpc_models.CreateAPeerToPeerConnectionRequest())

    def test_create_a_regular_security_group_v2(self):
        self.client.create_a_regular_security_group_v2(vpc_models.CreateARegularSecurityGroupV2Request())

    def test_create_dedicated_gateway(self):
        self.client.create_dedicated_gateway(vpc_models.CreateDedicatedGatewayRequest())

    def test_create_dedicated_gateway_health_check(self):
        self.client.create_dedicated_gateway_health_check(vpc_models.CreateDedicatedGatewayHealthCheckRequest())

    def test_create_enterprise_security_group(self):
        self.client.create_enterprise_security_group(vpc_models.CreateEnterpriseSecurityGroupRequest())

    def test_create_gateway_limit_rules(self):
        self.client.create_gateway_limit_rules(vpc_models.CreateGatewayLimitRulesRequest())

    def test_create_ip_reserved(self):
        self.client.create_ip_reserved(vpc_models.CreateIpReservedRequest())

    def test_create_routing_rules(self):
        self.client.create_routing_rules(vpc_models.CreateRoutingRulesRequest())

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

    def test_delete_enterprise_security_group(self):
        self.client.delete_enterprise_security_group(vpc_models.DeleteEnterpriseSecurityGroupRequest())

    def test_delete_enterprise_security_group_rules(self):
        self.client.delete_enterprise_security_group_rules(vpc_models.DeleteEnterpriseSecurityGroupRulesRequest())

    def test_delete_gateway_limit_rule(self):
        self.client.delete_gateway_limit_rule(vpc_models.DeleteGatewayLimitRuleRequest())

    def test_delete_ip_reserve(self):
        self.client.delete_ip_reserve(vpc_models.DeleteIpReserveRequest())

    def test_delete_regular_security_group_rules_v2(self):
        self.client.delete_regular_security_group_rules_v2(vpc_models.DeleteRegularSecurityGroupRulesV2Request())

    def test_delete_regular_security_group_v2(self):
        self.client.delete_regular_security_group_v2(vpc_models.DeleteRegularSecurityGroupV2Request())

    def test_delete_routing_rules(self):
        self.client.delete_routing_rules(vpc_models.DeleteRoutingRulesRequest())

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

    def test_enable_peer_to_peer_connection_to_synchronize_dns(self):
        self.client.enable_peer_to_peer_connection_to_synchronize_dns(
            vpc_models.EnablePeerToPeerConnectionToSynchronizeDnsRequest()
        )

    def test_get_vpc_resource_ip_info(self):
        self.client.get_vpc_resource_ip_info(vpc_models.GetVpcResourceIpInfoRequest())

    def test_list_ip_reserve(self):
        self.client.list_ip_reserve(vpc_models.ListIpReserveRequest())

    def test_modify_gateway_limit_rules(self):
        self.client.modify_gateway_limit_rules(vpc_models.ModifyGatewayLimitRulesRequest())

    def test_open_vpc_relay(self):
        self.client.open_vpc_relay(vpc_models.OpenVpcRelayRequest())

    def test_peer_to_peer_connection_bandwidth_upgrade_and_downgrade(self):
        self.client.peer_to_peer_connection_bandwidth_upgrade_and_downgrade(
            vpc_models.PeerToPeerConnectionBandwidthUpgradeAndDowngradeRequest()
        )

    def test_peer_to_peer_connection_renewal(self):
        self.client.peer_to_peer_connection_renewal(vpc_models.PeerToPeerConnectionRenewalRequest())

    def test_prepaid_peer_to_peer_connection_unsubscribe(self):
        self.client.prepaid_peer_to_peer_connection_unsubscribe(
            vpc_models.PrepaidPeerToPeerConnectionUnsubscribeRequest()
        )

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

    def test_query_the_list_of_enterprise_security_groups(self):
        self.client.query_the_list_of_enterprise_security_groups(
            vpc_models.QueryTheListOfEnterpriseSecurityGroupsRequest()
        )

    def test_query_the_list_of_peer_connections(self):
        self.client.query_the_list_of_peer_connections(vpc_models.QueryTheListOfPeerConnectionsRequest())

    def test_query_the_list_of_regular_security_groups_v2(self):
        self.client.query_the_list_of_regular_security_groups_v2(
            vpc_models.QueryTheListOfRegularSecurityGroupsV2Request()
        )

    def test_query_vpc_intranet_ip(self):
        self.client.query_vpc_intranet_ip(vpc_models.QueryVpcIntranetIpRequest())

    def test_query_vpc_list(self):
        self.client.query_vpc_list(vpc_models.QueryVpcListRequest())

    def test_query_vpn_list(self):
        self.client.query_vpn_list(vpc_models.QueryVpnListRequest())

    def test_reject_peer_to_peer_connection_request(self):
        self.client.reject_peer_to_peer_connection_request(vpc_models.RejectPeerToPeerConnectionRequestRequest())

    def test_release_dedicated_gateway(self):
        self.client.release_dedicated_gateway(vpc_models.ReleaseDedicatedGatewayRequest())

    def test_release_peer_to_peer_connection(self):
        self.client.release_peer_to_peer_connection(vpc_models.ReleasePeerToPeerConnectionRequest())

    def test_release_vpn(self):
        self.client.release_vpn(vpc_models.ReleaseVpnRequest())

    def test_renew_vpn(self):
        self.client.renew_vpn(vpc_models.RenewVpnRequest())

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

    def test_update_dedicated_gateway(self):
        self.client.update_dedicated_gateway(vpc_models.UpdateDedicatedGatewayRequest())

    def test_update_enterprise_security_group_rules(self):
        self.client.update_enterprise_security_group_rules(vpc_models.UpdateEnterpriseSecurityGroupRulesRequest())

    def test_update_peer_to_peer_connection_release_protection_switch(self):
        self.client.update_peer_to_peer_connection_release_protection_switch(
            vpc_models.UpdatePeerToPeerConnectionReleaseProtectionSwitchRequest()
        )

    def test_update_regular_security_group_rules_v2(self):
        self.client.update_regular_security_group_rules_v2(vpc_models.UpdateRegularSecurityGroupRulesV2Request())

    def test_update_routing_rules(self):
        self.client.update_routing_rules(vpc_models.UpdateRoutingRulesRequest())

    def test_update_ssl_vpn_server(self):
        self.client.update_ssl_vpn_server(vpc_models.UpdateSslVpnServerRequest())

    def test_update_ssl_vpn_users(self):
        self.client.update_ssl_vpn_users(vpc_models.UpdateSslVpnUsersRequest())

    def test_update_subnet(self):
        self.client.update_subnet(vpc_models.UpdateSubnetRequest())

    def test_update_the_name_and_comments_of_the_local_interface_for_peer_to_peer_connections(self):
        self.client.update_the_name_and_comments_of_the_local_interface_for_peer_to_peer_connections(
            vpc_models.UpdateTheNameAndCommentsOfTheLocalInterfaceForPeerToPeerConnectionsRequest()
        )

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

    def test_view_peer_to_peer_connection_details(self):
        self.client.view_peer_to_peer_connection_details(vpc_models.ViewPeerToPeerConnectionDetailsRequest())

    def test_view_security_group_details_v2(self):
        self.client.view_security_group_details_v2(vpc_models.ViewSecurityGroupDetailsV2Request())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(VpcClientTest("test_accept_peer_to_peer_connection_applications"))
    suite.addTest(VpcClientTest("test_active_standby_switchover"))
    suite.addTest(VpcClientTest("test_authorize_regular_security_group_rules_v2"))
    suite.addTest(VpcClientTest("test_authorized_enterprise_security_group_rules"))
    suite.addTest(VpcClientTest("test_batch_create_ssl_vpn_users"))
    suite.addTest(VpcClientTest("test_bind_eip"))
    suite.addTest(VpcClientTest("test_bind_physical_dedicated_line"))
    suite.addTest(VpcClientTest("test_close_peer_to_peer_connection_to_synchronize_dns"))
    suite.addTest(VpcClientTest("test_close_vpc_relay"))
    suite.addTest(VpcClientTest("test_create_a_peer_to_peer_connection"))
    suite.addTest(VpcClientTest("test_create_a_regular_security_group_v2"))
    suite.addTest(VpcClientTest("test_create_dedicated_gateway"))
    suite.addTest(VpcClientTest("test_create_dedicated_gateway_health_check"))
    suite.addTest(VpcClientTest("test_create_enterprise_security_group"))
    suite.addTest(VpcClientTest("test_create_gateway_limit_rules"))
    suite.addTest(VpcClientTest("test_create_ip_reserved"))
    suite.addTest(VpcClientTest("test_create_routing_rules"))
    suite.addTest(VpcClientTest("test_create_ssl_vpn_server"))
    suite.addTest(VpcClientTest("test_create_subnet"))
    suite.addTest(VpcClientTest("test_create_user_gateway"))
    suite.addTest(VpcClientTest("test_create_vpc"))
    suite.addTest(VpcClientTest("test_create_vpn"))
    suite.addTest(VpcClientTest("test_create_vpn_tunnel"))
    suite.addTest(VpcClientTest("test_delete_enterprise_security_group"))
    suite.addTest(VpcClientTest("test_delete_enterprise_security_group_rules"))
    suite.addTest(VpcClientTest("test_delete_gateway_limit_rule"))
    suite.addTest(VpcClientTest("test_delete_ip_reserve"))
    suite.addTest(VpcClientTest("test_delete_regular_security_group_rules_v2"))
    suite.addTest(VpcClientTest("test_delete_regular_security_group_v2"))
    suite.addTest(VpcClientTest("test_delete_routing_rules"))
    suite.addTest(VpcClientTest("test_delete_ssl_vpn_server"))
    suite.addTest(VpcClientTest("test_delete_ssl_vpn_user"))
    suite.addTest(VpcClientTest("test_delete_subnet"))
    suite.addTest(VpcClientTest("test_delete_user_gateway"))
    suite.addTest(VpcClientTest("test_delete_vpc"))
    suite.addTest(VpcClientTest("test_delete_vpn_tunnel"))
    suite.addTest(VpcClientTest("test_enable_peer_to_peer_connection_to_synchronize_dns"))
    suite.addTest(VpcClientTest("test_get_vpc_resource_ip_info"))
    suite.addTest(VpcClientTest("test_list_ip_reserve"))
    suite.addTest(VpcClientTest("test_modify_gateway_limit_rules"))
    suite.addTest(VpcClientTest("test_open_vpc_relay"))
    suite.addTest(VpcClientTest("test_peer_to_peer_connection_bandwidth_upgrade_and_downgrade"))
    suite.addTest(VpcClientTest("test_peer_to_peer_connection_renewal"))
    suite.addTest(VpcClientTest("test_prepaid_peer_to_peer_connection_unsubscribe"))
    suite.addTest(VpcClientTest("test_query_routing_rules"))
    suite.addTest(VpcClientTest("test_query_routing_table"))
    suite.addTest(VpcClientTest("test_query_specified_subnet"))
    suite.addTest(VpcClientTest("test_query_specified_vpc"))
    suite.addTest(VpcClientTest("test_query_ssl_vpn_server"))
    suite.addTest(VpcClientTest("test_query_ssl_vpn_users"))
    suite.addTest(VpcClientTest("test_query_subnet_list"))
    suite.addTest(VpcClientTest("test_query_the_details_of_the_dedicated_gateway"))
    suite.addTest(VpcClientTest("test_query_the_list_of_dedicated_line_gateways"))
    suite.addTest(VpcClientTest("test_query_the_list_of_enterprise_security_groups"))
    suite.addTest(VpcClientTest("test_query_the_list_of_peer_connections"))
    suite.addTest(VpcClientTest("test_query_the_list_of_regular_security_groups_v2"))
    suite.addTest(VpcClientTest("test_query_vpc_intranet_ip"))
    suite.addTest(VpcClientTest("test_query_vpc_list"))
    suite.addTest(VpcClientTest("test_query_vpn_list"))
    suite.addTest(VpcClientTest("test_reject_peer_to_peer_connection_request"))
    suite.addTest(VpcClientTest("test_release_dedicated_gateway"))
    suite.addTest(VpcClientTest("test_release_peer_to_peer_connection"))
    suite.addTest(VpcClientTest("test_release_vpn"))
    suite.addTest(VpcClientTest("test_renew_vpn"))
    suite.addTest(VpcClientTest("test_revoke_regular_security_group_rules_v2"))
    suite.addTest(VpcClientTest("test_search_for_vpn_details"))
    suite.addTest(VpcClientTest("test_search_vpn_tunnel"))
    suite.addTest(VpcClientTest("test_unbind_eip"))
    suite.addTest(VpcClientTest("test_unbind_physical_dedicated_line"))
    suite.addTest(VpcClientTest("test_update_dedicated_gateway"))
    suite.addTest(VpcClientTest("test_update_enterprise_security_group_rules"))
    suite.addTest(VpcClientTest("test_update_peer_to_peer_connection_release_protection_switch"))
    suite.addTest(VpcClientTest("test_update_regular_security_group_rules_v2"))
    suite.addTest(VpcClientTest("test_update_routing_rules"))
    suite.addTest(VpcClientTest("test_update_ssl_vpn_server"))
    suite.addTest(VpcClientTest("test_update_ssl_vpn_users"))
    suite.addTest(VpcClientTest("test_update_subnet"))
    suite.addTest(
        VpcClientTest("test_update_the_name_and_comments_of_the_local_interface_for_peer_to_peer_connections")
    )
    suite.addTest(VpcClientTest("test_update_user_gateway"))
    suite.addTest(VpcClientTest("test_update_vpc"))
    suite.addTest(VpcClientTest("test_update_vpn"))
    suite.addTest(VpcClientTest("test_update_vpn_release_protection"))
    suite.addTest(VpcClientTest("test_update_vpn_tunnel"))
    suite.addTest(VpcClientTest("test_user_gateway_details"))
    suite.addTest(VpcClientTest("test_user_gateway_list"))
    suite.addTest(VpcClientTest("test_view_gateway_limit_rules"))
    suite.addTest(VpcClientTest("test_view_peer_to_peer_connection_details"))
    suite.addTest(VpcClientTest("test_view_security_group_details_v2"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
