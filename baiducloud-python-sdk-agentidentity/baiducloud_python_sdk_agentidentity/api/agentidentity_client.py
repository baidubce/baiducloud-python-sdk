"""
Example for agentidentity client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.auth import bce_v1_signer
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_agentidentity.models.batch_get_resource_api_key_response import (
    BatchGetResourceApiKeyResponse,
)
from baiducloud_python_sdk_agentidentity.models.list_agents_response import ListAgentsResponse
from baiducloud_python_sdk_agentidentity.models.list_credential_providers_response import (
    ListCredentialProvidersResponse,
)
from baiducloud_python_sdk_agentidentity.models.list_idp_configurations_response import ListIdpConfigurationsResponse
from baiducloud_python_sdk_agentidentity.models.list_oauth2_clients_response import ListOauth2ClientsResponse
from baiducloud_python_sdk_agentidentity.models.list_user_pools_response import ListUserPoolsResponse
from baiducloud_python_sdk_agentidentity.models.list_users_response import ListUsersResponse
from baiducloud_python_sdk_agentidentity.models.userinfo_endpoint_response import UserinfoEndpointResponse

_logger = logging.getLogger(__name__)


class AgentidentityClient(BceBaseClient):
    """
    agentidentity base sdk client
    """

    VERSION_V1 = b'/v1'

    CONSTANT_AGENT_IDENTITY = b'agent-identity'

    CONSTANT_WORKLOAD_ACCESS_TOKEN = b'workload-access-token'

    CONSTANT_AGENT = b'agent'

    CONSTANT_LIST = b'list'

    CONSTANT_USER_POOL = b'user-pool'

    CONSTANT_USER = b'user'

    CONSTANT_RESET_PASSWORD = b'resetPassword'

    CONSTANT_OAUTH2_CLIENT = b'oauth2-client'

    CONSTANT_GET = b'get'

    CONSTANT_UPDATE = b'update'

    CONSTANT_CREDENTIAL = b'credential'

    CONSTANT_APIKEY = b'apikey'

    CONSTANT_BATCH = b'batch'

    CONSTANT_IDP_CONFIG = b'idp-config'

    CONSTANT_CREATE = b'create'

    CONSTANT_DELETE = b'delete'

    CONSTANT_CREDENTIAL_PROVIDER = b'credential-provider'

    CONSTANT_INBOUND = b'inbound'

    CONSTANT_TOKEN = b'token'

    CONSTANT_WORKLOAD_ACCESS_TOKEN_FOR_USER = b'workload-access-token-for-user'

    CONSTANT_OAUTH2 = b'oauth2'

    CONSTANT_CALLBACK = b'callback'

    CONSTANT_WELL_KNOWN = b'.well-known'

    CONSTANT_OPENID_CONFIGURATION = b'openid-configuration'

    CONSTANT_ENABLE = b'enable'

    CONSTANT_USERINFO = b'userinfo'

    CONSTANT_AUTHORIZE = b'authorize'

    CONSTANT_COMPLETE_AUTH = b'complete-auth'

    CONSTANT_DISABLE = b'disable'

    def __init__(self, config=None):
        """
        Initialize the agentidentity client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def authorize_endpoint(self, request, config=None):
        """
        authorize_endpoint

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_INBOUND,
            request.user_pool_id,
            AgentidentityClient.CONSTANT_AUTHORIZE,
        )
        headers = None
        params = {}
        if request.client_id is not None:
            params['clientId'] = request.client_id
        if request.redirect_uri is not None:
            params['redirectUri'] = request.redirect_uri
        if request.response_type is not None:
            params['responseType'] = request.response_type
        if request.scope is not None:
            params['scope'] = request.scope
        if request.state is not None:
            params['state'] = request.state
        if request.nonce is not None:
            params['nonce'] = request.nonce
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, params=params, config=merged_config)

    def batch_acquisition_of_users(self, request, config=None):
        """
        batch_acquisition_of_users

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_USER_POOL,
            AgentidentityClient.CONSTANT_USER,
            AgentidentityClient.CONSTANT_BATCH,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def batch_get_resource_api_key(self, request, config=None):
        """
        batch_get_resource_api_key

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BatchGetResourceApiKeyResponse data
        :rtype: BatchGetResourceApiKeyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_CREDENTIAL,
            AgentidentityClient.CONSTANT_APIKEY,
            AgentidentityClient.CONSTANT_BATCH,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=BatchGetResourceApiKeyResponse,
        )

    def complete_oauth2session(self, request, config=None):
        """
        complete_oauth2session

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_OAUTH2,
            AgentidentityClient.CONSTANT_COMPLETE_AUTH,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def create_agent(self, request, config=None):
        """
        create_agent

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_AGENT,
            AgentidentityClient.CONSTANT_CREATE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def create_credential_provider(self, request, config=None):
        """
        create_credential_provider

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_CREDENTIAL_PROVIDER,
            AgentidentityClient.CONSTANT_CREATE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def create_idp_configuration(self, request, config=None):
        """
        create_idp_configuration

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_USER_POOL,
            AgentidentityClient.CONSTANT_IDP_CONFIG,
            AgentidentityClient.CONSTANT_CREATE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def create_oauth2_client(self, request, config=None):
        """
        create_oauth2_client

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_USER_POOL,
            AgentidentityClient.CONSTANT_OAUTH2_CLIENT,
            AgentidentityClient.CONSTANT_CREATE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def create_user(self, request, config=None):
        """
        create_user

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_USER_POOL,
            AgentidentityClient.CONSTANT_USER,
            AgentidentityClient.CONSTANT_CREATE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def create_user_pool(self, request, config=None):
        """
        create_user_pool

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_USER_POOL,
            AgentidentityClient.CONSTANT_CREATE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def delete_agent(self, request, config=None):
        """
        delete_agent

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_AGENT,
            AgentidentityClient.CONSTANT_DELETE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def delete_credential_provider(self, request, config=None):
        """
        delete_credential_provider

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_CREDENTIAL_PROVIDER,
            AgentidentityClient.CONSTANT_DELETE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def delete_idp_configuration(self, request, config=None):
        """
        delete_idp_configuration

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_USER_POOL,
            AgentidentityClient.CONSTANT_IDP_CONFIG,
            AgentidentityClient.CONSTANT_DELETE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def delete_oauth2_client(self, request, config=None):
        """
        delete_oauth2_client

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_USER_POOL,
            AgentidentityClient.CONSTANT_OAUTH2_CLIENT,
            AgentidentityClient.CONSTANT_DELETE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def delete_user(self, request, config=None):
        """
        delete_user

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_USER_POOL,
            AgentidentityClient.CONSTANT_USER,
            AgentidentityClient.CONSTANT_DELETE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def delete_user_pool(self, request, config=None):
        """
        delete_user_pool

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_USER_POOL,
            AgentidentityClient.CONSTANT_DELETE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def disable_idp_configuration(self, request, config=None):
        """
        disable_idp_configuration

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_USER_POOL,
            AgentidentityClient.CONSTANT_IDP_CONFIG,
            AgentidentityClient.CONSTANT_DISABLE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def enable_idp_configuration(self, request, config=None):
        """
        enable_idp_configuration

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_USER_POOL,
            AgentidentityClient.CONSTANT_IDP_CONFIG,
            AgentidentityClient.CONSTANT_ENABLE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def get_agent(self, request, config=None):
        """
        get_agent

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_AGENT,
            AgentidentityClient.CONSTANT_GET,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def get_credential_provider(self, request, config=None):
        """
        get_credential_provider

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_CREDENTIAL_PROVIDER,
            AgentidentityClient.CONSTANT_GET,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def get_idp_configuration(self, request, config=None):
        """
        get_idp_configuration

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_USER_POOL,
            AgentidentityClient.CONSTANT_IDP_CONFIG,
            AgentidentityClient.CONSTANT_GET,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def get_oauth2_client(self, request, config=None):
        """
        get_oauth2_client

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_USER_POOL,
            AgentidentityClient.CONSTANT_OAUTH2_CLIENT,
            AgentidentityClient.CONSTANT_GET,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def get_resource_apikey(self, request, config=None):
        """
        get_resource_apikey

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_CREDENTIAL,
            AgentidentityClient.CONSTANT_APIKEY,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def get_resource_oauth2token(self, request, config=None):
        """
        get_resource_oauth2token

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_CREDENTIAL,
            AgentidentityClient.CONSTANT_OAUTH2,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def get_user(self, request, config=None):
        """
        get_user

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_USER_POOL,
            AgentidentityClient.CONSTANT_USER,
            AgentidentityClient.CONSTANT_GET,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def get_user_pool(self, request, config=None):
        """
        get_user_pool

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_USER_POOL,
            AgentidentityClient.CONSTANT_GET,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def get_wat_for_user(self, request, config=None):
        """
        get_wat_for_user

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_WORKLOAD_ACCESS_TOKEN_FOR_USER,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def get_workload_access_token(self, request, config=None):
        """
        get_workload_access_token

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_WORKLOAD_ACCESS_TOKEN,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def list_agents(self, request, config=None):
        """
        list_agents

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListAgentsResponse data
        :rtype: ListAgentsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_AGENT,
            AgentidentityClient.CONSTANT_LIST,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), config=merged_config, model=ListAgentsResponse
        )

    def list_credential_providers(self, request, config=None):
        """
        list_credential_providers

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListCredentialProvidersResponse data
        :rtype: ListCredentialProvidersResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_CREDENTIAL_PROVIDER,
            AgentidentityClient.CONSTANT_LIST,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=ListCredentialProvidersResponse,
        )

    def list_idp_configurations(self, request, config=None):
        """
        list_idp_configurations

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListIdpConfigurationsResponse data
        :rtype: ListIdpConfigurationsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_USER_POOL,
            AgentidentityClient.CONSTANT_IDP_CONFIG,
            AgentidentityClient.CONSTANT_LIST,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=ListIdpConfigurationsResponse,
        )

    def list_oauth2_clients(self, request, config=None):
        """
        list_oauth2_clients

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListOauth2ClientsResponse data
        :rtype: ListOauth2ClientsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_USER_POOL,
            AgentidentityClient.CONSTANT_OAUTH2_CLIENT,
            AgentidentityClient.CONSTANT_LIST,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=ListOauth2ClientsResponse,
        )

    def list_user_pools(self, request, config=None):
        """
        list_user_pools

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListUserPoolsResponse data
        :rtype: ListUserPoolsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_USER_POOL,
            AgentidentityClient.CONSTANT_LIST,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=ListUserPoolsResponse,
        )

    def list_users(self, request, config=None):
        """
        list_users

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListUsersResponse data
        :rtype: ListUsersResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_USER_POOL,
            AgentidentityClient.CONSTANT_USER,
            AgentidentityClient.CONSTANT_LIST,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), config=merged_config, model=ListUsersResponse
        )

    def o_idc_discovery(self, request, config=None):
        """
        o_idc_discovery

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_INBOUND,
            request.user_pool_id,
            AgentidentityClient.CONSTANT_WELL_KNOWN,
            AgentidentityClient.CONSTANT_OPENID_CONFIGURATION,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config)

    def oauth2idp_callback(self, request, config=None):
        """
        oauth2idp_callback

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_OAUTH2,
            AgentidentityClient.CONSTANT_CALLBACK,
            request.provider_id,
        )
        headers = None
        params = {}
        if request.code is not None:
            params['code'] = request.code
        if request.state is not None:
            params['state'] = request.state
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, params=params, config=merged_config)

    def reset_password(self, request, config=None):
        """
        reset_password

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_USER_POOL,
            AgentidentityClient.CONSTANT_USER,
            AgentidentityClient.CONSTANT_RESET_PASSWORD,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def token_endpoint(self, request, config=None):
        """
        token_endpoint

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_INBOUND,
            request.user_pool_id,
            AgentidentityClient.CONSTANT_TOKEN,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def update_agent(self, request, config=None):
        """
        update_agent

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_AGENT,
            AgentidentityClient.CONSTANT_UPDATE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def update_credential_provider(self, request, config=None):
        """
        update_credential_provider

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_CREDENTIAL_PROVIDER,
            AgentidentityClient.CONSTANT_UPDATE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def update_idp_configuration(self, request, config=None):
        """
        update_idp_configuration

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_USER_POOL,
            AgentidentityClient.CONSTANT_IDP_CONFIG,
            AgentidentityClient.CONSTANT_UPDATE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def update_oauth2_client(self, request, config=None):
        """
        update_oauth2_client

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_USER_POOL,
            AgentidentityClient.CONSTANT_OAUTH2_CLIENT,
            AgentidentityClient.CONSTANT_UPDATE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def update_user(self, request, config=None):
        """
        update_user

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_USER_POOL,
            AgentidentityClient.CONSTANT_USER,
            AgentidentityClient.CONSTANT_UPDATE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def update_user_pool(self, request, config=None):
        """
        update_user_pool

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_USER_POOL,
            AgentidentityClient.CONSTANT_UPDATE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def userinfo_endpoint(self, request, config=None):
        """
        userinfo_endpoint

        :param request: Request entity containing all parameters
        :type request: AgentidentityClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UserinfoEndpointResponse data
        :rtype: UserinfoEndpointResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            AgentidentityClient.VERSION_V1,
            AgentidentityClient.CONSTANT_AGENT_IDENTITY,
            AgentidentityClient.CONSTANT_INBOUND,
            request.user_pool_id,
            AgentidentityClient.CONSTANT_USERINFO,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=UserinfoEndpointResponse)

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
