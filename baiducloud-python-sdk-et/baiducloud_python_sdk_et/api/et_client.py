"""
Example for et client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.auth import bce_v1_signer
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_et.models.apply_physical_dedicated_line_response import ApplyPhysicalDedicatedLineResponse
from baiducloud_python_sdk_et.models.create_dedicated_channel_response import CreateDedicatedChannelResponse
from baiducloud_python_sdk_et.models.create_dedicated_channel_route_rules_response import (
    CreateDedicatedChannelRouteRulesResponse,
)
from baiducloud_python_sdk_et.models.query_dedicated_channel_response import QueryDedicatedChannelResponse
from baiducloud_python_sdk_et.models.query_dedicated_channel_route_rules_response import (
    QueryDedicatedChannelRouteRulesResponse,
)
from baiducloud_python_sdk_et.models.query_dedicated_line_detail_response import QueryDedicatedLineDetailResponse
from baiducloud_python_sdk_et.models.query_dedicated_lines_response import QueryDedicatedLinesResponse

_logger = logging.getLogger(__name__)


class EtClient(BceBaseClient):
    """
    et base sdk client
    """

    VERSION_V1 = b'/v1'

    CONSTANT_ET = b'et'

    CONSTANT_CHANNEL = b'channel'

    CONSTANT_ROUTE = b'route'

    CONSTANT_RULE = b'rule'

    CONSTANT_INIT = b'init'

    CONSTANT_BFD = b'bfd'

    def __init__(self, config=None):
        """
        Initialize the et client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def apply_physical_dedicated_line(self, request, config=None):
        """
        apply_physical_dedicated_line

        :param request: Request entity containing all parameters
        :type request: EtClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ApplyPhysicalDedicatedLineResponse data
        :rtype: ApplyPhysicalDedicatedLineResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EtClient.VERSION_V1, EtClient.CONSTANT_ET, EtClient.CONSTANT_INIT)
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
            model=ApplyPhysicalDedicatedLineResponse,
        )

    def associated_dedicated_channel(self, request, config=None):
        """
        associated_dedicated_channel

        :param request: Request entity containing all parameters
        :type request: EtClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            EtClient.VERSION_V1, EtClient.CONSTANT_ET, request.et_id, EtClient.CONSTANT_CHANNEL, request.et_channel_id
        )
        headers = None
        params = {}
        params['associate'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def create_dedicated_channel(self, request, config=None):
        """
        create_dedicated_channel

        :param request: Request entity containing all parameters
        :type request: EtClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateDedicatedChannelResponse data
        :rtype: CreateDedicatedChannelResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EtClient.VERSION_V1, EtClient.CONSTANT_ET, request.et_id, EtClient.CONSTANT_CHANNEL)
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
            model=CreateDedicatedChannelResponse,
        )

    def create_dedicated_channel_bfd(self, request, config=None):
        """
        create_dedicated_channel_bfd

        :param request: Request entity containing all parameters
        :type request: EtClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            EtClient.VERSION_V1,
            EtClient.CONSTANT_ET,
            request.et_id,
            EtClient.CONSTANT_CHANNEL,
            request.et_channel_id,
            EtClient.CONSTANT_BFD,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def create_dedicated_channel_route_parameters(self, request, config=None):
        """
        create_dedicated_channel_route_parameters

        :param request: Request entity containing all parameters
        :type request: EtClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            EtClient.VERSION_V1, EtClient.CONSTANT_ET, request.et_id, EtClient.CONSTANT_CHANNEL, request.et_channel_id
        )
        headers = None
        params = {}
        params['addRoutes'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def create_dedicated_channel_route_rules(self, request, config=None):
        """
        create_dedicated_channel_route_rules

        :param request: Request entity containing all parameters
        :type request: EtClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateDedicatedChannelRouteRulesResponse data
        :rtype: CreateDedicatedChannelRouteRulesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            EtClient.VERSION_V1,
            EtClient.CONSTANT_ET,
            request.et_id,
            EtClient.CONSTANT_CHANNEL,
            request.et_channel_id,
            EtClient.CONSTANT_ROUTE,
            EtClient.CONSTANT_RULE,
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
            model=CreateDedicatedChannelRouteRulesResponse,
        )

    def create_dedicated_channel_user_object(self, request, config=None):
        """
        create_dedicated_channel_user_object

        :param request: Request entity containing all parameters
        :type request: EtClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            EtClient.VERSION_V1, EtClient.CONSTANT_ET, request.et_id, EtClient.CONSTANT_CHANNEL, request.et_channel_id
        )
        headers = None
        params = {}
        params['addUsers'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def delete_dedicated_channel(self, request, config=None):
        """
        delete_dedicated_channel

        :param request: Request entity containing all parameters
        :type request: EtClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            EtClient.VERSION_V1, EtClient.CONSTANT_ET, request.et_id, EtClient.CONSTANT_CHANNEL, request.et_channel_id
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_dedicated_channel_bfd(self, request, config=None):
        """
        delete_dedicated_channel_bfd

        :param request: Request entity containing all parameters
        :type request: EtClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            EtClient.VERSION_V1,
            EtClient.CONSTANT_ET,
            request.et_id,
            EtClient.CONSTANT_CHANNEL,
            request.et_channel_id,
            EtClient.CONSTANT_BFD,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_dedicated_channel_route_rules(self, request, config=None):
        """
        delete_dedicated_channel_route_rules

        :param request: Request entity containing all parameters
        :type request: EtClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            EtClient.VERSION_V1,
            EtClient.CONSTANT_ET,
            request.et_id,
            EtClient.CONSTANT_CHANNEL,
            request.et_channel_id,
            EtClient.CONSTANT_ROUTE,
            EtClient.CONSTANT_RULE,
            request.route_rule_id,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_physical_dedicated_line(self, request, config=None):
        """
        delete_physical_dedicated_line

        :param request: Request entity containing all parameters
        :type request: EtClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EtClient.VERSION_V1, EtClient.CONSTANT_ET, request.dcphy_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def disable_dedicated_channel_ipv6(self, request, config=None):
        """
        disable_dedicated_channel_ipv6

        :param request: Request entity containing all parameters
        :type request: EtClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            EtClient.VERSION_V1, EtClient.CONSTANT_ET, request.et_id, EtClient.CONSTANT_CHANNEL, request.et_channel_id
        )
        headers = None
        params = {}
        params['disableIpv6'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def enable_dedicated_channel_ipv6(self, request, config=None):
        """
        enable_dedicated_channel_ipv6

        :param request: Request entity containing all parameters
        :type request: EtClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            EtClient.VERSION_V1, EtClient.CONSTANT_ET, request.et_id, EtClient.CONSTANT_CHANNEL, request.et_channel_id
        )
        headers = None
        params = {}
        params['enableIpv6'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def query_dedicated_channel(self, request, config=None):
        """
        query_dedicated_channel

        :param request: Request entity containing all parameters
        :type request: EtClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryDedicatedChannelResponse data
        :rtype: QueryDedicatedChannelResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EtClient.VERSION_V1, EtClient.CONSTANT_ET, request.et_id, EtClient.CONSTANT_CHANNEL)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        if request.et_channel_id is not None:
            params['etChannelId'] = request.et_channel_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryDedicatedChannelResponse
        )

    def query_dedicated_channel_route_rules(self, request, config=None):
        """
        query_dedicated_channel_route_rules

        :param request: Request entity containing all parameters
        :type request: EtClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryDedicatedChannelRouteRulesResponse data
        :rtype: QueryDedicatedChannelRouteRulesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            EtClient.VERSION_V1,
            EtClient.CONSTANT_ET,
            request.et_id,
            EtClient.CONSTANT_CHANNEL,
            request.et_channel_id,
            EtClient.CONSTANT_ROUTE,
            EtClient.CONSTANT_RULE,
        )
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.dest_address is not None:
            params['destAddress'] = request.dest_address
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            params=params,
            config=merged_config,
            model=QueryDedicatedChannelRouteRulesResponse,
        )

    def query_dedicated_line_detail(self, request, config=None):
        """
        query_dedicated_line_detail

        :param request: Request entity containing all parameters
        :type request: EtClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryDedicatedLineDetailResponse data
        :rtype: QueryDedicatedLineDetailResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EtClient.VERSION_V1, EtClient.CONSTANT_ET, request.dcphy_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=QueryDedicatedLineDetailResponse
        )

    def query_dedicated_lines(self, request, config=None):
        """
        query_dedicated_lines

        :param request: Request entity containing all parameters
        :type request: EtClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryDedicatedLinesResponse data
        :rtype: QueryDedicatedLinesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EtClient.VERSION_V1, EtClient.CONSTANT_ET)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.status is not None:
            params['status'] = request.status
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryDedicatedLinesResponse
        )

    def remove_dedicated_channel_route_parameters(self, request, config=None):
        """
        remove_dedicated_channel_route_parameters

        :param request: Request entity containing all parameters
        :type request: EtClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            EtClient.VERSION_V1, EtClient.CONSTANT_ET, request.et_id, EtClient.CONSTANT_CHANNEL, request.et_channel_id
        )
        headers = None
        params = {}
        params['removeRoutes'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def remove_dedicated_channel_user_object(self, request, config=None):
        """
        remove_dedicated_channel_user_object

        :param request: Request entity containing all parameters
        :type request: EtClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            EtClient.VERSION_V1, EtClient.CONSTANT_ET, request.et_id, EtClient.CONSTANT_CHANNEL, request.et_channel_id
        )
        headers = None
        params = {}
        params['removeUsers'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def resubmit_dedicated_channel(self, request, config=None):
        """
        resubmit_dedicated_channel

        :param request: Request entity containing all parameters
        :type request: EtClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            EtClient.VERSION_V1, EtClient.CONSTANT_ET, request.et_id, EtClient.CONSTANT_CHANNEL, request.et_channel_id
        )
        headers = None
        params = {}
        params['reCreate'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def unrelated_dedicated_line_channel(self, request, config=None):
        """
        unrelated_dedicated_line_channel

        :param request: Request entity containing all parameters
        :type request: EtClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            EtClient.VERSION_V1, EtClient.CONSTANT_ET, request.et_id, EtClient.CONSTANT_CHANNEL, request.et_channel_id
        )
        headers = None
        params = {}
        params['disassociate'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_dedicated_channel(self, request, config=None):
        """
        update_dedicated_channel

        :param request: Request entity containing all parameters
        :type request: EtClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            EtClient.VERSION_V1, EtClient.CONSTANT_ET, request.et_id, EtClient.CONSTANT_CHANNEL, request.et_channel_id
        )
        headers = None
        params = {}
        params['modifyAttribute'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_dedicated_channel_bfd(self, request, config=None):
        """
        update_dedicated_channel_bfd

        :param request: Request entity containing all parameters
        :type request: EtClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            EtClient.VERSION_V1,
            EtClient.CONSTANT_ET,
            request.et_id,
            EtClient.CONSTANT_CHANNEL,
            request.et_channel_id,
            EtClient.CONSTANT_BFD,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_dedicated_channel_route_rules(self, request, config=None):
        """
        update_dedicated_channel_route_rules

        :param request: Request entity containing all parameters
        :type request: EtClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            EtClient.VERSION_V1,
            EtClient.CONSTANT_ET,
            request.et_id,
            EtClient.CONSTANT_CHANNEL,
            request.et_channel_id,
            EtClient.CONSTANT_ROUTE,
            EtClient.CONSTANT_RULE,
            request.route_rule_id,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_physical_dedicated_line(self, request, config=None):
        """
        update_physical_dedicated_line

        :param request: Request entity containing all parameters
        :type request: EtClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EtClient.VERSION_V1, EtClient.CONSTANT_ET, request.dcphy_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
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
