"""
Example for csn client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.auth import bce_v1_signer
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_csn.models.create_csn_response import CreateCsnResponse
from baiducloud_python_sdk_csn.models.create_csn_bp_response import CreateCsnBpResponse
from baiducloud_python_sdk_csn.models.query_association_relation_response import QueryAssociationRelationResponse
from baiducloud_python_sdk_csn.models.query_csn_bp_detail_response import QueryCsnBpDetailResponse
from baiducloud_python_sdk_csn.models.query_csn_bp_list_response import QueryCsnBpListResponse
from baiducloud_python_sdk_csn.models.query_csn_bp_price_response import QueryCsnBpPriceResponse
from baiducloud_python_sdk_csn.models.query_csn_detail_response import QueryCsnDetailResponse
from baiducloud_python_sdk_csn.models.query_csn_instance_response import QueryCsnInstanceResponse
from baiducloud_python_sdk_csn.models.query_csn_list_response import QueryCsnListResponse
from baiducloud_python_sdk_csn.models.query_region_bandwidth_response import QueryRegionBandwidthResponse
from baiducloud_python_sdk_csn.models.query_region_bandwidth_by_csn_response import QueryRegionBandwidthByCsnResponse
from baiducloud_python_sdk_csn.models.query_route_rule_response import QueryRouteRuleResponse
from baiducloud_python_sdk_csn.models.query_route_table_list_response import QueryRouteTableListResponse
from baiducloud_python_sdk_csn.models.query_study_relation_response import QueryStudyRelationResponse
from baiducloud_python_sdk_csn.models.query_tgw_list_response import QueryTgwListResponse
from baiducloud_python_sdk_csn.models.query_tgw_route_response import QueryTgwRouteResponse

_logger = logging.getLogger(__name__)


class CsnClient(BceBaseClient):
    """
    csn base sdk client
    """

    VERSION_V1 = b'/v1'

    CONSTANT_CSN = b'csn'

    CONSTANT_ROUTE_TABLE = b'routeTable'

    CONSTANT_RULE = b'rule'

    CONSTANT_BP = b'bp'

    CONSTANT_LIMIT = b'limit'

    CONSTANT_PROPAGATION = b'propagation'

    CONSTANT_TGW = b'tgw'

    CONSTANT_ASSOCIATION = b'association'

    CONSTANT_PRICE = b'price'

    CONSTANT_DELETE = b'delete'

    CONSTANT_INSTANCE = b'instance'

    def __init__(self, config=None):
        """
        Initialize the csn client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def add_route_rule(self, request, config=None):
        """
        add_route_rule

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CsnClient.VERSION_V1,
            CsnClient.CONSTANT_CSN,
            CsnClient.CONSTANT_ROUTE_TABLE,
            request.csn_rt_id,
            CsnClient.CONSTANT_RULE,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def attach_csn_instance(self, request, config=None):
        """
        attach_csn_instance

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CsnClient.VERSION_V1, CsnClient.CONSTANT_CSN, request.csn_id)
        headers = None
        params = {}
        params['attach'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def bind_csn_bp(self, request, config=None):
        """
        bind_csn_bp

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CsnClient.VERSION_V1, CsnClient.CONSTANT_CSN, CsnClient.CONSTANT_BP, request.csn_bp_id)
        headers = None
        params = {}
        params['bind'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def create_association_relation(self, request, config=None):
        """
        create_association_relation

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CsnClient.VERSION_V1,
            CsnClient.CONSTANT_CSN,
            CsnClient.CONSTANT_ROUTE_TABLE,
            request.csn_rt_id,
            CsnClient.CONSTANT_ASSOCIATION,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def create_csn(self, request, config=None):
        """
        create_csn

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateCsnResponse data
        :rtype: CreateCsnResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CsnClient.VERSION_V1, CsnClient.CONSTANT_CSN)
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
            model=CreateCsnResponse,
        )

    def create_csn_bp(self, request, config=None):
        """
        create_csn_bp

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateCsnBpResponse data
        :rtype: CreateCsnBpResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CsnClient.VERSION_V1, CsnClient.CONSTANT_CSN, CsnClient.CONSTANT_BP)
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
            model=CreateCsnBpResponse,
        )

    def create_region_bandwidth(self, request, config=None):
        """
        create_region_bandwidth

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CsnClient.VERSION_V1,
            CsnClient.CONSTANT_CSN,
            CsnClient.CONSTANT_BP,
            request.csn_bp_id,
            CsnClient.CONSTANT_LIMIT,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def create_study_relation(self, request, config=None):
        """
        create_study_relation

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CsnClient.VERSION_V1,
            CsnClient.CONSTANT_CSN,
            CsnClient.CONSTANT_ROUTE_TABLE,
            request.csn_rt_id,
            CsnClient.CONSTANT_PROPAGATION,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def delete_association_relation(self, request, config=None):
        """
        delete_association_relation

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CsnClient.VERSION_V1,
            CsnClient.CONSTANT_CSN,
            CsnClient.CONSTANT_ROUTE_TABLE,
            request.csn_rt_id,
            CsnClient.CONSTANT_ASSOCIATION,
            request.attach_id,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_csn(self, request, config=None):
        """
        delete_csn

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CsnClient.VERSION_V1, CsnClient.CONSTANT_CSN, request.csn_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_csn_bp(self, request, config=None):
        """
        delete_csn_bp

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CsnClient.VERSION_V1, CsnClient.CONSTANT_CSN, CsnClient.CONSTANT_BP, request.csn_bp_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_region_bandwidth(self, request, config=None):
        """
        delete_region_bandwidth

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CsnClient.VERSION_V1,
            CsnClient.CONSTANT_CSN,
            CsnClient.CONSTANT_BP,
            request.csn_bp_id,
            CsnClient.CONSTANT_LIMIT,
            CsnClient.CONSTANT_DELETE,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def delete_route_rule(self, request, config=None):
        """
        delete_route_rule

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CsnClient.VERSION_V1,
            CsnClient.CONSTANT_CSN,
            CsnClient.CONSTANT_ROUTE_TABLE,
            request.csn_rt_id,
            CsnClient.CONSTANT_RULE,
            request.csn_rt_rule_id,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_study_relation(self, request, config=None):
        """
        delete_study_relation

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CsnClient.VERSION_V1,
            CsnClient.CONSTANT_CSN,
            CsnClient.CONSTANT_ROUTE_TABLE,
            request.csn_rt_id,
            CsnClient.CONSTANT_PROPAGATION,
            request.attach_id,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def detach_csn_instance(self, request, config=None):
        """
        detach_csn_instance

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CsnClient.VERSION_V1, CsnClient.CONSTANT_CSN, request.csn_id)
        headers = None
        params = {}
        params['detach'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def query_association_relation(self, request, config=None):
        """
        query_association_relation

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryAssociationRelationResponse data
        :rtype: QueryAssociationRelationResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CsnClient.VERSION_V1,
            CsnClient.CONSTANT_CSN,
            CsnClient.CONSTANT_ROUTE_TABLE,
            request.csn_rt_id,
            CsnClient.CONSTANT_ASSOCIATION,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=QueryAssociationRelationResponse
        )

    def query_csn_bp_detail(self, request, config=None):
        """
        query_csn_bp_detail

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryCsnBpDetailResponse data
        :rtype: QueryCsnBpDetailResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CsnClient.VERSION_V1, CsnClient.CONSTANT_CSN, CsnClient.CONSTANT_BP, request.csn_bp_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=QueryCsnBpDetailResponse)

    def query_csn_bp_list(self, request, config=None):
        """
        query_csn_bp_list

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryCsnBpListResponse data
        :rtype: QueryCsnBpListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CsnClient.VERSION_V1, CsnClient.CONSTANT_CSN, CsnClient.CONSTANT_BP)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryCsnBpListResponse
        )

    def query_csn_bp_price(self, request, config=None):
        """
        query_csn_bp_price

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryCsnBpPriceResponse data
        :rtype: QueryCsnBpPriceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CsnClient.VERSION_V1, CsnClient.CONSTANT_CSN, CsnClient.CONSTANT_BP, CsnClient.CONSTANT_PRICE
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=QueryCsnBpPriceResponse,
        )

    def query_csn_detail(self, request, config=None):
        """
        query_csn_detail

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryCsnDetailResponse data
        :rtype: QueryCsnDetailResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CsnClient.VERSION_V1, CsnClient.CONSTANT_CSN, request.csn_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=QueryCsnDetailResponse)

    def query_csn_instance(self, request, config=None):
        """
        query_csn_instance

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryCsnInstanceResponse data
        :rtype: QueryCsnInstanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CsnClient.VERSION_V1, CsnClient.CONSTANT_CSN, request.csn_id, CsnClient.CONSTANT_INSTANCE
        )
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryCsnInstanceResponse
        )

    def query_csn_list(self, request, config=None):
        """
        query_csn_list

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryCsnListResponse data
        :rtype: QueryCsnListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CsnClient.VERSION_V1, CsnClient.CONSTANT_CSN)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryCsnListResponse
        )

    def query_region_bandwidth(self, request, config=None):
        """
        query_region_bandwidth

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryRegionBandwidthResponse data
        :rtype: QueryRegionBandwidthResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CsnClient.VERSION_V1,
            CsnClient.CONSTANT_CSN,
            CsnClient.CONSTANT_BP,
            request.csn_bp_id,
            CsnClient.CONSTANT_LIMIT,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=QueryRegionBandwidthResponse
        )

    def query_region_bandwidth_by_csn(self, request, config=None):
        """
        query_region_bandwidth_by_csn

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryRegionBandwidthByCsnResponse data
        :rtype: QueryRegionBandwidthByCsnResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CsnClient.VERSION_V1,
            CsnClient.CONSTANT_CSN,
            request.csn_id,
            CsnClient.CONSTANT_BP,
            CsnClient.CONSTANT_LIMIT,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=QueryRegionBandwidthByCsnResponse
        )

    def query_route_rule(self, request, config=None):
        """
        query_route_rule

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryRouteRuleResponse data
        :rtype: QueryRouteRuleResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CsnClient.VERSION_V1,
            CsnClient.CONSTANT_CSN,
            CsnClient.CONSTANT_ROUTE_TABLE,
            request.csn_rt_id,
            CsnClient.CONSTANT_RULE,
        )
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryRouteRuleResponse
        )

    def query_route_table_list(self, request, config=None):
        """
        query_route_table_list

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryRouteTableListResponse data
        :rtype: QueryRouteTableListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CsnClient.VERSION_V1, CsnClient.CONSTANT_CSN, request.csn_id, CsnClient.CONSTANT_ROUTE_TABLE
        )
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryRouteTableListResponse
        )

    def query_study_relation(self, request, config=None):
        """
        query_study_relation

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryStudyRelationResponse data
        :rtype: QueryStudyRelationResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CsnClient.VERSION_V1,
            CsnClient.CONSTANT_CSN,
            CsnClient.CONSTANT_ROUTE_TABLE,
            request.csn_rt_id,
            CsnClient.CONSTANT_PROPAGATION,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=QueryStudyRelationResponse)

    def query_tgw_list(self, request, config=None):
        """
        query_tgw_list

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryTgwListResponse data
        :rtype: QueryTgwListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CsnClient.VERSION_V1, CsnClient.CONSTANT_CSN, request.csn_id, CsnClient.CONSTANT_TGW)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryTgwListResponse
        )

    def query_tgw_route(self, request, config=None):
        """
        query_tgw_route

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryTgwRouteResponse data
        :rtype: QueryTgwRouteResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CsnClient.VERSION_V1,
            CsnClient.CONSTANT_CSN,
            request.csn_id,
            CsnClient.CONSTANT_TGW,
            request.tgw_id,
            CsnClient.CONSTANT_RULE,
        )
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryTgwRouteResponse
        )

    def resize_csn_bp(self, request, config=None):
        """
        resize_csn_bp

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CsnClient.VERSION_V1, CsnClient.CONSTANT_CSN, CsnClient.CONSTANT_BP, request.csn_bp_id)
        headers = None
        params = {}
        params['resize'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def unbind_csn_bp(self, request, config=None):
        """
        unbind_csn_bp

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CsnClient.VERSION_V1, CsnClient.CONSTANT_CSN, CsnClient.CONSTANT_BP, request.csn_bp_id)
        headers = None
        params = {}
        params['unbind'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_csn(self, request, config=None):
        """
        update_csn

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CsnClient.VERSION_V1, CsnClient.CONSTANT_CSN, request.csn_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_csn_bp(self, request, config=None):
        """
        update_csn_bp

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CsnClient.VERSION_V1, CsnClient.CONSTANT_CSN, CsnClient.CONSTANT_BP, request.csn_bp_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_region_bandwidth(self, request, config=None):
        """
        update_region_bandwidth

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CsnClient.VERSION_V1,
            CsnClient.CONSTANT_CSN,
            CsnClient.CONSTANT_BP,
            request.csn_bp_id,
            CsnClient.CONSTANT_LIMIT,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_tgw(self, request, config=None):
        """
        update_tgw

        :param request: Request entity containing all parameters
        :type request: CsnClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CsnClient.VERSION_V1, CsnClient.CONSTANT_CSN, request.csn_id, CsnClient.CONSTANT_TGW, request.tgw_id
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

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
