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
from baiducloud_python_sdk_vpc.models.add_eni_ip_response import AddEniIpResponse
from baiducloud_python_sdk_vpc.models.batch_add_dnat_rules_response import BatchAddDnatRulesResponse
from baiducloud_python_sdk_vpc.models.batch_add_eni_ip_response import BatchAddEniIpResponse
from baiducloud_python_sdk_vpc.models.batch_add_snat_rules_response import BatchAddSnatRulesResponse
from baiducloud_python_sdk_vpc.models.batch_create_ssl_vpn_users_response import BatchCreateSslVpnUsersResponse
from baiducloud_python_sdk_vpc.models.create_dedicated_gateway_response import CreateDedicatedGatewayResponse
from baiducloud_python_sdk_vpc.models.create_dnat_rule_response import CreateDnatRuleResponse
from baiducloud_python_sdk_vpc.models.create_egress_only_rule_response import CreateEgressOnlyRuleResponse
from baiducloud_python_sdk_vpc.models.create_eni_response import CreateEniResponse
from baiducloud_python_sdk_vpc.models.create_enterprise_security_group_response import (
    CreateEnterpriseSecurityGroupResponse,
)
from baiducloud_python_sdk_vpc.models.create_gateway_limit_rules_response import CreateGatewayLimitRulesResponse
from baiducloud_python_sdk_vpc.models.create_ha_vip_response import CreateHaVipResponse
from baiducloud_python_sdk_vpc.models.create_ip_group_response import CreateIpGroupResponse
from baiducloud_python_sdk_vpc.models.create_ip_reserved_response import CreateIpReservedResponse
from baiducloud_python_sdk_vpc.models.create_ip_set_response import CreateIpSetResponse
from baiducloud_python_sdk_vpc.models.create_ipv6_gateway_response import CreateIpv6GatewayResponse
from baiducloud_python_sdk_vpc.models.create_nat_response import CreateNatResponse
from baiducloud_python_sdk_vpc.models.create_peer_conn_response import CreatePeerConnResponse
from baiducloud_python_sdk_vpc.models.create_probe_response import CreateProbeResponse
from baiducloud_python_sdk_vpc.models.create_rate_limit_rule_response import CreateRateLimitRuleResponse
from baiducloud_python_sdk_vpc.models.create_routing_rules_response import CreateRoutingRulesResponse
from baiducloud_python_sdk_vpc.models.create_security_group_response import CreateSecurityGroupResponse
from baiducloud_python_sdk_vpc.models.create_snat_rule_response import CreateSnatRuleResponse
from baiducloud_python_sdk_vpc.models.create_ssl_vpn_server_response import CreateSslVpnServerResponse
from baiducloud_python_sdk_vpc.models.create_subnet_response import CreateSubnetResponse
from baiducloud_python_sdk_vpc.models.create_user_gateway_response import CreateUserGatewayResponse
from baiducloud_python_sdk_vpc.models.create_vpc_response import CreateVpcResponse
from baiducloud_python_sdk_vpc.models.create_vpn_response import CreateVpnResponse
from baiducloud_python_sdk_vpc.models.create_vpn_tunnel_response import CreateVpnTunnelResponse
from baiducloud_python_sdk_vpc.models.get_eni_detail_response import GetEniDetailResponse
from baiducloud_python_sdk_vpc.models.get_eni_status_response import GetEniStatusResponse
from baiducloud_python_sdk_vpc.models.get_ha_vip_detail_response import GetHaVipDetailResponse
from baiducloud_python_sdk_vpc.models.get_nat_response import GetNatResponse
from baiducloud_python_sdk_vpc.models.get_peer_conn_response import GetPeerConnResponse
from baiducloud_python_sdk_vpc.models.get_probe_detail_response import GetProbeDetailResponse
from baiducloud_python_sdk_vpc.models.get_security_group_details_response import GetSecurityGroupDetailsResponse
from baiducloud_python_sdk_vpc.models.get_vpc_resource_ip_info_response import GetVpcResourceIpInfoResponse
from baiducloud_python_sdk_vpc.models.list_dnat_rule_response import ListDnatRuleResponse
from baiducloud_python_sdk_vpc.models.list_egress_only_rule_response import ListEgressOnlyRuleResponse
from baiducloud_python_sdk_vpc.models.list_eni_response import ListEniResponse
from baiducloud_python_sdk_vpc.models.list_ha_vip_response import ListHaVipResponse
from baiducloud_python_sdk_vpc.models.list_ip_reserve_response import ListIpReserveResponse
from baiducloud_python_sdk_vpc.models.list_nat_response import ListNatResponse
from baiducloud_python_sdk_vpc.models.list_peer_conn_response import ListPeerConnResponse
from baiducloud_python_sdk_vpc.models.list_probes_response import ListProbesResponse
from baiducloud_python_sdk_vpc.models.list_rate_limit_rule_response import ListRateLimitRuleResponse
from baiducloud_python_sdk_vpc.models.list_snat_rule_response import ListSnatRuleResponse
from baiducloud_python_sdk_vpc.models.query_acl_response import QueryAclResponse
from baiducloud_python_sdk_vpc.models.query_acl_rules_response import QueryAclRulesResponse
from baiducloud_python_sdk_vpc.models.query_enterprise_security_group_list_response import (
    QueryEnterpriseSecurityGroupListResponse,
)
from baiducloud_python_sdk_vpc.models.query_ip_group_detail_response import QueryIpGroupDetailResponse
from baiducloud_python_sdk_vpc.models.query_ip_group_list_response import QueryIpGroupListResponse
from baiducloud_python_sdk_vpc.models.query_ip_set_detail_response import QueryIpSetDetailResponse
from baiducloud_python_sdk_vpc.models.query_ip_set_list_response import QueryIpSetListResponse
from baiducloud_python_sdk_vpc.models.query_ipv6_gateway_response import QueryIpv6GatewayResponse
from baiducloud_python_sdk_vpc.models.query_routing_rules_response import QueryRoutingRulesResponse
from baiducloud_python_sdk_vpc.models.query_routing_table_response import QueryRoutingTableResponse
from baiducloud_python_sdk_vpc.models.query_security_groups_list_response import QuerySecurityGroupsListResponse
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
from baiducloud_python_sdk_vpc.models.query_vpc_intranet_ip_response import QueryVpcIntranetIpResponse
from baiducloud_python_sdk_vpc.models.query_vpc_list_response import QueryVpcListResponse
from baiducloud_python_sdk_vpc.models.query_vpn_list_response import QueryVpnListResponse
from baiducloud_python_sdk_vpc.models.search_for_vpn_details_response import SearchForVpnDetailsResponse
from baiducloud_python_sdk_vpc.models.search_vpn_tunnel_response import SearchVpnTunnelResponse
from baiducloud_python_sdk_vpc.models.user_gateway_details_response import UserGatewayDetailsResponse
from baiducloud_python_sdk_vpc.models.user_gateway_list_response import UserGatewayListResponse
from baiducloud_python_sdk_vpc.models.view_gateway_limit_rules_response import ViewGatewayLimitRulesResponse

