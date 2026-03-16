import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.auth import bce_v1_signer
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_vpc.models.batch_create_ssl_vpn_users_response import BatchCreateSslVpnUsersResponse
from baiducloud_python_sdk_vpc.models.create_ip_reserved_response import CreateIpReservedResponse
from baiducloud_python_sdk_vpc.models.create_ssl_vpn_server_response import CreateSslVpnServerResponse
from baiducloud_python_sdk_vpc.models.create_subnet_response import CreateSubnetResponse
from baiducloud_python_sdk_vpc.models.create_user_gateway_response import CreateUserGatewayResponse
from baiducloud_python_sdk_vpc.models.create_vpc_response import CreateVpcResponse
from baiducloud_python_sdk_vpc.models.create_vpn_response import CreateVpnResponse
from baiducloud_python_sdk_vpc.models.create_vpn_tunnel_response import CreateVpnTunnelResponse
from baiducloud_python_sdk_vpc.models.get_vpc_resource_ip_info_response import GetVpcResourceIpInfoResponse
from baiducloud_python_sdk_vpc.models.list_ip_reserve_response import ListIpReserveResponse
from baiducloud_python_sdk_vpc.models.query_specified_subnet_response import QuerySpecifiedSubnetResponse
from baiducloud_python_sdk_vpc.models.query_specified_vpc_response import QuerySpecifiedVpcResponse
from baiducloud_python_sdk_vpc.models.query_ssl_vpn_server_response import QuerySslVpnServerResponse
from baiducloud_python_sdk_vpc.models.query_ssl_vpn_users_response import QuerySslVpnUsersResponse
from baiducloud_python_sdk_vpc.models.query_subnet_list_response import QuerySubnetListResponse
from baiducloud_python_sdk_vpc.models.query_vpc_intranet_ip_response import QueryVpcIntranetIpResponse
from baiducloud_python_sdk_vpc.models.query_vpc_list_response import QueryVpcListResponse
from baiducloud_python_sdk_vpc.models.query_vpn_list_response import QueryVpnListResponse
from baiducloud_python_sdk_vpc.models.search_for_vpn_details_response import SearchForVpnDetailsResponse
from baiducloud_python_sdk_vpc.models.search_vpn_tunnel_response import SearchVpnTunnelResponse
from baiducloud_python_sdk_vpc.models.user_gateway_details_response import UserGatewayDetailsResponse
from baiducloud_python_sdk_vpc.models.user_gateway_list_response import UserGatewayListResponse

_logger = logging.getLogger(__name__)


