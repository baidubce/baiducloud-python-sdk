"""
Example for aigw client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_core.util import request_body_utils
from baiducloud_python_sdk_aigw.models.create_consumer_response import CreateConsumerResponse
from baiducloud_python_sdk_aigw.models.create_route_response import CreateRouteResponse
from baiducloud_python_sdk_aigw.models.delete_consumer_response import DeleteConsumerResponse
from baiducloud_python_sdk_aigw.models.delete_route_response import DeleteRouteResponse
from baiducloud_python_sdk_aigw.models.get_consumer_response import GetConsumerResponse
from baiducloud_python_sdk_aigw.models.get_consumer_list_response import GetConsumerListResponse
from baiducloud_python_sdk_aigw.models.query_routing_details_response import QueryRoutingDetailsResponse
from baiducloud_python_sdk_aigw.models.query_routing_list_response import QueryRoutingListResponse
from baiducloud_python_sdk_aigw.models.update_consumer_response import UpdateConsumerResponse
from baiducloud_python_sdk_aigw.models.update_route_response import UpdateRouteResponse

_logger = logging.getLogger(__name__)


class AigwClient(BceBaseClient):
    """
    aigw base sdk client
    """

    CONSTANT_V1 = b'v1'

    CONSTANT_AIGW = b'aigw'

    CONSTANT_ROUTE = b'route'

    CONSTANT_DETAIL = b'detail'

    CONSTANT_CONSUMER = b'consumer'

    CONSTANT_CLUSTER = b'cluster'

    CONSTANT_CONSUMERS = b'consumers'

    def __init__(self, config=None):
        """
        Initialize the aigw client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def create_consumer(self, request, config=None):
        """
        create_consumer

        :param request: Request entity containing all parameters
        :type request: AigwClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateConsumerResponse data
        :rtype: CreateConsumerResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/', AigwClient.CONSTANT_V1, AigwClient.CONSTANT_AIGW, request.instance_id, AigwClient.CONSTANT_CONSUMER
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateConsumerResponse,
        )

    def create_route(self, request, config=None):
        """
        create_route

        :param request: Request entity containing all parameters
        :type request: AigwClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateRouteResponse data
        :rtype: CreateRouteResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            AigwClient.CONSTANT_V1,
            AigwClient.CONSTANT_AIGW,
            request.instance_id,
            request.cluster_id,
            AigwClient.CONSTANT_ROUTE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateRouteResponse,
        )

    def delete_consumer(self, request, config=None):
        """
        delete_consumer

        :param request: Request entity containing all parameters
        :type request: AigwClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DeleteConsumerResponse data
        :rtype: DeleteConsumerResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            AigwClient.CONSTANT_V1,
            AigwClient.CONSTANT_AIGW,
            request.instance_id,
            AigwClient.CONSTANT_CONSUMER,
            request.consumer_id,
        )
        headers = None
        params = {}
        if request.key_type is not None:
            params['keyType'] = request.key_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.DELETE, path=path, params=params, config=merged_config, model=DeleteConsumerResponse
        )

    def delete_route(self, request, config=None):
        """
        delete_route

        :param request: Request entity containing all parameters
        :type request: AigwClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DeleteRouteResponse data
        :rtype: DeleteRouteResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            AigwClient.CONSTANT_V1,
            AigwClient.CONSTANT_AIGW,
            request.instance_id,
            request.route_name,
            AigwClient.CONSTANT_ROUTE,
            AigwClient.CONSTANT_DETAIL,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config, model=DeleteRouteResponse)

    def get_consumer(self, request, config=None):
        """
        get_consumer

        :param request: Request entity containing all parameters
        :type request: AigwClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetConsumerResponse data
        :rtype: GetConsumerResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            AigwClient.CONSTANT_V1,
            AigwClient.CONSTANT_AIGW,
            request.instance_id,
            AigwClient.CONSTANT_CONSUMER,
            request.consumer_id,
        )
        headers = None
        params = {}
        if request.key_type is not None:
            params['keyType'] = request.key_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetConsumerResponse
        )

    def get_consumer_list(self, request, config=None):
        """
        get_consumer_list

        :param request: Request entity containing all parameters
        :type request: AigwClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetConsumerListResponse data
        :rtype: GetConsumerListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/', AigwClient.CONSTANT_V1, AigwClient.CONSTANT_AIGW, request.instance_id, AigwClient.CONSTANT_CONSUMERS
        )
        headers = None
        params = {}
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        if request.tag_key is not None:
            params['tagKey'] = request.tag_key
        if request.tag_value is not None:
            params['tagValue'] = request.tag_value
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetConsumerListResponse
        )

    def query_routing_details(self, request, config=None):
        """
        query_routing_details

        :param request: Request entity containing all parameters
        :type request: AigwClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryRoutingDetailsResponse data
        :rtype: QueryRoutingDetailsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            AigwClient.CONSTANT_V1,
            AigwClient.CONSTANT_AIGW,
            request.instance_id,
            request.route_name,
            AigwClient.CONSTANT_ROUTE,
            AigwClient.CONSTANT_DETAIL,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=QueryRoutingDetailsResponse)

    def query_routing_list(self, request, config=None):
        """
        query_routing_list

        :param request: Request entity containing all parameters
        :type request: AigwClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryRoutingListResponse data
        :rtype: QueryRoutingListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            AigwClient.CONSTANT_V1,
            AigwClient.CONSTANT_AIGW,
            AigwClient.CONSTANT_CLUSTER,
            request.instance_id,
            AigwClient.CONSTANT_ROUTE,
        )
        headers = None
        params = {}
        if request.route_name is not None:
            params['routeName'] = request.route_name
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        if request.order_by is not None:
            params['orderBy'] = request.order_by
        if request.order is not None:
            params['order'] = request.order
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryRoutingListResponse
        )

    def update_consumer(self, request, config=None):
        """
        update_consumer

        :param request: Request entity containing all parameters
        :type request: AigwClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UpdateConsumerResponse data
        :rtype: UpdateConsumerResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            AigwClient.CONSTANT_V1,
            AigwClient.CONSTANT_AIGW,
            request.instance_id,
            AigwClient.CONSTANT_CONSUMER,
            request.consumer_id,
        )
        headers = None
        params = {}
        if request.key_type is not None:
            params['keyType'] = request.key_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=UpdateConsumerResponse,
        )

    def update_route(self, request, config=None):
        """
        update_route

        :param request: Request entity containing all parameters
        :type request: AigwClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UpdateRouteResponse data
        :rtype: UpdateRouteResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            AigwClient.CONSTANT_V1,
            AigwClient.CONSTANT_AIGW,
            request.instance_id,
            request.route_name,
            AigwClient.CONSTANT_ROUTE,
            AigwClient.CONSTANT_DETAIL,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config, model=UpdateRouteResponse
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
        sign_fn, params = self._choose_signer(config, params)
        return bce_http_client.send_request(
            config, sign_fn, [handler.parse_error, body_parser], http_method, path, body, headers, params, model=model
        )
