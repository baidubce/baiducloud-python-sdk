"""
Example for ax client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_core.util import request_body_utils
from baiducloud_python_sdk_ax.models.batch_release_sandboxes_response import BatchReleaseSandboxesResponse
from baiducloud_python_sdk_ax.models.connect_sandbox_response import ConnectSandboxResponse
from baiducloud_python_sdk_ax.models.create_sandbox_response import CreateSandboxResponse
from baiducloud_python_sdk_ax.models.create_sandbox_snapshot_response import CreateSandboxSnapshotResponse
from baiducloud_python_sdk_ax.models.fork_sandbox_response import ForkSandboxResponse
from baiducloud_python_sdk_ax.models.get_sandbox_response import GetSandboxResponse
from baiducloud_python_sdk_ax.models.get_sandbox_resources_response import GetSandboxResourcesResponse
from baiducloud_python_sdk_ax.models.get_sandbox_snapshot_response import GetSandboxSnapshotResponse
from baiducloud_python_sdk_ax.models.list_sandbox_snapshots_response import ListSandboxSnapshotsResponse
from baiducloud_python_sdk_ax.models.list_sandboxes_response import ListSandboxesResponse
from baiducloud_python_sdk_ax.models.list_sandboxes_v2_response import ListSandboxesV2Response
from baiducloud_python_sdk_ax.models.list_sandboxes_v2_by_path_response import ListSandboxesV2ByPathResponse
from baiducloud_python_sdk_ax.models.query_sandboxes_response import QuerySandboxesResponse
from baiducloud_python_sdk_ax.models.resume_sandbox_response import ResumeSandboxResponse

_logger = logging.getLogger(__name__)


class AxClient(BceBaseClient):
    """
    ax base sdk client
    """

    CONSTANT_SANDBOXES = b'sandboxes'

    CONSTANT_RESOURCES = b'resources'

    CONSTANT_TIMEOUT = b'timeout'

    CONSTANT_V2 = b'v2'

    CONSTANT_RESUME = b'resume'

    CONSTANT_SNAPSHOTS = b'snapshots'

    CONSTANT_BATCH_RELEASE = b'batchRelease'

    CONSTANT_CONNECT = b'connect'

    CONSTANT_FORK = b'fork'

    CONSTANT_QUERY = b'query'

    CONSTANT_PAUSE = b'pause'

    def __init__(self, config=None):
        """
        Initialize the ax client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def batch_release_sandboxes(self, request, config=None):
        """
        batch_release_sandboxes

        :param request: Request entity containing all parameters
        :type request: AxClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BatchReleaseSandboxesResponse data
        :rtype: BatchReleaseSandboxesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AxClient.CONSTANT_SANDBOXES, AxClient.CONSTANT_BATCH_RELEASE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=BatchReleaseSandboxesResponse,
        )

    def connect_sandbox(self, request, config=None):
        """
        connect_sandbox

        :param request: Request entity containing all parameters
        :type request: AxClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ConnectSandboxResponse data
        :rtype: ConnectSandboxResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AxClient.CONSTANT_SANDBOXES, request.sandbox_id, AxClient.CONSTANT_CONNECT)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=ConnectSandboxResponse,
        )

    def create_sandbox(self, request, config=None):
        """
        create_sandbox

        :param request: Request entity containing all parameters
        :type request: AxClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateSandboxResponse data
        :rtype: CreateSandboxResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AxClient.CONSTANT_SANDBOXES)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateSandboxResponse,
        )

    def create_sandbox_snapshot(self, request, config=None):
        """
        create_sandbox_snapshot

        :param request: Request entity containing all parameters
        :type request: AxClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateSandboxSnapshotResponse data
        :rtype: CreateSandboxSnapshotResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AxClient.CONSTANT_SANDBOXES, request.sandbox_id, AxClient.CONSTANT_SNAPSHOTS)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateSandboxSnapshotResponse,
        )

    def delete_sandbox(self, request, config=None):
        """
        delete_sandbox

        :param request: Request entity containing all parameters
        :type request: AxClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AxClient.CONSTANT_SANDBOXES, request.sandbox_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def fork_sandbox(self, request, config=None):
        """
        fork_sandbox

        :param request: Request entity containing all parameters
        :type request: AxClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ForkSandboxResponse data
        :rtype: ForkSandboxResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AxClient.CONSTANT_SANDBOXES, request.sandbox_id, AxClient.CONSTANT_FORK)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, config=merged_config, model=ForkSandboxResponse)

    def get_sandbox(self, request, config=None):
        """
        get_sandbox

        :param request: Request entity containing all parameters
        :type request: AxClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetSandboxResponse data
        :rtype: GetSandboxResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AxClient.CONSTANT_SANDBOXES, request.sandbox_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetSandboxResponse)

    def get_sandbox_resources(self, request, config=None):
        """
        get_sandbox_resources

        :param request: Request entity containing all parameters
        :type request: AxClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetSandboxResourcesResponse data
        :rtype: GetSandboxResourcesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AxClient.CONSTANT_SANDBOXES, request.sandbox_id, AxClient.CONSTANT_RESOURCES)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetSandboxResourcesResponse)

    def get_sandbox_snapshot(self, request, config=None):
        """
        get_sandbox_snapshot

        :param request: Request entity containing all parameters
        :type request: AxClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetSandboxSnapshotResponse data
        :rtype: GetSandboxSnapshotResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/', AxClient.CONSTANT_SANDBOXES, request.sandbox_id, AxClient.CONSTANT_SNAPSHOTS, request.snapshot_id
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetSandboxSnapshotResponse)

    def list_sandbox_snapshots(self, request, config=None):
        """
        list_sandbox_snapshots

        :param request: Request entity containing all parameters
        :type request: AxClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListSandboxSnapshotsResponse data
        :rtype: ListSandboxSnapshotsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AxClient.CONSTANT_SANDBOXES, request.sandbox_id, AxClient.CONSTANT_SNAPSHOTS)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=ListSandboxSnapshotsResponse
        )

    def list_sandboxes(self, request, config=None):
        """
        list_sandboxes

        :param request: Request entity containing all parameters
        :type request: AxClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListSandboxesResponse data
        :rtype: ListSandboxesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AxClient.CONSTANT_SANDBOXES)
        headers = None
        params = {}
        if request.metadata is not None:
            params['metadata'] = request.metadata
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListSandboxesResponse
        )

    def list_sandboxes_v2(self, request, config=None):
        """
        list_sandboxes_v2

        :param request: Request entity containing all parameters
        :type request: AxClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListSandboxesV2Response data
        :rtype: ListSandboxesV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AxClient.CONSTANT_V2, AxClient.CONSTANT_SANDBOXES)
        headers = None
        params = {}
        if request.limit is not None:
            params['limit'] = request.limit
        if request.next_token is not None:
            params['nextToken'] = request.next_token
        if request.metadata is not None:
            params['metadata'] = request.metadata
        if request.state is not None:
            params['state'] = request.state
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListSandboxesV2Response
        )

    def list_sandboxes_v2_by_path(self, request, config=None):
        """
        list_sandboxes_v2_by_path

        :param request: Request entity containing all parameters
        :type request: AxClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListSandboxesV2ByPathResponse data
        :rtype: ListSandboxesV2ByPathResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AxClient.CONSTANT_SANDBOXES, AxClient.CONSTANT_V2)
        headers = None
        params = {}
        if request.limit is not None:
            params['limit'] = request.limit
        if request.next_token is not None:
            params['nextToken'] = request.next_token
        if request.metadata is not None:
            params['metadata'] = request.metadata
        if request.state is not None:
            params['state'] = request.state
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListSandboxesV2ByPathResponse
        )

    def pause_sandbox(self, request, config=None):
        """
        pause_sandbox

        :param request: Request entity containing all parameters
        :type request: AxClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AxClient.CONSTANT_SANDBOXES, request.sandbox_id, AxClient.CONSTANT_PAUSE)
        headers = None
        params = {}
        if request.hibernate_mode is not None:
            params['hibernateMode'] = request.hibernate_mode
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, params=params, config=merged_config)

    def query_sandboxes(self, request, config=None):
        """
        query_sandboxes

        :param request: Request entity containing all parameters
        :type request: AxClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QuerySandboxesResponse data
        :rtype: QuerySandboxesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AxClient.CONSTANT_SANDBOXES, AxClient.CONSTANT_QUERY)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=QuerySandboxesResponse,
        )

    def resume_sandbox(self, request, config=None):
        """
        resume_sandbox

        :param request: Request entity containing all parameters
        :type request: AxClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ResumeSandboxResponse data
        :rtype: ResumeSandboxResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AxClient.CONSTANT_SANDBOXES, request.sandbox_id, AxClient.CONSTANT_RESUME)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=ResumeSandboxResponse,
        )

    def set_sandbox_timeout(self, request, config=None):
        """
        set_sandbox_timeout

        :param request: Request entity containing all parameters
        :type request: AxClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', AxClient.CONSTANT_SANDBOXES, request.sandbox_id, AxClient.CONSTANT_TIMEOUT)
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
        sign_fn, params = self._choose_signer(config, params)
        return bce_http_client.send_request(
            config, sign_fn, [handler.parse_error, body_parser], http_method, path, body, headers, params, model=model
        )
