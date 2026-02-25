import copy
import logging
import uuid

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.auth import bce_v1_signer
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_vpc.models.create_a_reserved_network_segment_response import CreateAReservedNetworkSegmentResponse
from baiducloud_python_sdk_vpc.models.create_subnet_response import CreateSubnetResponse
from baiducloud_python_sdk_vpc.models.create_vpc_response import CreateVpcResponse
from baiducloud_python_sdk_vpc.models.query_specified_subnet_response import QuerySpecifiedSubnetResponse
from baiducloud_python_sdk_vpc.models.query_specified_vpc_response import QuerySpecifiedVpcResponse
from baiducloud_python_sdk_vpc.models.query_subnet_list_response import QuerySubnetListResponse
from baiducloud_python_sdk_vpc.models.query_the_ip_addresses_occupied_by_products_within_vpc_response import QueryTheIpAddressesOccupiedByProductsWithinVpcResponse
from baiducloud_python_sdk_vpc.models.query_the_reserved_network_segment_list_response import QueryTheReservedNetworkSegmentListResponse
from baiducloud_python_sdk_vpc.models.query_vpc_intranet_ip_response import QueryVpcIntranetIpResponse
from baiducloud_python_sdk_vpc.models.query_vpc_list_response import QueryVpcListResponse

_logger = logging.getLogger(__name__)


class VpcClient(BceBaseClient):

    VERSION_V1 = b'/v1'

    CONSTANT_VPC = b'vpc'

    CONSTANT_SHUTDOWN_RELAY = b'shutdownRelay'

    CONSTANT_RESOURCE_IP = b'resourceIp'

    CONSTANT_SUBNET = b'subnet'

    CONSTANT_IPRESERVE = b'ipreserve'

    CONSTANT_OPEN_RELAY = b'openRelay'

    CONSTANT_PRIVATE_IP_ADDRESS_INFO = b'privateIpAddressInfo'

    def __init__(self, config=None):
        bce_base_client.BceBaseClient.__init__(self, config)

    def close_vpc_relay(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPC, VpcClient.CONSTANT_SHUTDOWN_RELAY, request.vpc_id)
        params = {
            'clientToken' : request.client_token,
        }
        return self._send_request(http_methods.PUT, path=path
                                , params=params, config=config)

    def create_a_reserved_network_segment(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_SUBNET, VpcClient.CONSTANT_IPRESERVE)
        params = {
            'clientToken' : request.client_token,
        }
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), params=params, config=config, model=CreateAReservedNetworkSegmentResponse)

    def create_subnet(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_SUBNET)
        params = {
            'clientToken' : request.client_token,
        }
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), params=params, config=config, model=CreateSubnetResponse)

    def create_vpc(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPC)
        params = {
            'clientToken' : request.client_token,
        }
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), params=params, config=config, model=CreateVpcResponse)

    def delete_reserved_network_segment(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_SUBNET, VpcClient.CONSTANT_IPRESERVE, request.ip_reserve_id)
        params = {
            'clientToken' : request.client_token,
        }
        return self._send_request(http_methods.DELETE, path=path
                                , params=params, config=config)

    def delete_subnet(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_SUBNET, request.subnet_id)
        params = {
            'clientToken' : request.client_token,
        }
        return self._send_request(http_methods.DELETE, path=path
                                , params=params, config=config)

    def delete_vpc(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPC, request.vpc_id)
        params = {
            'clientToken' : request.client_token,
        }
        return self._send_request(http_methods.DELETE, path=path
                                , params=params, config=config)

    def enable_vpc_relay(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPC, VpcClient.CONSTANT_OPEN_RELAY, request.vpc_id)
        params = {
            'clientToken' : request.client_token,
        }
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

    def query_subnet_list(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_SUBNET)
        params = {
            'marker' : request.marker,
            'maxKeys' : request.max_keys,
            'vpcId' : request.vpc_id,
            'zoneName' : request.zone_name,
            'subnetType' : request.subnet_type,
            'subnetIds' : request.subnet_ids,
        }
        return self._send_request(http_methods.GET, path=path
                                , params=params, config=config, model=QuerySubnetListResponse)

    def query_the_ip_addresses_occupied_by_products_within_vpc(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPC, VpcClient.CONSTANT_RESOURCE_IP)
        params = {
            'vpcId' : request.vpc_id,
            'subnetId' : request.subnet_id,
            'resourceType' : request.resource_type,
            'pageNo' : request.page_no,
            'pageSize' : request.page_size,
        }
        return self._send_request(http_methods.GET, path=path
                                , params=params, config=config, model=QueryTheIpAddressesOccupiedByProductsWithinVpcResponse)

    def query_the_reserved_network_segment_list(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_SUBNET, VpcClient.CONSTANT_IPRESERVE)
        params = {
            'subnetId' : request.subnet_id,
            'marker' : request.marker,
            'maxKeys' : request.max_keys,
        }
        return self._send_request(http_methods.GET, path=path
                                , params=params, config=config, model=QueryTheReservedNetworkSegmentListResponse)

    def query_vpc_intranet_ip(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPC, request.vpc_id, VpcClient.CONSTANT_PRIVATE_IP_ADDRESS_INFO)
        params = {
            'privateIpAddresses' : ','.join(request.private_ip_addresses) if request.private_ip_addresses else None,
            'privateIpRange' : request.private_ip_range,
        }
        return self._send_request(http_methods.GET, path=path
                                , params=params, config=config, model=QueryVpcIntranetIpResponse)

    def query_vpc_list(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPC)
        params = {
            'marker' : request.marker,
            'maxKeys' : request.max_keys,
            'isDefault' : request.is_default,
            'vpcIds' : request.vpc_ids,
        }
        return self._send_request(http_methods.GET, path=path
                                , params=params, config=config, model=QueryVpcListResponse)

    def update_subnet(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_SUBNET, request.subnet_id)
        params = {
            'modifyAttribute' : None,
            'clientToken' : request.client_token,
        }
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), params=params, config=config)

    def update_vpc(self, request, config=None):
        path = utils.append_uri(VpcClient.VERSION_V1, VpcClient.CONSTANT_VPC, request.vpc_id)
        params = {
            'modifyAttribute' : None,
            'clientToken' : request.client_token,
        }
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), params=params, config=config)



    @staticmethod
    def _generate_default_client_token():
        """
        default client token by uuid1
        """
        return uuid.uuid1()

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
