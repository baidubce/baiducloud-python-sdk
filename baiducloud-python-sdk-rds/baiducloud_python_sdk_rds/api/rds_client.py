"""
Example for rds client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_core.util import request_body_utils
from baiducloud_python_sdk_rds.models.batch_configuration_of_instances_response import (
    BatchConfigurationOfInstancesResponse,
)
from baiducloud_python_sdk_rds.models.check_the_whitelist_response import CheckTheWhitelistResponse
from baiducloud_python_sdk_rds.models.cluster_status_check_response import ClusterStatusCheckResponse
from baiducloud_python_sdk_rds.models.create_a_primary_instance_response import CreateAPrimaryInstanceResponse
from baiducloud_python_sdk_rds.models.create_a_proxy_instance_response import CreateAProxyInstanceResponse
from baiducloud_python_sdk_rds.models.create_read_only_instance_response import CreateReadOnlyInstanceResponse
from baiducloud_python_sdk_rds.models.dial_test_interface_response import DialTestInterfaceResponse
from baiducloud_python_sdk_rds.models.does_the_instance_support_enabling_automatic_expansion_response import (
    DoesTheInstanceSupportEnablingAutomaticExpansionResponse,
)
from baiducloud_python_sdk_rds.models.error_log_download_details_response import ErrorLogDownloadDetailsResponse
from baiducloud_python_sdk_rds.models.error_log_list_response import ErrorLogListResponse
from baiducloud_python_sdk_rds.models.get_parameter_template_details_response import (
    GetParameterTemplateDetailsResponse,
)
from baiducloud_python_sdk_rds.models.get_parameter_template_list_response import GetParameterTemplateListResponse
from baiducloud_python_sdk_rds.models.get_pg_log_details_response import GetPgLogDetailsResponse
from baiducloud_python_sdk_rds.models.get_pg_log_list_response import GetPgLogListResponse
from baiducloud_python_sdk_rds.models.obtain_binlog_information_response import ObtainBinlogInformationResponse
from baiducloud_python_sdk_rds.models.obtain_ssl_encryption_certificate_response import (
    ObtainSslEncryptionCertificateResponse,
)
from baiducloud_python_sdk_rds.models.obtain_ssl_encryption_information_response import (
    ObtainSslEncryptionInformationResponse,
)
from baiducloud_python_sdk_rds.models.query_account_details_response import QueryAccountDetailsResponse
from baiducloud_python_sdk_rds.models.query_account_list_response import QueryAccountListResponse
from baiducloud_python_sdk_rds.models.query_and_modify_history_response import QueryAndModifyHistoryResponse
from baiducloud_python_sdk_rds.models.query_backup_details_response import QueryBackupDetailsResponse
from baiducloud_python_sdk_rds.models.query_backup_list_response import QueryBackupListResponse
from baiducloud_python_sdk_rds.models.query_instance_list_response import QueryInstanceListResponse
from baiducloud_python_sdk_rds.models.query_parameter_list_response import QueryParameterListResponse
from baiducloud_python_sdk_rds.models.query_subnet_list_response import QuerySubnetListResponse
from baiducloud_python_sdk_rds.models.query_task_list_response import QueryTaskListResponse
from baiducloud_python_sdk_rds.models.query_the_details_of_the_specified_instance_response import (
    QueryTheDetailsOfTheSpecifiedInstanceResponse,
)
from baiducloud_python_sdk_rds.models.query_the_list_of_available_zones_response import (
    QueryTheListOfAvailableZonesResponse,
)
from baiducloud_python_sdk_rds.models.release_instance_response import ReleaseInstanceResponse
from baiducloud_python_sdk_rds.models.renewal_example_response import RenewalExampleResponse
from baiducloud_python_sdk_rds.models.retrieve_database_list_response import RetrieveDatabaseListResponse
from baiducloud_python_sdk_rds.models.retrieve_instance_auto_scaling_config_response import (
    RetrieveInstanceAutoScalingConfigResponse,
)
from baiducloud_python_sdk_rds.models.retrieve_the_binlog_list_response import RetrieveTheBinlogListResponse
from baiducloud_python_sdk_rds.models.slow_log_download_details_response import SlowLogDownloadDetailsResponse
from baiducloud_python_sdk_rds.models.slow_log_list_response import SlowLogListResponse
from baiducloud_python_sdk_rds.models.table_granularity_query_user_details_api_response import (
    TableGranularityQueryUserDetailsApiResponse,
)
from baiducloud_python_sdk_rds.models.table_granularity_query_user_list_api_response import (
    TableGranularityQueryUserListApiResponse,
)
from baiducloud_python_sdk_rds.models.target_region_mapping_list_api_response import TargetRegionMappingListApiResponse
from baiducloud_python_sdk_rds.models.transformation_example_response import TransformationExampleResponse

_logger = logging.getLogger(__name__)


class RdsClient(BceBaseClient):
    """
    rds base sdk client
    """

    VERSION_V1 = b'/v1'

    CONSTANT_INSTANCE = b'instance'

    CONSTANT_ACCOUNT = b'account'

    CONSTANT_V2 = b'v2'

    CONSTANT_TABLE_LEVEL = b'tableLevel'

    CONSTANT_UPDATE_DESC = b'update_desc'

    CONSTANT_STATUS = b'status'

    CONSTANT_BACKUP = b'backup'

    CONSTANT_BINLOGS = b'binlogs'

    CONSTANT_PARA_TEMPLATE = b'paraTemplate'

    CONSTANT_TEMPLATE = b'template'

    CONSTANT_DETAIL = b'detail'

    CONSTANT_PORT = b'port'

    CONSTANT_SLOWLOGS = b'slowlogs'

    CONSTANT_DOWNLOAD_URL = b'download_url'

    CONSTANT_V1 = b'v1'

    CONSTANT_TASK = b'task'

    CONSTANT_DESC = b'desc'

    CONSTANT_RENEW = b'renew'

    CONSTANT_PASSWORD = b'password'

    CONSTANT_SSL = b'ssl'

    CONSTANT_STATIC = b'static'

    CONSTANT_CA = b'ca'

    CONSTANT_AUTO_RESIZE_CONFIG = b'autoResizeConfig'

    CONSTANT_ZONE = b'zone'

    CONSTANT_DATABASES = b'databases'

    CONSTANT_PARAMETER = b'parameter'

    CONSTANT_HISTORY = b'history'

    CONSTANT_SUBNET = b'subnet'

    CONSTANT_SECURITY_IP = b'securityIp'

    CONSTANT_ERRORLOGS = b'errorlogs'

    CONSTANT_DUPLICATE = b'duplicate'

    CONSTANT_MAINTAINTIME = b'maintaintime'

    CONSTANT_TAGS = b'tags'

    CONSTANT_RECOVERY_TO_SOURCE_INSTANCE_BY_SNAPSHOT = b'recoveryToSourceInstanceBySnapshot'

    CONSTANT_DISK_AUTO_RESIZE = b'diskAutoResize'

    CONSTANT_CONFIG = b'config'

    CONSTANT_CREATE = b'create'

    CONSTANT_PROBE = b'probe'

    CONSTANT_LIST = b'list'

    CONSTANT_PG = b'pg'

    CONSTANT_LOG_LIST = b'logList'

    CONSTANT_PRIVILEGES = b'privileges'

    CONSTANT_RECOVERY_TO_SOURCE_INSTANCE_BY_DATETIME = b'recoveryToSourceInstanceByDatetime'

    CONSTANT_TARGET = b'target'

    CONSTANT_REGION = b'region'

    CONSTANT_REMARK = b'remark'

    CONSTANT_DOWNLOAD = b'download'

    CONSTANT_AUTO_EXPANSION = b'autoExpansion'

    def __init__(self, config=None):
        """
        Initialize the rds client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def add_account_api_at_table_granularity(self, request, config=None):
        """
        add_account_api_at_table_granularity

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            RdsClient.CONSTANT_V2,
            RdsClient.CONSTANT_INSTANCE,
            request.instance_id,
            RdsClient.CONSTANT_ACCOUNT,
            RdsClient.CONSTANT_TABLE_LEVEL,
            RdsClient.CONSTANT_CREATE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, config=merged_config)

    def batch_configuration_of_instances(self, request, config=None):
        """
        batch_configuration_of_instances

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BatchConfigurationOfInstancesResponse data
        :rtype: BatchConfigurationOfInstancesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE, request.instance_id)
        headers = None
        params = {}
        params['resize'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=BatchConfigurationOfInstancesResponse,
        )

    def binding_tags(self, request, config=None):
        """
        binding_tags

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE, RdsClient.CONSTANT_TAGS)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def change_account_password(self, request, config=None):
        """
        change_account_password

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1,
            RdsClient.CONSTANT_INSTANCE,
            request.instance_id,
            RdsClient.CONSTANT_ACCOUNT,
            request.account_name,
            RdsClient.CONSTANT_PASSWORD,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def check_the_whitelist(self, request, config=None):
        """
        check_the_whitelist

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CheckTheWhitelistResponse data
        :rtype: CheckTheWhitelistResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE, request.instance_id, RdsClient.CONSTANT_SECURITY_IP
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=CheckTheWhitelistResponse)

    def cluster_status_check(self, request, config=None):
        """
        cluster_status_check

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ClusterStatusCheckResponse data
        :rtype: ClusterStatusCheckResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE, request.instance_id, RdsClient.CONSTANT_STATUS
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=ClusterStatusCheckResponse)

    def copy_parameter_template(self, request, config=None):
        """
        copy_parameter_template

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1,
            RdsClient.CONSTANT_INSTANCE,
            RdsClient.CONSTANT_PARA_TEMPLATE,
            RdsClient.CONSTANT_DUPLICATE,
            RdsClient.CONSTANT_TEMPLATE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def create_a_database(self, request, config=None):
        """
        create_a_database

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE, request.instance_id, RdsClient.CONSTANT_DATABASES
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def create_a_primary_instance(self, request, config=None):
        """
        create_a_primary_instance

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateAPrimaryInstanceResponse data
        :rtype: CreateAPrimaryInstanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateAPrimaryInstanceResponse,
        )

    def create_a_proxy_instance(self, request, config=None):
        """
        create_a_proxy_instance

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateAProxyInstanceResponse data
        :rtype: CreateAProxyInstanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE)
        headers = None
        params = {}
        params['rdsproxy'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateAProxyInstanceResponse,
        )

    def create_account(self, request, config=None):
        """
        create_account

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE, request.instance_id, RdsClient.CONSTANT_ACCOUNT
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def create_read_only_instance(self, request, config=None):
        """
        create_read_only_instance

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateReadOnlyInstanceResponse data
        :rtype: CreateReadOnlyInstanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE)
        headers = None
        params = {}
        params['readReplica'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateReadOnlyInstanceResponse,
        )

    def delete_account(self, request, config=None):
        """
        delete_account

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1,
            RdsClient.CONSTANT_INSTANCE,
            request.instance_id,
            RdsClient.CONSTANT_ACCOUNT,
            request.account_name,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def delete_the_database(self, request, config=None):
        """
        delete_the_database

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1,
            RdsClient.CONSTANT_INSTANCE,
            request.instance_id,
            RdsClient.CONSTANT_DATABASES,
            request.db_name,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def delete_the_specified_backup_set(self, request, config=None):
        """
        delete_the_specified_backup_set

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1,
            RdsClient.CONSTANT_INSTANCE,
            request.instance_id,
            RdsClient.CONSTANT_BACKUP,
            request.snapshot_id,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def dial_test_interface(self, request, config=None):
        """
        dial_test_interface

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DialTestInterfaceResponse data
        :rtype: DialTestInterfaceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE, request.instance_id, RdsClient.CONSTANT_PROBE
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=DialTestInterfaceResponse)

    def does_the_instance_support_enabling_automatic_expansion(self, request, config=None):
        """
        does_the_instance_support_enabling_automatic_expansion

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DoesTheInstanceSupportEnablingAutomaticExpansionResponse data
        :rtype: DoesTheInstanceSupportEnablingAutomaticExpansionResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE, request.instance_id, RdsClient.CONSTANT_AUTO_EXPANSION
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            config=merged_config,
            model=DoesTheInstanceSupportEnablingAutomaticExpansionResponse,
        )

    def error_log_download_details(self, request, config=None):
        """
        error_log_download_details

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ErrorLogDownloadDetailsResponse data
        :rtype: ErrorLogDownloadDetailsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1,
            RdsClient.CONSTANT_INSTANCE,
            request.instance_id,
            RdsClient.CONSTANT_ERRORLOGS,
            RdsClient.CONSTANT_DOWNLOAD_URL,
            request.log_id,
            request.download_valid_time_in_sec,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=ErrorLogDownloadDetailsResponse
        )

    def error_log_list(self, request, config=None):
        """
        error_log_list

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ErrorLogListResponse data
        :rtype: ErrorLogListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1,
            RdsClient.CONSTANT_INSTANCE,
            request.instance_id,
            RdsClient.CONSTANT_ERRORLOGS,
            RdsClient.CONSTANT_LOG_LIST,
            request.datetime,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=ErrorLogListResponse)

    def get_parameter_template_details(self, request, config=None):
        """
        get_parameter_template_details

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetParameterTemplateDetailsResponse data
        :rtype: GetParameterTemplateDetailsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1,
            RdsClient.CONSTANT_INSTANCE,
            RdsClient.CONSTANT_PARA_TEMPLATE,
            RdsClient.CONSTANT_TEMPLATE,
            RdsClient.CONSTANT_DETAIL,
            request.template_id,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=GetParameterTemplateDetailsResponse
        )

    def get_parameter_template_list(self, request, config=None):
        """
        get_parameter_template_list

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetParameterTemplateListResponse data
        :rtype: GetParameterTemplateListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE, RdsClient.CONSTANT_PARA_TEMPLATE)
        headers = None
        params = {}
        params['pageNo'] = '1'
        params['pageSize'] = '10'
        params['type'] = 'system'
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        if request.db_type is not None:
            params['dbType'] = request.db_type
        if request.db_version is not None:
            params['dbVersion'] = request.db_version
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetParameterTemplateListResponse
        )

    def get_pg_log_details(self, request, config=None):
        """
        get_pg_log_details

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetPgLogDetailsResponse data
        :rtype: GetPgLogDetailsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1,
            RdsClient.CONSTANT_INSTANCE,
            request.instance_id,
            RdsClient.CONSTANT_PG,
            RdsClient.CONSTANT_DOWNLOAD,
        )
        headers = None
        params = {}
        if request.pglog_id is not None:
            params['pglogId'] = request.pglog_id
        if request.download_valid_time_in_sec is not None:
            params['downloadValidTimeInSec'] = request.download_valid_time_in_sec
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetPgLogDetailsResponse
        )

    def get_pg_log_list(self, request, config=None):
        """
        get_pg_log_list

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetPgLogListResponse data
        :rtype: GetPgLogListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1,
            RdsClient.CONSTANT_INSTANCE,
            request.instance_id,
            RdsClient.CONSTANT_PG,
            RdsClient.CONSTANT_LIST,
        )
        headers = None
        params = {}
        if request.var_date is not None:
            params['date'] = request.var_date
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetPgLogListResponse
        )

    def instance_enables_automatic_renewal(self, request, config=None):
        """
        instance_enables_automatic_renewal

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE)
        headers = None
        params = {}
        params['autoRenew'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def manually_initiate_full_physical_backup(self, request, config=None):
        """
        manually_initiate_full_physical_backup

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE, request.instance_id, RdsClient.CONSTANT_BACKUP
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def modify_account_notes(self, request, config=None):
        """
        modify_account_notes

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1,
            RdsClient.CONSTANT_INSTANCE,
            request.instance_id,
            RdsClient.CONSTANT_ACCOUNT,
            request.account_name,
            RdsClient.CONSTANT_DESC,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def modify_account_permissions(self, request, config=None):
        """
        modify_account_permissions

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1,
            RdsClient.CONSTANT_INSTANCE,
            request.instance_id,
            RdsClient.CONSTANT_ACCOUNT,
            request.account_name,
            RdsClient.CONSTANT_PRIVILEGES,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def modify_backup_strategy(self, request, config=None):
        """
        modify_backup_strategy

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE, request.instance_id)
        headers = None
        params = {}
        params['modifyBackupPolicy'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def modify_configuration_parameters(self, request, config=None):
        """
        modify_configuration_parameters

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE, request.instance_id, RdsClient.CONSTANT_PARAMETER
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def modify_database_port(self, request, config=None):
        """
        modify_database_port

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE, request.instance_id, RdsClient.CONSTANT_PORT
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def modify_description_information(self, request, config=None):
        """
        modify_description_information

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1,
            RdsClient.CONSTANT_INSTANCE,
            request.instance_id,
            RdsClient.CONSTANT_DATABASES,
            request.db_name,
            RdsClient.CONSTANT_REMARK,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def obtain_binlog_information(self, request, config=None):
        """
        obtain_binlog_information

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ObtainBinlogInformationResponse data
        :rtype: ObtainBinlogInformationResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1,
            RdsClient.CONSTANT_INSTANCE,
            request.instance_id,
            RdsClient.CONSTANT_BINLOGS,
            request.log_id,
            request.download_valid_time_in_sec,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=ObtainBinlogInformationResponse
        )

    def obtain_ssl_encryption_certificate(self, config=None):
        """
        obtain_ssl_encryption_certificate
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ObtainSslEncryptionCertificateResponse data
        :rtype: ObtainSslEncryptionCertificateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1,
            RdsClient.CONSTANT_INSTANCE,
            RdsClient.CONSTANT_SSL,
            RdsClient.CONSTANT_STATIC,
            RdsClient.CONSTANT_CA,
        )
        headers = None
        return self._send_request(
            http_methods.GET, path=path, config=config, model=ObtainSslEncryptionCertificateResponse
        )

    def obtain_ssl_encryption_information(self, request, config=None):
        """
        obtain_ssl_encryption_information

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ObtainSslEncryptionInformationResponse data
        :rtype: ObtainSslEncryptionInformationResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE, RdsClient.CONSTANT_SSL, request.instance_id
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=ObtainSslEncryptionInformationResponse
        )

    def query_account_details(self, request, config=None):
        """
        query_account_details

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryAccountDetailsResponse data
        :rtype: QueryAccountDetailsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1,
            RdsClient.CONSTANT_INSTANCE,
            request.instance_id,
            RdsClient.CONSTANT_ACCOUNT,
            request.account_name,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=QueryAccountDetailsResponse)

    def query_account_list(self, request, config=None):
        """
        query_account_list

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryAccountListResponse data
        :rtype: QueryAccountListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE, request.instance_id, RdsClient.CONSTANT_ACCOUNT
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=QueryAccountListResponse)

    def query_and_modify_history(self, request, config=None):
        """
        query_and_modify_history

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryAndModifyHistoryResponse data
        :rtype: QueryAndModifyHistoryResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1,
            RdsClient.CONSTANT_INSTANCE,
            request.instance_id,
            RdsClient.CONSTANT_PARAMETER,
            RdsClient.CONSTANT_HISTORY,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=QueryAndModifyHistoryResponse
        )

    def query_backup_details(self, request, config=None):
        """
        query_backup_details

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryBackupDetailsResponse data
        :rtype: QueryBackupDetailsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1,
            RdsClient.CONSTANT_INSTANCE,
            request.instance_id,
            RdsClient.CONSTANT_BACKUP,
            request.backup_id,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=QueryBackupDetailsResponse)

    def query_backup_list(self, request, config=None):
        """
        query_backup_list

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryBackupListResponse data
        :rtype: QueryBackupListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE, request.instance_id, RdsClient.CONSTANT_BACKUP
        )
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryBackupListResponse
        )

    def query_instance_list(self, request, config=None):
        """
        query_instance_list

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryInstanceListResponse data
        :rtype: QueryInstanceListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.vnet_ip is not None:
            params['vnetIp'] = request.vnet_ip
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryInstanceListResponse
        )

    def query_parameter_list(self, request, config=None):
        """
        query_parameter_list

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryParameterListResponse data
        :rtype: QueryParameterListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE, request.instance_id, RdsClient.CONSTANT_PARAMETER
        )
        headers = None
        params = {}
        params['keyword'] = 'keyword'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryParameterListResponse
        )

    def query_subnet_list(self, request, config=None):
        """
        query_subnet_list

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QuerySubnetListResponse data
        :rtype: QuerySubnetListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RdsClient.VERSION_V1, RdsClient.CONSTANT_SUBNET)
        headers = None
        params = {}
        if request.zone_name is not None:
            params['zoneName'] = request.zone_name
        if request.vpc_id is not None:
            params['vpcId'] = request.vpc_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QuerySubnetListResponse
        )

    def query_task_list(self, request, config=None):
        """
        query_task_list

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryTaskListResponse data
        :rtype: QueryTaskListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', RdsClient.CONSTANT_V1, RdsClient.CONSTANT_INSTANCE, RdsClient.CONSTANT_TASK)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=QueryTaskListResponse,
        )

    def query_the_details_of_the_specified_instance(self, request, config=None):
        """
        query_the_details_of_the_specified_instance

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryTheDetailsOfTheSpecifiedInstanceResponse data
        :rtype: QueryTheDetailsOfTheSpecifiedInstanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE, request.instance_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=QueryTheDetailsOfTheSpecifiedInstanceResponse
        )

    def query_the_list_of_available_zones(self, config=None):
        """
        query_the_list_of_available_zones
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryTheListOfAvailableZonesResponse data
        :rtype: QueryTheListOfAvailableZonesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RdsClient.VERSION_V1, RdsClient.CONSTANT_ZONE)
        headers = None
        return self._send_request(
            http_methods.GET, path=path, config=config, model=QueryTheListOfAvailableZonesResponse
        )

    def release_instance(self, request, config=None):
        """
        release_instance

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ReleaseInstanceResponse data
        :rtype: ReleaseInstanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE)
        headers = None
        params = {}
        if request.instance_ids is not None:
            params['instanceIds'] = request.instance_ids
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.DELETE, path=path, params=params, config=merged_config, model=ReleaseInstanceResponse
        )

    def renewal_example(self, request, config=None):
        """
        renewal_example

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing RenewalExampleResponse data
        :rtype: RenewalExampleResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', RdsClient.CONSTANT_V1, RdsClient.CONSTANT_INSTANCE, RdsClient.CONSTANT_RENEW)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=RenewalExampleResponse,
        )

    def restart_the_instance(self, request, config=None):
        """
        restart_the_instance

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE, request.instance_id)
        headers = None
        params = {}
        params['reboot'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def restore_library_tables_based_on_backup_sets(self, request, config=None):
        """
        restore_library_tables_based_on_backup_sets

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1,
            RdsClient.CONSTANT_INSTANCE,
            request.instance_id,
            RdsClient.CONSTANT_RECOVERY_TO_SOURCE_INSTANCE_BY_SNAPSHOT,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def restore_the_database_table_by_time_point(self, request, config=None):
        """
        restore_the_database_table_by_time_point

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1,
            RdsClient.CONSTANT_INSTANCE,
            request.instance_id,
            RdsClient.CONSTANT_RECOVERY_TO_SOURCE_INSTANCE_BY_DATETIME,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def retrieve_database_list(self, request, config=None):
        """
        retrieve_database_list

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing RetrieveDatabaseListResponse data
        :rtype: RetrieveDatabaseListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE, request.instance_id, RdsClient.CONSTANT_DATABASES
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=RetrieveDatabaseListResponse
        )

    def retrieve_instance_auto_scaling_config(self, request, config=None):
        """
        retrieve_instance_auto_scaling_config

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing RetrieveInstanceAutoScalingConfigResponse data
        :rtype: RetrieveInstanceAutoScalingConfigResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1,
            RdsClient.CONSTANT_INSTANCE,
            request.instance_id,
            RdsClient.CONSTANT_AUTO_RESIZE_CONFIG,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=RetrieveInstanceAutoScalingConfigResponse
        )

    def retrieve_the_binlog_list(self, request, config=None):
        """
        retrieve_the_binlog_list

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing RetrieveTheBinlogListResponse data
        :rtype: RetrieveTheBinlogListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1,
            RdsClient.CONSTANT_INSTANCE,
            request.instance_id,
            RdsClient.CONSTANT_BINLOGS,
            request.datetime,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=RetrieveTheBinlogListResponse
        )

    def set_encryption_policy_api(self, request, config=None):
        """
        set_encryption_policy_api

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', RdsClient.CONSTANT_V1, RdsClient.CONSTANT_INSTANCE, request.instance_id)
        headers = None
        params = {}
        params['updateEncryptPolicy'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def slow_log_download_details(self, request, config=None):
        """
        slow_log_download_details

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing SlowLogDownloadDetailsResponse data
        :rtype: SlowLogDownloadDetailsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1,
            RdsClient.CONSTANT_INSTANCE,
            request.instance_id,
            RdsClient.CONSTANT_SLOWLOGS,
            RdsClient.CONSTANT_DOWNLOAD_URL,
            request.log_id,
            request.download_valid_time_in_sec,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=SlowLogDownloadDetailsResponse
        )

    def slow_log_list(self, request, config=None):
        """
        slow_log_list

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing SlowLogListResponse data
        :rtype: SlowLogListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1,
            RdsClient.CONSTANT_INSTANCE,
            request.instance_id,
            RdsClient.CONSTANT_SLOWLOGS,
            RdsClient.CONSTANT_LOG_LIST,
            request.datetime,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=SlowLogListResponse)

    def table_granularity_query_user_details_api(self, request, config=None):
        """
        table_granularity_query_user_details_api

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing TableGranularityQueryUserDetailsApiResponse data
        :rtype: TableGranularityQueryUserDetailsApiResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            RdsClient.CONSTANT_V2,
            RdsClient.CONSTANT_INSTANCE,
            RdsClient.CONSTANT_ACCOUNT,
            RdsClient.CONSTANT_TABLE_LEVEL,
            RdsClient.CONSTANT_DETAIL,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=TableGranularityQueryUserDetailsApiResponse,
        )

    def table_granularity_query_user_list_api(self, request, config=None):
        """
        table_granularity_query_user_list_api

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing TableGranularityQueryUserListApiResponse data
        :rtype: TableGranularityQueryUserListApiResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            RdsClient.CONSTANT_V2,
            RdsClient.CONSTANT_INSTANCE,
            request.instance_id,
            RdsClient.CONSTANT_ACCOUNT,
            RdsClient.CONSTANT_TABLE_LEVEL,
            RdsClient.CONSTANT_LIST,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=TableGranularityQueryUserListApiResponse
        )

    def table_granularity_update_user_description_api(self, request, config=None):
        """
        table_granularity_update_user_description_api

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            RdsClient.CONSTANT_V2,
            RdsClient.CONSTANT_INSTANCE,
            RdsClient.CONSTANT_ACCOUNT,
            RdsClient.CONSTANT_TABLE_LEVEL,
            RdsClient.CONSTANT_UPDATE_DESC,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def target_region_mapping_list_api(self, request, config=None):
        """
        target_region_mapping_list_api

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing TargetRegionMappingListApiResponse data
        :rtype: TargetRegionMappingListApiResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            RdsClient.CONSTANT_V1,
            RdsClient.CONSTANT_INSTANCE,
            request.instance_id,
            RdsClient.CONSTANT_BACKUP,
            RdsClient.CONSTANT_TARGET,
            RdsClient.CONSTANT_REGION,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=TargetRegionMappingListApiResponse
        )

    def transformation_example(self, request, config=None):
        """
        transformation_example

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing TransformationExampleResponse data
        :rtype: TransformationExampleResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE, request.instance_id)
        headers = None
        params = {}
        params['resize'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=TransformationExampleResponse,
        )

    def update_automatic_storage_expansion_configuration(self, request, config=None):
        """
        update_automatic_storage_expansion_configuration

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1,
            RdsClient.CONSTANT_INSTANCE,
            request.instance_id,
            RdsClient.CONSTANT_DISK_AUTO_RESIZE,
            RdsClient.CONSTANT_CONFIG,
            request.action,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def update_instance_connection_information(self, request, config=None):
        """
        update_instance_connection_information

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE, request.instance_id)
        headers = None
        params = {}
        params['modifyEndpoint'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_instance_name(self, request, config=None):
        """
        update_instance_name

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE, request.instance_id)
        headers = None
        params = {}
        params['rename'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_instance_public_network_access_status(self, request, config=None):
        """
        update_instance_public_network_access_status

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE, request.instance_id)
        headers = None
        params = {}
        params['modifyPublicAccess'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_instance_synchronization_mode(self, request, config=None):
        """
        update_instance_synchronization_mode

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE, request.instance_id)
        headers = None
        params = {}
        params['modifySyncMode'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_time_window(self, request, config=None):
        """
        update_time_window

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE, request.instance_id, RdsClient.CONSTANT_MAINTAINTIME
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def update_whitelist(self, request, config=None):
        """
        update_whitelist

        :param request: Request entity containing all parameters
        :type request: RdsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            RdsClient.VERSION_V1, RdsClient.CONSTANT_INSTANCE, request.instance_id, RdsClient.CONSTANT_SECURITY_IP
        )
        headers = None
        params = {}
        if request.action is not None:
            params['action'] = request.action
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
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
        sign_fn, params = self._choose_signer(config, params)
        return bce_http_client.send_request(
            config, sign_fn, [handler.parse_error, body_parser], http_method, path, body, headers, params, model=model
        )
