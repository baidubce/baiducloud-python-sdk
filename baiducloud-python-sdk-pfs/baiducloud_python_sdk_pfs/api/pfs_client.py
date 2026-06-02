"""
Example for pfs client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.auth import bce_v1_signer
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_pfs.models.create_fileset_response import CreateFilesetResponse
from baiducloud_python_sdk_pfs.models.create_pfs_response import CreatePfsResponse
from baiducloud_python_sdk_pfs.models.delete_fileset_response import DeleteFilesetResponse
from baiducloud_python_sdk_pfs.models.desc_fileset_response import DescFilesetResponse
from baiducloud_python_sdk_pfs.models.desc_pfs_response import DescPfsResponse
from baiducloud_python_sdk_pfs.models.instance_list_clients_response import InstanceListClientsResponse
from baiducloud_python_sdk_pfs.models.list_fileset_response import ListFilesetResponse
from baiducloud_python_sdk_pfs.models.list_pfs_response import ListPfsResponse
from baiducloud_python_sdk_pfs.models.mount_target_list_clients_response import MountTargetListClientsResponse
from baiducloud_python_sdk_pfs.models.update_fileset_response import UpdateFilesetResponse

_logger = logging.getLogger(__name__)


class PfsClient(BceBaseClient):
    """
    pfs base sdk client
    """

    CONSTANT_V1 = b'v1'

    CONSTANT_PFS = b'pfs'

    CONSTANT_INSTANCE = b'instance'

    CONSTANT_TAG = b'tag'

    def __init__(self, config=None):
        """
        Initialize the pfs client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def create_fileset(self, request, config=None):
        """
        create_fileset

        :param request: Request entity containing all parameters
        :type request: PfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateFilesetResponse data
        :rtype: CreateFilesetResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = {}
        headers[b'Version'] = b'v2'
        params = {}
        params['action'] = 'CreateFileset'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            headers=headers,
            params=params,
            config=merged_config,
            model=CreateFilesetResponse,
        )

    def create_pfs(self, request, config=None):
        """
        create_pfs

        :param request: Request entity containing all parameters
        :type request: PfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreatePfsResponse data
        :rtype: CreatePfsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', PfsClient.CONSTANT_V1, PfsClient.CONSTANT_PFS, PfsClient.CONSTANT_INSTANCE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), config=merged_config, model=CreatePfsResponse
        )

    def delete_fileset(self, request, config=None):
        """
        delete_fileset

        :param request: Request entity containing all parameters
        :type request: PfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DeleteFilesetResponse data
        :rtype: DeleteFilesetResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = {}
        headers[b'Version'] = b'v2'
        params = {}
        params['action'] = 'DeleteFileset'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            headers=headers,
            params=params,
            config=merged_config,
            model=DeleteFilesetResponse,
        )

    def delete_pfs(self, request, config=None):
        """
        delete_pfs

        :param request: Request entity containing all parameters
        :type request: PfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', PfsClient.CONSTANT_V1, PfsClient.CONSTANT_PFS, PfsClient.CONSTANT_INSTANCE)
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def desc_fileset(self, request, config=None):
        """
        desc_fileset

        :param request: Request entity containing all parameters
        :type request: PfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescFilesetResponse data
        :rtype: DescFilesetResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = {}
        headers[b'Version'] = b'v2'
        params = {}
        params['action'] = 'DescribeFileset'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            headers=headers,
            params=params,
            config=merged_config,
            model=DescFilesetResponse,
        )

    def desc_pfs(self, request, config=None):
        """
        desc_pfs

        :param request: Request entity containing all parameters
        :type request: PfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescPfsResponse data
        :rtype: DescPfsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', PfsClient.CONSTANT_V1, PfsClient.CONSTANT_PFS, PfsClient.CONSTANT_INSTANCE)
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=DescPfsResponse
        )

    def instance_list_clients(self, request, config=None):
        """
        instance_list_clients

        :param request: Request entity containing all parameters
        :type request: PfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing InstanceListClientsResponse data
        :rtype: InstanceListClientsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = {}
        headers[b'Version'] = b'v2'
        params = {}
        params['action'] = 'InstanceListClients'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            headers=headers,
            params=params,
            config=merged_config,
            model=InstanceListClientsResponse,
        )

    def list_fileset(self, request, config=None):
        """
        list_fileset

        :param request: Request entity containing all parameters
        :type request: PfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListFilesetResponse data
        :rtype: ListFilesetResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = {}
        headers[b'Version'] = b'v2'
        params = {}
        params['action'] = 'ListFileset'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            headers=headers,
            params=params,
            config=merged_config,
            model=ListFilesetResponse,
        )

    def list_pfs(self, request, config=None):
        """
        list_pfs

        :param request: Request entity containing all parameters
        :type request: PfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListPfsResponse data
        :rtype: ListPfsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', PfsClient.CONSTANT_V1, PfsClient.CONSTANT_PFS, PfsClient.CONSTANT_INSTANCE)
        headers = None
        params = {}
        params['manner'] = 'marker'
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.marker is not None:
            params['marker'] = request.marker
        if request.filter_tag is not None:
            params['filterTag'] = request.filter_tag
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListPfsResponse
        )

    def mount_target_list_clients(self, request, config=None):
        """
        mount_target_list_clients

        :param request: Request entity containing all parameters
        :type request: PfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing MountTargetListClientsResponse data
        :rtype: MountTargetListClientsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = {}
        headers[b'Version'] = b'v2'
        params = {}
        params['action'] = 'MountTargetListClients'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            headers=headers,
            params=params,
            config=merged_config,
            model=MountTargetListClientsResponse,
        )

    def update_fileset(self, request, config=None):
        """
        update_fileset

        :param request: Request entity containing all parameters
        :type request: PfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UpdateFilesetResponse data
        :rtype: UpdateFilesetResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = {}
        headers[b'Version'] = b'v2'
        params = {}
        params['action'] = 'UpdateFileset'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            headers=headers,
            params=params,
            config=merged_config,
            model=UpdateFilesetResponse,
        )

    def update_pfs_tag(self, request, config=None):
        """
        update_pfs_tag

        :param request: Request entity containing all parameters
        :type request: PfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', PfsClient.CONSTANT_V1, PfsClient.CONSTANT_PFS, PfsClient.CONSTANT_TAG)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

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
