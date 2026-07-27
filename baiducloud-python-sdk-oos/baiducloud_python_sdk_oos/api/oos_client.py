"""
Example for oos client.
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
from baiducloud_python_sdk_oos.models.check_template_v2_response import CheckTemplateV2Response
from baiducloud_python_sdk_oos.models.create_execution_v2_response import CreateExecutionV2Response
from baiducloud_python_sdk_oos.models.create_template_v2_response import CreateTemplateV2Response
from baiducloud_python_sdk_oos.models.delete_template_v2_response import DeleteTemplateV2Response
from baiducloud_python_sdk_oos.models.get_execution_detail_v2_response import GetExecutionDetailV2Response
from baiducloud_python_sdk_oos.models.get_execution_list_v2_response import GetExecutionListV2Response
from baiducloud_python_sdk_oos.models.get_operator_list_v2_response import GetOperatorListV2Response
from baiducloud_python_sdk_oos.models.get_task_children_list_v2_response import GetTaskChildrenListV2Response
from baiducloud_python_sdk_oos.models.get_task_detail_v2_response import GetTaskDetailV2Response
from baiducloud_python_sdk_oos.models.get_template_detail_v2_response import GetTemplateDetailV2Response
from baiducloud_python_sdk_oos.models.get_template_list_v2_response import GetTemplateListV2Response
from baiducloud_python_sdk_oos.models.update_template_v2_response import UpdateTemplateV2Response

_logger = logging.getLogger(__name__)


class OosClient(BceBaseClient):
    """
    oos base sdk client
    """

    VERSION_V2 = b'/v2'

    CONSTANT_TEMPLATE = b'template'

    CONSTANT_EXECUTION = b'execution'

    CONSTANT_CHECK = b'check'

    CONSTANT_LIST = b'list'

    CONSTANT_TASK = b'task'

    CONSTANT_OPERATOR = b'operator'

    CONSTANT_CHILDREN = b'children'

    def __init__(self, config=None):
        """
        Initialize the oos client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def check_template_v2(self, request, config=None):
        """
        check_template_v2

        :param request: Request entity containing all parameters
        :type request: OosClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CheckTemplateV2Response data
        :rtype: CheckTemplateV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(OosClient.VERSION_V2, OosClient.CONSTANT_TEMPLATE, OosClient.CONSTANT_CHECK)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CheckTemplateV2Response,
        )

    def create_execution_v2(self, request, config=None):
        """
        create_execution_v2

        :param request: Request entity containing all parameters
        :type request: OosClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateExecutionV2Response data
        :rtype: CreateExecutionV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(OosClient.VERSION_V2, OosClient.CONSTANT_EXECUTION)
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
            model=CreateExecutionV2Response,
        )

    def create_template_v2(self, request, config=None):
        """
        create_template_v2

        :param request: Request entity containing all parameters
        :type request: OosClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateTemplateV2Response data
        :rtype: CreateTemplateV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(OosClient.VERSION_V2, OosClient.CONSTANT_TEMPLATE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateTemplateV2Response,
        )

    def delete_template_v2(self, request, config=None):
        """
        delete_template_v2

        :param request: Request entity containing all parameters
        :type request: OosClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DeleteTemplateV2Response data
        :rtype: DeleteTemplateV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(OosClient.VERSION_V2, OosClient.CONSTANT_TEMPLATE)
        headers = None
        params = {}
        if request.id is not None:
            params['id'] = request.id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.DELETE, path=path, params=params, config=merged_config, model=DeleteTemplateV2Response
        )

    def get_execution_detail_v2(self, request, config=None):
        """
        get_execution_detail_v2

        :param request: Request entity containing all parameters
        :type request: OosClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetExecutionDetailV2Response data
        :rtype: GetExecutionDetailV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(OosClient.VERSION_V2, OosClient.CONSTANT_EXECUTION)
        headers = None
        params = {}
        if request.id is not None:
            params['id'] = request.id
        if request.with_log is not None:
            params['withLog'] = request.with_log
        if request.locale is not None:
            params['locale'] = request.locale
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetExecutionDetailV2Response
        )

    def get_execution_list_v2(self, request, config=None):
        """
        get_execution_list_v2

        :param request: Request entity containing all parameters
        :type request: OosClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetExecutionListV2Response data
        :rtype: GetExecutionListV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(OosClient.VERSION_V2, OosClient.CONSTANT_EXECUTION, OosClient.CONSTANT_LIST)
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
            model=GetExecutionListV2Response,
        )

    def get_operator_list_v2(self, request, config=None):
        """
        get_operator_list_v2

        :param request: Request entity containing all parameters
        :type request: OosClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetOperatorListV2Response data
        :rtype: GetOperatorListV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(OosClient.VERSION_V2, OosClient.CONSTANT_OPERATOR, OosClient.CONSTANT_LIST)
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
            model=GetOperatorListV2Response,
        )

    def get_task_children_list_v2(self, request, config=None):
        """
        get_task_children_list_v2

        :param request: Request entity containing all parameters
        :type request: OosClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetTaskChildrenListV2Response data
        :rtype: GetTaskChildrenListV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            OosClient.VERSION_V2, OosClient.CONSTANT_TASK, OosClient.CONSTANT_CHILDREN, OosClient.CONSTANT_LIST
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
            model=GetTaskChildrenListV2Response,
        )

    def get_task_detail_v2(self, request, config=None):
        """
        get_task_detail_v2

        :param request: Request entity containing all parameters
        :type request: OosClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetTaskDetailV2Response data
        :rtype: GetTaskDetailV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(OosClient.VERSION_V2, OosClient.CONSTANT_TASK)
        headers = None
        params = {}
        if request.dag_id is not None:
            params['dagId'] = request.dag_id
        if request.task_id is not None:
            params['taskId'] = request.task_id
        if request.ignore_children is not None:
            params['ignoreChildren'] = request.ignore_children
        if request.locale is not None:
            params['locale'] = request.locale
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetTaskDetailV2Response
        )

    def get_template_detail_v2(self, request, config=None):
        """
        get_template_detail_v2

        :param request: Request entity containing all parameters
        :type request: OosClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetTemplateDetailV2Response data
        :rtype: GetTemplateDetailV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(OosClient.VERSION_V2, OosClient.CONSTANT_TEMPLATE)
        headers = None
        params = {}
        if request.id is not None:
            params['id'] = request.id
        if request.name is not None:
            params['name'] = request.name
        if request.type is not None:
            params['type'] = request.type
        if request.locale is not None:
            params['locale'] = request.locale
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetTemplateDetailV2Response
        )

    def get_template_list_v2(self, request, config=None):
        """
        get_template_list_v2

        :param request: Request entity containing all parameters
        :type request: OosClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetTemplateListV2Response data
        :rtype: GetTemplateListV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(OosClient.VERSION_V2, OosClient.CONSTANT_TEMPLATE, OosClient.CONSTANT_LIST)
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
            model=GetTemplateListV2Response,
        )

    def update_template_v2(self, request, config=None):
        """
        update_template_v2

        :param request: Request entity containing all parameters
        :type request: OosClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UpdateTemplateV2Response data
        :rtype: UpdateTemplateV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(OosClient.VERSION_V2, OosClient.CONSTANT_TEMPLATE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=UpdateTemplateV2Response,
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
