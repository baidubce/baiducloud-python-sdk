"""
Example for ccr client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.auth import bce_v1_signer
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_ccr.models.create_project_response import CreateProjectResponse
from baiducloud_python_sdk_ccr.models.create_robot_account_response import CreateRobotAccountResponse
from baiducloud_python_sdk_ccr.models.create_temporary_password_response import CreateTemporaryPasswordResponse
from baiducloud_python_sdk_ccr.models.get_accelerator_filter_detail_response import GetAcceleratorFilterDetailResponse
from baiducloud_python_sdk_ccr.models.get_image_migration_execution_record_detail_response import (
    GetImageMigrationExecutionRecordDetailResponse,
)
from baiducloud_python_sdk_ccr.models.get_image_migration_rule_detail_response import (
    GetImageMigrationRuleDetailResponse,
)
from baiducloud_python_sdk_ccr.models.get_instance_detail_response import GetInstanceDetailResponse
from baiducloud_python_sdk_ccr.models.get_instance_sync_detail_response import GetInstanceSyncDetailResponse
from baiducloud_python_sdk_ccr.models.get_instance_sync_execution_detail_response import (
    GetInstanceSyncExecutionDetailResponse,
)
from baiducloud_python_sdk_ccr.models.get_project_detail_response import GetProjectDetailResponse
from baiducloud_python_sdk_ccr.models.get_public_network_config_response import GetPublicNetworkConfigResponse
from baiducloud_python_sdk_ccr.models.get_repository_response import GetRepositoryResponse
from baiducloud_python_sdk_ccr.models.get_tag_build_history_response import GetTagBuildHistoryResponse
from baiducloud_python_sdk_ccr.models.get_tag_detail_response import GetTagDetailResponse
from baiducloud_python_sdk_ccr.models.get_tags_scan_overview_response import GetTagsScanOverviewResponse
from baiducloud_python_sdk_ccr.models.get_trigger_detail_response import GetTriggerDetailResponse
from baiducloud_python_sdk_ccr.models.get_user_detail_response import GetUserDetailResponse
from baiducloud_python_sdk_ccr.models.list_accelerator_filters_response import ListAcceleratorFiltersResponse
from baiducloud_python_sdk_ccr.models.list_chart_versions_response import ListChartVersionsResponse
from baiducloud_python_sdk_ccr.models.list_charts_response import ListChartsResponse
from baiducloud_python_sdk_ccr.models.list_image_migration_records_response import ListImageMigrationRecordsResponse
from baiducloud_python_sdk_ccr.models.list_image_migration_rules_response import ListImageMigrationRulesResponse
from baiducloud_python_sdk_ccr.models.list_image_migration_task_records_response import (
    ListImageMigrationTaskRecordsResponse,
)
from baiducloud_python_sdk_ccr.models.list_instance_sync_records_response import ListInstanceSyncRecordsResponse
from baiducloud_python_sdk_ccr.models.list_instance_sync_task_records_response import (
    ListInstanceSyncTaskRecordsResponse,
)
from baiducloud_python_sdk_ccr.models.list_instance_syncs_response import ListInstanceSyncsResponse
from baiducloud_python_sdk_ccr.models.list_instances_response import ListInstancesResponse
from baiducloud_python_sdk_ccr.models.list_projects_response import ListProjectsResponse
from baiducloud_python_sdk_ccr.models.list_repositories_response import ListRepositoriesResponse
from baiducloud_python_sdk_ccr.models.list_robot_accounts_response import ListRobotAccountsResponse
from baiducloud_python_sdk_ccr.models.list_tags_response import ListTagsResponse
from baiducloud_python_sdk_ccr.models.list_trigger_tasks_response import ListTriggerTasksResponse
from baiducloud_python_sdk_ccr.models.list_triggers_response import ListTriggersResponse
from baiducloud_python_sdk_ccr.models.list_vpc_links_response import ListVpcLinksResponse
from baiducloud_python_sdk_ccr.models.refresh_robot_account_key_response import RefreshRobotAccountKeyResponse
from baiducloud_python_sdk_ccr.models.test_accelerator_filter_response import TestAcceleratorFilterResponse
from baiducloud_python_sdk_ccr.models.update_instance_name_response import UpdateInstanceNameResponse
from baiducloud_python_sdk_ccr.models.update_project_response import UpdateProjectResponse
from baiducloud_python_sdk_ccr.models.update_repository_response import UpdateRepositoryResponse

_logger = logging.getLogger(__name__)


class CcrClient(BceBaseClient):
    """
    ccr base sdk client
    """

    CONSTANT_V1 = b'v1'

    CONSTANT_INSTANCES = b'instances'

    CONSTANT_CREDENTIAL = b'credential'

    CONSTANT_PROJECTS = b'projects'

    CONSTANT_ACCELERATORS = b'accelerators'

    CONSTANT_POLICIES = b'policies'

    CONSTANT_FILTERS = b'filters'

    CONSTANT_SYNCS = b'syncs'

    CONSTANT_REPOSITORIES = b'repositories'

    CONSTANT_TAGS = b'tags'

    CONSTANT_BUILDHISTORY = b'buildhistory'

    CONSTANT_TRIGGERS = b'triggers'

    CONSTANT_EXECUTIONS = b'executions'

    CONSTANT_PUBLICLINKS = b'publiclinks'

    CONSTANT_ROBOTS = b'robots'

    CONSTANT_REPLICATIONS = b'replications'

    CONSTANT_SCANOVERVIEW = b'scanoverview'

    CONSTANT_TARGETS = b'targets'

    CONSTANT_TASKS = b'tasks'

    CONSTANT_SCAN = b'scan'

    CONSTANT_PRIVATELINKS = b'privatelinks'

    CONSTANT_CHARTS = b'charts'

    CONSTANT_VERSIONS = b'versions'

    CONSTANT_SECRET = b'secret'

    CONSTANT_LOG = b'log'

    CONSTANT_WHITELIST = b'whitelist'

    CONSTANT_USERS = b'users'

    CONSTANT_PROFILE = b'profile'

    CONSTANT_ENABLE = b'enable'

    CONSTANT_DOWNLOAD = b'download'

    CONSTANT_JOBS = b'jobs'

    CONSTANT_RETRY = b'retry'

    def __init__(self, config=None):
        """
        Initialize the ccr client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def add_public_network_whitelist(self, request, config=None):
        """
        add_public_network_whitelist

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_PUBLICLINKS,
            CcrClient.CONSTANT_WHITELIST,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def add_vpc_link(self, request, config=None):
        """
        add_vpc_link

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_PRIVATELINKS,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def create_accelerator_filter(self, request, config=None):
        """
        create_accelerator_filter

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_ACCELERATORS,
            CcrClient.CONSTANT_POLICIES,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def create_image_migration_rule(self, request, config=None):
        """
        create_image_migration_rule

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_REPLICATIONS,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def create_instance_sync(self, request, config=None):
        """
        create_instance_sync

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/', CcrClient.CONSTANT_V1, CcrClient.CONSTANT_INSTANCES, request.instance_id, CcrClient.CONSTANT_SYNCS
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def create_project(self, request, config=None):
        """
        create_project

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateProjectResponse data
        :rtype: CreateProjectResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/', CcrClient.CONSTANT_V1, CcrClient.CONSTANT_INSTANCES, request.instance_id, CcrClient.CONSTANT_PROJECTS
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateProjectResponse,
        )

    def create_robot_account(self, request, config=None):
        """
        create_robot_account

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateRobotAccountResponse data
        :rtype: CreateRobotAccountResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/', CcrClient.CONSTANT_V1, CcrClient.CONSTANT_INSTANCES, request.instance_id, CcrClient.CONSTANT_ROBOTS
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateRobotAccountResponse,
        )

    def create_temporary_password(self, request, config=None):
        """
        create_temporary_password

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateTemporaryPasswordResponse data
        :rtype: CreateTemporaryPasswordResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_CREDENTIAL,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateTemporaryPasswordResponse,
        )

    def create_trigger(self, request, config=None):
        """
        create_trigger

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_TRIGGERS,
            CcrClient.CONSTANT_POLICIES,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def delete_accelerator_filter(self, request, config=None):
        """
        delete_accelerator_filter

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_ACCELERATORS,
            CcrClient.CONSTANT_POLICIES,
            request.policy_id,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def delete_accelerator_filters(self, request, config=None):
        """
        delete_accelerator_filters

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_ACCELERATORS,
            CcrClient.CONSTANT_POLICIES,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, body=request.to_json_string(), config=merged_config)

    def delete_chart(self, request, config=None):
        """
        delete_chart

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_PROJECTS,
            request.project_name,
            CcrClient.CONSTANT_CHARTS,
            request.chart_name,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def delete_chart_version(self, request, config=None):
        """
        delete_chart_version

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_PROJECTS,
            request.project_name,
            CcrClient.CONSTANT_CHARTS,
            request.chart_name,
            CcrClient.CONSTANT_VERSIONS,
            request.chart_version,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def delete_chart_versions(self, request, config=None):
        """
        delete_chart_versions

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_PROJECTS,
            request.project_name,
            CcrClient.CONSTANT_CHARTS,
            request.chart_name,
            CcrClient.CONSTANT_VERSIONS,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, body=request.to_json_string(), config=merged_config)

    def delete_charts(self, request, config=None):
        """
        delete_charts

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_PROJECTS,
            request.project_name,
            CcrClient.CONSTANT_CHARTS,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, body=request.to_json_string(), config=merged_config)

    def delete_image_migration_rule(self, request, config=None):
        """
        delete_image_migration_rule

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_REPLICATIONS,
            request.policy_id,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def delete_instance_sync(self, request, config=None):
        """
        delete_instance_sync

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_SYNCS,
            request.policy_id,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def delete_project(self, request, config=None):
        """
        delete_project

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_PROJECTS,
            request.project_name,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def delete_projects(self, request, config=None):
        """
        delete_projects

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/', CcrClient.CONSTANT_V1, CcrClient.CONSTANT_INSTANCES, request.instance_id, CcrClient.CONSTANT_PROJECTS
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, body=request.to_json_string(), config=merged_config)

    def delete_public_network_whitelist(self, request, config=None):
        """
        delete_public_network_whitelist

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_PUBLICLINKS,
            CcrClient.CONSTANT_WHITELIST,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, body=request.to_json_string(), config=merged_config)

    def delete_repositories(self, request, config=None):
        """
        delete_repositories

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_PROJECTS,
            request.project_name,
            CcrClient.CONSTANT_REPOSITORIES,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, body=request.to_json_string(), config=merged_config)

    def delete_repository(self, request, config=None):
        """
        delete_repository

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_PROJECTS,
            request.project_name,
            CcrClient.CONSTANT_REPOSITORIES,
            request.repository_name,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def delete_robot_account(self, request, config=None):
        """
        delete_robot_account

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_ROBOTS,
            request.robot_id,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def delete_tag(self, request, config=None):
        """
        delete_tag

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_PROJECTS,
            request.project_name,
            CcrClient.CONSTANT_REPOSITORIES,
            request.repository_name,
            CcrClient.CONSTANT_TAGS,
            request.tag_name,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def delete_tags(self, request, config=None):
        """
        delete_tags

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_PROJECTS,
            request.project_name,
            CcrClient.CONSTANT_REPOSITORIES,
            request.repository_name,
            CcrClient.CONSTANT_TAGS,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, body=request.to_json_string(), config=merged_config)

    def delete_trigger(self, request, config=None):
        """
        delete_trigger

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_TRIGGERS,
            CcrClient.CONSTANT_POLICIES,
            request.policy_id,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def delete_triggers(self, request, config=None):
        """
        delete_triggers

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_TRIGGERS,
            CcrClient.CONSTANT_POLICIES,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, body=request.to_json_string(), config=merged_config)

    def delete_vpc_link(self, request, config=None):
        """
        delete_vpc_link

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_PRIVATELINKS,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, body=request.to_json_string(), config=merged_config)

    def download_chart(self, request, config=None):
        """
        download_chart

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_PROJECTS,
            request.project_name,
            CcrClient.CONSTANT_CHARTS,
            CcrClient.CONSTANT_DOWNLOAD,
            request.filename,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config)

    def execute_image_migration(self, request, config=None):
        """
        execute_image_migration

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_EXECUTIONS,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def execute_instance_sync(self, request, config=None):
        """
        execute_instance_sync

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_EXECUTIONS,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def get_accelerator_filter_detail(self, request, config=None):
        """
        get_accelerator_filter_detail

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetAcceleratorFilterDetailResponse data
        :rtype: GetAcceleratorFilterDetailResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_ACCELERATORS,
            CcrClient.CONSTANT_POLICIES,
            request.policy_id,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=GetAcceleratorFilterDetailResponse
        )

    def get_image_migration_execution_record_detail(self, request, config=None):
        """
        get_image_migration_execution_record_detail

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetImageMigrationExecutionRecordDetailResponse data
        :rtype: GetImageMigrationExecutionRecordDetailResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_EXECUTIONS,
            request.execution_id,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=GetImageMigrationExecutionRecordDetailResponse
        )

    def get_image_migration_rule_detail(self, request, config=None):
        """
        get_image_migration_rule_detail

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetImageMigrationRuleDetailResponse data
        :rtype: GetImageMigrationRuleDetailResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_REPLICATIONS,
            request.policy_id,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=GetImageMigrationRuleDetailResponse
        )

    def get_image_migration_task_logs(self, request, config=None):
        """
        get_image_migration_task_logs

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_EXECUTIONS,
            request.execution_id,
            CcrClient.CONSTANT_TASKS,
            request.task_id,
            CcrClient.CONSTANT_LOG,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config)

    def get_instance_detail(self, request, config=None):
        """
        get_instance_detail

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetInstanceDetailResponse data
        :rtype: GetInstanceDetailResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', CcrClient.CONSTANT_V1, CcrClient.CONSTANT_INSTANCES, request.instance_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetInstanceDetailResponse)

    def get_instance_sync_detail(self, request, config=None):
        """
        get_instance_sync_detail

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetInstanceSyncDetailResponse data
        :rtype: GetInstanceSyncDetailResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_SYNCS,
            request.policy_id,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=GetInstanceSyncDetailResponse
        )

    def get_instance_sync_execution_detail(self, request, config=None):
        """
        get_instance_sync_execution_detail

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetInstanceSyncExecutionDetailResponse data
        :rtype: GetInstanceSyncExecutionDetailResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_EXECUTIONS,
            request.execution_id,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=GetInstanceSyncExecutionDetailResponse
        )

    def get_instance_sync_task_logs(self, request, config=None):
        """
        get_instance_sync_task_logs

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_EXECUTIONS,
            request.execution_id,
            CcrClient.CONSTANT_TASKS,
            request.task_id,
            CcrClient.CONSTANT_LOG,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config)

    def get_project_detail(self, request, config=None):
        """
        get_project_detail

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetProjectDetailResponse data
        :rtype: GetProjectDetailResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_PROJECTS,
            request.project_name,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetProjectDetailResponse)

    def get_public_network_config(self, request, config=None):
        """
        get_public_network_config

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetPublicNetworkConfigResponse data
        :rtype: GetPublicNetworkConfigResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_PUBLICLINKS,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=GetPublicNetworkConfigResponse
        )

    def get_repository(self, request, config=None):
        """
        get_repository

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetRepositoryResponse data
        :rtype: GetRepositoryResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_PROJECTS,
            request.project_name,
            CcrClient.CONSTANT_REPOSITORIES,
            request.repository_name,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetRepositoryResponse)

    def get_tag_build_history(self, request, config=None):
        """
        get_tag_build_history

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetTagBuildHistoryResponse data
        :rtype: GetTagBuildHistoryResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_PROJECTS,
            request.project_name,
            CcrClient.CONSTANT_REPOSITORIES,
            request.repository_name,
            CcrClient.CONSTANT_TAGS,
            request.tag_name,
            CcrClient.CONSTANT_BUILDHISTORY,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetTagBuildHistoryResponse)

    def get_tag_detail(self, request, config=None):
        """
        get_tag_detail

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetTagDetailResponse data
        :rtype: GetTagDetailResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_PROJECTS,
            request.project_name,
            CcrClient.CONSTANT_REPOSITORIES,
            request.repository_name,
            CcrClient.CONSTANT_TAGS,
            request.tag_name,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetTagDetailResponse)

    def get_tags_scan_overview(self, request, config=None):
        """
        get_tags_scan_overview

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetTagsScanOverviewResponse data
        :rtype: GetTagsScanOverviewResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_PROJECTS,
            request.project_name,
            CcrClient.CONSTANT_REPOSITORIES,
            request.repository_name,
            CcrClient.CONSTANT_TAGS,
            request.tag_name,
            CcrClient.CONSTANT_SCANOVERVIEW,
        )
        headers = None
        params = {}
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetTagsScanOverviewResponse
        )

    def get_trigger_detail(self, request, config=None):
        """
        get_trigger_detail

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetTriggerDetailResponse data
        :rtype: GetTriggerDetailResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_TRIGGERS,
            CcrClient.CONSTANT_POLICIES,
            request.policy_id,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetTriggerDetailResponse)

    def get_user_detail(self, request, config=None):
        """
        get_user_detail

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetUserDetailResponse data
        :rtype: GetUserDetailResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', CcrClient.CONSTANT_V1, CcrClient.CONSTANT_USERS, CcrClient.CONSTANT_PROFILE)
        headers = None
        params = {}
        if request.user_id is not None:
            params['userId'] = request.user_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetUserDetailResponse
        )

    def list_accelerator_filters(self, request, config=None):
        """
        list_accelerator_filters

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListAcceleratorFiltersResponse data
        :rtype: ListAcceleratorFiltersResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_ACCELERATORS,
            CcrClient.CONSTANT_POLICIES,
        )
        headers = None
        params = {}
        if request.policy_name is not None:
            params['policyName'] = request.policy_name
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListAcceleratorFiltersResponse
        )

    def list_chart_versions(self, request, config=None):
        """
        list_chart_versions

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListChartVersionsResponse data
        :rtype: ListChartVersionsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_PROJECTS,
            request.project_name,
            CcrClient.CONSTANT_CHARTS,
            request.chart_name,
            CcrClient.CONSTANT_VERSIONS,
        )
        headers = None
        params = {}
        if request.chart_version is not None:
            params['chartVersion'] = request.chart_version
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListChartVersionsResponse
        )

    def list_charts(self, request, config=None):
        """
        list_charts

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListChartsResponse data
        :rtype: ListChartsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_PROJECTS,
            request.project_name,
            CcrClient.CONSTANT_CHARTS,
        )
        headers = None
        params = {}
        if request.chart_name is not None:
            params['chartName'] = request.chart_name
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListChartsResponse
        )

    def list_image_migration_records(self, request, config=None):
        """
        list_image_migration_records

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListImageMigrationRecordsResponse data
        :rtype: ListImageMigrationRecordsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_EXECUTIONS,
        )
        headers = None
        params = {}
        if request.policy_id is not None:
            params['policyId'] = request.policy_id
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListImageMigrationRecordsResponse
        )

    def list_image_migration_rules(self, request, config=None):
        """
        list_image_migration_rules

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListImageMigrationRulesResponse data
        :rtype: ListImageMigrationRulesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_REPLICATIONS,
        )
        headers = None
        params = {}
        if request.policy_name is not None:
            params['policyName'] = request.policy_name
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListImageMigrationRulesResponse
        )

    def list_image_migration_task_records(self, request, config=None):
        """
        list_image_migration_task_records

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListImageMigrationTaskRecordsResponse data
        :rtype: ListImageMigrationTaskRecordsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_EXECUTIONS,
            request.execution_id,
            CcrClient.CONSTANT_TASKS,
        )
        headers = None
        params = {}
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
            model=ListImageMigrationTaskRecordsResponse,
        )

    def list_instance_sync_records(self, request, config=None):
        """
        list_instance_sync_records

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListInstanceSyncRecordsResponse data
        :rtype: ListInstanceSyncRecordsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_EXECUTIONS,
        )
        headers = None
        params = {}
        if request.policy_id is not None:
            params['policyId'] = request.policy_id
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListInstanceSyncRecordsResponse
        )

    def list_instance_sync_task_records(self, request, config=None):
        """
        list_instance_sync_task_records

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListInstanceSyncTaskRecordsResponse data
        :rtype: ListInstanceSyncTaskRecordsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_EXECUTIONS,
            request.execution_id,
            CcrClient.CONSTANT_TASKS,
        )
        headers = None
        params = {}
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListInstanceSyncTaskRecordsResponse
        )

    def list_instance_syncs(self, request, config=None):
        """
        list_instance_syncs

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListInstanceSyncsResponse data
        :rtype: ListInstanceSyncsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/', CcrClient.CONSTANT_V1, CcrClient.CONSTANT_INSTANCES, request.instance_id, CcrClient.CONSTANT_SYNCS
        )
        headers = None
        params = {}
        if request.policy_name is not None:
            params['policyName'] = request.policy_name
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListInstanceSyncsResponse
        )

    def list_instances(self, request, config=None):
        """
        list_instances

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListInstancesResponse data
        :rtype: ListInstancesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', CcrClient.CONSTANT_V1, CcrClient.CONSTANT_INSTANCES)
        headers = None
        params = {}
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        if request.keyword_type is not None:
            params['keywordType'] = request.keyword_type
        if request.keyword is not None:
            params['keyword'] = request.keyword
        if request.acrossregion is not None:
            params['acrossregion'] = request.acrossregion
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListInstancesResponse
        )

    def list_projects(self, request, config=None):
        """
        list_projects

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListProjectsResponse data
        :rtype: ListProjectsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/', CcrClient.CONSTANT_V1, CcrClient.CONSTANT_INSTANCES, request.instance_id, CcrClient.CONSTANT_PROJECTS
        )
        headers = None
        params = {}
        if request.project_name is not None:
            params['projectName'] = request.project_name
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListProjectsResponse
        )

    def list_repositories(self, request, config=None):
        """
        list_repositories

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListRepositoriesResponse data
        :rtype: ListRepositoriesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_PROJECTS,
            request.project_name,
            CcrClient.CONSTANT_REPOSITORIES,
        )
        headers = None
        params = {}
        if request.repository_name is not None:
            params['repositoryName'] = request.repository_name
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListRepositoriesResponse
        )

    def list_robot_accounts(self, request, config=None):
        """
        list_robot_accounts

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListRobotAccountsResponse data
        :rtype: ListRobotAccountsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/', CcrClient.CONSTANT_V1, CcrClient.CONSTANT_INSTANCES, request.instance_id, CcrClient.CONSTANT_ROBOTS
        )
        headers = None
        params = {}
        if request.status is not None:
            params['status'] = request.status
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListRobotAccountsResponse
        )

    def list_tags(self, request, config=None):
        """
        list_tags

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListTagsResponse data
        :rtype: ListTagsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_PROJECTS,
            request.project_name,
            CcrClient.CONSTANT_REPOSITORIES,
            request.repository_name,
            CcrClient.CONSTANT_TAGS,
        )
        headers = None
        params = {}
        if request.tag_name is not None:
            params['tagName'] = request.tag_name
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListTagsResponse
        )

    def list_trigger_tasks(self, request, config=None):
        """
        list_trigger_tasks

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListTriggerTasksResponse data
        :rtype: ListTriggerTasksResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_TRIGGERS,
            CcrClient.CONSTANT_POLICIES,
            request.policy_id,
            CcrClient.CONSTANT_JOBS,
        )
        headers = None
        params = {}
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListTriggerTasksResponse
        )

    def list_triggers(self, request, config=None):
        """
        list_triggers

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListTriggersResponse data
        :rtype: ListTriggersResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_TRIGGERS,
            CcrClient.CONSTANT_POLICIES,
        )
        headers = None
        params = {}
        if request.policy_name is not None:
            params['policyName'] = request.policy_name
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListTriggersResponse
        )

    def list_vpc_links(self, request, config=None):
        """
        list_vpc_links

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListVpcLinksResponse data
        :rtype: ListVpcLinksResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_PRIVATELINKS,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=ListVpcLinksResponse)

    def re_execute_trigger_task(self, request, config=None):
        """
        re_execute_trigger_task

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_TRIGGERS,
            CcrClient.CONSTANT_POLICIES,
            request.policy_id,
            CcrClient.CONSTANT_JOBS,
            request.job_id,
            CcrClient.CONSTANT_RETRY,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, config=merged_config)

    def refresh_robot_account_key(self, request, config=None):
        """
        refresh_robot_account_key

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing RefreshRobotAccountKeyResponse data
        :rtype: RefreshRobotAccountKeyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_ROBOTS,
            request.robot_id,
            CcrClient.CONSTANT_SECRET,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=RefreshRobotAccountKeyResponse,
        )

    def reset_password(self, request, config=None):
        """
        reset_password

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_CREDENTIAL,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def stop_image_migration(self, request, config=None):
        """
        stop_image_migration

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_EXECUTIONS,
            request.execution_id,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, config=merged_config)

    def stop_instance_sync(self, request, config=None):
        """
        stop_instance_sync

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_EXECUTIONS,
            request.execution_id,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, config=merged_config)

    def test_accelerator_filter(self, request, config=None):
        """
        test_accelerator_filter

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing TestAcceleratorFilterResponse data
        :rtype: TestAcceleratorFilterResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_ACCELERATORS,
            CcrClient.CONSTANT_POLICIES,
            CcrClient.CONSTANT_FILTERS,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=TestAcceleratorFilterResponse,
        )

    def test_trigger_target_address(self, request, config=None):
        """
        test_trigger_target_address

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_TRIGGERS,
            CcrClient.CONSTANT_POLICIES,
            CcrClient.CONSTANT_TARGETS,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def toggle_accelerator_filter(self, request, config=None):
        """
        toggle_accelerator_filter

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_ACCELERATORS,
            CcrClient.CONSTANT_POLICIES,
            request.policy_id,
            CcrClient.CONSTANT_ENABLE,
        )
        headers = None
        params = {}
        if request.enabled is not None:
            params['enabled'] = request.enabled
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def toggle_trigger(self, request, config=None):
        """
        toggle_trigger

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_TRIGGERS,
            CcrClient.CONSTANT_POLICIES,
            request.policy_id,
            CcrClient.CONSTANT_ENABLE,
        )
        headers = None
        params = {}
        if request.enabled is not None:
            params['enabled'] = request.enabled
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def trigger_tag_scan(self, request, config=None):
        """
        trigger_tag_scan

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_PROJECTS,
            request.project_name,
            CcrClient.CONSTANT_REPOSITORIES,
            request.repository_name,
            CcrClient.CONSTANT_TAGS,
            request.tag_name,
            CcrClient.CONSTANT_SCAN,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, config=merged_config)

    def update_accelerator_filter(self, request, config=None):
        """
        update_accelerator_filter

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_ACCELERATORS,
            CcrClient.CONSTANT_POLICIES,
            request.policy_id,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def update_image_migration_rule(self, request, config=None):
        """
        update_image_migration_rule

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_REPLICATIONS,
            request.policy_id,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def update_instance_name(self, request, config=None):
        """
        update_instance_name

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UpdateInstanceNameResponse data
        :rtype: UpdateInstanceNameResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', CcrClient.CONSTANT_V1, CcrClient.CONSTANT_INSTANCES, request.instance_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=UpdateInstanceNameResponse,
        )

    def update_instance_sync(self, request, config=None):
        """
        update_instance_sync

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_SYNCS,
            request.policy_id,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def update_instance_tags(self, request, config=None):
        """
        update_instance_tags

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/', CcrClient.CONSTANT_V1, CcrClient.CONSTANT_INSTANCES, request.instance_id, CcrClient.CONSTANT_TAGS
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def update_project(self, request, config=None):
        """
        update_project

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UpdateProjectResponse data
        :rtype: UpdateProjectResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_PROJECTS,
            request.project_name,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=UpdateProjectResponse,
        )

    def update_public_network(self, request, config=None):
        """
        update_public_network

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_PUBLICLINKS,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def update_repository(self, request, config=None):
        """
        update_repository

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UpdateRepositoryResponse data
        :rtype: UpdateRepositoryResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_PROJECTS,
            request.project_name,
            CcrClient.CONSTANT_REPOSITORIES,
            request.repository_name,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=UpdateRepositoryResponse,
        )

    def update_robot_account(self, request, config=None):
        """
        update_robot_account

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_ROBOTS,
            request.robot_id,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def update_trigger(self, request, config=None):
        """
        update_trigger

        :param request: Request entity containing all parameters
        :type request: CcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CcrClient.CONSTANT_V1,
            CcrClient.CONSTANT_INSTANCES,
            request.instance_id,
            CcrClient.CONSTANT_TRIGGERS,
            CcrClient.CONSTANT_POLICIES,
            request.policy_id,
        )
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
