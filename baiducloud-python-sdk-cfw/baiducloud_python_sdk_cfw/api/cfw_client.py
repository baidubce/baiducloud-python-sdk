"""
Example for cfw client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.auth import bce_v1_signer
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_cfw.models.create_cfw_response import CreateCfwResponse
from baiducloud_python_sdk_cfw.models.get_cfw_response import GetCfwResponse
from baiducloud_python_sdk_cfw.models.list_cfw_response import ListCfwResponse
from baiducloud_python_sdk_cfw.models.list_protect_instances_response import ListProtectInstancesResponse

_logger = logging.getLogger(__name__)


class CfwClient(BceBaseClient):
    """
    cfw base sdk client
    """

    VERSION_V1 = b'/v1'

    CONSTANT_CFW = b'cfw'

    CONSTANT_RULE = b'rule'

    CONSTANT_DELETE = b'delete'

    CONSTANT_INSTANCE = b'instance'

    def __init__(self, config=None):
        """
        Initialize the cfw client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def bind_cfw(self, request, config=None):
        """
        bind_cfw

        :param request: Request entity containing all parameters
        :type request: CfwClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CfwClient.VERSION_V1, CfwClient.CONSTANT_CFW, request.cfw_id)
        headers = None
        params = {}
        params['bind'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def create_cfw(self, request, config=None):
        """
        create_cfw

        :param request: Request entity containing all parameters
        :type request: CfwClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateCfwResponse data
        :rtype: CreateCfwResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CfwClient.VERSION_V1, CfwClient.CONSTANT_CFW)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), config=merged_config, model=CreateCfwResponse
        )

    def create_cfw_rule(self, request, config=None):
        """
        create_cfw_rule

        :param request: Request entity containing all parameters
        :type request: CfwClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CfwClient.VERSION_V1, CfwClient.CONSTANT_CFW, request.cfw_id, CfwClient.CONSTANT_RULE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def delete_cfw(self, request, config=None):
        """
        delete_cfw

        :param request: Request entity containing all parameters
        :type request: CfwClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CfwClient.VERSION_V1, CfwClient.CONSTANT_CFW, request.cfw_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def delete_cfw_rule(self, request, config=None):
        """
        delete_cfw_rule

        :param request: Request entity containing all parameters
        :type request: CfwClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CfwClient.VERSION_V1,
            CfwClient.CONSTANT_CFW,
            request.cfw_id,
            CfwClient.CONSTANT_DELETE,
            CfwClient.CONSTANT_RULE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def disable_cfw_protect(self, request, config=None):
        """
        disable_cfw_protect

        :param request: Request entity containing all parameters
        :type request: CfwClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CfwClient.VERSION_V1, CfwClient.CONSTANT_CFW, request.cfw_id)
        headers = None
        params = {}
        params['off'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def enable_cfw_protect(self, request, config=None):
        """
        enable_cfw_protect

        :param request: Request entity containing all parameters
        :type request: CfwClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CfwClient.VERSION_V1, CfwClient.CONSTANT_CFW, request.cfw_id)
        headers = None
        params = {}
        params['on'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def get_cfw(self, request, config=None):
        """
        get_cfw

        :param request: Request entity containing all parameters
        :type request: CfwClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetCfwResponse data
        :rtype: GetCfwResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CfwClient.VERSION_V1, CfwClient.CONSTANT_CFW, request.cfw_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetCfwResponse)

    def list_cfw(self, request, config=None):
        """
        list_cfw

        :param request: Request entity containing all parameters
        :type request: CfwClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListCfwResponse data
        :rtype: ListCfwResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CfwClient.VERSION_V1, CfwClient.CONSTANT_CFW)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListCfwResponse
        )

    def list_protect_instances(self, request, config=None):
        """
        list_protect_instances

        :param request: Request entity containing all parameters
        :type request: CfwClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListProtectInstancesResponse data
        :rtype: ListProtectInstancesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CfwClient.VERSION_V1, CfwClient.CONSTANT_CFW, CfwClient.CONSTANT_INSTANCE)
        headers = None
        params = {}
        if request.instance_type is not None:
            params['instanceType'] = request.instance_type
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.status is not None:
            params['status'] = request.status
        if request.region is not None:
            params['region'] = request.region
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListProtectInstancesResponse
        )

    def unbind_cfw(self, request, config=None):
        """
        unbind_cfw

        :param request: Request entity containing all parameters
        :type request: CfwClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CfwClient.VERSION_V1, CfwClient.CONSTANT_CFW, request.cfw_id)
        headers = None
        params = {}
        params['unbind'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_cfw(self, request, config=None):
        """
        update_cfw

        :param request: Request entity containing all parameters
        :type request: CfwClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CfwClient.VERSION_V1, CfwClient.CONSTANT_CFW, request.cfw_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def update_cfw_rule(self, request, config=None):
        """
        update_cfw_rule

        :param request: Request entity containing all parameters
        :type request: CfwClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CfwClient.VERSION_V1, CfwClient.CONSTANT_CFW, request.cfw_id, CfwClient.CONSTANT_RULE, request.cfw_rule_id
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
