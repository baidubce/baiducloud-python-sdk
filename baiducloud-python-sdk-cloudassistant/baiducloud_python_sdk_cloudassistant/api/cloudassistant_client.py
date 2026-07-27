"""
Example for cloudassistant client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.auth import bce_v1_signer
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_core.util import request_body_utils
from baiducloud_python_sdk_cloudassistant.models.action_list_response import ActionListResponse
from baiducloud_python_sdk_cloudassistant.models.action_log_response import ActionLogResponse
from baiducloud_python_sdk_cloudassistant.models.action_run_response import ActionRunResponse
from baiducloud_python_sdk_cloudassistant.models.action_run_list_response import ActionRunListResponse
from baiducloud_python_sdk_cloudassistant.models.batch_get_agent_response import BatchGetAgentResponse
from baiducloud_python_sdk_cloudassistant.models.create_action_response import CreateActionResponse
from baiducloud_python_sdk_cloudassistant.models.delete_action_response import DeleteActionResponse
from baiducloud_python_sdk_cloudassistant.models.get_action_response import GetActionResponse
from baiducloud_python_sdk_cloudassistant.models.get_action_run_response import GetActionRunResponse
from baiducloud_python_sdk_cloudassistant.models.update_action_response import UpdateActionResponse

_logger = logging.getLogger(__name__)


class CloudassistantClient(BceBaseClient):
    """
    cloudassistant base sdk client
    """

    VERSION_V1 = b'/v1'

    CONSTANT_CA = b'ca'

    CONSTANT_ACTION = b'action'

    CONSTANT_ACTION_RUN = b'actionRun'

    CONSTANT_AGENT = b'agent'

    CONSTANT_BATCH = b'batch'

    CONSTANT_LIST = b'list'

    CONSTANT_LOG = b'log'

    def __init__(self, config=None):
        """
        Initialize the cloudassistant client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def action_list(self, request, config=None):
        """
        action_list

        :param request: Request entity containing all parameters
        :type request: CloudassistantClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ActionListResponse data
        :rtype: ActionListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CloudassistantClient.VERSION_V1,
            CloudassistantClient.CONSTANT_CA,
            CloudassistantClient.CONSTANT_ACTION,
            CloudassistantClient.CONSTANT_LIST,
        )
        headers = None
        params = {}
        if request.locale is not None:
            params['locale'] = request.locale
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=ActionListResponse,
        )

    def action_log(self, request, config=None):
        """
        action_log

        :param request: Request entity containing all parameters
        :type request: CloudassistantClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ActionLogResponse data
        :rtype: ActionLogResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CloudassistantClient.VERSION_V1, CloudassistantClient.CONSTANT_CA, CloudassistantClient.CONSTANT_LOG
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), config=merged_config, model=ActionLogResponse
        )

    def action_run(self, request, config=None):
        """
        action_run

        :param request: Request entity containing all parameters
        :type request: CloudassistantClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ActionRunResponse data
        :rtype: ActionRunResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CloudassistantClient.VERSION_V1, CloudassistantClient.CONSTANT_CA, CloudassistantClient.CONSTANT_ACTION_RUN
        )
        headers = None
        params = {}
        if request.locale is not None:
            params['locale'] = request.locale
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=ActionRunResponse,
        )

    def action_run_list(self, request, config=None):
        """
        action_run_list

        :param request: Request entity containing all parameters
        :type request: CloudassistantClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ActionRunListResponse data
        :rtype: ActionRunListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CloudassistantClient.VERSION_V1,
            CloudassistantClient.CONSTANT_CA,
            CloudassistantClient.CONSTANT_ACTION_RUN,
            CloudassistantClient.CONSTANT_LIST,
        )
        headers = None
        params = {}
        if request.locale is not None:
            params['locale'] = request.locale
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=ActionRunListResponse,
        )

    def batch_get_agent(self, request, config=None):
        """
        batch_get_agent

        :param request: Request entity containing all parameters
        :type request: CloudassistantClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BatchGetAgentResponse data
        :rtype: BatchGetAgentResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CloudassistantClient.VERSION_V1,
            CloudassistantClient.CONSTANT_CA,
            CloudassistantClient.CONSTANT_AGENT,
            CloudassistantClient.CONSTANT_BATCH,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=BatchGetAgentResponse,
        )

    def create_action(self, request, config=None):
        """
        create_action

        :param request: Request entity containing all parameters
        :type request: CloudassistantClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateActionResponse data
        :rtype: CreateActionResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CloudassistantClient.VERSION_V1, CloudassistantClient.CONSTANT_CA, CloudassistantClient.CONSTANT_ACTION
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateActionResponse,
        )

    def delete_action(self, request, config=None):
        """
        delete_action

        :param request: Request entity containing all parameters
        :type request: CloudassistantClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DeleteActionResponse data
        :rtype: DeleteActionResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CloudassistantClient.VERSION_V1,
            CloudassistantClient.CONSTANT_CA,
            CloudassistantClient.CONSTANT_ACTION,
            request.id,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config, model=DeleteActionResponse)

    def get_action(self, request, config=None):
        """
        get_action

        :param request: Request entity containing all parameters
        :type request: CloudassistantClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetActionResponse data
        :rtype: GetActionResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CloudassistantClient.VERSION_V1, CloudassistantClient.CONSTANT_CA, CloudassistantClient.CONSTANT_ACTION
        )
        headers = None
        params = {}
        if request.id is not None:
            params['id'] = request.id
        if request.locale is not None:
            params['locale'] = request.locale
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetActionResponse
        )

    def get_action_run(self, request, config=None):
        """
        get_action_run

        :param request: Request entity containing all parameters
        :type request: CloudassistantClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetActionRunResponse data
        :rtype: GetActionRunResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CloudassistantClient.VERSION_V1, CloudassistantClient.CONSTANT_CA, CloudassistantClient.CONSTANT_ACTION_RUN
        )
        headers = None
        params = {}
        if request.id is not None:
            params['id'] = request.id
        if request.with_log is not None:
            params['withLog'] = request.with_log
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        if request.child_run_state is not None:
            params['childRunState'] = request.child_run_state
        if request.locale is not None:
            params['locale'] = request.locale
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetActionRunResponse
        )

    def update_action(self, request, config=None):
        """
        update_action

        :param request: Request entity containing all parameters
        :type request: CloudassistantClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UpdateActionResponse data
        :rtype: UpdateActionResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CloudassistantClient.VERSION_V1, CloudassistantClient.CONSTANT_CA, CloudassistantClient.CONSTANT_ACTION
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=UpdateActionResponse,
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