_logger = logging.getLogger(__name__)


class VpcClient(BceBaseClient):
    """
    vpc base sdk client
    """

    VERSION_V1 = b'/v1'

    CONSTANT_VPC = b'vpc'

    CONSTANT_NAT = b'nat'

    CONSTANT_DNAT_RULE = b'dnatRule'

    CONSTANT_IP_GROUP = b'ipGroup'

    CONSTANT_UNBIND_IP_SET = b'unbindIpSet'

    CONSTANT_SECURITY_GROUP = b'securityGroup'

    CONSTANT_RULE = b'rule'

    CONSTANT_RESOURCE_IP = b'resourceIp'

    CONSTANT_UPDATE = b'update'

    CONSTANT_IP_SET = b'ipSet'

    CONSTANT_PRIVATE_IP_ADDRESS_INFO = b'privateIpAddressInfo'

    CONSTANT_ENI = b'eni'

    CONSTANT_SNAT_RULE = b'snatRule'

    CONSTANT_ET_GATEWAY = b'etGateway'

    CONSTANT_VPN = b'vpn'

    CONSTANT_CGW = b'cgw'

    CONSTANT_HAVIP = b'havip'

    CONSTANT_PEERCONN = b'peerconn'

    CONSTANT_BATCH_CREATE = b'batchCreate'

    CONSTANT_VPNCONN = b'vpnconn'

    CONSTANT_ENTERPRISE = b'enterprise'

    CONSTANT_SECURITY = b'security'

    CONSTANT_ACL = b'acl'

    CONSTANT_GATEWAY = b'gateway'

    CONSTANT_LIMITRULE = b'limitrule'

    CONSTANT_SUBNET = b'subnet'

    CONSTANT_I_PV6_GATEWAY = b'IPv6Gateway'

    CONSTANT_EGRESS_ONLY_RULE = b'egressOnlyRule'

    CONSTANT_IPRESERVE = b'ipreserve'

    CONSTANT_SSL_VPN_SERVER = b'sslVpnServer'

    CONSTANT_DELETE_PROTECT = b'deleteProtect'

    CONSTANT_PRIVATE_IP = b'privateIp'

    CONSTANT_BATCH_ADD = b'batchAdd'

    CONSTANT_ROUTE = b'route'

    CONSTANT_RATE_LIMIT_RULE = b'rateLimitRule'

    CONSTANT_PROBE = b'probe'

    CONSTANT_SHUTDOWN_RELAY = b'shutdownRelay'

    CONSTANT_HEALTH_CHECK = b'healthCheck'

    CONSTANT_SSL_VPN_USER = b'sslVpnUser'

    CONSTANT_DELETE_IP_ADDRESS = b'deleteIpAddress'

    CONSTANT_BIND_IP_SET = b'bindIpSet'

    CONSTANT_BATCH_DEL = b'batchDel'

    CONSTANT_OPEN_RELAY = b'openRelay'

    CONSTANT_STATUS = b'status'

    CONSTANT_IP_ADDRESS = b'ipAddress'

    def __init__(self, config=None):
        """
        Initialize the vpc client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def accept_peer_conn(self, request, config=None):
        """
        accept_peer_conn

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

    def add_eni_ip(self, request, config=None):
        """
        add_eni_ip

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing AddEniIpResponse data
        :rtype: AddEniIpResponse

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
            model=AddEniIpResponse,
        )

    def add_ip_address_to_ip_group(self, request, config=None):
        """
        add_ip_address_to_ip_group

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

    def add_ip_group_to_ip_set(self, request, config=None):
        """
        add_ip_group_to_ip_set

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

    def attach_eni_instance(self, request, config=None):
        """
        attach_eni_instance

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

    def authorize_enterprise_security_group_rules(self, request, config=None):
        """
        authorize_enterprise_security_group_rules

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

    def authorize_security_group_rules(self, request, config=None):
        """
        authorize_security_group_rules

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_SECURITY_GROUP, request.security_group_id)
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

    def batch_add_dnat_rules(self, request, config=None):
        """
        batch_add_dnat_rules

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BatchAddDnatRulesResponse data
        :rtype: BatchAddDnatRulesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1,
            VpcClient.CONSTANT_NAT,
            request.nat_id,
            VpcClient.CONSTANT_DNAT_RULE,
            VpcClient.CONSTANT_BATCH_CREATE,
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
            model=BatchAddDnatRulesResponse,
        )

    def batch_add_eni_ip(self, request, config=None):
        """
        batch_add_eni_ip

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BatchAddEniIpResponse data
        :rtype: BatchAddEniIpResponse

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
            model=BatchAddEniIpResponse,
        )

    def batch_add_snat_rules(self, request, config=None):
        """
        batch_add_snat_rules

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BatchAddSnatRulesResponse data
        :rtype: BatchAddSnatRulesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_NAT, VpcClient.CONSTANT_SNAT_RULE, VpcClient.CONSTANT_BATCH_CREATE
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
            model=BatchAddSnatRulesResponse,
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

    def batch_delete_eni_ip(self, request, config=None):
        """
        batch_delete_eni_ip

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

    def bind_eni_eip(self, request, config=None):
        """
        bind_eni_eip

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

    def bind_ha_vip_eip(self, request, config=None):
        """
        bind_ha_vip_eip

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

    def bind_ha_vip_instance(self, request, config=None):
        """
        bind_ha_vip_instance

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

    def close_peer_conn_sync_dns(self, request, config=None):
        """
        close_peer_conn_sync_dns

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

    def create_dnat_rule(self, request, config=None):
        """
        create_dnat_rule

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateDnatRuleResponse data
        :rtype: CreateDnatRuleResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_NAT, request.nat_id, VpcClient.CONSTANT_DNAT_RULE
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
            model=CreateDnatRuleResponse,
        )

    def create_egress_only_rule(self, request, config=None):
        """
        create_egress_only_rule

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateEgressOnlyRuleResponse data
        :rtype: CreateEgressOnlyRuleResponse

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
            model=CreateEgressOnlyRuleResponse,
        )

    def create_eni(self, request, config=None):
        """
        create_eni

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateEniResponse data
        :rtype: CreateEniResponse

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
            model=CreateEniResponse,
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

    def create_ha_vip(self, request, config=None):
        """
        create_ha_vip

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateHaVipResponse data
        :rtype: CreateHaVipResponse

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
            model=CreateHaVipResponse,
        )

    def create_ip_group(self, request, config=None):
        """
        create_ip_group

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateIpGroupResponse data
        :rtype: CreateIpGroupResponse

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
            model=CreateIpGroupResponse,
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

    def create_ip_set(self, request, config=None):
        """
        create_ip_set

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateIpSetResponse data
        :rtype: CreateIpSetResponse

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
            model=CreateIpSetResponse,
        )

    def create_ipv6_gateway(self, request, config=None):
        """
        create_ipv6_gateway

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateIpv6GatewayResponse data
        :rtype: CreateIpv6GatewayResponse

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
            model=CreateIpv6GatewayResponse,
        )

    def create_nat(self, request, config=None):
        """
        create_nat

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateNatResponse data
        :rtype: CreateNatResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_NAT)
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
            model=CreateNatResponse,
        )

    def create_peer_conn(self, request, config=None):
        """
        create_peer_conn

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreatePeerConnResponse data
        :rtype: CreatePeerConnResponse

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
            model=CreatePeerConnResponse,
        )

    def create_probe(self, request, config=None):
        """
        create_probe

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateProbeResponse data
        :rtype: CreateProbeResponse

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
            model=CreateProbeResponse,
        )

    def create_rate_limit_rule(self, request, config=None):
        """
        create_rate_limit_rule

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateRateLimitRuleResponse data
        :rtype: CreateRateLimitRuleResponse

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
            model=CreateRateLimitRuleResponse,
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

    def create_security_group(self, request, config=None):
        """
        create_security_group

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateSecurityGroupResponse data
        :rtype: CreateSecurityGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_SECURITY_GROUP)
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
            model=CreateSecurityGroupResponse,
        )

    def create_snat_rule(self, request, config=None):
        """
        create_snat_rule

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateSnatRuleResponse data
        :rtype: CreateSnatRuleResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_NAT, request.nat_id, VpcClient.CONSTANT_SNAT_RULE
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
            model=CreateSnatRuleResponse,
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

    def delete_dnat_rule(self, request, config=None):
        """
        delete_dnat_rule

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
            VpcClient.VERSION_V1, VpcClient.CONSTANT_NAT, request.nat_id, VpcClient.CONSTANT_DNAT_RULE, request.rule_id
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_eni_ip(self, request, config=None):
        """
        delete_eni_ip

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

    def delete_ha_vip(self, request, config=None):
        """
        delete_ha_vip

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

    def delete_ip_group(self, request, config=None):
        """
        delete_ip_group

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

    def delete_ip_set(self, request, config=None):
        """
        delete_ip_set

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

    def delete_ipv6_gateway_egress_only_rule(self, request, config=None):
        """
        delete_ipv6_gateway_egress_only_rule

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

    def delete_ipv6_gateway_rate_limit_rule(self, request, config=None):
        """
        delete_ipv6_gateway_rate_limit_rule

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

    def delete_probe(self, request, config=None):
        """
        delete_probe

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

    def delete_security_group(self, request, config=None):
        """
        delete_security_group

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_SECURITY_GROUP, request.security_group_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_security_group_rules(self, request, config=None):
        """
        delete_security_group_rules

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

    def delete_snat_rule(self, request, config=None):
        """
        delete_snat_rule

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
            VpcClient.VERSION_V1, VpcClient.CONSTANT_NAT, request.nat_id, VpcClient.CONSTANT_SNAT_RULE, request.rule_id
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

    def detach_eni_instance(self, request, config=None):
        """
        detach_eni_instance

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

    def get_eni_detail(self, request, config=None):
        """
        get_eni_detail

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetEniDetailResponse data
        :rtype: GetEniDetailResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_ENI, request.eni_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetEniDetailResponse)

    def get_eni_status(self, request, config=None):
        """
        get_eni_status

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetEniStatusResponse data
        :rtype: GetEniStatusResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_ENI, request.eni_id, VpcClient.CONSTANT_STATUS
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetEniStatusResponse)

    def get_ha_vip_detail(self, request, config=None):
        """
        get_ha_vip_detail

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetHaVipDetailResponse data
        :rtype: GetHaVipDetailResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_HAVIP, request.ha_vip_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetHaVipDetailResponse)

    def get_nat(self, request, config=None):
        """
        get_nat

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetNatResponse data
        :rtype: GetNatResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_NAT, request.nat_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetNatResponse)

    def get_peer_conn(self, request, config=None):
        """
        get_peer_conn

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetPeerConnResponse data
        :rtype: GetPeerConnResponse

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
            http_methods.GET, path=path, params=params, config=merged_config, model=GetPeerConnResponse
        )

    def get_probe_detail(self, request, config=None):
        """
        get_probe_detail

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetProbeDetailResponse data
        :rtype: GetProbeDetailResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_PROBE, request.probe_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetProbeDetailResponse)

    def get_security_group_details(self, request, config=None):
        """
        get_security_group_details

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetSecurityGroupDetailsResponse data
        :rtype: GetSecurityGroupDetailsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_SECURITY_GROUP, request.security_group_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=GetSecurityGroupDetailsResponse
        )

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

    def list_dnat_rule(self, request, config=None):
        """
        list_dnat_rule

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListDnatRuleResponse data
        :rtype: ListDnatRuleResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_NAT, request.nat_id, VpcClient.CONSTANT_DNAT_RULE
        )
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListDnatRuleResponse
        )

    def list_egress_only_rule(self, request, config=None):
        """
        list_egress_only_rule

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListEgressOnlyRuleResponse data
        :rtype: ListEgressOnlyRuleResponse

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
            http_methods.GET, path=path, params=params, config=merged_config, model=ListEgressOnlyRuleResponse
        )

    def list_eni(self, request, config=None):
        """
        list_eni

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListEniResponse data
        :rtype: ListEniResponse

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
            http_methods.GET, path=path, params=params, config=merged_config, model=ListEniResponse
        )

    def list_ha_vip(self, request, config=None):
        """
        list_ha_vip

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListHaVipResponse data
        :rtype: ListHaVipResponse

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
            http_methods.GET, path=path, params=params, config=merged_config, model=ListHaVipResponse
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

    def list_nat(self, request, config=None):
        """
        list_nat

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListNatResponse data
        :rtype: ListNatResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_NAT)
        headers = None
        params = {}
        if request.vpc_id is not None:
            params['vpcId'] = request.vpc_id
        if request.nat_id is not None:
            params['natId'] = request.nat_id
        if request.name is not None:
            params['name'] = request.name
        if request.ip is not None:
            params['ip'] = request.ip
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListNatResponse
        )

    def list_peer_conn(self, request, config=None):
        """
        list_peer_conn

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListPeerConnResponse data
        :rtype: ListPeerConnResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_PEERCONN)
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
            http_methods.GET, path=path, params=params, config=merged_config, model=ListPeerConnResponse
        )

    def list_probes(self, request, config=None):
        """
        list_probes

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListProbesResponse data
        :rtype: ListProbesResponse

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
            http_methods.GET, path=path, params=params, config=merged_config, model=ListProbesResponse
        )

    def list_rate_limit_rule(self, request, config=None):
        """
        list_rate_limit_rule

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListRateLimitRuleResponse data
        :rtype: ListRateLimitRuleResponse

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
            http_methods.GET, path=path, params=params, config=merged_config, model=ListRateLimitRuleResponse
        )

    def list_snat_rule(self, request, config=None):
        """
        list_snat_rule

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListSnatRuleResponse data
        :rtype: ListSnatRuleResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VpcClient.VERSION_V1, VpcClient.CONSTANT_NAT, request.nat_id, VpcClient.CONSTANT_SNAT_RULE
        )
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListSnatRuleResponse
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

    def modify_nat(self, request, config=None):
        """
        modify_nat

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_NAT, request.nat_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def nat_bind_eip(self, request, config=None):
        """
        nat_bind_eip

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_NAT, request.nat_id)
        headers = None
        params = {}
        params['bind'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def nat_un_bind_eip(self, request, config=None):
        """
        nat_un_bind_eip

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_NAT, request.nat_id)
        headers = None
        params = {}
        params['unbind'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def open_peer_conn_sync_dns(self, request, config=None):
        """
        open_peer_conn_sync_dns

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

    def purchase_reserved_nat(self, request, config=None):
        """
        purchase_reserved_nat

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_NAT, request.nat_id)
        headers = None
        params = {}
        params['purchaseReserved'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

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

    def query_enterprise_security_group_list(self, request, config=None):
        """
        query_enterprise_security_group_list

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryEnterpriseSecurityGroupListResponse data
        :rtype: QueryEnterpriseSecurityGroupListResponse

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
            model=QueryEnterpriseSecurityGroupListResponse,
        )

    def query_ip_group_detail(self, request, config=None):
        """
        query_ip_group_detail

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryIpGroupDetailResponse data
        :rtype: QueryIpGroupDetailResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_IP_SET, request.ip_set_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=QueryIpGroupDetailResponse)

    def query_ip_group_list(self, request, config=None):
        """
        query_ip_group_list

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryIpGroupListResponse data
        :rtype: QueryIpGroupListResponse

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
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryIpGroupListResponse
        )

    def query_ip_set_detail(self, request, config=None):
        """
        query_ip_set_detail

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryIpSetDetailResponse data
        :rtype: QueryIpSetDetailResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_IP_GROUP, request.ip_group_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=QueryIpSetDetailResponse)

    def query_ip_set_list(self, request, config=None):
        """
        query_ip_set_list

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryIpSetListResponse data
        :rtype: QueryIpSetListResponse

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
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryIpSetListResponse
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

    def query_security_groups_list(self, request, config=None):
        """
        query_security_groups_list

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QuerySecurityGroupsListResponse data
        :rtype: QuerySecurityGroupsListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_SECURITY_GROUP)
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
            http_methods.GET, path=path, params=params, config=merged_config, model=QuerySecurityGroupsListResponse
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

    def refund_peer_conn(self, request, config=None):
        """
        refund_peer_conn

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

    def reject_peer_conn(self, request, config=None):
        """
        reject_peer_conn

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

    def release_nat(self, request, config=None):
        """
        release_nat

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_NAT, request.nat_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def release_peer_conn(self, request, config=None):
        """
        release_peer_conn

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

    def remove_eni(self, request, config=None):
        """
        remove_eni

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

    def remove_ip_address_from_ip_group(self, request, config=None):
        """
        remove_ip_address_from_ip_group

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

    def remove_ip_group_from_ip_set(self, request, config=None):
        """
        remove_ip_group_from_ip_set

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

    def renew_peer_conn(self, request, config=None):
        """
        renew_peer_conn

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

    def resize_ipv6_gateway(self, request, config=None):
        """
        resize_ipv6_gateway

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

    def resize_nat(self, request, config=None):
        """
        resize_nat

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_NAT, request.nat_id)
        headers = None
        params = {}
        params['resize'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def revoke_security_group_rules(self, request, config=None):
        """
        revoke_security_group_rules

        :param request: Request entity containing all parameters
        :type request: VpcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_SECURITY_GROUP, request.security_group_id)
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

    def unbind_eni_eip(self, request, config=None):
        """
        unbind_eni_eip

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

    def unbind_ha_vip_eip(self, request, config=None):
        """
        unbind_ha_vip_eip

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

    def unbind_ha_vip_instance(self, request, config=None):
        """
        unbind_ha_vip_instance

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

    def update_delete_protect(self, request, config=None):
        """
        update_delete_protect

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

    def update_dnat_rule(self, request, config=None):
        """
        update_dnat_rule

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
            VpcClient.VERSION_V1, VpcClient.CONSTANT_NAT, request.nat_id, VpcClient.CONSTANT_DNAT_RULE, request.rule_id
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_eni(self, request, config=None):
        """
        update_eni

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

    def update_eni_enterprise_security_group(self, request, config=None):
        """
        update_eni_enterprise_security_group

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

    def update_eni_security_group(self, request, config=None):
        """
        update_eni_security_group

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

    def update_ha_vip(self, request, config=None):
        """
        update_ha_vip

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

    def update_ip_group(self, request, config=None):
        """
        update_ip_group

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

    def update_ip_set(self, request, config=None):
        """
        update_ip_set

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

    def update_nat_release_protection_switch(self, request, config=None):
        """
        update_nat_release_protection_switch

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
            VpcClient.VERSION_V1, VpcClient.CONSTANT_NAT, request.nat_id, VpcClient.CONSTANT_DELETE_PROTECT
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_peer_conn(self, request, config=None):
        """
        update_peer_conn

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
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_peer_conn_bandwidth(self, request, config=None):
        """
        update_peer_conn_bandwidth

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

    def update_peer_conn_delete_protect(self, request, config=None):
        """
        update_peer_conn_delete_protect

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
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_probe(self, request, config=None):
        """
        update_probe

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

    def update_rate_limit_rule(self, request, config=None):
        """
        update_rate_limit_rule

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

    def update_security_group_rules(self, request, config=None):
        """
        update_security_group_rules

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
            VpcClient.VERSION_V1, VpcClient.CONSTANT_SECURITY_GROUP, VpcClient.CONSTANT_RULE, VpcClient.CONSTANT_UPDATE
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

    def update_snat_rule(self, request, config=None):
        """
        update_snat_rule

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
            VpcClient.VERSION_V1, VpcClient.CONSTANT_NAT, request.nat_id, VpcClient.CONSTANT_SNAT_RULE, request.rule_id
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
