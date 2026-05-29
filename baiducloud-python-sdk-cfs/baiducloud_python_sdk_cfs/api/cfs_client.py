"""
Example for cfs client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.auth import bce_v1_signer
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_cfs.models.batch_creation_of_permission_group_rules_response import (
    BatchCreationOfPermissionGroupRulesResponse,
)
from baiducloud_python_sdk_cfs.models.create_file_system_response import CreateFileSystemResponse
from baiducloud_python_sdk_cfs.models.create_mounting_target_response import CreateMountingTargetResponse
from baiducloud_python_sdk_cfs.models.create_permission_group_rules_response import CreatePermissionGroupRulesResponse
from baiducloud_python_sdk_cfs.models.query_file_system_response import QueryFileSystemResponse
from baiducloud_python_sdk_cfs.models.query_mounted_client_response import QueryMountedClientResponse
from baiducloud_python_sdk_cfs.models.query_mounting_target_response import QueryMountingTargetResponse
from baiducloud_python_sdk_cfs.models.query_permission_group_response import QueryPermissionGroupResponse
from baiducloud_python_sdk_cfs.models.query_permission_group_rules_response import QueryPermissionGroupRulesResponse

_logger = logging.getLogger(__name__)


class CfsClient(BceBaseClient):
    """
    cfs base sdk client
    """

    VERSION_V1 = b'/v1'

    CONSTANT_ACCESS_GROUP = b'accessGroup'

    CONSTANT_CFS = b'cfs'

    CONSTANT_BATCH_CREATE_ACCESS_RULE = b'batchCreateAccessRule'

    CONSTANT_CLIENTS = b'clients'

    def __init__(self, config=None):
        """
        Initialize the cfs client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def batch_creation_of_permission_group_rules(self, request, config=None):
        """
        batch_creation_of_permission_group_rules

        :param request: Request entity containing all parameters
        :type request: CfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BatchCreationOfPermissionGroupRulesResponse data
        :rtype: BatchCreationOfPermissionGroupRulesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            CfsClient.VERSION_V1, CfsClient.CONSTANT_ACCESS_GROUP, CfsClient.CONSTANT_BATCH_CREATE_ACCESS_RULE
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=BatchCreationOfPermissionGroupRulesResponse,
        )

    def create_file_system(self, request, config=None):
        """
        create_file_system

        :param request: Request entity containing all parameters
        :type request: CfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateFileSystemResponse data
        :rtype: CreateFileSystemResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CfsClient.VERSION_V1, CfsClient.CONSTANT_CFS)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateFileSystemResponse,
        )

    def create_mounting_target(self, request, config=None):
        """
        create_mounting_target

        :param request: Request entity containing all parameters
        :type request: CfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateMountingTargetResponse data
        :rtype: CreateMountingTargetResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CfsClient.VERSION_V1, CfsClient.CONSTANT_CFS, request.fs_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateMountingTargetResponse,
        )

    def create_permission_group(self, request, config=None):
        """
        create_permission_group

        :param request: Request entity containing all parameters
        :type request: CfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CfsClient.VERSION_V1, CfsClient.CONSTANT_ACCESS_GROUP)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def create_permission_group_rules(self, request, config=None):
        """
        create_permission_group_rules

        :param request: Request entity containing all parameters
        :type request: CfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreatePermissionGroupRulesResponse data
        :rtype: CreatePermissionGroupRulesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CfsClient.VERSION_V1, CfsClient.CONSTANT_ACCESS_GROUP, request.ag_name)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreatePermissionGroupRulesResponse,
        )

    def delete_permission_group(self, request, config=None):
        """
        delete_permission_group

        :param request: Request entity containing all parameters
        :type request: CfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CfsClient.VERSION_V1, CfsClient.CONSTANT_ACCESS_GROUP, request.ag_name)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def delete_permission_group_rule(self, request, config=None):
        """
        delete_permission_group_rule

        :param request: Request entity containing all parameters
        :type request: CfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CfsClient.VERSION_V1, CfsClient.CONSTANT_ACCESS_GROUP, request.ag_name, request.ar_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def drop_file_system(self, request, config=None):
        """
        drop_file_system

        :param request: Request entity containing all parameters
        :type request: CfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CfsClient.VERSION_V1, CfsClient.CONSTANT_CFS, request.fs_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def drop_mount_target(self, request, config=None):
        """
        drop_mount_target

        :param request: Request entity containing all parameters
        :type request: CfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CfsClient.VERSION_V1, CfsClient.CONSTANT_CFS, request.fs_id, request.mount_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def modify_the_mount_target_permission_group(self, request, config=None):
        """
        modify_the_mount_target_permission_group

        :param request: Request entity containing all parameters
        :type request: CfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CfsClient.VERSION_V1, CfsClient.CONSTANT_CFS, request.fs_id, request.mount_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def query_file_system(self, request, config=None):
        """
        query_file_system

        :param request: Request entity containing all parameters
        :type request: CfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryFileSystemResponse data
        :rtype: QueryFileSystemResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CfsClient.VERSION_V1, CfsClient.CONSTANT_CFS)
        headers = None
        params = {}
        if request.user_id is not None:
            params['userId'] = request.user_id
        if request.fs_id is not None:
            params['fsId'] = request.fs_id
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.filter_tag is not None:
            params['filterTag'] = request.filter_tag
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryFileSystemResponse
        )

    def query_mounted_client(self, request, config=None):
        """
        query_mounted_client

        :param request: Request entity containing all parameters
        :type request: CfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryMountedClientResponse data
        :rtype: QueryMountedClientResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CfsClient.VERSION_V1, CfsClient.CONSTANT_CFS, CfsClient.CONSTANT_CLIENTS)
        headers = None
        params = {}
        if request.fs_id is not None:
            params['fsId'] = request.fs_id
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryMountedClientResponse
        )

    def query_mounting_target(self, request, config=None):
        """
        query_mounting_target

        :param request: Request entity containing all parameters
        :type request: CfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryMountingTargetResponse data
        :rtype: QueryMountingTargetResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CfsClient.VERSION_V1, CfsClient.CONSTANT_CFS, request.f_id)
        headers = None
        params = {}
        params[''] = None
        if request.mount_id is not None:
            params['mountId'] = request.mount_id
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryMountingTargetResponse
        )

    def query_permission_group(self, request, config=None):
        """
        query_permission_group

        :param request: Request entity containing all parameters
        :type request: CfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryPermissionGroupResponse data
        :rtype: QueryPermissionGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CfsClient.VERSION_V1, CfsClient.CONSTANT_ACCESS_GROUP)
        headers = None
        params = {}
        if request.ag_name is not None:
            params['agName'] = request.ag_name
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryPermissionGroupResponse
        )

    def query_permission_group_rules(self, request, config=None):
        """
        query_permission_group_rules

        :param request: Request entity containing all parameters
        :type request: CfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryPermissionGroupRulesResponse data
        :rtype: QueryPermissionGroupRulesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CfsClient.VERSION_V1, CfsClient.CONSTANT_ACCESS_GROUP, request.ag_name)
        headers = None
        params = {}
        if request.ar_id is not None:
            params['arId'] = request.ar_id
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryPermissionGroupRulesResponse
        )

    def update_file_system(self, request, config=None):
        """
        update_file_system

        :param request: Request entity containing all parameters
        :type request: CfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CfsClient.VERSION_V1, CfsClient.CONSTANT_CFS, request.fs_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def update_file_system_labels(self, request, config=None):
        """
        update_file_system_labels

        :param request: Request entity containing all parameters
        :type request: CfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CfsClient.VERSION_V1, CfsClient.CONSTANT_CFS)
        headers = None
        params = {}
        params['tag'] = None
        if request.tag is not None:
            params['tag'] = request.tag
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_permission_group(self, request, config=None):
        """
        update_permission_group

        :param request: Request entity containing all parameters
        :type request: CfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CfsClient.VERSION_V1, CfsClient.CONSTANT_ACCESS_GROUP, request.ag_name)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def update_permission_group_rules(self, request, config=None):
        """
        update_permission_group_rules

        :param request: Request entity containing all parameters
        :type request: CfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(CfsClient.VERSION_V1, CfsClient.CONSTANT_ACCESS_GROUP, request.ag_name, request.ar_id)
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