class VpcClient(BceBaseClient):

    VERSION_V1 = b'/v1'

    CONSTANT_VPC = b'vpc'

    CONSTANT_VPN = b'vpn'

    CONSTANT_VPNCONN = b'vpnconn'

    CONSTANT_SSL_VPN_SERVER = b'sslVpnServer'

    CONSTANT_SHUTDOWN_RELAY = b'shutdownRelay'

    CONSTANT_RESOURCE_IP = b'resourceIp'

    CONSTANT_CGW = b'cgw'

    CONSTANT_SSL_VPN_USER = b'sslVpnUser'

    CONSTANT_SUBNET = b'subnet'

    CONSTANT_PRIVATE_IP_ADDRESS_INFO = b'privateIpAddressInfo'

    CONSTANT_IPRESERVE = b'ipreserve'

    CONSTANT_OPEN_RELAY = b'openRelay'

    CONSTANT_DELETE_PROTECT = b'deleteProtect'

    def __init__(self, config=None):
        bce_base_client.BceBaseClient.__init__(self, config)

    def batch_create_ssl_vpn_users(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, request.vpn_id, VpcClient.CONSTANT_SSL_VPN_USER)
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), params=params, config=config, model=BatchCreateSslVpnUsersResponse)

    def bind_eip(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, request.vpn_id)
        params = {}
        params['bind'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), params=params, config=config)

    def close_vpc_relay(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPC, VpcClient.CONSTANT_SHUTDOWN_RELAY, request.vpc_id)
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.PUT, path=path
                                , params=params, config=config)

    def create_ip_reserved(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_SUBNET, VpcClient.CONSTANT_IPRESERVE)
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), params=params, config=config, model=CreateIpReservedResponse)

    def create_ssl_vpn_server(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, request.vpn_id, VpcClient.CONSTANT_SSL_VPN_SERVER)
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), params=params, config=config, model=CreateSslVpnServerResponse)

    def create_subnet(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_SUBNET)
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), params=params, config=config, model=CreateSubnetResponse)

    def create_user_gateway(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, VpcClient.CONSTANT_CGW)
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), params=params, config=config, model=CreateUserGatewayResponse)

    def create_vpc(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPC)
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), params=params, config=config, model=CreateVpcResponse)

    def create_vpn(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN)
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), params=params, config=config, model=CreateVpnResponse)

    def create_vpn_tunnel(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, request.vpn_id, VpcClient.CONSTANT_VPNCONN)
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), params=params, config=config, model=CreateVpnTunnelResponse)

    def delete_ip_reserve(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_SUBNET, VpcClient.CONSTANT_IPRESERVE, request.ip_reserve_id)
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.DELETE, path=path
                                , params=params, config=config)

    def delete_ssl_vpn_server(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, request.vpn_id, VpcClient.CONSTANT_SSL_VPN_SERVER, request.ssl_vpn_server_id)
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.DELETE, path=path
                                , params=params, config=config)

    def delete_ssl_vpn_user(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, request.vpn_id, VpcClient.CONSTANT_SSL_VPN_USER, request.user_id)
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.DELETE, path=path
                                , params=params, config=config)

    def delete_subnet(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_SUBNET, request.subnet_id)
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.DELETE, path=path
                                , params=params, config=config)

    def delete_user_gateway(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, VpcClient.CONSTANT_CGW, request.cgw_id)
        return self._send_request(http_methods.DELETE, path=path
                                , config=config)

    def delete_vpc(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPC, request.vpc_id)
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.DELETE, path=path
                                , params=params, config=config)

    def delete_vpn_tunnel(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, VpcClient.CONSTANT_VPNCONN, request.vpn_conn_id)
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.DELETE, path=path
                                , params=params, config=config)

    def get_vpc_resource_ip_info(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPC, VpcClient.CONSTANT_RESOURCE_IP)
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
        return self._send_request(http_methods.GET, path=path
                                , params=params, config=config, model=GetVpcResourceIpInfoResponse)

    def list_ip_reserve(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_SUBNET, VpcClient.CONSTANT_IPRESERVE)
        params = {}
        if request.subnet_id is not None:
            params['subnetId'] = request.subnet_id
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        return self._send_request(http_methods.GET, path=path
                                , params=params, config=config, model=ListIpReserveResponse)

    def open_vpc_relay(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPC, VpcClient.CONSTANT_OPEN_RELAY, request.vpc_id)
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.PUT, path=path
                                , params=params, config=config)

    def query_specified_subnet(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_SUBNET, request.subnet_id)
        return self._send_request(http_methods.GET, path=path
                                , config=config, model=QuerySpecifiedSubnetResponse)

    def query_specified_vpc(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPC, request.vpc_id)
        return self._send_request(http_methods.GET, path=path
                                , config=config, model=QuerySpecifiedVpcResponse)

    def query_ssl_vpn_server(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, request.vpn_id, VpcClient.CONSTANT_SSL_VPN_SERVER)
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.GET, path=path
                                , params=params, config=config, model=QuerySslVpnServerResponse)

    def query_ssl_vpn_users(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, request.vpn_id, VpcClient.CONSTANT_SSL_VPN_USER)
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.user_name is not None:
            params['userName'] = request.user_name
        return self._send_request(http_methods.GET, path=path
                                , params=params, config=config, model=QuerySslVpnUsersResponse)

    def query_subnet_list(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_SUBNET)
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
        return self._send_request(http_methods.GET, path=path
                                , params=params, config=config, model=QuerySubnetListResponse)

    def query_vpc_intranet_ip(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPC, request.vpc_id, VpcClient.CONSTANT_PRIVATE_IP_ADDRESS_INFO)
        params = {}
        if request.private_ip_addresses is not None:
            params['privateIpAddresses'] = ','.join(request.private_ip_addresses)
        if request.private_ip_range is not None:
            params['privateIpRange'] = request.private_ip_range
        return self._send_request(http_methods.GET, path=path
                                , params=params, config=config, model=QueryVpcIntranetIpResponse)

    def query_vpc_list(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPC)
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.is_default is not None:
            params['isDefault'] = request.is_default
        if request.vpc_ids is not None:
            params['vpcIds'] = request.vpc_ids
        return self._send_request(http_methods.GET, path=path
                                , params=params, config=config, model=QueryVpcListResponse)

    def query_vpn_list(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN)
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
        return self._send_request(http_methods.GET, path=path
                                , params=params, config=config, model=QueryVpnListResponse)

    def release_vpn(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, request.vpn_id)
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.DELETE, path=path
                                , params=params, config=config)

    def renew_vpn(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, request.vpn_id)
        params = {}
        params['purchaseReserved'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), params=params, config=config)

    def search_for_vpn_details(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, request.vpn_id)
        return self._send_request(http_methods.GET, path=path
                                , config=config, model=SearchForVpnDetailsResponse)

    def search_vpn_tunnel(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, VpcClient.CONSTANT_VPNCONN, request.vpn_id)
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.GET, path=path
                                , params=params, config=config, model=SearchVpnTunnelResponse)

    def unbind_eip(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, request.vpn_id)
        params = {}
        params['unbind'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.PUT, path=path
                                , params=params, config=config)

    def update_ssl_vpn_server(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, request.vpn_id, VpcClient.CONSTANT_SSL_VPN_SERVER, request.ssl_vpn_server_id)
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), params=params, config=config)

    def update_ssl_vpn_users(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, request.vpn_id, VpcClient.CONSTANT_SSL_VPN_USER, request.user_id)
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), params=params, config=config)

    def update_subnet(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_SUBNET, request.subnet_id)
        params = {}
        params['modifyAttribute'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), params=params, config=config)

    def update_user_gateway(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, VpcClient.CONSTANT_CGW, request.cgw_id)
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), params=params, config=config)

    def update_vpc(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPC, request.vpc_id)
        params = {}
        params['modifyAttribute'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), params=params, config=config)

    def update_vpn(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, request.vpn_id)
        params = {}
        params['modifyAttribute'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), params=params, config=config)

    def update_vpn_release_protection(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, request.vpn_id, VpcClient.CONSTANT_DELETE_PROTECT)
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), params=params, config=config)

    def update_vpn_tunnel(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, VpcClient.CONSTANT_VPNCONN, request.vpn_conn_id)
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), params=params, config=config)

    def user_gateway_details(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, VpcClient.CONSTANT_CGW, request.cgw_id)
        return self._send_request(http_methods.GET, path=path
                                , config=config, model=UserGatewayDetailsResponse)

    def user_gateway_list(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPN, VpcClient.CONSTANT_CGW)
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        return self._send_request(http_methods.GET, path=path
                                , params=params, config=config, model=UserGatewayListResponse)


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

    def _send_request(self, http_method, path,
                      body=None, headers=None, params=None,
                      config=None, body_parser=None, model=None):
        config = self._merge_config(config)
        if body_parser is None:
            body_parser = handler.parse_json
        if headers is None:
            headers = {b'Accept': b'*/*', b'Content-Type':
                b'application/json;charset=utf-8'}
        return bce_http_client.send_request(
            config, bce_v1_signer.sign, [handler.parse_error, body_parser],
            http_method, path, body, headers, params, model=model)
