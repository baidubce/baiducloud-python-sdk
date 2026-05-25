"""
Example for vpc client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.auth import bce_v1_signer
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_vpc.models.add_elastic_network_card_auxiliary_ip_response import (
    AddElasticNetworkCardAuxiliaryIpResponse,
)
from baiducloud_python_sdk_vpc.models.add_ipv6_only_outbound_and_no_inbound_policy_response import (
    AddIpv6OnlyOutboundAndNoInboundPolicyResponse,
)
from baiducloud_python_sdk_vpc.models.batch_create_ssl_vpn_users_response import BatchCreateSslVpnUsersResponse
from baiducloud_python_sdk_vpc.models.batch_increase_elastic_network_card_intranet_ip_response import (
    BatchIncreaseElasticNetworkCardIntranetIpResponse,
)
from baiducloud_python_sdk_vpc.models.create_a_highly_available_virtual_ip_response import (
    CreateAHighlyAvailableVirtualIpResponse,
)
from baiducloud_python_sdk_vpc.models.create_a_peer_to_peer_connection_response import (
    CreateAPeerToPeerConnectionResponse,
)
from baiducloud_python_sdk_vpc.models.create_a_regular_security_group_v2_response import (
    CreateARegularSecurityGroupV2Response,
)
from baiducloud_python_sdk_vpc.models.create_an_ipv6_gateway_response import CreateAnIpv6GatewayResponse
from baiducloud_python_sdk_vpc.models.create_dedicated_gateway_response import CreateDedicatedGatewayResponse
from baiducloud_python_sdk_vpc.models.create_elastic_network_card_response import CreateElasticNetworkCardResponse
from baiducloud_python_sdk_vpc.models.create_enterprise_security_group_response import (
    CreateEnterpriseSecurityGroupResponse,
)
from baiducloud_python_sdk_vpc.models.create_gateway_limit_rules_response import CreateGatewayLimitRulesResponse
from baiducloud_python_sdk_vpc.models.create_ip_address_family_response import CreateIpAddressFamilyResponse
from baiducloud_python_sdk_vpc.models.create_ip_address_group_response import CreateIpAddressGroupResponse
from baiducloud_python_sdk_vpc.models.create_ip_reserved_response import CreateIpReservedResponse
from baiducloud_python_sdk_vpc.models.create_ipv6_gateway_speed_limit_policy_response import (
    CreateIpv6GatewaySpeedLimitPolicyResponse,
)
from baiducloud_python_sdk_vpc.models.create_network_detection_response import CreateNetworkDetectionResponse
from baiducloud_python_sdk_vpc.models.create_routing_rules_response import CreateRoutingRulesResponse
from baiducloud_python_sdk_vpc.models.create_ssl_vpn_server_response import CreateSslVpnServerResponse
from baiducloud_python_sdk_vpc.models.create_subnet_response import CreateSubnetResponse
from baiducloud_python_sdk_vpc.models.create_user_gateway_response import CreateUserGatewayResponse
from baiducloud_python_sdk_vpc.models.create_vpc_response import CreateVpcResponse
from baiducloud_python_sdk_vpc.models.create_vpn_response import CreateVpnResponse
from baiducloud_python_sdk_vpc.models.create_vpn_tunnel_response import CreateVpnTunnelResponse
from baiducloud_python_sdk_vpc.models.get_vpc_resource_ip_info_response import GetVpcResourceIpInfoResponse
from baiducloud_python_sdk_vpc.models.list_ip_reserve_response import ListIpReserveResponse
from baiducloud_python_sdk_vpc.models.query_acl_response import QueryAclResponse
from baiducloud_python_sdk_vpc.models.query_acl_rules_response import QueryAclRulesResponse
from baiducloud_python_sdk_vpc.models.query_ip_address_family_list_response import QueryIpAddressFamilyListResponse
from baiducloud_python_sdk_vpc.models.query_ipv6_gateway_response import QueryIpv6GatewayResponse
from baiducloud_python_sdk_vpc.models.query_network_detection_details_response import (
    QueryNetworkDetectionDetailsResponse,
)
from baiducloud_python_sdk_vpc.models.query_network_detection_list_response import QueryNetworkDetectionListResponse
from baiducloud_python_sdk_vpc.models.query_routing_rules_response import QueryRoutingRulesResponse
from baiducloud_python_sdk_vpc.models.query_routing_table_response import QueryRoutingTableResponse
from baiducloud_python_sdk_vpc.models.query_specified_subnet_response import QuerySpecifiedSubnetResponse
from baiducloud_python_sdk_vpc.models.query_specified_vpc_response import QuerySpecifiedVpcResponse
from baiducloud_python_sdk_vpc.models.query_ssl_vpn_server_response import QuerySslVpnServerResponse
from baiducloud_python_sdk_vpc.models.query_ssl_vpn_users_response import QuerySslVpnUsersResponse
from baiducloud_python_sdk_vpc.models.query_subnet_list_response import QuerySubnetListResponse
from baiducloud_python_sdk_vpc.models.query_the_details_of_the_dedicated_gateway_response import (
    QueryTheDetailsOfTheDedicatedGatewayResponse,
)
from baiducloud_python_sdk_vpc.models.query_the_list_of_dedicated_line_gateways_response import (
    QueryTheListOfDedicatedLineGatewaysResponse,
)
from baiducloud_python_sdk_vpc.models.query_the_list_of_elastic_network_cards_response import (
    QueryTheListOfElasticNetworkCardsResponse,
)
from baiducloud_python_sdk_vpc.models.query_the_list_of_enterprise_security_groups_response import (
    QueryTheListOfEnterpriseSecurityGroupsResponse,
)
from baiducloud_python_sdk_vpc.models.query_the_list_of_highly_available_virtual_ips_response import (
    QueryTheListOfHighlyAvailableVirtualIpsResponse,
)
from baiducloud_python_sdk_vpc.models.query_the_list_of_ip_address_groups_response import (
    QueryTheListOfIpAddressGroupsResponse,
)
from baiducloud_python_sdk_vpc.models.query_the_list_of_peer_connections_response import (
    QueryTheListOfPeerConnectionsResponse,
)
from baiducloud_python_sdk_vpc.models.query_the_list_of_regular_security_groups_v2_response import (
    QueryTheListOfRegularSecurityGroupsV2Response,
)
from baiducloud_python_sdk_vpc.models.query_the_list_of_speed_limit_policies_for_ipv6_gateway_response import (
    QueryTheListOfSpeedLimitPoliciesForIpv6GatewayResponse,
)
from baiducloud_python_sdk_vpc.models.query_the_specified_elastic_network_card_response import (
    QueryTheSpecifiedElasticNetworkCardResponse,
)
from baiducloud_python_sdk_vpc.models.query_the_specified_highly_available_virtual_ip_response import (
    QueryTheSpecifiedHighlyAvailableVirtualIpResponse,
)
from baiducloud_python_sdk_vpc.models.query_the_specified_ip_address_family_response import (
    QueryTheSpecifiedIpAddressFamilyResponse,
)
from baiducloud_python_sdk_vpc.models.query_the_specified_ip_address_group_response import (
    QueryTheSpecifiedIpAddressGroupResponse,
)
from baiducloud_python_sdk_vpc.models.query_the_status_of_the_elastic_network_card_response import (
    QueryTheStatusOfTheElasticNetworkCardResponse,
)
from baiducloud_python_sdk_vpc.models.query_vpc_intranet_ip_response import QueryVpcIntranetIpResponse
from baiducloud_python_sdk_vpc.models.query_vpc_list_response import QueryVpcListResponse
from baiducloud_python_sdk_vpc.models.query_vpn_list_response import QueryVpnListResponse
from baiducloud_python_sdk_vpc.models.querying_the_ipv6_policy_list_with_only_output_and_no_inclusion_response import (
    QueryingTheIpv6PolicyListWithOnlyOutputAndNoInclusionResponse,
)
from baiducloud_python_sdk_vpc.models.search_for_vpn_details_response import SearchForVpnDetailsResponse
from baiducloud_python_sdk_vpc.models.search_vpn_tunnel_response import SearchVpnTunnelResponse
from baiducloud_python_sdk_vpc.models.user_gateway_details_response import UserGatewayDetailsResponse
from baiducloud_python_sdk_vpc.models.user_gateway_list_response import UserGatewayListResponse
from baiducloud_python_sdk_vpc.models.view_gateway_limit_rules_response import ViewGatewayLimitRulesResponse
from baiducloud_python_sdk_vpc.models.view_peer_to_peer_connection_details_response import (
    ViewPeerToPeerConnectionDetailsResponse,
)
from baiducloud_python_sdk_vpc.models.view_security_group_details_v2_response import ViewSecurityGroupDetailsV2Response

_logger = logging.getLogger(__name__)


class VpcClient(BceBaseClient):
    """
    vpc base sdk client
    """

    VERSION_V1 = b'/v1'

    VERSION_V2 = b'/v2'

    CONSTANT_VPC = b'vpc'

    CONSTANT_SECURITY_GROUP = b'securityGroup'

    CONSTANT_RESOURCE_IP = b'resourceIp'

    CONSTANT_ENI = b'eni'

    CONSTANT_IP_GROUP = b'ipGroup'

    CONSTANT_PRIVATE_IP_ADDRESS_INFO = b'privateIpAddressInfo'

    CONSTANT_HAVIP = b'havip'

    CONSTANT_ET_GATEWAY = b'etGateway'

    CONSTANT_IP_SET = b'ipSet'

    CONSTANT_ENTERPRISE = b'enterprise'

    CONSTANT_SECURITY = b'security'

    CONSTANT_VPN = b'vpn'

    CONSTANT_CGW = b'cgw'

    CONSTANT_DELETE_IP_ADDRESS = b'deleteIpAddress'

    CONSTANT_PEERCONN = b'peerconn'

    CONSTANT_I_PV6_GATEWAY = b'IPv6Gateway'

    CONSTANT_RATE_LIMIT_RULE = b'rateLimitRule'

    CONSTANT_VPNCONN = b'vpnconn'

    CONSTANT_STATUS = b'status'

    CONSTANT_ACL = b'acl'

    CONSTANT_RULE = b'rule'

    CONSTANT_BIND_IP_SET = b'bindIpSet'

    CONSTANT_PROBE = b'probe'

    CONSTANT_GATEWAY = b'gateway'

    CONSTANT_LIMITRULE = b'limitrule'

    CONSTANT_SUBNET = b'subnet'

    CONSTANT_UPDATE = b'update'

    CONSTANT_IPRESERVE = b'ipreserve'

    CONSTANT_SSL_VPN_SERVER = b'sslVpnServer'

    CONSTANT_PRIVATE_IP = b'privateIp'

    CONSTANT_DELETE_PROTECT = b'deleteProtect'

    CONSTANT_IP_ADDRESS = b'ipAddress'

    CONSTANT_ROUTE = b'route'

    CONSTANT_EGRESS_ONLY_RULE = b'egressOnlyRule'

    CONSTANT_SHUTDOWN_RELAY = b'shutdownRelay'

    CONSTANT_HEALTH_CHECK = b'healthCheck'

    CONSTANT_SSL_VPN_USER = b'sslVpnUser'

    CONSTANT_UNBIND_IP_SET = b'unbindIpSet'

    CONSTANT_OPEN_RELAY = b'openRelay'

    CONSTANT_BATCH_ADD = b'batchAdd'

    CONSTANT_BATCH_DEL = b'batchDel'

    def __init__(self, config=None):
        """
        Initialize the vpc client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def accept_peer_to_peer_connection_applications(self, request, config=None):
        """
        accept_peer_to_peer_connection_applications

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_PEERCONN, request.peer_conn_id)
        headers = None
        params = {}
        params['accept'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def active_standby_switchover(self, request, config=None):
        """
        active_standby_switchover

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_ROUTE, VpcClient.CONSTANT_RULE, request.route_rule_id
        )
        headers = None
        params = {}
        params['switchRouteHA'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def add_acl_rule(self, request, config=None):
        """
        add_acl_rule

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_ACL, VpcClient.CONSTANT_RULE)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def add_elastic_network_card_auxiliary_ip(self, request, config=None):
        """
        add_elastic_network_card_auxiliary_ip

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing AddElasticNetworkCardAuxiliaryIpResponse data
        :rtype: AddElasticNetworkCardAuxiliaryIpResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_ENI, request.eni_id, VpcClient.CONSTANT_PRIVATE_IP
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=AddElasticNetworkCardAuxiliaryIpResponse,
        )

    def add_ip_address_group_to_ip_address_family(self, request, config=None):
        """
        add_ip_address_group_to_ip_address_family

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_IP_GROUP, request.ip_group_id, VpcClient.CONSTANT_BIND_IP_SET
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def add_ip_addresses_to_the_ip_address_group(self, request, config=None):
        """
        add_ip_addresses_to_the_ip_address_group

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_IP_SET, request.ip_set_id, VpcClient.CONSTANT_IP_ADDRESS
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def add_ipv6_only_outbound_and_no_inbound_policy(self, request, config=None):
        """
        add_ipv6_only_outbound_and_no_inbound_policy

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing AddIpv6OnlyOutboundAndNoInboundPolicyResponse data
        :rtype: AddIpv6OnlyOutboundAndNoInboundPolicyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1,
            VpcClient.CONSTANT_I_PV6_GATEWAY,
            request.gateway_id,
            VpcClient.CONSTANT_EGRESS_ONLY_RULE,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=AddIpv6OnlyOutboundAndNoInboundPolicyResponse,
        )

    def authorize_regular_security_group_rules_v2(self, request, config=None):
        """
        authorize_regular_security_group_rules_v2

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V2, VpcClient.CONSTANT_SECURITY_GROUP, request.security_group_id)
        headers = None
        params = {}
        params['authorizeRule'] = None
        if request.sg_version is not None:
            params['sgVersion'] = request.sg_version
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def authorized_enterprise_security_group_rules(self, request, config=None):
        """
        authorized_enterprise_security_group_rules

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1,
            VpcClient.CONSTANT_ENTERPRISE,
            VpcClient.CONSTANT_SECURITY,
            request.enterprise_security_group_id,
        )
        headers = None
        params = {}
        params['authorizeRule'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def batch_create_ssl_vpn_users(self, request, config=None):
        """
        batch_create_ssl_vpn_users

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BatchCreateSslVpnUsersResponse data
        :rtype: BatchCreateSslVpnUsersResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, request.vpn_id, VpcClient.CONSTANT_SSL_VPN_USER
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=BatchCreateSslVpnUsersResponse,
        )

    def batch_delete_elastic_network_card_intranet_ip(self, request, config=None):
        """
        batch_delete_elastic_network_card_intranet_ip

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1,
            VpcClient.CONSTANT_ENI,
            request.eni_id,
            VpcClient.CONSTANT_PRIVATE_IP,
            VpcClient.CONSTANT_BATCH_DEL,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def batch_increase_elastic_network_card_intranet_ip(self, request, config=None):
        """
        batch_increase_elastic_network_card_intranet_ip

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BatchIncreaseElasticNetworkCardIntranetIpResponse data
        :rtype: BatchIncreaseElasticNetworkCardIntranetIpResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1,
            VpcClient.CONSTANT_ENI,
            request.eni_id,
            VpcClient.CONSTANT_PRIVATE_IP,
            VpcClient.CONSTANT_BATCH_ADD,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=BatchIncreaseElasticNetworkCardIntranetIpResponse,
        )

    def bind_eip(self, request, config=None):
        """
        bind_eip

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, request.vpn_id)
        headers = None
        params = {}
        params['bind'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def bind_physical_dedicated_line(self, request, config=None):
        """
        bind_physical_dedicated_line

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_ET_GATEWAY, request.et_gateway_id)
        headers = None
        params = {}
        params['bind'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def close_peer_to_peer_connection_to_synchronize_dns(self, request, config=None):
        """
        close_peer_to_peer_connection_to_synchronize_dns

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_PEERCONN, request.peer_conn_id)
        headers = None
        params = {}
        params['close'] = None
        if request.role is not None:
            params['role'] = request.role
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def close_vpc_relay(self, request, config=None):
        """
        close_vpc_relay

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_VPC, VpcClient.CONSTANT_SHUTDOWN_RELAY, request.vpc_id
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def create_a_highly_available_virtual_ip(self, request, config=None):
        """
        create_a_highly_available_virtual_ip

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateAHighlyAvailableVirtualIpResponse data
        :rtype: CreateAHighlyAvailableVirtualIpResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_HAVIP)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateAHighlyAvailableVirtualIpResponse,
        )

    def create_a_peer_to_peer_connection(self, request, config=None):
        """
        create_a_peer_to_peer_connection

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateAPeerToPeerConnectionResponse data
        :rtype: CreateAPeerToPeerConnectionResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_PEERCONN)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateAPeerToPeerConnectionResponse,
        )

    def create_a_regular_security_group_v2(self, request, config=None):
        """
        create_a_regular_security_group_v2

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateARegularSecurityGroupV2Response data
        :rtype: CreateARegularSecurityGroupV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V2, VpcClient.CONSTANT_SECURITY_GROUP)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateARegularSecurityGroupV2Response,
        )

    def create_an_ipv6_gateway(self, request, config=None):
        """
        create_an_ipv6_gateway

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateAnIpv6GatewayResponse data
        :rtype: CreateAnIpv6GatewayResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_I_PV6_GATEWAY)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateAnIpv6GatewayResponse,
        )

    def create_dedicated_gateway(self, request, config=None):
        """
        create_dedicated_gateway

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateDedicatedGatewayResponse data
        :rtype: CreateDedicatedGatewayResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_ET_GATEWAY)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateDedicatedGatewayResponse,
        )

    def create_dedicated_gateway_health_check(self, request, config=None):
        """
        create_dedicated_gateway_health_check

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_ET_GATEWAY, request.et_gateway_id, VpcClient.CONSTANT_HEALTH_CHECK
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def create_elastic_network_card(self, request, config=None):
        """
        create_elastic_network_card

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateElasticNetworkCardResponse data
        :rtype: CreateElasticNetworkCardResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_ENI)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateElasticNetworkCardResponse,
        )

    def create_enterprise_security_group(self, request, config=None):
        """
        create_enterprise_security_group

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateEnterpriseSecurityGroupResponse data
        :rtype: CreateEnterpriseSecurityGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_ENTERPRISE, VpcClient.CONSTANT_SECURITY)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateEnterpriseSecurityGroupResponse,
        )

    def create_gateway_limit_rules(self, request, config=None):
        """
        create_gateway_limit_rules

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateGatewayLimitRulesResponse data
        :rtype: CreateGatewayLimitRulesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_GATEWAY, VpcClient.CONSTANT_LIMITRULE)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateGatewayLimitRulesResponse,
        )

    def create_ip_address_family(self, request, config=None):
        """
        create_ip_address_family

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateIpAddressFamilyResponse data
        :rtype: CreateIpAddressFamilyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_IP_GROUP)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateIpAddressFamilyResponse,
        )

    def create_ip_address_group(self, request, config=None):
        """
        create_ip_address_group

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateIpAddressGroupResponse data
        :rtype: CreateIpAddressGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_IP_SET)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateIpAddressGroupResponse,
        )

    def create_ip_reserved(self, request, config=None):
        """
        create_ip_reserved

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateIpReservedResponse data
        :rtype: CreateIpReservedResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_SUBNET, VpcClient.CONSTANT_IPRESERVE)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateIpReservedResponse,
        )

    def create_ipv6_gateway_speed_limit_policy(self, request, config=None):
        """
        create_ipv6_gateway_speed_limit_policy

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateIpv6GatewaySpeedLimitPolicyResponse data
        :rtype: CreateIpv6GatewaySpeedLimitPolicyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1,
            VpcClient.CONSTANT_I_PV6_GATEWAY,
            request.gateway_id,
            VpcClient.CONSTANT_RATE_LIMIT_RULE,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateIpv6GatewaySpeedLimitPolicyResponse,
        )

    def create_network_detection(self, request, config=None):
        """
        create_network_detection

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateNetworkDetectionResponse data
        :rtype: CreateNetworkDetectionResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_PROBE)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateNetworkDetectionResponse,
        )

    def create_routing_rules(self, request, config=None):
        """
        create_routing_rules

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateRoutingRulesResponse data
        :rtype: CreateRoutingRulesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_ROUTE, VpcClient.CONSTANT_RULE)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateRoutingRulesResponse,
        )

    def create_ssl_vpn_server(self, request, config=None):
        """
        create_ssl_vpn_server

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateSslVpnServerResponse data
        :rtype: CreateSslVpnServerResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, request.vpn_id, VpcClient.CONSTANT_SSL_VPN_SERVER
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateSslVpnServerResponse,
        )

    def create_subnet(self, request, config=None):
        """
        create_subnet

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateSubnetResponse data
        :rtype: CreateSubnetResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_SUBNET)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateSubnetResponse,
        )

    def create_user_gateway(self, request, config=None):
        """
        create_user_gateway

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateUserGatewayResponse data
        :rtype: CreateUserGatewayResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, VpcClient.CONSTANT_CGW)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateUserGatewayResponse,
        )

    def create_vpc(self, request, config=None):
        """
        create_vpc

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateVpcResponse data
        :rtype: CreateVpcResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPC)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateVpcResponse,
        )

    def create_vpn(self, request, config=None):
        """
        create_vpn

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateVpnResponse data
        :rtype: CreateVpnResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateVpnResponse,
        )

    def create_vpn_tunnel(self, request, config=None):
        """
        create_vpn_tunnel

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateVpnTunnelResponse data
        :rtype: CreateVpnTunnelResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, request.vpn_id, VpcClient.CONSTANT_VPNCONN
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateVpnTunnelResponse,
        )

    def delete_acl_rule(self, request, config=None):
        """
        delete_acl_rule

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_ACL, VpcClient.CONSTANT_RULE, request.acl_rule_id
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_elastic_network_card_auxiliary_ip(self, request, config=None):
        """
        delete_elastic_network_card_auxiliary_ip

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1,
            VpcClient.CONSTANT_ENI,
            request.eni_id,
            VpcClient.CONSTANT_PRIVATE_IP,
            request.private_ip_address,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_enterprise_security_group(self, request, config=None):
        """
        delete_enterprise_security_group

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1,
            VpcClient.CONSTANT_ENTERPRISE,
            VpcClient.CONSTANT_SECURITY,
            request.enterprise_security_group_id,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_enterprise_security_group_rules(self, request, config=None):
        """
        delete_enterprise_security_group_rules

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1,
            VpcClient.CONSTANT_ENTERPRISE,
            VpcClient.CONSTANT_SECURITY,
            VpcClient.CONSTANT_RULE,
            request.enterprise_security_group_rule_id,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_gateway_limit_rule(self, request, config=None):
        """
        delete_gateway_limit_rule

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_GATEWAY, VpcClient.CONSTANT_LIMITRULE, request.glr_id
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_highly_available_virtual_ip(self, request, config=None):
        """
        delete_highly_available_virtual_ip

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_HAVIP, request.ha_vip_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_ip_address_family(self, request, config=None):
        """
        delete_ip_address_family

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_IP_GROUP, request.ip_group_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_ip_address_from_ip_address_group(self, request, config=None):
        """
        delete_ip_address_from_ip_address_group

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_IP_SET, request.ip_set_id, VpcClient.CONSTANT_DELETE_IP_ADDRESS
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def delete_ip_address_group(self, request, config=None):
        """
        delete_ip_address_group

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_IP_SET, request.ip_set_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_ip_reserve(self, request, config=None):
        """
        delete_ip_reserve

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_SUBNET, VpcClient.CONSTANT_IPRESERVE, request.ip_reserve_id
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_ipv6_gateway(self, request, config=None):
        """
        delete_ipv6_gateway

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_I_PV6_GATEWAY, request.gateway_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_ipv6_gateway_speed_limit_policy(self, request, config=None):
        """
        delete_ipv6_gateway_speed_limit_policy

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1,
            VpcClient.CONSTANT_I_PV6_GATEWAY,
            request.gateway_id,
            VpcClient.CONSTANT_RATE_LIMIT_RULE,
            request.rate_limit_rule_id,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_ipv6_only_access_policy(self, request, config=None):
        """
        delete_ipv6_only_access_policy

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1,
            VpcClient.CONSTANT_I_PV6_GATEWAY,
            request.gateway_id,
            VpcClient.CONSTANT_EGRESS_ONLY_RULE,
            request.egress_only_rule_id,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_network_detection(self, request, config=None):
        """
        delete_network_detection

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_PROBE, request.probe_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_regular_security_group_rules_v2(self, request, config=None):
        """
        delete_regular_security_group_rules_v2

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V2,
            VpcClient.CONSTANT_SECURITY_GROUP,
            VpcClient.CONSTANT_RULE,
            request.security_group_rule_id,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        if request.sg_version is not None:
            params['sgVersion'] = request.sg_version
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_regular_security_group_v2(self, request, config=None):
        """
        delete_regular_security_group_v2

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V2, VpcClient.CONSTANT_SECURITY_GROUP, request.security_group_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_routing_rules(self, request, config=None):
        """
        delete_routing_rules

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_ROUTE, VpcClient.CONSTANT_RULE, request.route_rule_id
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_ssl_vpn_server(self, request, config=None):
        """
        delete_ssl_vpn_server

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1,
            VpcClient.CONSTANT_VPN,
            request.vpn_id,
            VpcClient.CONSTANT_SSL_VPN_SERVER,
            request.ssl_vpn_server_id,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_ssl_vpn_user(self, request, config=None):
        """
        delete_ssl_vpn_user

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1,
            VpcClient.CONSTANT_VPN,
            request.vpn_id,
            VpcClient.CONSTANT_SSL_VPN_USER,
            request.user_id,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_subnet(self, request, config=None):
        """
        delete_subnet

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_SUBNET, request.subnet_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_user_gateway(self, request, config=None):
        """
        delete_user_gateway

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, VpcClient.CONSTANT_CGW, request.cgw_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def delete_vpc(self, request, config=None):
        """
        delete_vpc

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPC, request.vpc_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_vpn_tunnel(self, request, config=None):
        """
        delete_vpn_tunnel

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, VpcClient.CONSTANT_VPNCONN, request.vpn_conn_id
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def elastic_network_card_binding_eip(self, request, config=None):
        """
        elastic_network_card_binding_eip

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_ENI, request.eni_id)
        headers = None
        params = {}
        params['bind'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def elastic_network_card_mounted_cloud_product_instance(self, request, config=None):
        """
        elastic_network_card_mounted_cloud_product_instance

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_ENI, request.eni_id)
        headers = None
        params = {}
        params['attach'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def elastic_network_card_unbinding_eip(self, request, config=None):
        """
        elastic_network_card_unbinding_eip

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_ENI, request.eni_id)
        headers = None
        params = {}
        params['unBind'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def elastic_network_card_uninstallation_cloud_product_instance(self, request, config=None):
        """
        elastic_network_card_uninstallation_cloud_product_instance

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_ENI, request.eni_id)
        headers = None
        params = {}
        params['detach'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def elastic_network_card_update_enterprise_security_group(self, request, config=None):
        """
        elastic_network_card_update_enterprise_security_group

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_ENI, request.eni_id)
        headers = None
        params = {}
        params['bindEsg'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def elastic_network_card_updates_regular_security_group(self, request, config=None):
        """
        elastic_network_card_updates_regular_security_group

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_ENI, request.eni_id)
        headers = None
        params = {}
        params['bindSg'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def enable_peer_to_peer_connection_to_synchronize_dns(self, request, config=None):
        """
        enable_peer_to_peer_connection_to_synchronize_dns

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_PEERCONN, request.peer_conn_id)
        headers = None
        params = {}
        params['open'] = None
        if request.role is not None:
            params['role'] = request.role
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def get_vpc_resource_ip_info(self, request, config=None):
        """
        get_vpc_resource_ip_info

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetVpcResourceIpInfoResponse data
        :rtype: GetVpcResourceIpInfoResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPC, VpcClient.CONSTANT_RESOURCE_IP)
        headers = None
        params = {}
        if request.vpc_id is not None:
            params['vpcId'] = request.vpc_id
        if request.subnet_id is not None:
            params['subnetId'] = request.subnet_id
        if request.resource_type is not None:
            params['resourceType'] = request.resource_type
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetVpcResourceIpInfoResponse
        )

    def high_availability_virtual_ip_unbinding_eip(self, request, config=None):
        """
        high_availability_virtual_ip_unbinding_eip

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_HAVIP, request.ha_vip_id)
        headers = None
        params = {}
        params['unbindPublicIp'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def high_availability_virtual_ip_unbinding_instance(self, request, config=None):
        """
        high_availability_virtual_ip_unbinding_instance

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_HAVIP, request.ha_vip_id)
        headers = None
        params = {}
        params['detach'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def highly_available_virtual_ip_binding_eip(self, request, config=None):
        """
        highly_available_virtual_ip_binding_eip

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_HAVIP, request.ha_vip_id)
        headers = None
        params = {}
        params['bindPublicIp'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def highly_available_virtual_ip_binding_instance(self, request, config=None):
        """
        highly_available_virtual_ip_binding_instance

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_HAVIP, request.ha_vip_id)
        headers = None
        params = {}
        params['attach'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def ipv6_gateway_bandwidth_upgrade_and_downgrade(self, request, config=None):
        """
        ipv6_gateway_bandwidth_upgrade_and_downgrade

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_I_PV6_GATEWAY, request.gateway_id)
        headers = None
        params = {}
        params['resize'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def list_ip_reserve(self, request, config=None):
        """
        list_ip_reserve

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListIpReserveResponse data
        :rtype: ListIpReserveResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_SUBNET, VpcClient.CONSTANT_IPRESERVE)
        headers = None
        params = {}
        if request.subnet_id is not None:
            params['subnetId'] = request.subnet_id
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListIpReserveResponse
        )

    def modify_gateway_limit_rules(self, request, config=None):
        """
        modify_gateway_limit_rules

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_GATEWAY, VpcClient.CONSTANT_LIMITRULE, request.glr_id
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def open_vpc_relay(self, request, config=None):
        """
        open_vpc_relay

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_VPC, VpcClient.CONSTANT_OPEN_RELAY, request.vpc_id
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def peer_to_peer_connection_bandwidth_upgrade_and_downgrade(self, request, config=None):
        """
        peer_to_peer_connection_bandwidth_upgrade_and_downgrade

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_PEERCONN, request.peer_conn_id)
        headers = None
        params = {}
        params['resize'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def peer_to_peer_connection_renewal(self, request, config=None):
        """
        peer_to_peer_connection_renewal

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_PEERCONN, request.peer_conn_id)
        headers = None
        params = {}
        params['purchaseReserved'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def prepaid_peer_to_peer_connection_unsubscribe(self, request, config=None):
        """
        prepaid_peer_to_peer_connection_unsubscribe

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_PEERCONN, request.peer_conn_id)
        headers = None
        params = {}
        params['refund'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def query_acl(self, request, config=None):
        """
        query_acl

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryAclResponse data
        :rtype: QueryAclResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_ACL)
        headers = None
        params = {}
        if request.vpc_id is not None:
            params['vpcId'] = request.vpc_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryAclResponse
        )

    def query_acl_rules(self, request, config=None):
        """
        query_acl_rules

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryAclRulesResponse data
        :rtype: QueryAclRulesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_ACL, VpcClient.CONSTANT_RULE)
        headers = None
        params = {}
        if request.subnet_id is not None:
            params['subnetId'] = request.subnet_id
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryAclRulesResponse
        )

    def query_ip_address_family_list(self, request, config=None):
        """
        query_ip_address_family_list

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryIpAddressFamilyListResponse data
        :rtype: QueryIpAddressFamilyListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_IP_GROUP)
        headers = None
        params = {}
        if request.ip_version is not None:
            params['ipVersion'] = request.ip_version
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryIpAddressFamilyListResponse
        )

    def query_ipv6_gateway(self, request, config=None):
        """
        query_ipv6_gateway

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryIpv6GatewayResponse data
        :rtype: QueryIpv6GatewayResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_I_PV6_GATEWAY)
        headers = None
        params = {}
        if request.vpc_id is not None:
            params['vpcId'] = request.vpc_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryIpv6GatewayResponse
        )

    def query_network_detection_details(self, request, config=None):
        """
        query_network_detection_details

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryNetworkDetectionDetailsResponse data
        :rtype: QueryNetworkDetectionDetailsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_PROBE, request.probe_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=QueryNetworkDetectionDetailsResponse
        )

    def query_network_detection_list(self, request, config=None):
        """
        query_network_detection_list

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryNetworkDetectionListResponse data
        :rtype: QueryNetworkDetectionListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_PROBE)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryNetworkDetectionListResponse
        )

    def query_routing_rules(self, request, config=None):
        """
        query_routing_rules

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryRoutingRulesResponse data
        :rtype: QueryRoutingRulesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_ROUTE, VpcClient.CONSTANT_RULE)
        headers = None
        params = {}
        if request.route_table_id is not None:
            params['routeTableId'] = request.route_table_id
        if request.vpc_id is not None:
            params['vpcId'] = request.vpc_id
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryRoutingRulesResponse
        )

    def query_routing_table(self, request, config=None):
        """
        query_routing_table

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryRoutingTableResponse data
        :rtype: QueryRoutingTableResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_ROUTE)
        headers = None
        params = {}
        if request.route_table_id is not None:
            params['routeTableId'] = request.route_table_id
        if request.vpc_id is not None:
            params['vpcId'] = request.vpc_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryRoutingTableResponse
        )

    def query_specified_subnet(self, request, config=None):
        """
        query_specified_subnet

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QuerySpecifiedSubnetResponse data
        :rtype: QuerySpecifiedSubnetResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_SUBNET, request.subnet_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=QuerySpecifiedSubnetResponse
        )

    def query_specified_vpc(self, request, config=None):
        """
        query_specified_vpc

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QuerySpecifiedVpcResponse data
        :rtype: QuerySpecifiedVpcResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPC, request.vpc_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=QuerySpecifiedVpcResponse)

    def query_ssl_vpn_server(self, request, config=None):
        """
        query_ssl_vpn_server

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QuerySslVpnServerResponse data
        :rtype: QuerySslVpnServerResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, request.vpn_id, VpcClient.CONSTANT_SSL_VPN_SERVER
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QuerySslVpnServerResponse
        )

    def query_ssl_vpn_users(self, request, config=None):
        """
        query_ssl_vpn_users

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QuerySslVpnUsersResponse data
        :rtype: QuerySslVpnUsersResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, request.vpn_id, VpcClient.CONSTANT_SSL_VPN_USER
        )
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.user_name is not None:
            params['userName'] = request.user_name
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QuerySslVpnUsersResponse
        )

    def query_subnet_list(self, request, config=None):
        """
        query_subnet_list

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QuerySubnetListResponse data
        :rtype: QuerySubnetListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_SUBNET)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.vpc_id is not None:
            params['vpcId'] = request.vpc_id
        if request.zone_name is not None:
            params['zoneName'] = request.zone_name
        if request.subnet_type is not None:
            params['subnetType'] = request.subnet_type
        if request.subnet_ids is not None:
            params['subnetIds'] = request.subnet_ids
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QuerySubnetListResponse
        )

    def query_the_details_of_the_dedicated_gateway(self, request, config=None):
        """
        query_the_details_of_the_dedicated_gateway

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryTheDetailsOfTheDedicatedGatewayResponse data
        :rtype: QueryTheDetailsOfTheDedicatedGatewayResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_ET_GATEWAY, request.et_gateway_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=QueryTheDetailsOfTheDedicatedGatewayResponse
        )

    def query_the_list_of_dedicated_line_gateways(self, request, config=None):
        """
        query_the_list_of_dedicated_line_gateways

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryTheListOfDedicatedLineGatewaysResponse data
        :rtype: QueryTheListOfDedicatedLineGatewaysResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_ET_GATEWAY)
        headers = None
        params = {}
        if request.vpc_id is not None:
            params['vpcId'] = request.vpc_id
        if request.et_gateway_id is not None:
            params['etGatewayId'] = request.et_gateway_id
        if request.name is not None:
            params['name'] = request.name
        if request.status is not None:
            params['status'] = request.status
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            params=params,
            config=merged_config,
            model=QueryTheListOfDedicatedLineGatewaysResponse,
        )

    def query_the_list_of_elastic_network_cards(self, request, config=None):
        """
        query_the_list_of_elastic_network_cards

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryTheListOfElasticNetworkCardsResponse data
        :rtype: QueryTheListOfElasticNetworkCardsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_ENI)
        headers = None
        params = {}
        if request.vpc_id is not None:
            params['vpcId'] = request.vpc_id
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.name is not None:
            params['name'] = request.name
        if request.private_ip_address is not None:
            params['privateIpAddress'] = ','.join(request.private_ip_address)
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            params=params,
            config=merged_config,
            model=QueryTheListOfElasticNetworkCardsResponse,
        )

    def query_the_list_of_enterprise_security_groups(self, request, config=None):
        """
        query_the_list_of_enterprise_security_groups

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryTheListOfEnterpriseSecurityGroupsResponse data
        :rtype: QueryTheListOfEnterpriseSecurityGroupsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_ENTERPRISE, VpcClient.CONSTANT_SECURITY)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            params=params,
            config=merged_config,
            model=QueryTheListOfEnterpriseSecurityGroupsResponse,
        )

    def query_the_list_of_highly_available_virtual_ips(self, request, config=None):
        """
        query_the_list_of_highly_available_virtual_ips

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryTheListOfHighlyAvailableVirtualIpsResponse data
        :rtype: QueryTheListOfHighlyAvailableVirtualIpsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_HAVIP)
        headers = None
        params = {}
        if request.vpc_id is not None:
            params['vpcId'] = request.vpc_id
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            params=params,
            config=merged_config,
            model=QueryTheListOfHighlyAvailableVirtualIpsResponse,
        )

    def query_the_list_of_ip_address_groups(self, request, config=None):
        """
        query_the_list_of_ip_address_groups

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryTheListOfIpAddressGroupsResponse data
        :rtype: QueryTheListOfIpAddressGroupsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_IP_SET)
        headers = None
        params = {}
        if request.ip_version is not None:
            params['ipVersion'] = request.ip_version
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            params=params,
            config=merged_config,
            model=QueryTheListOfIpAddressGroupsResponse,
        )

    def query_the_list_of_peer_connections(self, request, config=None):
        """
        query_the_list_of_peer_connections

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryTheListOfPeerConnectionsResponse data
        :rtype: QueryTheListOfPeerConnectionsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_PEERCONN)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            params=params,
            config=merged_config,
            model=QueryTheListOfPeerConnectionsResponse,
        )

    def query_the_list_of_regular_security_groups_v2(self, request, config=None):
        """
        query_the_list_of_regular_security_groups_v2

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryTheListOfRegularSecurityGroupsV2Response data
        :rtype: QueryTheListOfRegularSecurityGroupsV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V2, VpcClient.CONSTANT_SECURITY_GROUP)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.vpc_id is not None:
            params['vpcId'] = request.vpc_id
        if request.security_group_id is not None:
            params['securityGroupId'] = request.security_group_id
        if request.security_group_ids is not None:
            params['securityGroupIds'] = request.security_group_ids
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            params=params,
            config=merged_config,
            model=QueryTheListOfRegularSecurityGroupsV2Response,
        )

    def query_the_list_of_speed_limit_policies_for_ipv6_gateway(self, request, config=None):
        """
        query_the_list_of_speed_limit_policies_for_ipv6_gateway

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryTheListOfSpeedLimitPoliciesForIpv6GatewayResponse data
        :rtype: QueryTheListOfSpeedLimitPoliciesForIpv6GatewayResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1,
            VpcClient.CONSTANT_I_PV6_GATEWAY,
            request.gateway_id,
            VpcClient.CONSTANT_RATE_LIMIT_RULE,
        )
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            params=params,
            config=merged_config,
            model=QueryTheListOfSpeedLimitPoliciesForIpv6GatewayResponse,
        )

    def query_the_specified_elastic_network_card(self, request, config=None):
        """
        query_the_specified_elastic_network_card

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryTheSpecifiedElasticNetworkCardResponse data
        :rtype: QueryTheSpecifiedElasticNetworkCardResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_ENI, request.eni_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=QueryTheSpecifiedElasticNetworkCardResponse
        )

    def query_the_specified_highly_available_virtual_ip(self, request, config=None):
        """
        query_the_specified_highly_available_virtual_ip

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryTheSpecifiedHighlyAvailableVirtualIpResponse data
        :rtype: QueryTheSpecifiedHighlyAvailableVirtualIpResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_HAVIP, request.ha_vip_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=QueryTheSpecifiedHighlyAvailableVirtualIpResponse
        )

    def query_the_specified_ip_address_family(self, request, config=None):
        """
        query_the_specified_ip_address_family

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryTheSpecifiedIpAddressFamilyResponse data
        :rtype: QueryTheSpecifiedIpAddressFamilyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_IP_GROUP, request.ip_group_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=QueryTheSpecifiedIpAddressFamilyResponse
        )

    def query_the_specified_ip_address_group(self, request, config=None):
        """
        query_the_specified_ip_address_group

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryTheSpecifiedIpAddressGroupResponse data
        :rtype: QueryTheSpecifiedIpAddressGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_IP_SET, request.ip_set_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=QueryTheSpecifiedIpAddressGroupResponse
        )

    def query_the_status_of_the_elastic_network_card(self, request, config=None):
        """
        query_the_status_of_the_elastic_network_card

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryTheStatusOfTheElasticNetworkCardResponse data
        :rtype: QueryTheStatusOfTheElasticNetworkCardResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_ENI, request.eni_id, VpcClient.CONSTANT_STATUS
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=QueryTheStatusOfTheElasticNetworkCardResponse
        )

    def query_vpc_intranet_ip(self, request, config=None):
        """
        query_vpc_intranet_ip

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryVpcIntranetIpResponse data
        :rtype: QueryVpcIntranetIpResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_VPC, request.vpc_id, VpcClient.CONSTANT_PRIVATE_IP_ADDRESS_INFO
        )
        headers = None
        params = {}
        if request.private_ip_addresses is not None:
            params['privateIpAddresses'] = ','.join(request.private_ip_addresses)
        if request.private_ip_range is not None:
            params['privateIpRange'] = request.private_ip_range
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryVpcIntranetIpResponse
        )

    def query_vpc_list(self, request, config=None):
        """
        query_vpc_list

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryVpcListResponse data
        :rtype: QueryVpcListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPC)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.is_default is not None:
            params['isDefault'] = request.is_default
        if request.vpc_ids is not None:
            params['vpcIds'] = request.vpc_ids
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryVpcListResponse
        )

    def query_vpn_list(self, request, config=None):
        """
        query_vpn_list

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryVpnListResponse data
        :rtype: QueryVpnListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN)
        headers = None
        params = {}
        if request.vpc_id is not None:
            params['vpcId'] = request.vpc_id
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.eip is not None:
            params['eip'] = request.eip
        if request.type is not None:
            params['type'] = request.type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryVpnListResponse
        )

    def querying_the_ipv6_policy_list_with_only_output_and_no_inclusion(self, request, config=None):
        """
        querying_the_ipv6_policy_list_with_only_output_and_no_inclusion

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryingTheIpv6PolicyListWithOnlyOutputAndNoInclusionResponse data
        :rtype: QueryingTheIpv6PolicyListWithOnlyOutputAndNoInclusionResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1,
            VpcClient.CONSTANT_I_PV6_GATEWAY,
            request.gateway_id,
            VpcClient.CONSTANT_EGRESS_ONLY_RULE,
        )
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            params=params,
            config=merged_config,
            model=QueryingTheIpv6PolicyListWithOnlyOutputAndNoInclusionResponse,
        )

    def reject_peer_to_peer_connection_request(self, request, config=None):
        """
        reject_peer_to_peer_connection_request

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_PEERCONN, request.peer_conn_id)
        headers = None
        params = {}
        params['reject'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def release_dedicated_gateway(self, request, config=None):
        """
        release_dedicated_gateway

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_ET_GATEWAY, request.et_gateway_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def release_peer_to_peer_connection(self, request, config=None):
        """
        release_peer_to_peer_connection

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_PEERCONN, request.peer_conn_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def release_vpn(self, request, config=None):
        """
        release_vpn

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, request.vpn_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def remove_elastic_network_card(self, request, config=None):
        """
        remove_elastic_network_card

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_ENI, request.eni_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def remove_ip_address_group_from_ip_address_family(self, request, config=None):
        """
        remove_ip_address_group_from_ip_address_family

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_IP_GROUP, request.ip_group_id, VpcClient.CONSTANT_UNBIND_IP_SET
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def renew_vpn(self, request, config=None):
        """
        renew_vpn

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, request.vpn_id)
        headers = None
        params = {}
        params['purchaseReserved'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def revoke_regular_security_group_rules_v2(self, request, config=None):
        """
        revoke_regular_security_group_rules_v2

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V2, VpcClient.CONSTANT_SECURITY_GROUP, request.security_group_id)
        headers = None
        params = {}
        params['revokeRule'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        if request.sg_version is not None:
            params['sgVersion'] = request.sg_version
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def search_for_vpn_details(self, request, config=None):
        """
        search_for_vpn_details

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing SearchForVpnDetailsResponse data
        :rtype: SearchForVpnDetailsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, request.vpn_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=SearchForVpnDetailsResponse)

    def search_vpn_tunnel(self, request, config=None):
        """
        search_vpn_tunnel

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing SearchVpnTunnelResponse data
        :rtype: SearchVpnTunnelResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, VpcClient.CONSTANT_VPNCONN, request.vpn_id
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=SearchVpnTunnelResponse
        )

    def unbind_eip(self, request, config=None):
        """
        unbind_eip

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, request.vpn_id)
        headers = None
        params = {}
        params['unbind'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def unbind_physical_dedicated_line(self, request, config=None):
        """
        unbind_physical_dedicated_line

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_ET_GATEWAY, request.et_gateway_id)
        headers = None
        params = {}
        params['unbind'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def update_acl_rules(self, request, config=None):
        """
        update_acl_rules

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_ACL, VpcClient.CONSTANT_RULE, request.acl_rule_id
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_dedicated_gateway(self, request, config=None):
        """
        update_dedicated_gateway

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_ET_GATEWAY, request.et_gateway_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_elastic_network_card(self, request, config=None):
        """
        update_elastic_network_card

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_ENI, request.eni_id)
        headers = None
        params = {}
        params['modifyAttribute'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_enterprise_security_group_rules(self, request, config=None):
        """
        update_enterprise_security_group_rules

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1,
            VpcClient.CONSTANT_ENTERPRISE,
            VpcClient.CONSTANT_SECURITY,
            VpcClient.CONSTANT_RULE,
            request.enterprise_security_group_rule_id,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_highly_available_virtual_ip(self, request, config=None):
        """
        update_highly_available_virtual_ip

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_HAVIP, request.ha_vip_id)
        headers = None
        params = {}
        params['modifyAttribute'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_ip_address_family(self, request, config=None):
        """
        update_ip_address_family

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_IP_GROUP, request.ip_group_id)
        headers = None
        params = {}
        params['modifyAttribute'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_ip_address_group(self, request, config=None):
        """
        update_ip_address_group

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_IP_SET, request.ip_set_id)
        headers = None
        params = {}
        params['modifyAttribute'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_ipv6_gateway_release_protection_switch(self, request, config=None):
        """
        update_ipv6_gateway_release_protection_switch

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1,
            VpcClient.CONSTANT_I_PV6_GATEWAY,
            request.gateway_id,
            VpcClient.CONSTANT_DELETE_PROTECT,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_ipv6_gateway_speed_limit_policy(self, request, config=None):
        """
        update_ipv6_gateway_speed_limit_policy

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1,
            VpcClient.CONSTANT_I_PV6_GATEWAY,
            request.gateway_id,
            VpcClient.CONSTANT_RATE_LIMIT_RULE,
            request.rate_limit_rule_id,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_network_detection(self, request, config=None):
        """
        update_network_detection

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_PROBE, request.probe_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_peer_to_peer_connection_release_protection_switch(self, request, config=None):
        """
        update_peer_to_peer_connection_release_protection_switch

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_PEERCONN, request.peer_conn_id, VpcClient.CONSTANT_DELETE_PROTECT
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def update_regular_security_group_rules_v2(self, request, config=None):
        """
        update_regular_security_group_rules_v2

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V2, VpcClient.CONSTANT_SECURITY_GROUP, VpcClient.CONSTANT_RULE, VpcClient.CONSTANT_UPDATE
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        if request.sg_version is not None:
            params['sgVersion'] = request.sg_version
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_routing_rules(self, request, config=None):
        """
        update_routing_rules

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_ROUTE, VpcClient.CONSTANT_RULE, request.route_rule_id
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_ssl_vpn_server(self, request, config=None):
        """
        update_ssl_vpn_server

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1,
            VpcClient.CONSTANT_VPN,
            request.vpn_id,
            VpcClient.CONSTANT_SSL_VPN_SERVER,
            request.ssl_vpn_server_id,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_ssl_vpn_users(self, request, config=None):
        """
        update_ssl_vpn_users

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1,
            VpcClient.CONSTANT_VPN,
            request.vpn_id,
            VpcClient.CONSTANT_SSL_VPN_USER,
            request.user_id,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_subnet(self, request, config=None):
        """
        update_subnet

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_SUBNET, request.subnet_id)
        headers = None
        params = {}
        params['modifyAttribute'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_the_name_and_comments_of_the_local_interface_for_peer_to_peer_connections(self, request, config=None):
        """
        update_the_name_and_comments_of_the_local_interface_for_peer_to_peer_connections

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_PEERCONN, request.peer_conn_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def update_user_gateway(self, request, config=None):
        """
        update_user_gateway

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, VpcClient.CONSTANT_CGW, request.cgw_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_vpc(self, request, config=None):
        """
        update_vpc

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPC, request.vpc_id)
        headers = None
        params = {}
        params['modifyAttribute'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_vpn(self, request, config=None):
        """
        update_vpn

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, request.vpn_id)
        headers = None
        params = {}
        params['modifyAttribute'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_vpn_release_protection(self, request, config=None):
        """
        update_vpn_release_protection

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, request.vpn_id, VpcClient.CONSTANT_DELETE_PROTECT
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_vpn_tunnel(self, request, config=None):
        """
        update_vpn_tunnel

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, VpcClient.CONSTANT_VPNCONN, request.vpn_conn_id
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def user_gateway_details(self, request, config=None):
        """
        user_gateway_details

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UserGatewayDetailsResponse data
        :rtype: UserGatewayDetailsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, VpcClient.CONSTANT_CGW, request.cgw_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=UserGatewayDetailsResponse)

    def user_gateway_list(self, request, config=None):
        """
        user_gateway_list

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UserGatewayListResponse data
        :rtype: UserGatewayListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, VpcClient.CONSTANT_CGW)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=UserGatewayListResponse
        )

    def view_gateway_limit_rules(self, request, config=None):
        """
        view_gateway_limit_rules

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ViewGatewayLimitRulesResponse data
        :rtype: ViewGatewayLimitRulesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_GATEWAY, VpcClient.CONSTANT_LIMITRULE)
        headers = None
        params = {}
        if request.service_type is not None:
            params['serviceType'] = request.service_type
        if request.name is not None:
            params['name'] = request.name
        if request.glr_id is not None:
            params['glrId'] = request.glr_id
        if request.resource_id is not None:
            params['resourceId'] = request.resource_id
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ViewGatewayLimitRulesResponse
        )

    def view_peer_to_peer_connection_details(self, request, config=None):
        """
        view_peer_to_peer_connection_details

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ViewPeerToPeerConnectionDetailsResponse data
        :rtype: ViewPeerToPeerConnectionDetailsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_PEERCONN, request.peer_conn_id)
        headers = None
        params = {}
        if request.role is not None:
            params['role'] = request.role
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            params=params,
            config=merged_config,
            model=ViewPeerToPeerConnectionDetailsResponse,
        )

    def view_security_group_details_v2(self, request, config=None):
        """
        view_security_group_details_v2

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ViewSecurityGroupDetailsV2Response data
        :rtype: ViewSecurityGroupDetailsV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V2, VpcClient.CONSTANT_SECURITY_GROUP, request.security_group_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=ViewSecurityGroupDetailsV2Response
        )

    def _merge_config(self, config=None):
        """
        :param config:
        :type config: baiducloud_python_sdk_core.BceClientConfiguration
        """
        if config is None:
            return self.config
        else:
            new_config = copy.copy(self.config)
            new_config.merge_non_none_values(config)
            return new_config

    def _send_request(
        self, http_method, path, body=None, headers=None, params=None, config=None, body_parser=None, model=None
    ):
        """
        Send an HTTP request to the service endpoint.

        :param http_method: HTTP method (GET, POST, PUT, DELETE, etc.)
        :type http_method: bytes
        :param path: Request path
        :type path: bytes
        :param body: Optional request body
        :type body: str or bytes
        :param headers: Optional HTTP headers
        :type headers: dict
        :param params: Optional query parameters
        :type params: dict
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration
        :param body_parser: Optional custom body parser function
        :type body_parser: callable
        :param model: Optional response model class for deserialization
        :type model: class

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network connection failure, SSL errors, etc.)
        :raises BceServerError: Server returned error response
        """
        config = self._merge_config(config)
        if body_parser is None:
            body_parser = handler.parse_json
        if headers is None:
            headers = {b'Accept': b'*/*', b'Content-Type': b'application/json;charset=utf-8'}
        return bce_http_client.send_request(
            config,
            bce_v1_signer.sign,
            [handler.parse_error, body_parser],
            http_method,
            path,
            body,
            headers,
            params,
            model=model,
        )
