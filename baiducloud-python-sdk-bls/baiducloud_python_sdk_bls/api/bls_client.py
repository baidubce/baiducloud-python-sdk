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
from baiducloud_python_sdk_bls.models.async_search_response import AsyncSearchResponse
from baiducloud_python_sdk_bls.models.batch_get_log_store_response import BatchGetLogStoreResponse
from baiducloud_python_sdk_bls.models.bulk_delete_log_shipper_response import BulkDeleteLogShipperResponse
from baiducloud_python_sdk_bls.models.bulk_set_log_shipper_status_response import BulkSetLogShipperStatusResponse
from baiducloud_python_sdk_bls.models.create_alarm_policy_response import CreateAlarmPolicyResponse
from baiducloud_python_sdk_bls.models.create_download_task_response import CreateDownloadTaskResponse
from baiducloud_python_sdk_bls.models.create_fast_query_response import CreateFastQueryResponse
from baiducloud_python_sdk_bls.models.create_index_response import CreateIndexResponse
from baiducloud_python_sdk_bls.models.create_log_shipper_response import CreateLogShipperResponse
from baiducloud_python_sdk_bls.models.create_log_store_response import CreateLogStoreResponse
from baiducloud_python_sdk_bls.models.create_log_store_template_response import CreateLogStoreTemplateResponse
from baiducloud_python_sdk_bls.models.create_project_response import CreateProjectResponse
from baiducloud_python_sdk_bls.models.create_task_response import CreateTaskResponse
from baiducloud_python_sdk_bls.models.delete_alarm_policy_response import DeleteAlarmPolicyResponse
from baiducloud_python_sdk_bls.models.delete_download_task_response import DeleteDownloadTaskResponse
from baiducloud_python_sdk_bls.models.delete_fast_query_response import DeleteFastQueryResponse
from baiducloud_python_sdk_bls.models.delete_index_response import DeleteIndexResponse
from baiducloud_python_sdk_bls.models.delete_log_store_response import DeleteLogStoreResponse
from baiducloud_python_sdk_bls.models.delete_log_store_templates_response import DeleteLogStoreTemplatesResponse
from baiducloud_python_sdk_bls.models.delete_log_store_view_response import DeleteLogStoreViewResponse
from baiducloud_python_sdk_bls.models.delete_project_response import DeleteProjectResponse
from baiducloud_python_sdk_bls.models.delete_single_log_shipper_response import DeleteSingleLogShipperResponse
from baiducloud_python_sdk_bls.models.describe_alarm_policy_response import DescribeAlarmPolicyResponse
from baiducloud_python_sdk_bls.models.describe_alarm_record_response import DescribeAlarmRecordResponse
from baiducloud_python_sdk_bls.models.describe_download_task_response import DescribeDownloadTaskResponse
from baiducloud_python_sdk_bls.models.describe_fast_query_response import DescribeFastQueryResponse
from baiducloud_python_sdk_bls.models.describe_index_response import DescribeIndexResponse
from baiducloud_python_sdk_bls.models.describe_log_store_response import DescribeLogStoreResponse
from baiducloud_python_sdk_bls.models.describe_log_store_template_response import DescribeLogStoreTemplateResponse
from baiducloud_python_sdk_bls.models.describe_log_store_templates_response import DescribeLogStoreTemplatesResponse
from baiducloud_python_sdk_bls.models.describe_log_store_view_response import DescribeLogStoreViewResponse
from baiducloud_python_sdk_bls.models.describe_project_response import DescribeProjectResponse
from baiducloud_python_sdk_bls.models.disable_alarm_policy_response import DisableAlarmPolicyResponse
from baiducloud_python_sdk_bls.models.enable_alarm_policy_response import EnableAlarmPolicyResponse
from baiducloud_python_sdk_bls.models.field_caps_response import FieldCapsResponse
from baiducloud_python_sdk_bls.models.get_download_task_link_response import GetDownloadTaskLinkResponse
from baiducloud_python_sdk_bls.models.get_log_shipper_response import GetLogShipperResponse
from baiducloud_python_sdk_bls.models.list_alarm_execution_stats_response import ListAlarmExecutionStatsResponse
from baiducloud_python_sdk_bls.models.list_alarm_executions_response import ListAlarmExecutionsResponse
from baiducloud_python_sdk_bls.models.list_alarm_policy_response import ListAlarmPolicyResponse
from baiducloud_python_sdk_bls.models.list_alarm_record_response import ListAlarmRecordResponse
from baiducloud_python_sdk_bls.models.list_download_task_response import ListDownloadTaskResponse
from baiducloud_python_sdk_bls.models.list_fast_query_response import ListFastQueryResponse
from baiducloud_python_sdk_bls.models.list_log_shipper_response import ListLogShipperResponse
from baiducloud_python_sdk_bls.models.list_log_shipper_record_response import ListLogShipperRecordResponse
from baiducloud_python_sdk_bls.models.list_log_store_response import ListLogStoreResponse
from baiducloud_python_sdk_bls.models.list_log_store_view_response import ListLogStoreViewResponse
from baiducloud_python_sdk_bls.models.list_log_stream_response import ListLogStreamResponse
from baiducloud_python_sdk_bls.models.list_project_response import ListProjectResponse
from baiducloud_python_sdk_bls.models.pull_log_record_response import PullLogRecordResponse
from baiducloud_python_sdk_bls.models.push_log_record_response import PushLogRecordResponse
from baiducloud_python_sdk_bls.models.query_log_histogram_response import QueryLogHistogramResponse
from baiducloud_python_sdk_bls.models.query_log_record_response import QueryLogRecordResponse
from baiducloud_python_sdk_bls.models.resolve_index_response import ResolveIndexResponse
from baiducloud_python_sdk_bls.models.set_single_log_shipper_status_response import SetSingleLogShipperStatusResponse
from baiducloud_python_sdk_bls.models.terms_enum_response import TermsEnumResponse
from baiducloud_python_sdk_bls.models.update_alarm_policy_response import UpdateAlarmPolicyResponse
from baiducloud_python_sdk_bls.models.update_fast_query_response import UpdateFastQueryResponse
from baiducloud_python_sdk_bls.models.update_index_response import UpdateIndexResponse
from baiducloud_python_sdk_bls.models.update_log_shipper_response import UpdateLogShipperResponse
from baiducloud_python_sdk_bls.models.update_log_store_response import UpdateLogStoreResponse
from baiducloud_python_sdk_bls.models.update_log_store_template_response import UpdateLogStoreTemplateResponse
from baiducloud_python_sdk_bls.models.update_project_response import UpdateProjectResponse
from baiducloud_python_sdk_bls.models.validate_alarm_condition_response import ValidateAlarmConditionResponse
from baiducloud_python_sdk_bls.models.validate_alarm_policy_sql_response import ValidateAlarmPolicySQLResponse

