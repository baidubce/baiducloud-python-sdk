"""
Example for rapidfs client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.auth import bce_v1_signer
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_rapidfs.models.add_cache_nodes_response import AddCacheNodesResponse
from baiducloud_python_sdk_rapidfs.models.check_before_add_cache_nodes_response import CheckBeforeAddCacheNodesResponse
from baiducloud_python_sdk_rapidfs.models.check_before_create_instance_response import (
    CheckBeforeCreateInstanceResponse,
)
from baiducloud_python_sdk_rapidfs.models.create_auth_group_response import CreateAuthGroupResponse
from baiducloud_python_sdk_rapidfs.models.create_cache_rule_response import CreateCacheRuleResponse
from baiducloud_python_sdk_rapidfs.models.create_instance_response import CreateInstanceResponse
from baiducloud_python_sdk_rapidfs.models.create_meta_sync_rule_response import CreateMetaSyncRuleResponse
from baiducloud_python_sdk_rapidfs.models.delete_instance_response import DeleteInstanceResponse
from baiducloud_python_sdk_rapidfs.models.describe_aihc_resource_pools_response import (
    DescribeAihcResourcePoolsResponse,
)
from baiducloud_python_sdk_rapidfs.models.describe_allocatable_data_src_quota_response import (
    DescribeAllocatableDataSrcQuotaResponse,
)
from baiducloud_python_sdk_rapidfs.models.describe_auth_group_response import DescribeAuthGroupResponse
from baiducloud_python_sdk_rapidfs.models.describe_auth_groups_response import DescribeAuthGroupsResponse
from baiducloud_python_sdk_rapidfs.models.describe_cache_deploy_group_response import DescribeCacheDeployGroupResponse
from baiducloud_python_sdk_rapidfs.models.describe_cache_deploy_groups_response import (
    DescribeCacheDeployGroupsResponse,
)
from baiducloud_python_sdk_rapidfs.models.describe_cache_node_response import DescribeCacheNodeResponse
from baiducloud_python_sdk_rapidfs.models.describe_cache_node_bcc_candidates_response import (
    DescribeCacheNodeBccCandidatesResponse,
)
from baiducloud_python_sdk_rapidfs.models.describe_cache_node_quota_response import DescribeCacheNodeQuotaResponse
from baiducloud_python_sdk_rapidfs.models.describe_cache_nodes_response import DescribeCacheNodesResponse
from baiducloud_python_sdk_rapidfs.models.describe_cache_rule_response import DescribeCacheRuleResponse
from baiducloud_python_sdk_rapidfs.models.describe_cache_rule_jobs_response import DescribeCacheRuleJobsResponse
from baiducloud_python_sdk_rapidfs.models.describe_cache_rules_response import DescribeCacheRulesResponse
from baiducloud_python_sdk_rapidfs.models.describe_cce_clusters_response import DescribeCceClustersResponse
from baiducloud_python_sdk_rapidfs.models.describe_data_src_response import DescribeDataSrcResponse
from baiducloud_python_sdk_rapidfs.models.describe_data_srcs_response import DescribeDataSrcsResponse
from baiducloud_python_sdk_rapidfs.models.describe_instance_response import DescribeInstanceResponse
from baiducloud_python_sdk_rapidfs.models.describe_instances_response import DescribeInstancesResponse
from baiducloud_python_sdk_rapidfs.models.describe_meta_sync_jobs_response import DescribeMetaSyncJobsResponse
from baiducloud_python_sdk_rapidfs.models.describe_meta_sync_rule_response import DescribeMetaSyncRuleResponse
from baiducloud_python_sdk_rapidfs.models.describe_meta_sync_rules_response import DescribeMetaSyncRulesResponse
from baiducloud_python_sdk_rapidfs.models.describe_order_response import DescribeOrderResponse
from baiducloud_python_sdk_rapidfs.models.describe_price_response import DescribePriceResponse
from baiducloud_python_sdk_rapidfs.models.describe_specs_response import DescribeSpecsResponse
from baiducloud_python_sdk_rapidfs.models.describe_token_response import DescribeTokenResponse
from baiducloud_python_sdk_rapidfs.models.describe_zones_response import DescribeZonesResponse
from baiducloud_python_sdk_rapidfs.models.import_data_src_response import ImportDataSrcResponse
from baiducloud_python_sdk_rapidfs.models.remove_data_src_response import RemoveDataSrcResponse
from baiducloud_python_sdk_rapidfs.models.resize_instance_response import ResizeInstanceResponse

_logger = logging.getLogger(__name__)


class RapidfsClient(BceBaseClient):
    """
    rapidfs base sdk client
    """

    VERSION_V2 = b'/v2'

    CONSTANT_CACHENODE = b'cachenode'

    CONSTANT_ORDER = b'order'

    CONSTANT_AUTHGROUP = b'authgroup'

    CONSTANT_INSTANCE = b'instance'

    CONSTANT_METASYNCRULE = b'metasyncrule'

    CONSTANT_DATASRC = b'datasrc'

    CONSTANT_CACHEDEPLOYGROUP = b'cachedeploygroup'

    CONSTANT_CACHERULE = b'cacherule'

    CONSTANT_AIHCRESOURCEPOOL = b'aihcresourcepool'

    CONSTANT_TAG = b'tag'

    CONSTANT_CCECLUSTER = b'ccecluster'

    CONSTANT_ZONE = b'zone'

    CONSTANT_PRICE = b'price'

    CONSTANT_SPECIFICATION = b'specification'

    def __init__(self, config=None):
        """
        Initialize the rapidfs client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def add_cache_nodes(self, request, config=None):
        """
        add_cache_nodes

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing AddCacheNodesResponse data
        :rtype: AddCacheNodesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_CACHENODE)
        headers = None
        params = {}
        params['action'] = 'AddCacheNodes'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=AddCacheNodesResponse,
        )

    def cancel_cache_rule_job(self, request, config=None):
        """
        cancel_cache_rule_job

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_CACHERULE)
        headers = None
        params = {}
        params['action'] = 'CancelCacheRuleJob'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def cancel_meta_sync_job(self, request, config=None):
        """
        cancel_meta_sync_job

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_METASYNCRULE)
        headers = None
        params = {}
        params['action'] = 'CancelMetaSyncJob'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def check_before_add_cache_nodes(self, request, config=None):
        """
        check_before_add_cache_nodes

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CheckBeforeAddCacheNodesResponse data
        :rtype: CheckBeforeAddCacheNodesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_CACHENODE)
        headers = None
        params = {}
        params['action'] = 'CheckBeforeAddCacheNodes'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CheckBeforeAddCacheNodesResponse,
        )

    def check_before_create_instance(self, request, config=None):
        """
        check_before_create_instance

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CheckBeforeCreateInstanceResponse data
        :rtype: CheckBeforeCreateInstanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_INSTANCE)
        headers = None
        params = {}
        params['action'] = 'CheckBeforeCreateInstance'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CheckBeforeCreateInstanceResponse,
        )

    def create_and_assign_tag(self, request, config=None):
        """
        create_and_assign_tag

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_TAG)
        headers = None
        params = {}
        params['action'] = 'CreateAndAssignTag'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def create_auth_group(self, request, config=None):
        """
        create_auth_group

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateAuthGroupResponse data
        :rtype: CreateAuthGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_AUTHGROUP)
        headers = None
        params = {}
        params['action'] = 'CreateAuthGroup'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateAuthGroupResponse,
        )

    def create_cache_rule(self, request, config=None):
        """
        create_cache_rule

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateCacheRuleResponse data
        :rtype: CreateCacheRuleResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_CACHERULE)
        headers = None
        params = {}
        params['action'] = 'CreateCacheRule'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateCacheRuleResponse,
        )

    def create_instance(self, request, config=None):
        """
        create_instance

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateInstanceResponse data
        :rtype: CreateInstanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_INSTANCE)
        headers = None
        params = {}
        params['action'] = 'CreateInstance'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateInstanceResponse,
        )

    def create_meta_sync_rule(self, request, config=None):
        """
        create_meta_sync_rule

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateMetaSyncRuleResponse data
        :rtype: CreateMetaSyncRuleResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_METASYNCRULE)
        headers = None
        params = {}
        params['action'] = 'CreateMetaSyncRule'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateMetaSyncRuleResponse,
        )

    def delete_auth_group(self, request, config=None):
        """
        delete_auth_group

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_AUTHGROUP)
        headers = None
        params = {}
        params['action'] = 'DeleteAuthGroup'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def delete_cache_rule(self, request, config=None):
        """
        delete_cache_rule

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_CACHERULE)
        headers = None
        params = {}
        params['action'] = 'DeleteCacheRule'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def delete_instance(self, request, config=None):
        """
        delete_instance

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DeleteInstanceResponse data
        :rtype: DeleteInstanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_INSTANCE)
        headers = None
        params = {}
        params['action'] = 'DeleteInstance'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DeleteInstanceResponse,
        )

    def delete_meta_sync_rule(self, request, config=None):
        """
        delete_meta_sync_rule

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_METASYNCRULE)
        headers = None
        params = {}
        params['action'] = 'DeleteMetaSyncRule'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def describe_aihc_resource_pools(self, request, config=None):
        """
        describe_aihc_resource_pools

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeAihcResourcePoolsResponse data
        :rtype: DescribeAihcResourcePoolsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_AIHCRESOURCEPOOL)
        headers = None
        params = {}
        params['action'] = 'DescribeAihcResourcePools'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeAihcResourcePoolsResponse,
        )

    def describe_allocatable_data_src_quota(self, request, config=None):
        """
        describe_allocatable_data_src_quota

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeAllocatableDataSrcQuotaResponse data
        :rtype: DescribeAllocatableDataSrcQuotaResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_DATASRC)
        headers = None
        params = {}
        params['action'] = 'DescribeAllocatableDataSrcQuota'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeAllocatableDataSrcQuotaResponse,
        )

    def describe_auth_group(self, request, config=None):
        """
        describe_auth_group

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeAuthGroupResponse data
        :rtype: DescribeAuthGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_AUTHGROUP)
        headers = None
        params = {}
        params['action'] = 'DescribeAuthGroup'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeAuthGroupResponse,
        )

    def describe_auth_groups(self, request, config=None):
        """
        describe_auth_groups

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeAuthGroupsResponse data
        :rtype: DescribeAuthGroupsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_AUTHGROUP)
        headers = None
        params = {}
        params['action'] = 'DescribeAuthGroups'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeAuthGroupsResponse,
        )

    def describe_cache_deploy_group(self, request, config=None):
        """
        describe_cache_deploy_group

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeCacheDeployGroupResponse data
        :rtype: DescribeCacheDeployGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_CACHEDEPLOYGROUP)
        headers = None
        params = {}
        params['action'] = 'DescribeCacheDeployGroup'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeCacheDeployGroupResponse,
        )

    def describe_cache_deploy_groups(self, request, config=None):
        """
        describe_cache_deploy_groups

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeCacheDeployGroupsResponse data
        :rtype: DescribeCacheDeployGroupsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_CACHEDEPLOYGROUP)
        headers = None
        params = {}
        params['action'] = 'DescribeCacheDeployGroups'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeCacheDeployGroupsResponse,
        )

    def describe_cache_node(self, request, config=None):
        """
        describe_cache_node

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeCacheNodeResponse data
        :rtype: DescribeCacheNodeResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_CACHENODE)
        headers = None
        params = {}
        params['action'] = 'DescribeCacheNode'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeCacheNodeResponse,
        )

    def describe_cache_node_bcc_candidates(self, request, config=None):
        """
        describe_cache_node_bcc_candidates

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeCacheNodeBccCandidatesResponse data
        :rtype: DescribeCacheNodeBccCandidatesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_CACHENODE)
        headers = None
        params = {}
        params['action'] = 'DescribeCacheNodeBccCandidates'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeCacheNodeBccCandidatesResponse,
        )

    def describe_cache_node_quota(self, request, config=None):
        """
        describe_cache_node_quota

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeCacheNodeQuotaResponse data
        :rtype: DescribeCacheNodeQuotaResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_CACHENODE)
        headers = None
        params = {}
        params['action'] = 'DescribeCacheNodeQuota'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeCacheNodeQuotaResponse,
        )

    def describe_cache_nodes(self, request, config=None):
        """
        describe_cache_nodes

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeCacheNodesResponse data
        :rtype: DescribeCacheNodesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_CACHENODE)
        headers = None
        params = {}
        params['action'] = 'DescribeCacheNodes'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeCacheNodesResponse,
        )

    def describe_cache_rule(self, request, config=None):
        """
        describe_cache_rule

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeCacheRuleResponse data
        :rtype: DescribeCacheRuleResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_CACHERULE)
        headers = None
        params = {}
        params['action'] = 'DescribeCacheRule'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeCacheRuleResponse,
        )

    def describe_cache_rule_jobs(self, request, config=None):
        """
        describe_cache_rule_jobs

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeCacheRuleJobsResponse data
        :rtype: DescribeCacheRuleJobsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_CACHERULE)
        headers = None
        params = {}
        params['action'] = 'DescribeCacheRuleJobs'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeCacheRuleJobsResponse,
        )

    def describe_cache_rules(self, request, config=None):
        """
        describe_cache_rules

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeCacheRulesResponse data
        :rtype: DescribeCacheRulesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_CACHERULE)
        headers = None
        params = {}
        params['action'] = 'DescribeCacheRules'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeCacheRulesResponse,
        )

    def describe_cce_clusters(self, request, config=None):
        """
        describe_cce_clusters

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeCceClustersResponse data
        :rtype: DescribeCceClustersResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_CCECLUSTER)
        headers = None
        params = {}
        params['action'] = 'DescribeCceClusters'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeCceClustersResponse,
        )

    def describe_data_src(self, request, config=None):
        """
        describe_data_src

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeDataSrcResponse data
        :rtype: DescribeDataSrcResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_DATASRC)
        headers = None
        params = {}
        params['action'] = 'DescribeDataSrc'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeDataSrcResponse,
        )

    def describe_data_srcs(self, request, config=None):
        """
        describe_data_srcs

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeDataSrcsResponse data
        :rtype: DescribeDataSrcsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_DATASRC)
        headers = None
        params = {}
        params['action'] = 'DescribeDataSrcs'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeDataSrcsResponse,
        )

    def describe_instance(self, request, config=None):
        """
        describe_instance

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeInstanceResponse data
        :rtype: DescribeInstanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_INSTANCE)
        headers = None
        params = {}
        params['action'] = 'DescribeInstance'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeInstanceResponse,
        )

    def describe_instances(self, request, config=None):
        """
        describe_instances

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeInstancesResponse data
        :rtype: DescribeInstancesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_INSTANCE)
        headers = None
        params = {}
        params['action'] = 'DescribeInstances'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeInstancesResponse,
        )

    def describe_meta_sync_jobs(self, request, config=None):
        """
        describe_meta_sync_jobs

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeMetaSyncJobsResponse data
        :rtype: DescribeMetaSyncJobsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_METASYNCRULE)
        headers = None
        params = {}
        params['action'] = 'DescribeMetaSyncJobs'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeMetaSyncJobsResponse,
        )

    def describe_meta_sync_rule(self, request, config=None):
        """
        describe_meta_sync_rule

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeMetaSyncRuleResponse data
        :rtype: DescribeMetaSyncRuleResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_METASYNCRULE)
        headers = None
        params = {}
        params['action'] = 'DescribeMetaSyncRule'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeMetaSyncRuleResponse,
        )

    def describe_meta_sync_rules(self, request, config=None):
        """
        describe_meta_sync_rules

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeMetaSyncRulesResponse data
        :rtype: DescribeMetaSyncRulesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_METASYNCRULE)
        headers = None
        params = {}
        params['action'] = 'DescribeMetaSyncRules'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeMetaSyncRulesResponse,
        )

    def describe_order(self, request, config=None):
        """
        describe_order

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeOrderResponse data
        :rtype: DescribeOrderResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_ORDER)
        headers = None
        params = {}
        params['action'] = 'DescribeOrder'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeOrderResponse,
        )

    def describe_price(self, request, config=None):
        """
        describe_price

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribePriceResponse data
        :rtype: DescribePriceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_PRICE)
        headers = None
        params = {}
        params['action'] = 'DescribePrice'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribePriceResponse,
        )

    def describe_specs(self, request, config=None):
        """
        describe_specs

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeSpecsResponse data
        :rtype: DescribeSpecsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_SPECIFICATION)
        headers = None
        params = {}
        params['action'] = 'DescribeSpecs'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeSpecsResponse,
        )

    def describe_token(self, request, config=None):
        """
        describe_token

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeTokenResponse data
        :rtype: DescribeTokenResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_INSTANCE)
        headers = None
        params = {}
        params['action'] = 'DescribeToken'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeTokenResponse,
        )

    def describe_zones(self, config=None):
        """
        describe_zones
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeZonesResponse data
        :rtype: DescribeZonesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_ZONE)
        headers = None
        params = {}
        params['action'] = 'DescribeZones'
        return self._send_request(
            http_methods.POST, path=path, params=params, config=config, model=DescribeZonesResponse
        )

    def disable_meta_sync_rule(self, request, config=None):
        """
        disable_meta_sync_rule

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_METASYNCRULE)
        headers = None
        params = {}
        params['action'] = 'DisableMetaSyncRule'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def enable_meta_sync_rule(self, request, config=None):
        """
        enable_meta_sync_rule

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_METASYNCRULE)
        headers = None
        params = {}
        params['action'] = 'EnableMetaSyncRule'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def execute_cache_rule_job(self, request, config=None):
        """
        execute_cache_rule_job

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_CACHERULE)
        headers = None
        params = {}
        params['action'] = 'ExecuteCacheRuleJob'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def execute_meta_sync_job(self, request, config=None):
        """
        execute_meta_sync_job

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_METASYNCRULE)
        headers = None
        params = {}
        params['action'] = 'ExecuteMetaSyncJob'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def import_data_src(self, request, config=None):
        """
        import_data_src

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ImportDataSrcResponse data
        :rtype: ImportDataSrcResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_DATASRC)
        headers = None
        params = {}
        params['action'] = 'ImportDataSrc'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=ImportDataSrcResponse,
        )

    def modify_auth_group(self, request, config=None):
        """
        modify_auth_group

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_AUTHGROUP)
        headers = None
        params = {}
        params['action'] = 'ModifyAuthGroup'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def modify_data_src(self, request, config=None):
        """
        modify_data_src

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_DATASRC)
        headers = None
        params = {}
        params['action'] = 'ModifyDataSrc'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def modify_meta_sync_rule(self, request, config=None):
        """
        modify_meta_sync_rule

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_METASYNCRULE)
        headers = None
        params = {}
        params['action'] = 'ModifyMetaSyncRule'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def modify_token(self, request, config=None):
        """
        modify_token

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_INSTANCE)
        headers = None
        params = {}
        params['action'] = 'ModifyToken'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def remove_cache_nodes(self, request, config=None):
        """
        remove_cache_nodes

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_CACHENODE)
        headers = None
        params = {}
        params['action'] = 'RemoveCacheNodes'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def remove_data_src(self, request, config=None):
        """
        remove_data_src

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing RemoveDataSrcResponse data
        :rtype: RemoveDataSrcResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_DATASRC)
        headers = None
        params = {}
        params['action'] = 'RemoveDataSrc'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=RemoveDataSrcResponse,
        )

    def resize_instance(self, request, config=None):
        """
        resize_instance

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ResizeInstanceResponse data
        :rtype: ResizeInstanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_INSTANCE)
        headers = None
        params = {}
        params['action'] = 'ResizeInstance'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=ResizeInstanceResponse,
        )

    def restart_cache_nodes(self, request, config=None):
        """
        restart_cache_nodes

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_CACHENODE)
        headers = None
        params = {}
        params['action'] = 'RestartCacheNodes'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def start_cache_nodes(self, request, config=None):
        """
        start_cache_nodes

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_CACHENODE)
        headers = None
        params = {}
        params['action'] = 'StartCacheNodes'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def stop_cache_nodes(self, request, config=None):
        """
        stop_cache_nodes

        :param request: Request entity containing all parameters
        :type request: RapidfsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(RapidfsClient.VERSION_V2, RapidfsClient.CONSTANT_CACHENODE)
        headers = None
        params = {}
        params['action'] = 'StopCacheNodes'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
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
