"""
Example for snic client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.auth import bce_v1_signer
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_snic.models.create_snic_response import CreateSnicResponse
from baiducloud_python_sdk_snic.models.describe_snic_response import DescribeSnicResponse
from baiducloud_python_sdk_snic.models.list_snic_response import ListSnicResponse
from baiducloud_python_sdk_snic.models.query_available_public_services_response import (
    QueryAvailablePublicServicesResponse,
)

_logger = logging.getLogger(__name__)


class SnicClient(BceBaseClient):
    """
    snic base sdk client
    """

    VERSION_V1 = b'/v1'

    CONSTANT_ENDPOINT = b'endpoint'

    CONSTANT_PUBLIC_SERVICE = b'publicService'

    def __init__(self, config=None):
        """
        Initialize the snic client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def create_snic(self, request, config=None):
        """
        create_snic

        :param request: Request entity containing all parameters
        :type request: SnicClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateSnicResponse data
        :rtype: CreateSnicResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(SnicClient.VERSION_V1, SnicClient.CONSTANT_ENDPOINT)
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
            model=CreateSnicResponse,
        )

    def delete_snic(self, request, config=None):
        """
        delete_snic

        :param request: Request entity containing all parameters
        :type request: SnicClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(SnicClient.VERSION_V1, SnicClient.CONSTANT_ENDPOINT, request.endpoint_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def describe_snic(self, request, config=None):
        """
        describe_snic

        :param request: Request entity containing all parameters
        :type request: SnicClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeSnicResponse data
        :rtype: DescribeSnicResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(SnicClient.VERSION_V1, SnicClient.CONSTANT_ENDPOINT, request.endpoint_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=DescribeSnicResponse)

    def list_snic(self, request, config=None):
        """
        list_snic

        :param request: Request entity containing all parameters
        :type request: SnicClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListSnicResponse data
        :rtype: ListSnicResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(SnicClient.VERSION_V1, SnicClient.CONSTANT_ENDPOINT)
        headers = None
        params = {}
        if request.vpc_id is not None:
            params['vpcId'] = request.vpc_id
        if request.name is not None:
            params['name'] = request.name
        if request.ip_address is not None:
            params['ipAddress'] = request.ip_address
        if request.status is not None:
            params['status'] = request.status
        if request.subnet_id is not None:
            params['subnetId'] = request.subnet_id
        if request.service is not None:
            params['service'] = request.service
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListSnicResponse
        )

    def query_available_public_services(self, config=None):
        """
        query_available_public_services
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryAvailablePublicServicesResponse data
        :rtype: QueryAvailablePublicServicesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            SnicClient.VERSION_V1, SnicClient.CONSTANT_ENDPOINT, SnicClient.CONSTANT_PUBLIC_SERVICE
        )
        headers = None
        return self._send_request(
            http_methods.GET, path=path, config=config, model=QueryAvailablePublicServicesResponse
        )

    def update_snic(self, request, config=None):
        """
        update_snic

        :param request: Request entity containing all parameters
        :type request: SnicClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(SnicClient.VERSION_V1, SnicClient.CONSTANT_ENDPOINT, request.endpoint_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_snic_esg(self, request, config=None):
        """
        update_snic_esg

        :param request: Request entity containing all parameters
        :type request: SnicClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(SnicClient.VERSION_V1, SnicClient.CONSTANT_ENDPOINT, request.endpoint_id)
        headers = None
        params = {}
        params['bindEsg'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_snic_sg(self, request, config=None):
        """
        update_snic_sg

        :param request: Request entity containing all parameters
        :type request: SnicClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(SnicClient.VERSION_V1, SnicClient.CONSTANT_ENDPOINT, request.endpoint_id)
        headers = None
        params = {}
        params['bindSg'] = None
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