_logger = logging.getLogger(__name__)


class BlsClient(BceBaseClient):
    """
    bls base sdk client
    """

    VERSION_V1 = b'/v1'

    VERSION_V2 = b'/v2'

    VERSION_V3 = b'/v3'

    CONSTANT_ALARM = b'alarm'

    CONSTANT_RECORD = b'record'

    CONSTANT_LOGSTORE = b'logstore'

    CONSTANT_DOWNLOAD = b'download'

    CONSTANT_LIST = b'list'

    CONSTANT_BLS = b'bls'

    CONSTANT_LOGSHIPPER = b'logshipper'

    CONSTANT_PROJECT = b'project'

    CONSTANT_INDEX = b'index'

    CONSTANT_EXECUTION = b'execution'

    CONSTANT_LOGSTREAM = b'logstream'

    CONSTANT_STATUS = b'status'

    CONSTANT_BATCH = b'batch'

    CONSTANT_POLICY = b'policy'

    CONSTANT_FIELD_CAPS = b'_field_caps'

    CONSTANT_FASTQUERY = b'fastquery'

    CONSTANT_TASK = b'task'

    CONSTANT_LOGHISTOGRAM = b'loghistogram'

    CONSTANT_LOGRECORD = b'logrecord'

    CONSTANT_STATS = b'stats'

    CONSTANT_ENABLE = b'enable'

    CONSTANT_LINK = b'link'

    CONSTANT_CONDITION = b'condition'

    CONSTANT_VALIDATE = b'validate'

    CONSTANT_ASYNC_SEARCH = b'_async_search'

    CONSTANT_DISABLE = b'disable'

    CONSTANT_RESOLVE = b'_resolve'

    CONSTANT_TERMS_ENUM = b'_terms_enum'

    def __init__(self, config=None):
        """
        Initialize the bls client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def async_search(self, request, config=None):
        """
        async_search

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing AsyncSearchResponse data
        :rtype: AsyncSearchResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', request.name, BlsClient.CONSTANT_ASYNC_SEARCH)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=AsyncSearchResponse,
        )

    def batch_get_log_store(self, request, config=None):
        """
        batch_get_log_store

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BatchGetLogStoreResponse data
        :rtype: BatchGetLogStoreResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V1, BlsClient.CONSTANT_LOGSTORE, BlsClient.CONSTANT_BATCH)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=BatchGetLogStoreResponse,
        )

    def bulk_delete_log_shipper(self, request, config=None):
        """
        bulk_delete_log_shipper

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BulkDeleteLogShipperResponse data
        :rtype: BulkDeleteLogShipperResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V1, BlsClient.CONSTANT_LOGSHIPPER)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.DELETE,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=BulkDeleteLogShipperResponse,
        )

    def bulk_set_log_shipper_status(self, request, config=None):
        """
        bulk_set_log_shipper_status

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BulkSetLogShipperStatusResponse data
        :rtype: BulkSetLogShipperStatusResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlsClient.VERSION_V1, BlsClient.CONSTANT_LOGSHIPPER, BlsClient.CONSTANT_STATUS, BlsClient.CONSTANT_BATCH
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=BulkSetLogShipperStatusResponse,
        )

    def create_alarm_policy(self, request, config=None):
        """
        create_alarm_policy

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateAlarmPolicyResponse data
        :rtype: CreateAlarmPolicyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V1, BlsClient.CONSTANT_ALARM, BlsClient.CONSTANT_POLICY)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateAlarmPolicyResponse,
        )

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

    def create_fast_query(self, request, config=None):
        """
        create_fast_query

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateFastQueryResponse data
        :rtype: CreateFastQueryResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V1, BlsClient.CONSTANT_FASTQUERY)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateFastQueryResponse,
        )

    def create_index(self, request, config=None):
        """
        create_index

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateIndexResponse data
        :rtype: CreateIndexResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlsClient.VERSION_V1, BlsClient.CONSTANT_LOGSTORE, request.log_store_name, BlsClient.CONSTANT_INDEX
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
            model=CreateIndexResponse,
        )

    def create_log_shipper(self, request, config=None):
        """
        create_log_shipper

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateLogShipperResponse data
        :rtype: CreateLogShipperResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V1, BlsClient.CONSTANT_LOGSHIPPER)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateLogShipperResponse,
        )

    def create_log_store(self, request, config=None):
        """
        create_log_store

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateLogStoreResponse data
        :rtype: CreateLogStoreResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V1, BlsClient.CONSTANT_LOGSTORE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateLogStoreResponse,
        )

    def create_log_store_template(self, request, config=None):
        """
        create_log_store_template

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateLogStoreTemplateResponse data
        :rtype: CreateLogStoreTemplateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V3, BlsClient.CONSTANT_BLS)
        headers = None
        params = {}
        params['action'] = 'CreateLogStoreTemplate'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateLogStoreTemplateResponse,
        )

    def create_log_store_view(self, request, config=None):
        """
        create_log_store_view

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V3, BlsClient.CONSTANT_BLS)
        headers = None
        params = {}
        params['action'] = 'CreateLogStoreView'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
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

    def create_task(self, request, config=None):
        """
        create_task

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateTaskResponse data
        :rtype: CreateTaskResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BlsClient.CONSTANT_TASK)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), config=merged_config, model=CreateTaskResponse
        )

    def delete_alarm_policy(self, request, config=None):
        """
        delete_alarm_policy

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DeleteAlarmPolicyResponse data
        :rtype: DeleteAlarmPolicyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V1, BlsClient.CONSTANT_ALARM, BlsClient.CONSTANT_POLICY)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.DELETE,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=DeleteAlarmPolicyResponse,
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

    def delete_fast_query(self, request, config=None):
        """
        delete_fast_query

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DeleteFastQueryResponse data
        :rtype: DeleteFastQueryResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V1, BlsClient.CONSTANT_FASTQUERY, request.fast_query_name)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config, model=DeleteFastQueryResponse)

    def delete_index(self, request, config=None):
        """
        delete_index

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DeleteIndexResponse data
        :rtype: DeleteIndexResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlsClient.VERSION_V1, BlsClient.CONSTANT_LOGSTORE, request.log_store_name, BlsClient.CONSTANT_INDEX
        )
        headers = None
        params = {}
        if request.project is not None:
            params['project'] = request.project
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.DELETE, path=path, params=params, config=merged_config, model=DeleteIndexResponse
        )

    def delete_log_store(self, request, config=None):
        """
        delete_log_store

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DeleteLogStoreResponse data
        :rtype: DeleteLogStoreResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V1, BlsClient.CONSTANT_LOGSTORE, request.log_store_name)
        headers = None
        params = {}
        if request.project is not None:
            params['project'] = request.project
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.DELETE, path=path, params=params, config=merged_config, model=DeleteLogStoreResponse
        )

    def delete_log_store_templates(self, request, config=None):
        """
        delete_log_store_templates

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DeleteLogStoreTemplatesResponse data
        :rtype: DeleteLogStoreTemplatesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V3, BlsClient.CONSTANT_BLS)
        headers = None
        params = {}
        params['action'] = 'DeleteLogStoreTemplates'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DeleteLogStoreTemplatesResponse,
        )

    def delete_log_store_view(self, request, config=None):
        """
        delete_log_store_view

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DeleteLogStoreViewResponse data
        :rtype: DeleteLogStoreViewResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V3, BlsClient.CONSTANT_BLS)
        headers = None
        params = {}
        params['action'] = 'DeleteLogStoreView'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DeleteLogStoreViewResponse,
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

    def delete_single_log_shipper(self, request, config=None):
        """
        delete_single_log_shipper

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DeleteSingleLogShipperResponse data
        :rtype: DeleteSingleLogShipperResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V1, BlsClient.CONSTANT_LOGSHIPPER, request.log_shipper_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.DELETE, path=path, config=merged_config, model=DeleteSingleLogShipperResponse
        )

    def describe_alarm_policy(self, request, config=None):
        """
        describe_alarm_policy

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeAlarmPolicyResponse data
        :rtype: DescribeAlarmPolicyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V1, BlsClient.CONSTANT_ALARM, BlsClient.CONSTANT_POLICY)
        headers = None
        params = {}
        if request.policy_name is not None:
            params['PolicyName'] = request.policy_name
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=DescribeAlarmPolicyResponse
        )

    def describe_alarm_record(self, request, config=None):
        """
        describe_alarm_record

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeAlarmRecordResponse data
        :rtype: DescribeAlarmRecordResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V1, BlsClient.CONSTANT_ALARM, BlsClient.CONSTANT_RECORD)
        headers = None
        params = {}
        if request.alarm_id is not None:
            params['alarmId'] = request.alarm_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=DescribeAlarmRecordResponse
        )

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

    def describe_fast_query(self, request, config=None):
        """
        describe_fast_query

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeFastQueryResponse data
        :rtype: DescribeFastQueryResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V1, BlsClient.CONSTANT_FASTQUERY, request.fast_query_name)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=DescribeFastQueryResponse)

    def describe_index(self, request, config=None):
        """
        describe_index

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeIndexResponse data
        :rtype: DescribeIndexResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlsClient.VERSION_V1, BlsClient.CONSTANT_LOGSTORE, request.log_store_name, BlsClient.CONSTANT_INDEX
        )
        headers = None
        params = {}
        if request.project is not None:
            params['project'] = request.project
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=DescribeIndexResponse
        )

    def describe_log_store(self, request, config=None):
        """
        describe_log_store

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeLogStoreResponse data
        :rtype: DescribeLogStoreResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V1, BlsClient.CONSTANT_LOGSTORE, request.log_store_name)
        headers = None
        params = {}
        if request.project is not None:
            params['project'] = request.project
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=DescribeLogStoreResponse
        )

    def describe_log_store_template(self, request, config=None):
        """
        describe_log_store_template

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeLogStoreTemplateResponse data
        :rtype: DescribeLogStoreTemplateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V3, BlsClient.CONSTANT_BLS)
        headers = None
        params = {}
        params['action'] = 'DescribeLogStoreTemplate'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeLogStoreTemplateResponse,
        )

    def describe_log_store_templates(self, request, config=None):
        """
        describe_log_store_templates

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeLogStoreTemplatesResponse data
        :rtype: DescribeLogStoreTemplatesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V3, BlsClient.CONSTANT_BLS)
        headers = None
        params = {}
        params['action'] = 'DescribeLogStoreTemplates'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeLogStoreTemplatesResponse,
        )

    def describe_log_store_view(self, request, config=None):
        """
        describe_log_store_view

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeLogStoreViewResponse data
        :rtype: DescribeLogStoreViewResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V3, BlsClient.CONSTANT_BLS)
        headers = None
        params = {}
        params['action'] = 'DescribeLogStoreView'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeLogStoreViewResponse,
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

    def disable_alarm_policy(self, request, config=None):
        """
        disable_alarm_policy

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DisableAlarmPolicyResponse data
        :rtype: DisableAlarmPolicyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlsClient.VERSION_V1, BlsClient.CONSTANT_ALARM, BlsClient.CONSTANT_POLICY, BlsClient.CONSTANT_DISABLE
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=DisableAlarmPolicyResponse,
        )

    def enable_alarm_policy(self, request, config=None):
        """
        enable_alarm_policy

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing EnableAlarmPolicyResponse data
        :rtype: EnableAlarmPolicyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlsClient.VERSION_V1, BlsClient.CONSTANT_ALARM, BlsClient.CONSTANT_POLICY, BlsClient.CONSTANT_ENABLE
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=EnableAlarmPolicyResponse,
        )

    def field_caps(self, request, config=None):
        """
        field_caps

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing FieldCapsResponse data
        :rtype: FieldCapsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', request.name, BlsClient.CONSTANT_FIELD_CAPS)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), config=merged_config, model=FieldCapsResponse
        )

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

    def get_log_shipper(self, request, config=None):
        """
        get_log_shipper

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetLogShipperResponse data
        :rtype: GetLogShipperResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V1, BlsClient.CONSTANT_LOGSHIPPER, request.log_shipper_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetLogShipperResponse)

    def list_alarm_execution_stats(self, request, config=None):
        """
        list_alarm_execution_stats

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListAlarmExecutionStatsResponse data
        :rtype: ListAlarmExecutionStatsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlsClient.VERSION_V1, BlsClient.CONSTANT_ALARM, BlsClient.CONSTANT_EXECUTION, BlsClient.CONSTANT_STATS
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=ListAlarmExecutionStatsResponse,
        )

    def list_alarm_executions(self, request, config=None):
        """
        list_alarm_executions

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListAlarmExecutionsResponse data
        :rtype: ListAlarmExecutionsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlsClient.VERSION_V1, BlsClient.CONSTANT_ALARM, BlsClient.CONSTANT_EXECUTION, BlsClient.CONSTANT_LIST
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=ListAlarmExecutionsResponse,
        )

    def list_alarm_policy(self, request, config=None):
        """
        list_alarm_policy

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListAlarmPolicyResponse data
        :rtype: ListAlarmPolicyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlsClient.VERSION_V1, BlsClient.CONSTANT_ALARM, BlsClient.CONSTANT_POLICY, BlsClient.CONSTANT_LIST
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=ListAlarmPolicyResponse,
        )

    def list_alarm_record(self, request, config=None):
        """
        list_alarm_record

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListAlarmRecordResponse data
        :rtype: ListAlarmRecordResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlsClient.VERSION_V1, BlsClient.CONSTANT_ALARM, BlsClient.CONSTANT_RECORD, BlsClient.CONSTANT_LIST
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=ListAlarmRecordResponse,
        )

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

    def list_fast_query(self, request, config=None):
        """
        list_fast_query

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListFastQueryResponse data
        :rtype: ListFastQueryResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V1, BlsClient.CONSTANT_FASTQUERY)
        headers = None
        params = {}
        if request.project is not None:
            params['project'] = request.project
        if request.log_store_name is not None:
            params['logStoreName'] = request.log_store_name
        if request.name_pattern is not None:
            params['namePattern'] = request.name_pattern
        if request.order is not None:
            params['order'] = request.order
        if request.order_by is not None:
            params['orderBy'] = request.order_by
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListFastQueryResponse
        )

    def list_log_shipper(self, request, config=None):
        """
        list_log_shipper

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListLogShipperResponse data
        :rtype: ListLogShipperResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V1, BlsClient.CONSTANT_LOGSHIPPER)
        headers = None
        params = {}
        params[''] = None
        if request.log_shipper_id is not None:
            params['logShipperID'] = request.log_shipper_id
        if request.log_shipper_name is not None:
            params['logShipperName'] = request.log_shipper_name
        if request.project is not None:
            params['project'] = request.project
        if request.log_store_name is not None:
            params['logStoreName'] = request.log_store_name
        if request.dest_type is not None:
            params['destType'] = request.dest_type
        if request.status is not None:
            params['status'] = request.status
        if request.order_by is not None:
            params['orderBy'] = request.order_by
        if request.order is not None:
            params['order'] = request.order
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListLogShipperResponse
        )

    def list_log_shipper_record(self, request, config=None):
        """
        list_log_shipper_record

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListLogShipperRecordResponse data
        :rtype: ListLogShipperRecordResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlsClient.VERSION_V1, BlsClient.CONSTANT_LOGSHIPPER, request.log_shipper_id, BlsClient.CONSTANT_RECORD
        )
        headers = None
        params = {}
        if request.since_hours is not None:
            params['sinceHours'] = request.since_hours
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListLogShipperRecordResponse
        )

    def list_log_store(self, request, config=None):
        """
        list_log_store

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListLogStoreResponse data
        :rtype: ListLogStoreResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V1, BlsClient.CONSTANT_LOGSTORE, BlsClient.CONSTANT_LIST)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=ListLogStoreResponse,
        )

    def list_log_store_view(self, request, config=None):
        """
        list_log_store_view

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListLogStoreViewResponse data
        :rtype: ListLogStoreViewResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V3, BlsClient.CONSTANT_BLS)
        headers = None
        params = {}
        params['action'] = 'DescribeLogStoreViews'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=ListLogStoreViewResponse,
        )

    def list_log_stream(self, request, config=None):
        """
        list_log_stream

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListLogStreamResponse data
        :rtype: ListLogStreamResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlsClient.VERSION_V1, BlsClient.CONSTANT_LOGSTORE, request.log_store_name, BlsClient.CONSTANT_LOGSTREAM
        )
        headers = None
        params = {}
        if request.project is not None:
            params['project'] = request.project
        if request.name_pattern is not None:
            params['namePattern'] = request.name_pattern
        if request.order is not None:
            params['order'] = request.order
        if request.order_by is not None:
            params['orderBy'] = request.order_by
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            params=params,
            config=merged_config,
            body_parser=handler.parse_stream,
            model=ListLogStreamResponse,
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

    def resolve_index(self, request, config=None):
        """
        resolve_index

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ResolveIndexResponse data
        :rtype: ResolveIndexResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BlsClient.CONSTANT_RESOLVE, BlsClient.CONSTANT_INDEX, request.name)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=ResolveIndexResponse)

    def set_single_log_shipper_status(self, request, config=None):
        """
        set_single_log_shipper_status

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing SetSingleLogShipperStatusResponse data
        :rtype: SetSingleLogShipperStatusResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlsClient.VERSION_V1, BlsClient.CONSTANT_LOGSHIPPER, request.log_shipper_id, BlsClient.CONSTANT_STATUS
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=SetSingleLogShipperStatusResponse,
        )

    def terms_enum(self, request, config=None):
        """
        terms_enum

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing TermsEnumResponse data
        :rtype: TermsEnumResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', request.name, BlsClient.CONSTANT_TERMS_ENUM)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), config=merged_config, model=TermsEnumResponse
        )

    def update_alarm_policy(self, request, config=None):
        """
        update_alarm_policy

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UpdateAlarmPolicyResponse data
        :rtype: UpdateAlarmPolicyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V1, BlsClient.CONSTANT_ALARM, BlsClient.CONSTANT_POLICY)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=UpdateAlarmPolicyResponse,
        )

    def update_fast_query(self, request, config=None):
        """
        update_fast_query

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UpdateFastQueryResponse data
        :rtype: UpdateFastQueryResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V1, BlsClient.CONSTANT_FASTQUERY, request.name)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=UpdateFastQueryResponse,
        )

    def update_index(self, request, config=None):
        """
        update_index

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UpdateIndexResponse data
        :rtype: UpdateIndexResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlsClient.VERSION_V1, BlsClient.CONSTANT_LOGSTORE, request.log_store_name, BlsClient.CONSTANT_INDEX
        )
        headers = None
        params = {}
        if request.project is not None:
            params['project'] = request.project
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=UpdateIndexResponse,
        )

    def update_log_shipper(self, request, config=None):
        """
        update_log_shipper

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UpdateLogShipperResponse data
        :rtype: UpdateLogShipperResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V1, BlsClient.CONSTANT_LOGSHIPPER, request.log_shipper_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=UpdateLogShipperResponse,
        )

    def update_log_store(self, request, config=None):
        """
        update_log_store

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UpdateLogStoreResponse data
        :rtype: UpdateLogStoreResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V1, BlsClient.CONSTANT_LOGSTORE, request.log_store_name)
        headers = None
        params = {}
        if request.project is not None:
            params['project'] = request.project
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=UpdateLogStoreResponse,
        )

    def update_log_store_template(self, request, config=None):
        """
        update_log_store_template

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UpdateLogStoreTemplateResponse data
        :rtype: UpdateLogStoreTemplateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V3, BlsClient.CONSTANT_BLS)
        headers = None
        params = {}
        params['action'] = 'UpdateLogStoreTemplate'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=UpdateLogStoreTemplateResponse,
        )

    def update_log_store_view(self, request, config=None):
        """
        update_log_store_view

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V3, BlsClient.CONSTANT_BLS)
        headers = None
        params = {}
        params['action'] = 'UpdateLogStoreView'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
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

    def update_task(self, request, config=None):
        """
        update_task

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BlsClient.CONSTANT_TASK, request.task_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def validate_alarm_condition(self, request, config=None):
        """
        validate_alarm_condition

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ValidateAlarmConditionResponse data
        :rtype: ValidateAlarmConditionResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlsClient.VERSION_V1, BlsClient.CONSTANT_ALARM, BlsClient.CONSTANT_CONDITION, BlsClient.CONSTANT_VALIDATE
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=ValidateAlarmConditionResponse,
        )

    def validate_alarm_policy_sql(self, request, config=None):
        """
        validate_alarm_policy_sql

        :param request: Request entity containing all parameters
        :type request: BlsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ValidateAlarmPolicySQLResponse data
        :rtype: ValidateAlarmPolicySQLResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlsClient.VERSION_V1, BlsClient.CONSTANT_LOGSTORE, BlsClient.CONSTANT_VALIDATE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=ValidateAlarmPolicySQLResponse,
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
