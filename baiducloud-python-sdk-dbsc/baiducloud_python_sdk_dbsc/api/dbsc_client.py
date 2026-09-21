"""
Example for dbsc client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_core.util import request_body_utils
from baiducloud_python_sdk_dbsc.models.check_mysql_rate_limit_support_response import (
    CheckMysqlRateLimitSupportResponse,
)
from baiducloud_python_sdk_dbsc.models.create_redis_big_key_analysis_task_response import (
    CreateRedisBigKeyAnalysisTaskResponse,
)
from baiducloud_python_sdk_dbsc.models.get_mongodb_collection_space_response import GetMongodbCollectionSpaceResponse
from baiducloud_python_sdk_dbsc.models.get_mongodb_collection_space_trend_response import (
    GetMongodbCollectionSpaceTrendResponse,
)
from baiducloud_python_sdk_dbsc.models.get_mongodb_database_space_response import GetMongodbDatabaseSpaceResponse
from baiducloud_python_sdk_dbsc.models.get_mongodb_database_space_trend_response import (
    GetMongodbDatabaseSpaceTrendResponse,
)
from baiducloud_python_sdk_dbsc.models.get_mongodb_slow_log_time_distribution_response import (
    GetMongodbSlowLogTimeDistributionResponse,
)
from baiducloud_python_sdk_dbsc.models.get_mongodb_slow_log_trend_response import GetMongodbSlowLogTrendResponse
from baiducloud_python_sdk_dbsc.models.get_mongodb_slow_query_template_response import (
    GetMongodbSlowQueryTemplateResponse,
)
from baiducloud_python_sdk_dbsc.models.get_mongodb_space_summary_response import GetMongodbSpaceSummaryResponse
from baiducloud_python_sdk_dbsc.models.get_mysql_active_sessions_response import GetMysqlActiveSessionsResponse
from baiducloud_python_sdk_dbsc.models.get_mysql_database_space_response import GetMysqlDatabaseSpaceResponse
from baiducloud_python_sdk_dbsc.models.get_mysql_deadlock_info_response import GetMysqlDeadlockInfoResponse
from baiducloud_python_sdk_dbsc.models.get_mysql_kill_session_history_response import (
    GetMysqlKillSessionHistoryResponse,
)
from baiducloud_python_sdk_dbsc.models.get_mysql_rate_limit_task_detail_response import (
    GetMysqlRateLimitTaskDetailResponse,
)
from baiducloud_python_sdk_dbsc.models.get_mysql_slow_log_template_response import GetMysqlSlowLogTemplateResponse
from baiducloud_python_sdk_dbsc.models.get_mysql_slow_log_time_distribution_response import (
    GetMysqlSlowLogTimeDistributionResponse,
)
from baiducloud_python_sdk_dbsc.models.get_mysql_slow_log_trend_response import GetMysqlSlowLogTrendResponse
from baiducloud_python_sdk_dbsc.models.get_mysql_space_summary_response import GetMysqlSpaceSummaryResponse
from baiducloud_python_sdk_dbsc.models.get_mysql_table_indexes_response import GetMysqlTableIndexesResponse
from baiducloud_python_sdk_dbsc.models.get_mysql_table_space_response import GetMysqlTableSpaceResponse
from baiducloud_python_sdk_dbsc.models.get_pegadb_slow_log_template_response import GetPegadbSlowLogTemplateResponse
from baiducloud_python_sdk_dbsc.models.get_pegadb_slow_log_time_distribution_response import (
    GetPegadbSlowLogTimeDistributionResponse,
)
from baiducloud_python_sdk_dbsc.models.get_pegadb_slow_log_trend_response import GetPegadbSlowLogTrendResponse
from baiducloud_python_sdk_dbsc.models.get_postgresql_slow_log_template_response import (
    GetPostgresqlSlowLogTemplateResponse,
)
from baiducloud_python_sdk_dbsc.models.get_postgresql_slow_log_time_distribution_response import (
    GetPostgresqlSlowLogTimeDistributionResponse,
)
from baiducloud_python_sdk_dbsc.models.get_postgresql_slow_log_trend_response import GetPostgresqlSlowLogTrendResponse
from baiducloud_python_sdk_dbsc.models.get_redis_big_key_analysis_result_response import (
    GetRedisBigKeyAnalysisResultResponse,
)
from baiducloud_python_sdk_dbsc.models.get_redis_slow_log_template_response import GetRedisSlowLogTemplateResponse
from baiducloud_python_sdk_dbsc.models.get_redis_slow_log_time_distribution_response import (
    GetRedisSlowLogTimeDistributionResponse,
)
from baiducloud_python_sdk_dbsc.models.get_redis_slow_log_trend_response import GetRedisSlowLogTrendResponse
from baiducloud_python_sdk_dbsc.models.kill_mysql_session_response import KillMysqlSessionResponse
from baiducloud_python_sdk_dbsc.models.list_mongodb_slow_logs_response import ListMongodbSlowLogsResponse
from baiducloud_python_sdk_dbsc.models.list_mysql_rate_limit_tasks_response import ListMysqlRateLimitTasksResponse
from baiducloud_python_sdk_dbsc.models.list_mysql_slow_logs_response import ListMysqlSlowLogsResponse
from baiducloud_python_sdk_dbsc.models.list_pegadb_slow_logs_response import ListPegadbSlowLogsResponse
from baiducloud_python_sdk_dbsc.models.list_postgresql_slow_logs_response import ListPostgresqlSlowLogsResponse
from baiducloud_python_sdk_dbsc.models.list_redis_big_key_analysis_tasks_response import (
    ListRedisBigKeyAnalysisTasksResponse,
)
from baiducloud_python_sdk_dbsc.models.list_redis_slow_logs_response import ListRedisSlowLogsResponse

_logger = logging.getLogger(__name__)


class DbscClient(BceBaseClient):
    """
    dbsc base sdk client
    """

    VERSION_V1 = b'/v1'

    CONSTANT_DIAGNOSIS = b'diagnosis'

    CONSTANT_MYSQL = b'mysql'

    CONSTANT_SQLFILTER = b'sqlfilter'

    CONSTANT_DELETE = b'delete'

    CONSTANT_SESSION = b'session'

    CONSTANT_KILL = b'kill'

    CONSTANT_LIST = b'list'

    CONSTANT_V1 = b'v1'

    CONSTANT_ACTION = b'action'

    CONSTANT_API = b'api'

    CONSTANT_REDIS = b'redis'

    CONSTANT_SLOWLOG = b'slowlog'

    CONSTANT_TREND = b'trend'

    CONSTANT_STATS = b'stats'

    CONSTANT_DURATION = b'duration'

    CONSTANT_DEADLOCK = b'deadlock'

    CONSTANT_LATEST = b'latest'

    CONSTANT_MONGODB = b'mongodb'

    CONSTANT_SPACE = b'space'

    CONSTANT_COLLECTION = b'collection'

    CONSTANT_PEGA = b'pega'

    CONSTANT_SCHEMA = b'schema'

    CONSTANT_TABLE = b'table'

    CONSTANT_INDEX = b'index'

    CONSTANT_BIG_KEY = b'big-key'

    CONSTANT_TASK = b'task'

    CONSTANT_TEMPLATE = b'template'

    CONSTANT_DATABASE = b'database'

    CONSTANT_POSTGRESQL = b'postgresql'

    CONSTANT_HISTORY = b'history'

    CONSTANT_SUMMARY = b'summary'

    CONSTANT_RESULT = b'result'

    CONSTANT_ALLOWED = b'allowed'

    def __init__(self, config=None):
        """
        Initialize the dbsc client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def check_mysql_rate_limit_support(self, request, config=None):
        """
        check_mysql_rate_limit_support

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CheckMysqlRateLimitSupportResponse data
        :rtype: CheckMysqlRateLimitSupportResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_MYSQL,
            DbscClient.CONSTANT_SQLFILTER,
            DbscClient.CONSTANT_ALLOWED,
        )
        headers = None
        params = {}
        params['appId'] = 'appId'
        params['nodeId'] = 'nodeId'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=CheckMysqlRateLimitSupportResponse
        )

    def create_mysql_rate_limit_task(self, request, config=None):
        """
        create_mysql_rate_limit_task

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_MYSQL,
            DbscClient.CONSTANT_SQLFILTER,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def create_redis_big_key_analysis_task(self, request, config=None):
        """
        create_redis_big_key_analysis_task

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateRedisBigKeyAnalysisTaskResponse data
        :rtype: CreateRedisBigKeyAnalysisTaskResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_REDIS,
            DbscClient.CONSTANT_BIG_KEY,
            DbscClient.CONSTANT_TASK,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateRedisBigKeyAnalysisTaskResponse,
        )

    def delete_mysql_rate_limit_task(self, request, config=None):
        """
        delete_mysql_rate_limit_task

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_MYSQL,
            DbscClient.CONSTANT_SQLFILTER,
            DbscClient.CONSTANT_DELETE,
        )
        headers = None
        params = {}
        params['appId'] = 'appId'
        params['nodeId'] = 'nodeId'
        params['filterId'] = 'filterId'
        if request.filter_id is not None:
            params['filterId'] = request.filter_id
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_redis_big_key_analysis_task(self, request, config=None):
        """
        delete_redis_big_key_analysis_task

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_REDIS,
            DbscClient.CONSTANT_BIG_KEY,
            DbscClient.CONSTANT_TASK,
        )
        headers = None
        params = {}
        if request.ids is not None:
            params['ids'] = ','.join(request.ids)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.DELETE, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def get_mongodb_collection_indexes(self, request, config=None):
        """
        get_mongodb_collection_indexes

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_API,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_MONGODB,
            DbscClient.CONSTANT_SCHEMA,
            DbscClient.CONSTANT_COLLECTION,
            DbscClient.CONSTANT_INDEX,
        )
        headers = None
        params = {}
        params['product'] = 'string'
        params['appId'] = 'string'
        params['nodeId'] = 'string'
        params['database'] = 'string'
        params['collection'] = 'string'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, params=params, config=merged_config)

    def get_mongodb_collection_space(self, request, config=None):
        """
        get_mongodb_collection_space

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetMongodbCollectionSpaceResponse data
        :rtype: GetMongodbCollectionSpaceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_API,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_MONGODB,
            DbscClient.CONSTANT_SPACE,
            DbscClient.CONSTANT_COLLECTION,
        )
        headers = None
        params = {}
        params['appId'] = 'appId'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        if request.database is not None:
            params['database'] = request.database
        if request.collection is not None:
            params['collection'] = request.collection
        if request.order_by is not None:
            params['orderBy'] = request.order_by
        if request.order is not None:
            params['order'] = request.order
        if request.page is not None:
            params['page'] = request.page
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetMongodbCollectionSpaceResponse
        )

    def get_mongodb_collection_space_trend(self, request, config=None):
        """
        get_mongodb_collection_space_trend

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetMongodbCollectionSpaceTrendResponse data
        :rtype: GetMongodbCollectionSpaceTrendResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_API,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_MONGODB,
            DbscClient.CONSTANT_SPACE,
            DbscClient.CONSTANT_COLLECTION,
            DbscClient.CONSTANT_TREND,
        )
        headers = None
        params = {}
        params['appId'] = 'appId'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.database is not None:
            params['database'] = request.database
        if request.collection is not None:
            params['collection'] = request.collection
        if request.period is not None:
            params['period'] = request.period
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        if request.start is not None:
            params['start'] = request.start
        if request.end is not None:
            params['end'] = request.end
        if request.metrics is not None:
            params['metrics'] = request.metrics
        if request.statistics is not None:
            params['statistics'] = request.statistics
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            params=params,
            config=merged_config,
            model=GetMongodbCollectionSpaceTrendResponse,
        )

    def get_mongodb_database_space(self, request, config=None):
        """
        get_mongodb_database_space

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetMongodbDatabaseSpaceResponse data
        :rtype: GetMongodbDatabaseSpaceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_API,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_MONGODB,
            DbscClient.CONSTANT_SPACE,
            DbscClient.CONSTANT_DATABASE,
        )
        headers = None
        params = {}
        params['appId'] = 'appId'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        if request.database is not None:
            params['database'] = request.database
        if request.order_by is not None:
            params['orderBy'] = request.order_by
        if request.order is not None:
            params['order'] = request.order
        if request.page is not None:
            params['page'] = request.page
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetMongodbDatabaseSpaceResponse
        )

    def get_mongodb_database_space_trend(self, request, config=None):
        """
        get_mongodb_database_space_trend

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetMongodbDatabaseSpaceTrendResponse data
        :rtype: GetMongodbDatabaseSpaceTrendResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_API,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_MONGODB,
            DbscClient.CONSTANT_SPACE,
            DbscClient.CONSTANT_DATABASE,
            DbscClient.CONSTANT_TREND,
        )
        headers = None
        params = {}
        params['appId'] = 'appId'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.database is not None:
            params['database'] = request.database
        if request.period is not None:
            params['period'] = request.period
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        if request.start is not None:
            params['start'] = request.start
        if request.end is not None:
            params['end'] = request.end
        if request.metrics is not None:
            params['metrics'] = request.metrics
        if request.statistics is not None:
            params['statistics'] = request.statistics
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            params=params,
            config=merged_config,
            model=GetMongodbDatabaseSpaceTrendResponse,
        )

    def get_mongodb_slow_log_time_distribution(self, request, config=None):
        """
        get_mongodb_slow_log_time_distribution

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetMongodbSlowLogTimeDistributionResponse data
        :rtype: GetMongodbSlowLogTimeDistributionResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_MYSQL,
            DbscClient.CONSTANT_SLOWLOG,
            DbscClient.CONSTANT_STATS,
            DbscClient.CONSTANT_DURATION,
        )
        headers = None
        params = {}
        params['appId'] = 'appId'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.start is not None:
            params['start'] = request.start
        if request.end is not None:
            params['end'] = request.end
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        if request.db_names is not None:
            params['dbNames'] = request.db_names
        if request.fingerprint_md5 is not None:
            params['fingerprintMd5'] = request.fingerprint_md5
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            params=params,
            config=merged_config,
            model=GetMongodbSlowLogTimeDistributionResponse,
        )

    def get_mongodb_slow_log_trend(self, request, config=None):
        """
        get_mongodb_slow_log_trend

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetMongodbSlowLogTrendResponse data
        :rtype: GetMongodbSlowLogTrendResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_MYSQL,
            DbscClient.CONSTANT_SLOWLOG,
            DbscClient.CONSTANT_TREND,
        )
        headers = None
        params = {}
        params['appId'] = 'appId'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.start is not None:
            params['start'] = request.start
        if request.end is not None:
            params['end'] = request.end
        if request.period is not None:
            params['period'] = request.period
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetMongodbSlowLogTrendResponse
        )

    def get_mongodb_slow_query_template(self, request, config=None):
        """
        get_mongodb_slow_query_template

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetMongodbSlowQueryTemplateResponse data
        :rtype: GetMongodbSlowQueryTemplateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_MONGODB,
            DbscClient.CONSTANT_SLOWLOG,
            DbscClient.CONSTANT_TEMPLATE,
        )
        headers = None
        params = {}
        params['appId'] = 'appId'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.start is not None:
            params['start'] = request.start
        if request.end is not None:
            params['end'] = request.end
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        if request.users is not None:
            params['users'] = request.users
        if request.db_names is not None:
            params['dbNames'] = request.db_names
        if request.client_ips is not None:
            params['clientIps'] = request.client_ips
        if request.fingerprint_md5 is not None:
            params['fingerprintMd5'] = request.fingerprint_md5
        if request.namespace is not None:
            params['namespace'] = request.namespace
        if request.order_by is not None:
            params['orderBy'] = request.order_by
        if request.order is not None:
            params['order'] = request.order
        if request.page is not None:
            params['page'] = request.page
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetMongodbSlowQueryTemplateResponse
        )

    def get_mongodb_space_summary(self, request, config=None):
        """
        get_mongodb_space_summary

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetMongodbSpaceSummaryResponse data
        :rtype: GetMongodbSpaceSummaryResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_API,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_MONGODB,
            DbscClient.CONSTANT_SPACE,
            DbscClient.CONSTANT_SUMMARY,
        )
        headers = None
        params = {}
        params['appId'] = 'appId'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetMongodbSpaceSummaryResponse
        )

    def get_mysql_active_sessions(self, request, config=None):
        """
        get_mysql_active_sessions

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetMysqlActiveSessionsResponse data
        :rtype: GetMysqlActiveSessionsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_MYSQL,
            DbscClient.CONSTANT_SESSION,
            DbscClient.CONSTANT_LIST,
        )
        headers = None
        params = {}
        params['appId'] = 'appId'
        params['nodeId'] = 'nodeId'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetMysqlActiveSessionsResponse
        )

    def get_mysql_database_space(self, request, config=None):
        """
        get_mysql_database_space

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetMysqlDatabaseSpaceResponse data
        :rtype: GetMysqlDatabaseSpaceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_API,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_MYSQL,
            DbscClient.CONSTANT_SPACE,
            DbscClient.CONSTANT_DATABASE,
        )
        headers = None
        params = {}
        params['appId'] = 'appId'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        if request.database is not None:
            params['database'] = request.database
        if request.order_by is not None:
            params['orderBy'] = request.order_by
        if request.order is not None:
            params['order'] = request.order
        if request.page is not None:
            params['page'] = request.page
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetMysqlDatabaseSpaceResponse
        )

    def get_mysql_deadlock_info(self, request, config=None):
        """
        get_mysql_deadlock_info

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetMysqlDeadlockInfoResponse data
        :rtype: GetMysqlDeadlockInfoResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_MYSQL,
            DbscClient.CONSTANT_DEADLOCK,
            DbscClient.CONSTANT_LATEST,
        )
        headers = None
        params = {}
        params['appId'] = 'appId'
        params['nodeId'] = 'nodeId'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetMysqlDeadlockInfoResponse
        )

    def get_mysql_kill_session_history(self, request, config=None):
        """
        get_mysql_kill_session_history

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetMysqlKillSessionHistoryResponse data
        :rtype: GetMysqlKillSessionHistoryResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_MYSQL,
            DbscClient.CONSTANT_SESSION,
            DbscClient.CONSTANT_KILL,
            DbscClient.CONSTANT_HISTORY,
        )
        headers = None
        params = {}
        params['appId'] = 'appId'
        params['nodeId'] = 'nodeId'
        params['start'] = 'start'
        params['end'] = 'end'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, params=params, config=merged_config, model=GetMysqlKillSessionHistoryResponse
        )

    def get_mysql_rate_limit_task_detail(self, request, config=None):
        """
        get_mysql_rate_limit_task_detail

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetMysqlRateLimitTaskDetailResponse data
        :rtype: GetMysqlRateLimitTaskDetailResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_MYSQL,
            DbscClient.CONSTANT_SQLFILTER,
        )
        headers = None
        params = {}
        params['filterId'] = None
        params['appId'] = 'appId'
        params['nodeId'] = 'nodeId'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        if request.filter_id is not None:
            params['filterId'] = request.filter_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetMysqlRateLimitTaskDetailResponse
        )

    def get_mysql_slow_log_template(self, request, config=None):
        """
        get_mysql_slow_log_template

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetMysqlSlowLogTemplateResponse data
        :rtype: GetMysqlSlowLogTemplateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_MYSQL,
            DbscClient.CONSTANT_SLOWLOG,
            DbscClient.CONSTANT_TEMPLATE,
        )
        headers = None
        params = {}
        params['appId'] = 'appId'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.start is not None:
            params['start'] = request.start
        if request.end is not None:
            params['end'] = request.end
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        if request.users is not None:
            params['users'] = request.users
        if request.db_names is not None:
            params['dbNames'] = request.db_names
        if request.client_ips is not None:
            params['clientIps'] = request.client_ips
        if request.fingerprint_md5 is not None:
            params['fingerprintMd5'] = request.fingerprint_md5
        if request.order_by is not None:
            params['orderBy'] = request.order_by
        if request.order is not None:
            params['order'] = request.order
        if request.page is not None:
            params['page'] = request.page
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetMysqlSlowLogTemplateResponse
        )

    def get_mysql_slow_log_time_distribution(self, request, config=None):
        """
        get_mysql_slow_log_time_distribution

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetMysqlSlowLogTimeDistributionResponse data
        :rtype: GetMysqlSlowLogTimeDistributionResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_MYSQL,
            DbscClient.CONSTANT_SLOWLOG,
            DbscClient.CONSTANT_STATS,
            DbscClient.CONSTANT_DURATION,
        )
        headers = None
        params = {}
        params['appId'] = 'appId'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.start is not None:
            params['start'] = request.start
        if request.end is not None:
            params['end'] = request.end
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        if request.db_names is not None:
            params['dbNames'] = request.db_names
        if request.fingerprint_md5 is not None:
            params['fingerprintMd5'] = request.fingerprint_md5
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            params=params,
            config=merged_config,
            model=GetMysqlSlowLogTimeDistributionResponse,
        )

    def get_mysql_slow_log_trend(self, request, config=None):
        """
        get_mysql_slow_log_trend

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetMysqlSlowLogTrendResponse data
        :rtype: GetMysqlSlowLogTrendResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_MYSQL,
            DbscClient.CONSTANT_SLOWLOG,
            DbscClient.CONSTANT_TREND,
        )
        headers = None
        params = {}
        params['appId'] = 'appId'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.start is not None:
            params['start'] = request.start
        if request.end is not None:
            params['end'] = request.end
        if request.period is not None:
            params['period'] = request.period
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetMysqlSlowLogTrendResponse
        )

    def get_mysql_space_summary(self, request, config=None):
        """
        get_mysql_space_summary

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetMysqlSpaceSummaryResponse data
        :rtype: GetMysqlSpaceSummaryResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_API,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_MYSQL,
            DbscClient.CONSTANT_SPACE,
            DbscClient.CONSTANT_SUMMARY,
        )
        headers = None
        params = {}
        params['appId'] = 'appId'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetMysqlSpaceSummaryResponse
        )

    def get_mysql_table_indexes(self, request, config=None):
        """
        get_mysql_table_indexes

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetMysqlTableIndexesResponse data
        :rtype: GetMysqlTableIndexesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_API,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_MYSQL,
            DbscClient.CONSTANT_SCHEMA,
            DbscClient.CONSTANT_TABLE,
            DbscClient.CONSTANT_INDEX,
        )
        headers = None
        params = {}
        params['product'] = 'string'
        params['appId'] = 'string'
        params['database'] = 'string'
        params['table'] = 'string'
        if request.app_id is not None:
            params['appId'] = request.app_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetMysqlTableIndexesResponse
        )

    def get_mysql_table_space(self, request, config=None):
        """
        get_mysql_table_space

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetMysqlTableSpaceResponse data
        :rtype: GetMysqlTableSpaceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_API,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_MYSQL,
            DbscClient.CONSTANT_SPACE,
            DbscClient.CONSTANT_TABLE,
        )
        headers = None
        params = {}
        params['appId'] = 'appId'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        if request.database is not None:
            params['database'] = request.database
        if request.table is not None:
            params['table'] = request.table
        if request.order_by is not None:
            params['orderBy'] = request.order_by
        if request.order is not None:
            params['order'] = request.order
        if request.page is not None:
            params['page'] = request.page
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetMysqlTableSpaceResponse
        )

    def get_pegadb_slow_log_template(self, request, config=None):
        """
        get_pegadb_slow_log_template

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetPegadbSlowLogTemplateResponse data
        :rtype: GetPegadbSlowLogTemplateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_API,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_PEGA,
            DbscClient.CONSTANT_SLOWLOG,
            DbscClient.CONSTANT_SUMMARY,
        )
        headers = None
        params = {}
        params['appId'] = 'string'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        if request.start is not None:
            params['start'] = request.start
        if request.end is not None:
            params['end'] = request.end
        if request.db_engine is not None:
            params['dbEngine'] = request.db_engine
        if request.page is not None:
            params['page'] = request.page
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        if request.order_by is not None:
            params['orderBy'] = request.order_by
        if request.order is not None:
            params['order'] = request.order
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetPegadbSlowLogTemplateResponse
        )

    def get_pegadb_slow_log_time_distribution(self, request, config=None):
        """
        get_pegadb_slow_log_time_distribution

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetPegadbSlowLogTimeDistributionResponse data
        :rtype: GetPegadbSlowLogTimeDistributionResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_API,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_PEGA,
            DbscClient.CONSTANT_SLOWLOG,
            DbscClient.CONSTANT_STATS,
            DbscClient.CONSTANT_DURATION,
        )
        headers = None
        params = {}
        params['appId'] = 'string'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        if request.start is not None:
            params['start'] = request.start
        if request.end is not None:
            params['end'] = request.end
        if request.db_engine is not None:
            params['dbEngine'] = request.db_engine
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            params=params,
            config=merged_config,
            model=GetPegadbSlowLogTimeDistributionResponse,
        )

    def get_pegadb_slow_log_trend(self, request, config=None):
        """
        get_pegadb_slow_log_trend

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetPegadbSlowLogTrendResponse data
        :rtype: GetPegadbSlowLogTrendResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_API,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_PEGA,
            DbscClient.CONSTANT_SLOWLOG,
            DbscClient.CONSTANT_TREND,
        )
        headers = None
        params = {}
        params['appId'] = 'string'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        if request.start is not None:
            params['start'] = request.start
        if request.end is not None:
            params['end'] = request.end
        if request.db_engine is not None:
            params['dbEngine'] = request.db_engine
        if request.period is not None:
            params['period'] = request.period
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetPegadbSlowLogTrendResponse
        )

    def get_postgresql_slow_log_template(self, request, config=None):
        """
        get_postgresql_slow_log_template

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetPostgresqlSlowLogTemplateResponse data
        :rtype: GetPostgresqlSlowLogTemplateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_API,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_POSTGRESQL,
            DbscClient.CONSTANT_SLOWLOG,
            DbscClient.CONSTANT_TEMPLATE,
        )
        headers = None
        params = {}
        params[''] = None
        params['product'] = 'string'
        params['appId'] = 'string'
        params['nodeId'] = 'string'
        params['start'] = 'string'
        params['end'] = 'string'
        params['dbNames'] = 'dbNames'
        params['clientIps'] = 'clientIps'
        params['fingerprintMd5'] = 'fingerprintMd5page'
        params['pageSize'] = 'int'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        if request.users is not None:
            params['users'] = request.users
        if request.db_names is not None:
            params['dbNames'] = request.db_names
        if request.client_ips is not None:
            params['clientIps'] = request.client_ips
        if request.fingerprint_md5 is not None:
            params['fingerprintMd5'] = request.fingerprint_md5
        if request.page is not None:
            params['page'] = request.page
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        if request.order_by is not None:
            params['orderBy'] = request.order_by
        if request.order is not None:
            params['order'] = request.order
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            params=params,
            config=merged_config,
            model=GetPostgresqlSlowLogTemplateResponse,
        )

    def get_postgresql_slow_log_time_distribution(self, request, config=None):
        """
        get_postgresql_slow_log_time_distribution

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetPostgresqlSlowLogTimeDistributionResponse data
        :rtype: GetPostgresqlSlowLogTimeDistributionResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_API,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_POSTGRESQL,
            DbscClient.CONSTANT_SLOWLOG,
            DbscClient.CONSTANT_STATS,
            DbscClient.CONSTANT_DURATION,
        )
        headers = None
        params = {}
        params['product'] = 'string'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        if request.start is not None:
            params['start'] = request.start
        if request.end is not None:
            params['end'] = request.end
        if request.db_names is not None:
            params['dbNames'] = ','.join(request.db_names)
        if request.users is not None:
            params['users'] = ','.join(request.users)
        if request.client_ips is not None:
            params['clientIPs'] = ','.join(request.client_ips)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            params=params,
            config=merged_config,
            model=GetPostgresqlSlowLogTimeDistributionResponse,
        )

    def get_postgresql_slow_log_trend(self, request, config=None):
        """
        get_postgresql_slow_log_trend

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetPostgresqlSlowLogTrendResponse data
        :rtype: GetPostgresqlSlowLogTrendResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_API,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_POSTGRESQL,
            DbscClient.CONSTANT_SLOWLOG,
            DbscClient.CONSTANT_TREND,
        )
        headers = None
        params = {}
        params['product'] = 'string'
        params['appId'] = 'string'
        params['nodeId'] = 'string'
        params['start'] = 'string'
        params['end'] = 'string'
        params['period'] = 'int'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetPostgresqlSlowLogTrendResponse
        )

    def get_redis_big_key_analysis_result(self, request, config=None):
        """
        get_redis_big_key_analysis_result

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetRedisBigKeyAnalysisResultResponse data
        :rtype: GetRedisBigKeyAnalysisResultResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_REDIS,
            DbscClient.CONSTANT_BIG_KEY,
            DbscClient.CONSTANT_TASK,
            DbscClient.CONSTANT_LIST,
        )
        headers = None
        params = {}
        params['appId'] = 'appId'
        params['page'] = 'page'
        params['pageSize'] = 'pageSize'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            params=params,
            config=merged_config,
            model=GetRedisBigKeyAnalysisResultResponse,
        )

    def get_redis_slow_log_template(self, request, config=None):
        """
        get_redis_slow_log_template

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetRedisSlowLogTemplateResponse data
        :rtype: GetRedisSlowLogTemplateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_API,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_REDIS,
            DbscClient.CONSTANT_SLOWLOG,
            DbscClient.CONSTANT_SUMMARY,
        )
        headers = None
        params = {}
        params['appId'] = 'string'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        if request.start is not None:
            params['start'] = request.start
        if request.end is not None:
            params['end'] = request.end
        if request.db_engine is not None:
            params['dbEngine'] = request.db_engine
        if request.page is not None:
            params['page'] = request.page
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        if request.order_by is not None:
            params['orderBy'] = request.order_by
        if request.order is not None:
            params['order'] = request.order
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetRedisSlowLogTemplateResponse
        )

    def get_redis_slow_log_time_distribution(self, request, config=None):
        """
        get_redis_slow_log_time_distribution

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetRedisSlowLogTimeDistributionResponse data
        :rtype: GetRedisSlowLogTimeDistributionResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_API,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_REDIS,
            DbscClient.CONSTANT_SLOWLOG,
            DbscClient.CONSTANT_STATS,
            DbscClient.CONSTANT_DURATION,
        )
        headers = None
        params = {}
        params['appId'] = 'string'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        if request.start is not None:
            params['start'] = request.start
        if request.end is not None:
            params['end'] = request.end
        if request.db_engine is not None:
            params['dbEngine'] = request.db_engine
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            params=params,
            config=merged_config,
            model=GetRedisSlowLogTimeDistributionResponse,
        )

    def get_redis_slow_log_trend(self, request, config=None):
        """
        get_redis_slow_log_trend

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetRedisSlowLogTrendResponse data
        :rtype: GetRedisSlowLogTrendResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_API,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_REDIS,
            DbscClient.CONSTANT_SLOWLOG,
            DbscClient.CONSTANT_TREND,
        )
        headers = None
        params = {}
        params['appId'] = 'string'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        if request.start is not None:
            params['start'] = request.start
        if request.end is not None:
            params['end'] = request.end
        if request.db_engine is not None:
            params['dbEngine'] = request.db_engine
        if request.period is not None:
            params['period'] = request.period
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetRedisSlowLogTrendResponse
        )

    def kill_mysql_session(self, request, config=None):
        """
        kill_mysql_session

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing KillMysqlSessionResponse data
        :rtype: KillMysqlSessionResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_MYSQL,
            DbscClient.CONSTANT_SESSION,
            DbscClient.CONSTANT_KILL,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=KillMysqlSessionResponse,
        )

    def list_mongodb_slow_logs(self, request, config=None):
        """
        list_mongodb_slow_logs

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListMongodbSlowLogsResponse data
        :rtype: ListMongodbSlowLogsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_MONGODB,
            DbscClient.CONSTANT_SLOWLOG,
            DbscClient.CONSTANT_LIST,
        )
        headers = None
        params = {}
        params['appId'] = 'appId'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.start is not None:
            params['start'] = request.start
        if request.end is not None:
            params['end'] = request.end
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        if request.users is not None:
            params['users'] = request.users
        if request.db_names is not None:
            params['dbNames'] = request.db_names
        if request.client_ips is not None:
            params['clientIps'] = request.client_ips
        if request.namespace is not None:
            params['namespace'] = request.namespace
        if request.fingerprint_md5 is not None:
            params['fingerprintMd5'] = request.fingerprint_md5
        if request.order_by is not None:
            params['orderBy'] = request.order_by
        if request.order is not None:
            params['order'] = request.order
        if request.page is not None:
            params['page'] = request.page
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListMongodbSlowLogsResponse
        )

    def list_mysql_rate_limit_tasks(self, request, config=None):
        """
        list_mysql_rate_limit_tasks

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListMysqlRateLimitTasksResponse data
        :rtype: ListMysqlRateLimitTasksResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_MYSQL,
            DbscClient.CONSTANT_SQLFILTER,
            DbscClient.CONSTANT_LIST,
        )
        headers = None
        params = {}
        params['appId'] = 'rds-OEEsaajh'
        params['nodeId'] = 'rds-OEEsaajh'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListMysqlRateLimitTasksResponse
        )

    def list_mysql_slow_logs(self, request, config=None):
        """
        list_mysql_slow_logs

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListMysqlSlowLogsResponse data
        :rtype: ListMysqlSlowLogsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_MYSQL,
            DbscClient.CONSTANT_SLOWLOG,
            DbscClient.CONSTANT_LIST,
        )
        headers = None
        params = {}
        params['appId'] = 'appId'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.start is not None:
            params['start'] = request.start
        if request.end is not None:
            params['end'] = request.end
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        if request.users is not None:
            params['users'] = request.users
        if request.db_names is not None:
            params['dbNames'] = request.db_names
        if request.client_ips is not None:
            params['clientIps'] = request.client_ips
        if request.fingerprint_md5 is not None:
            params['fingerprintMd5'] = request.fingerprint_md5
        if request.order_by is not None:
            params['orderBy'] = request.order_by
        if request.order is not None:
            params['order'] = request.order
        if request.page is not None:
            params['page'] = request.page
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListMysqlSlowLogsResponse
        )

    def list_pegadb_slow_logs(self, request, config=None):
        """
        list_pegadb_slow_logs

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListPegadbSlowLogsResponse data
        :rtype: ListPegadbSlowLogsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_API,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_PEGA,
            DbscClient.CONSTANT_SLOWLOG,
            DbscClient.CONSTANT_LIST,
        )
        headers = None
        params = {}
        params['appId'] = 'string'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        if request.start is not None:
            params['start'] = request.start
        if request.end is not None:
            params['end'] = request.end
        if request.db_engine is not None:
            params['dbEngine'] = request.db_engine
        if request.page is not None:
            params['page'] = request.page
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        if request.order_by is not None:
            params['orderBy'] = request.order_by
        if request.order is not None:
            params['order'] = request.order
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListPegadbSlowLogsResponse
        )

    def list_postgresql_slow_logs(self, request, config=None):
        """
        list_postgresql_slow_logs

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListPostgresqlSlowLogsResponse data
        :rtype: ListPostgresqlSlowLogsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_API,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_POSTGRESQL,
            DbscClient.CONSTANT_SLOWLOG,
            DbscClient.CONSTANT_LIST,
        )
        headers = None
        params = {}
        params['product'] = 'string'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        if request.start is not None:
            params['start'] = request.start
        if request.end is not None:
            params['end'] = request.end
        if request.page is not None:
            params['page'] = request.page
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        if request.db_names is not None:
            params['dbNames'] = ','.join(request.db_names)
        if request.client_ips is not None:
            params['clientIPs'] = ','.join(request.client_ips)
        if request.users is not None:
            params['users'] = ','.join(request.users)
        if request.order_by is not None:
            params['orderBy'] = request.order_by
        if request.order is not None:
            params['order'] = request.order
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListPostgresqlSlowLogsResponse
        )

    def list_redis_big_key_analysis_tasks(self, request, config=None):
        """
        list_redis_big_key_analysis_tasks

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListRedisBigKeyAnalysisTasksResponse data
        :rtype: ListRedisBigKeyAnalysisTasksResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_REDIS,
            DbscClient.CONSTANT_BIG_KEY,
            DbscClient.CONSTANT_TASK,
            DbscClient.CONSTANT_RESULT,
        )
        headers = None
        params = {}
        params['id'] = 'id'
        params['appId'] = 'appId'
        params['nodeId'] = 'nodeId'
        params['dataType'] = 'dataType'
        params['orderBy'] = 'orderBy'
        params['order'] = 'order'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.cluster_id is not None:
            params['clusterId'] = request.cluster_id
        if request.data_type is not None:
            params['dataType'] = request.data_type
        if request.order_by is not None:
            params['orderBy'] = request.order_by
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            params=params,
            config=merged_config,
            model=ListRedisBigKeyAnalysisTasksResponse,
        )

    def list_redis_slow_logs(self, request, config=None):
        """
        list_redis_slow_logs

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListRedisSlowLogsResponse data
        :rtype: ListRedisSlowLogsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_API,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_REDIS,
            DbscClient.CONSTANT_SLOWLOG,
            DbscClient.CONSTANT_LIST,
        )
        headers = None
        params = {}
        params['appId'] = 'string'
        if request.app_id is not None:
            params['appId'] = request.app_id
        if request.node_id is not None:
            params['nodeId'] = request.node_id
        if request.start is not None:
            params['start'] = request.start
        if request.end is not None:
            params['end'] = request.end
        if request.db_engine is not None:
            params['dbEngine'] = request.db_engine
        if request.page is not None:
            params['page'] = request.page
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        if request.order_by is not None:
            params['orderBy'] = request.order_by
        if request.order is not None:
            params['order'] = request.order
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListRedisSlowLogsResponse
        )

    def start_stop_mysql_instance_flow_limiting_task(self, request, config=None):
        """
        start_stop_mysql_instance_flow_limiting_task

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DbscClient.VERSION_V1,
            DbscClient.CONSTANT_V1,
            DbscClient.CONSTANT_DIAGNOSIS,
            DbscClient.CONSTANT_MYSQL,
            DbscClient.CONSTANT_SQLFILTER,
            DbscClient.CONSTANT_ACTION,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def update_mysql_rate_limit_task(self, request, config=None):
        """
        update_mysql_rate_limit_task

        :param request: Request entity containing all parameters
        :type request: DbscClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(DbscClient.VERSION_V1, DbscClient.CONSTANT_MYSQL, DbscClient.CONSTANT_SQLFILTER)
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
        sign_fn, params = self._choose_signer(config, params)
        return bce_http_client.send_request(
            config, sign_fn, [handler.parse_error, body_parser], http_method, path, body, headers, params, model=model
        )
