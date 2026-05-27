"""
Example for privatezone client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.auth import bce_v1_signer
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_privatezone.models.add_record_response import AddRecordResponse
from baiducloud_python_sdk_privatezone.models.create_private_zone_response import CreatePrivateZoneResponse
from baiducloud_python_sdk_privatezone.models.get_private_zone_response import GetPrivateZoneResponse
from baiducloud_python_sdk_privatezone.models.list_private_zone_response import ListPrivateZoneResponse
from baiducloud_python_sdk_privatezone.models.list_record_response import ListRecordResponse

_logger = logging.getLogger(__name__)


class PrivatezoneClient(BceBaseClient):
    """
    privatezone base sdk client
    """

    VERSION_V1 = b'/v1'

    CONSTANT_PRIVATEZONE = b'privatezone'

    CONSTANT_RECORD = b'record'

    def __init__(self, config=None):
        """
        Initialize the privatezone client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def add_record(self, request, config=None):
        """
        add_record

        :param request: Request entity containing all parameters
        :type request: PrivatezoneClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing AddRecordResponse data
        :rtype: AddRecordResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            PrivatezoneClient.VERSION_V1,
            PrivatezoneClient.CONSTANT_PRIVATEZONE,
            request.zone_id,
            PrivatezoneClient.CONSTANT_RECORD,
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
            model=AddRecordResponse,
        )

    def bind_vpc(self, request, config=None):
        """
        bind_vpc

        :param request: Request entity containing all parameters
        :type request: PrivatezoneClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(PrivatezoneClient.VERSION_V1, PrivatezoneClient.CONSTANT_PRIVATEZONE, request.zone_id)
        headers = None
        params = {}
        params[request.action] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def create_private_zone(self, request, config=None):
        """
        create_private_zone

        :param request: Request entity containing all parameters
        :type request: PrivatezoneClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreatePrivateZoneResponse data
        :rtype: CreatePrivateZoneResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(PrivatezoneClient.VERSION_V1, PrivatezoneClient.CONSTANT_PRIVATEZONE)
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
            model=CreatePrivateZoneResponse,
        )

    def delete_private_zone(self, request, config=None):
        """
        delete_private_zone

        :param request: Request entity containing all parameters
        :type request: PrivatezoneClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(PrivatezoneClient.VERSION_V1, PrivatezoneClient.CONSTANT_PRIVATEZONE, request.zone_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_record(self, request, config=None):
        """
        delete_record

        :param request: Request entity containing all parameters
        :type request: PrivatezoneClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            PrivatezoneClient.VERSION_V1,
            PrivatezoneClient.CONSTANT_PRIVATEZONE,
            PrivatezoneClient.CONSTANT_RECORD,
            request.record_id,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def disable_record(self, request, config=None):
        """
        disable_record

        :param request: Request entity containing all parameters
        :type request: PrivatezoneClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            PrivatezoneClient.VERSION_V1,
            PrivatezoneClient.CONSTANT_PRIVATEZONE,
            PrivatezoneClient.CONSTANT_RECORD,
            request.record_id,
        )
        headers = None
        params = {}
        params['disable'] = None
        if request.action is not None:
            params['action'] = request.action
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def enable_record(self, request, config=None):
        """
        enable_record

        :param request: Request entity containing all parameters
        :type request: PrivatezoneClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            PrivatezoneClient.VERSION_V1,
            PrivatezoneClient.CONSTANT_PRIVATEZONE,
            PrivatezoneClient.CONSTANT_RECORD,
            request.record_id,
        )
        headers = None
        params = {}
        params['enable'] = None
        if request.action is not None:
            params['action'] = request.action
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def get_private_zone(self, request, config=None):
        """
        get_private_zone

        :param request: Request entity containing all parameters
        :type request: PrivatezoneClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetPrivateZoneResponse data
        :rtype: GetPrivateZoneResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(PrivatezoneClient.VERSION_V1, PrivatezoneClient.CONSTANT_PRIVATEZONE, request.zone_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetPrivateZoneResponse)

    def list_private_zone(self, request, config=None):
        """
        list_private_zone

        :param request: Request entity containing all parameters
        :type request: PrivatezoneClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListPrivateZoneResponse data
        :rtype: ListPrivateZoneResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(PrivatezoneClient.VERSION_V1, PrivatezoneClient.CONSTANT_PRIVATEZONE)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListPrivateZoneResponse
        )

    def list_record(self, request, config=None):
        """
        list_record

        :param request: Request entity containing all parameters
        :type request: PrivatezoneClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListRecordResponse data
        :rtype: ListRecordResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            PrivatezoneClient.VERSION_V1,
            PrivatezoneClient.CONSTANT_PRIVATEZONE,
            request.zone_id,
            PrivatezoneClient.CONSTANT_RECORD,
        )
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.rr is not None:
            params['rr'] = request.rr
        if request.search_mode is not None:
            params['searchMode'] = request.search_mode
        if request.type is not None:
            params['type'] = request.type
        if request.value is not None:
            params['value'] = request.value
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListRecordResponse
        )

    def unbind_vpc(self, request, config=None):
        """
        unbind_vpc

        :param request: Request entity containing all parameters
        :type request: PrivatezoneClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(PrivatezoneClient.VERSION_V1, PrivatezoneClient.CONSTANT_PRIVATEZONE, request.zone_id)
        headers = None
        params = {}
        params[request.action] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_record(self, request, config=None):
        """
        update_record

        :param request: Request entity containing all parameters
        :type request: PrivatezoneClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            PrivatezoneClient.VERSION_V1,
            PrivatezoneClient.CONSTANT_PRIVATEZONE,
            PrivatezoneClient.CONSTANT_RECORD,
            request.record_id,
        )
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
