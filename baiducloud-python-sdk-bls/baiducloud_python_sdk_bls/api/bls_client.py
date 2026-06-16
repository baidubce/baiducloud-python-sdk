"""
Example for bls client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.auth import bce_v1_signer
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_bls.models.create_download_task_response import CreateDownloadTaskResponse
from baiducloud_python_sdk_bls.models.create_project_response import CreateProjectResponse
from baiducloud_python_sdk_bls.models.delete_download_task_response import DeleteDownloadTaskResponse
from baiducloud_python_sdk_bls.models.delete_project_response import DeleteProjectResponse
from baiducloud_python_sdk_bls.models.describe_download_task_response import DescribeDownloadTaskResponse
from baiducloud_python_sdk_bls.models.describe_project_response import DescribeProjectResponse
from baiducloud_python_sdk_bls.models.get_download_task_link_response import GetDownloadTaskLinkResponse
from baiducloud_python_sdk_bls.models.list_download_task_response import ListDownloadTaskResponse
from baiducloud_python_sdk_bls.models.list_project_response import ListProjectResponse
from baiducloud_python_sdk_bls.models.pull_log_record_response import PullLogRecordResponse
from baiducloud_python_sdk_bls.models.push_log_record_response import PushLogRecordResponse
from baiducloud_python_sdk_bls.models.query_log_histogram_response import QueryLogHistogramResponse
from baiducloud_python_sdk_bls.models.query_log_record_response import QueryLogRecordResponse
from baiducloud_python_sdk_bls.models.update_project_response import UpdateProjectResponse

_logger = logging.getLogger(__name__)


class BlsClient(BceBaseClient):
    """
    bls base sdk client
    """

    VERSION_V1 = b'/v1'

    VERSION_V2 = b'/v2'

    CONSTANT_PROJECT = b'project'

    CONSTANT_LOGSTORE = b'logstore'

    CONSTANT_LOGRECORD = b'logrecord'

    CONSTANT_DOWNLOAD = b'download'

    CONSTANT_LIST = b'list'

    CONSTANT_LOGHISTOGRAM = b'loghistogram'

    CONSTANT_LINK = b'link'

    def __init__(self, config=None):
        """
        Initialize the bls client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def create_download_task(self, request, config=None):
        """
        create_download_task

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateDownloadTaskResponse data
        :rtype: CreateDownloadTaskResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V2, BlsClient.CONSTANT_LOGSTORE, BlsClient.CONSTANT_DOWNLOAD)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateDownloadTaskResponse,
        )

    def create_project(self, request, config=None):
        """
        create_project

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateProjectResponse data
        :rtype: CreateProjectResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V1, BlsClient.CONSTANT_PROJECT)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateProjectResponse,
        )

    def delete_download_task(self, request, config=None):
        """
        delete_download_task

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DeleteDownloadTaskResponse data
        :rtype: DeleteDownloadTaskResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlsClient.VERSION_V2, BlsClient.CONSTANT_LOGSTORE, BlsClient.CONSTANT_DOWNLOAD, request.uuid
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.DELETE, path=path, config=merged_config, model=DeleteDownloadTaskResponse
        )

    def delete_project(self, request, config=None):
        """
        delete_project

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DeleteProjectResponse data
        :rtype: DeleteProjectResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V1, BlsClient.CONSTANT_PROJECT, request.uuid)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config, model=DeleteProjectResponse)

    def describe_download_task(self, request, config=None):
        """
        describe_download_task

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeDownloadTaskResponse data
        :rtype: DescribeDownloadTaskResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlsClient.VERSION_V2, BlsClient.CONSTANT_LOGSTORE, BlsClient.CONSTANT_DOWNLOAD, request.uuid
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=DescribeDownloadTaskResponse
        )

    def describe_project(self, request, config=None):
        """
        describe_project

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeProjectResponse data
        :rtype: DescribeProjectResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V1, BlsClient.CONSTANT_PROJECT, request.uuid)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=DescribeProjectResponse)

    def get_download_task_link(self, request, config=None):
        """
        get_download_task_link

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetDownloadTaskLinkResponse data
        :rtype: GetDownloadTaskLinkResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlsClient.VERSION_V2,
            BlsClient.CONSTANT_LOGSTORE,
            BlsClient.CONSTANT_DOWNLOAD,
            BlsClient.CONSTANT_LINK,
            request.uuid,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetDownloadTaskLinkResponse)

    def list_download_task(self, request, config=None):
        """
        list_download_task

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListDownloadTaskResponse data
        :rtype: ListDownloadTaskResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlsClient.VERSION_V2, BlsClient.CONSTANT_LOGSTORE, BlsClient.CONSTANT_DOWNLOAD, BlsClient.CONSTANT_LIST
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=ListDownloadTaskResponse,
        )

    def list_project(self, request, config=None):
        """
        list_project

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListProjectResponse data
        :rtype: ListProjectResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V1, BlsClient.CONSTANT_PROJECT, BlsClient.CONSTANT_LIST)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=ListProjectResponse,
        )

    def pull_log_record(self, request, config=None):
        """
        pull_log_record

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing PullLogRecordResponse data
        :rtype: PullLogRecordResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlsClient.VERSION_V1, BlsClient.CONSTANT_LOGSTORE, request.log_store_name, BlsClient.CONSTANT_LOGRECORD
        )
        headers = None
        params = {}
        if request.log_stream_name is not None:
            params['logStreamName'] = request.log_stream_name
        if request.start_date_time is not None:
            params['startDateTime'] = request.start_date_time
        if request.end_date_time is not None:
            params['endDateTime'] = request.end_date_time
        if request.project is not None:
            params['project'] = request.project
        if request.limit is not None:
            params['limit'] = request.limit
        if request.marker is not None:
            params['marker'] = request.marker
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=PullLogRecordResponse
        )

    def push_log_record(self, request, config=None):
        """
        push_log_record

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing PushLogRecordResponse data
        :rtype: PushLogRecordResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlsClient.VERSION_V1, BlsClient.CONSTANT_LOGSTORE, request.log_store_name, BlsClient.CONSTANT_LOGRECORD
        )
        headers = None
        params = {}
        if request.project is not None:
            params['project'] = request.project
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=PushLogRecordResponse,
        )

    def query_log_histogram(self, request, config=None):
        """
        query_log_histogram

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryLogHistogramResponse data
        :rtype: QueryLogHistogramResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlsClient.VERSION_V2, BlsClient.CONSTANT_LOGSTORE, request.log_store_name, BlsClient.CONSTANT_LOGHISTOGRAM
        )
        headers = None
        params = {}
        if request.query is not None:
            params['query'] = request.query
        if request.start_date_time is not None:
            params['startDateTime'] = request.start_date_time
        if request.end_date_time is not None:
            params['endDateTime'] = request.end_date_time
        if request.project is not None:
            params['project'] = request.project
        if request.log_stream_name is not None:
            params['logStreamName'] = request.log_stream_name
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryLogHistogramResponse
        )

    def query_log_record(self, request, config=None):
        """
        query_log_record

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryLogRecordResponse data
        :rtype: QueryLogRecordResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlsClient.VERSION_V1, BlsClient.CONSTANT_LOGSTORE, request.log_store_name, BlsClient.CONSTANT_LOGRECORD
        )
        headers = None
        params = {}
        if request.query is not None:
            params['query'] = request.query
        if request.start_date_time is not None:
            params['startDateTime'] = request.start_date_time
        if request.end_date_time is not None:
            params['endDateTime'] = request.end_date_time
        if request.project is not None:
            params['project'] = request.project
        if request.log_stream_name is not None:
            params['logStreamName'] = request.log_stream_name
        if request.marker is not None:
            params['marker'] = request.marker
        if request.limit is not None:
            params['limit'] = request.limit
        if request.sort is not None:
            params['sort'] = request.sort
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryLogRecordResponse
        )

    def update_project(self, request, config=None):
        """
        update_project

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UpdateProjectResponse data
        :rtype: UpdateProjectResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V1, BlsClient.CONSTANT_PROJECT)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=UpdateProjectResponse,
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
