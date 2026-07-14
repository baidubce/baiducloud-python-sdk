"""
Example for as client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.auth import bce_v1_signer
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_as.models.adjust_num_v2_response import AdjustNumV2Response
from baiducloud_python_sdk_as.models.attach_node_v2_response import AttachNodeV2Response
from baiducloud_python_sdk_as.models.create_as_group_v2_response import CreateAsGroupV2Response
from baiducloud_python_sdk_as.models.create_rule_v2_response import CreateRuleV2Response
from baiducloud_python_sdk_as.models.detach_node_v2_response import DetachNodeV2Response
from baiducloud_python_sdk_as.models.exec_rule_v2_response import ExecRuleV2Response
from baiducloud_python_sdk_as.models.get_as_group_v2_response import GetAsGroupV2Response
from baiducloud_python_sdk_as.models.get_rule_v2_response import GetRuleV2Response
from baiducloud_python_sdk_as.models.list_as_group_v2_response import ListAsGroupV2Response
from baiducloud_python_sdk_as.models.list_as_node_v2_response import ListAsNodeV2Response
from baiducloud_python_sdk_as.models.list_rule_v2_response import ListRuleV2Response
from baiducloud_python_sdk_as.models.list_task_v2_response import ListTaskV2Response
from baiducloud_python_sdk_as.models.scaling_down_v2_response import ScalingDownV2Response
from baiducloud_python_sdk_as.models.scaling_up_v2_response import ScalingUpV2Response

_logger = logging.getLogger(__name__)


class AsClient(BceBaseClient):
    """
    as base sdk client
    """

    CONSTANT_V2 = b'v2'

    CONSTANT_GROUP = b'group'

    CONSTANT_V1 = b'v1'

    CONSTANT_RULE = b'rule'

    CONSTANT_NODE = b'node'

    CONSTANT_DELETE = b'delete'

    CONSTANT_TASK = b'task'

    def __init__(self, config=None):
        """
        Initialize the as client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def adjust_num_v2(self, request, config=None):
        """
        adjust_num_v2

        :param request: Request entity containing all parameters
        :type request: AsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing AdjustNumV2Response data
        :rtype: AdjustNumV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AsClient.CONSTANT_V2, AsClient.CONSTANT_GROUP, request.group_id)
        headers = None
        params = {}
        if request.adjust_node is not None:
            params['adjustNode'] = request.adjust_node
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=AdjustNumV2Response,
        )

    def attach_node_v2(self, request, config=None):
        """
        attach_node_v2

        :param request: Request entity containing all parameters
        :type request: AsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing AttachNodeV2Response data
        :rtype: AttachNodeV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AsClient.CONSTANT_V2, AsClient.CONSTANT_GROUP, request.group_id)
        headers = None
        params = {}
        if request.attach_node is not None:
            params['attachNode'] = request.attach_node
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=AttachNodeV2Response,
        )

    def create_as_group_v2(self, request, config=None):
        """
        create_as_group_v2

        :param request: Request entity containing all parameters
        :type request: AsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateAsGroupV2Response data
        :rtype: CreateAsGroupV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AsClient.CONSTANT_V2, AsClient.CONSTANT_GROUP)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateAsGroupV2Response,
        )

    def create_rule_v2(self, request, config=None):
        """
        create_rule_v2

        :param request: Request entity containing all parameters
        :type request: AsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateRuleV2Response data
        :rtype: CreateRuleV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AsClient.CONSTANT_V1, AsClient.CONSTANT_RULE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateRuleV2Response,
        )

    def delete_as_group_v2(self, request, config=None):
        """
        delete_as_group_v2

        :param request: Request entity containing all parameters
        :type request: AsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AsClient.CONSTANT_V2, AsClient.CONSTANT_GROUP, AsClient.CONSTANT_DELETE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def delete_rule_v2(self, request, config=None):
        """
        delete_rule_v2

        :param request: Request entity containing all parameters
        :type request: AsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AsClient.CONSTANT_V1, AsClient.CONSTANT_RULE, request.rule_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def detach_node_v2(self, request, config=None):
        """
        detach_node_v2

        :param request: Request entity containing all parameters
        :type request: AsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DetachNodeV2Response data
        :rtype: DetachNodeV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AsClient.CONSTANT_V2, AsClient.CONSTANT_GROUP, request.group_id)
        headers = None
        params = {}
        if request.detach_node is not None:
            params['detachNode'] = request.detach_node
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DetachNodeV2Response,
        )

    def exec_rule_v2(self, request, config=None):
        """
        exec_rule_v2

        :param request: Request entity containing all parameters
        :type request: AsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ExecRuleV2Response data
        :rtype: ExecRuleV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AsClient.CONSTANT_V2, AsClient.CONSTANT_GROUP, request.group_id)
        headers = None
        params = {}
        if request.exec_rule is not None:
            params['execRule'] = request.exec_rule
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=ExecRuleV2Response,
        )

    def get_as_group_v2(self, request, config=None):
        """
        get_as_group_v2

        :param request: Request entity containing all parameters
        :type request: AsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetAsGroupV2Response data
        :rtype: GetAsGroupV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AsClient.CONSTANT_V1, AsClient.CONSTANT_GROUP, request.group_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetAsGroupV2Response)

    def get_rule_v2(self, request, config=None):
        """
        get_rule_v2

        :param request: Request entity containing all parameters
        :type request: AsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetRuleV2Response data
        :rtype: GetRuleV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AsClient.CONSTANT_V1, AsClient.CONSTANT_RULE, request.rule_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetRuleV2Response)

    def list_as_group_v2(self, request, config=None):
        """
        list_as_group_v2

        :param request: Request entity containing all parameters
        :type request: AsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListAsGroupV2Response data
        :rtype: ListAsGroupV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AsClient.CONSTANT_V1, AsClient.CONSTANT_GROUP)
        headers = None
        params = {}
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        if request.keyword is not None:
            params['keyword'] = request.keyword
        if request.keyword_type is not None:
            params['keywordType'] = request.keyword_type
        if request.sub_keyword_type is not None:
            params['subKeywordType'] = request.sub_keyword_type
        if request.order is not None:
            params['order'] = request.order
        if request.order_by is not None:
            params['orderBy'] = request.order_by
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListAsGroupV2Response
        )

    def list_as_node_v2(self, request, config=None):
        """
        list_as_node_v2

        :param request: Request entity containing all parameters
        :type request: AsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListAsNodeV2Response data
        :rtype: ListAsNodeV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AsClient.CONSTANT_V1, AsClient.CONSTANT_NODE)
        headers = None
        params = {}
        if request.groupid is not None:
            params['groupid'] = request.groupid
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        if request.keyword is not None:
            params['keyword'] = request.keyword
        if request.keyword_type is not None:
            params['keywordType'] = request.keyword_type
        if request.order is not None:
            params['order'] = request.order
        if request.order_by is not None:
            params['orderBy'] = request.order_by
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListAsNodeV2Response
        )

    def list_rule_v2(self, request, config=None):
        """
        list_rule_v2

        :param request: Request entity containing all parameters
        :type request: AsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListRuleV2Response data
        :rtype: ListRuleV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AsClient.CONSTANT_V1, AsClient.CONSTANT_RULE)
        headers = None
        params = {}
        if request.groupid is not None:
            params['groupid'] = request.groupid
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        if request.keyword is not None:
            params['keyword'] = request.keyword
        if request.keyword_type is not None:
            params['keywordType'] = request.keyword_type
        if request.order is not None:
            params['order'] = request.order
        if request.order_by is not None:
            params['orderBy'] = request.order_by
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListRuleV2Response
        )

    def list_task_v2(self, request, config=None):
        """
        list_task_v2

        :param request: Request entity containing all parameters
        :type request: AsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListTaskV2Response data
        :rtype: ListTaskV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AsClient.CONSTANT_V1, AsClient.CONSTANT_TASK)
        headers = None
        params = {}
        if request.groupid is not None:
            params['groupid'] = request.groupid
        if request.order_by is not None:
            params['orderBy'] = request.order_by
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.order is not None:
            params['order'] = request.order
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        if request.start_time is not None:
            params['startTime'] = request.start_time
        if request.end_time is not None:
            params['endTime'] = request.end_time
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListTaskV2Response
        )

    def scaling_down_v2(self, request, config=None):
        """
        scaling_down_v2

        :param request: Request entity containing all parameters
        :type request: AsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ScalingDownV2Response data
        :rtype: ScalingDownV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AsClient.CONSTANT_V2, AsClient.CONSTANT_GROUP, request.group_id)
        headers = None
        params = {}
        if request.scaling_down is not None:
            params['scalingDown'] = request.scaling_down
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=ScalingDownV2Response,
        )

    def scaling_up_v2(self, request, config=None):
        """
        scaling_up_v2

        :param request: Request entity containing all parameters
        :type request: AsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ScalingUpV2Response data
        :rtype: ScalingUpV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AsClient.CONSTANT_V2, AsClient.CONSTANT_GROUP, request.group_id)
        headers = None
        params = {}
        if request.scaling_up is not None:
            params['scalingUp'] = request.scaling_up
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=ScalingUpV2Response,
        )

    def update_is_managed_v2(self, request, config=None):
        """
        update_is_managed_v2

        :param request: Request entity containing all parameters
        :type request: AsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AsClient.CONSTANT_V1, AsClient.CONSTANT_NODE, request.group_id)
        headers = None
        params = {}
        if request.update_is_managed is not None:
            params['updateIsManaged'] = request.update_is_managed
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_protect_v2(self, request, config=None):
        """
        update_protect_v2

        :param request: Request entity containing all parameters
        :type request: AsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AsClient.CONSTANT_V1, AsClient.CONSTANT_GROUP, request.group_id)
        headers = None
        params = {}
        if request.update_protect is not None:
            params['updateProtect'] = request.update_protect
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
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
