"""
Example for sts client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.auth import bce_v1_signer
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_sts.models.assume_role_response import AssumeRoleResponse
from baiducloud_python_sdk_sts.models.get_session_token_response import GetSessionTokenResponse

_logger = logging.getLogger(__name__)


class StsClient(BceBaseClient):
    """
    sts base sdk client
    """

    VERSION_V1 = b'/v1'

    CONSTANT_SESSION_TOKEN = b'sessionToken'

    CONSTANT_CREDENTIAL = b'credential'

    def __init__(self, config=None):
        """
        Initialize the sts client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def assume_role(self, request, config=None):
        """
        assume_role

        :param request: Request entity containing all parameters
        :type request: StsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing AssumeRoleResponse data
        :rtype: AssumeRoleResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(StsClient.VERSION_V1, StsClient.CONSTANT_CREDENTIAL)
        headers = None
        params = {}
        params['assumeRole'] = None
        if request.account_id is not None:
            params['accountId'] = request.account_id
        if request.role_name is not None:
            params['roleName'] = request.role_name
        if request.duration_seconds is not None:
            params['durationSeconds'] = request.duration_seconds
        if request.user_id is not None:
            params['userId'] = request.user_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=AssumeRoleResponse,
        )

    def get_session_token(self, request, config=None):
        """
        get_session_token

        :param request: Request entity containing all parameters
        :type request: StsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetSessionTokenResponse data
        :rtype: GetSessionTokenResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(StsClient.VERSION_V1, StsClient.CONSTANT_SESSION_TOKEN)
        headers = None
        params = {}
        if request.duration_seconds is not None:
            params['durationSeconds'] = request.duration_seconds
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=GetSessionTokenResponse,
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
