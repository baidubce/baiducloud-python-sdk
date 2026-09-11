"""
Example for cce client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_core.util import request_body_utils
from baiducloud_python_sdk_cce.models.create_a_shrinking_node_group_task_v2_response import (
    CreateAShrinkingNodeGroupTaskV2Response,
)
from baiducloud_python_sdk_cce.models.create_an_autoscaler_v2_response import CreateAnAutoscalerV2Response
from baiducloud_python_sdk_cce.models.create_expansion_node_group_task_v2_response import (
    CreateExpansionNodeGroupTaskV2Response,
)
from baiducloud_python_sdk_cce.models.create_node_group_v2_response import CreateNodeGroupV2Response
from baiducloud_python_sdk_cce.models.delete_node_group_v2_response import DeleteNodeGroupV2Response
from baiducloud_python_sdk_cce.models.delete_nodes_cluster_scaling_v2_response import (
    DeleteNodesClusterScalingV2Response,
)
from baiducloud_python_sdk_cce.models.get_node_details_v2_response import GetNodeDetailsV2Response
from baiducloud_python_sdk_cce.models.get_node_group_details_v2_response import GetNodeGroupDetailsV2Response
from baiducloud_python_sdk_cce.models.get_package_list_v2_response import GetPackageListV2Response
from baiducloud_python_sdk_cce.models.get_task_list_v2_response import GetTaskListV2Response
from baiducloud_python_sdk_cce.models.get_the_list_of_cluster_node_groups_v2_response import (
    GetTheListOfClusterNodeGroupsV2Response,
)
from baiducloud_python_sdk_cce.models.get_the_list_of_cluster_nodes_v2_response import (
    GetTheListOfClusterNodesV2Response,
)
from baiducloud_python_sdk_cce.models.modify_ig_auto_scaler_response import ModifyIGAutoScalerResponse
from baiducloud_python_sdk_cce.models.modify_node_group_node_shrink_protection_status_v2_response import (
    ModifyNodeGroupNodeShrinkProtectionStatusV2Response,
)
from baiducloud_python_sdk_cce.models.modify_the_number_of_node_replicas_in_a_node_group_v2_response import (
    ModifyTheNumberOfNodeReplicasInANodeGroupV2Response,
)
from baiducloud_python_sdk_cce.models.move_into_an_existing_node_v2_response import MoveIntoAnExistingNodeV2Response
from baiducloud_python_sdk_cce.models.query_the_configuration_of_autoscaler_v2_response import (
    QueryTheConfigurationOfAutoscalerV2Response,
)
from baiducloud_python_sdk_cce.models.retrieve_the_node_group_node_list_v2_response import (
    RetrieveTheNodeGroupNodeListV2Response,
)
from baiducloud_python_sdk_cce.models.steps_to_obtain_node_events_v2_response import StepsToObtainNodeEventsV2Response
from baiducloud_python_sdk_cce.models.synchronize_node_metadata_v2_response import SynchronizeNodeMetadataV2Response
from baiducloud_python_sdk_cce.models.update_autoscaler_configuration_v2_response import (
    UpdateAutoscalerConfigurationV2Response,
)
from baiducloud_python_sdk_cce.models.update_node_attributes_v2_response import UpdateNodeAttributesV2Response
from baiducloud_python_sdk_cce.models.view_task_details_v2_response import ViewTaskDetailsV2Response

_logger = logging.getLogger(__name__)


class CceClient(BceBaseClient):
    """
    cce base sdk client
    """

    CONSTANT_V2 = b'v2'

    CONSTANT_EVENT = b'event'

    CONSTANT_INSTANCE = b'instance'

    CONSTANT_CLUSTER = b'cluster'

    CONSTANT_INSTANCEGROUPS = b'instancegroups'

    CONSTANT_CLUSTER_I_D = b'[clusterID]'

    CONSTANT_INSTANCEGROUP = b'instancegroup'

    CONSTANT_INSTANCE_GROUP_I_D = b'[instanceGroupID]'

    CONSTANT_ATTACH_INSTANCES = b'attachInstances'

    CONSTANT_INSTANCE_SCALE_DOWN = b'instanceScaleDown'

    CONSTANT_AUTOSCALER = b'autoscaler'

    CONSTANT_TASK = b'task'

    CONSTANT_SCALEUP = b'scaleup'

    CONSTANT_REPLICAS = b'replicas'

    CONSTANT_INSTANCES = b'instances'

    CONSTANT_TASKS = b'tasks'

    CONSTANT_SYNC = b'sync'

    CONSTANT_API = b'api'

    CONSTANT_CCE = b'cce'

    CONSTANT_ARTIFACT_SERVICE = b'artifact-service'

    CONSTANT_V1 = b'v1'

    CONSTANT_MACHINE_SPECS = b'machine-specs'

    CONSTANT_SCALEDOWN = b'scaledown'

    def __init__(self, config=None):
        """
        Initialize the cce client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def create_a_shrinking_node_group_task_v2(self, request, config=None):
        """
        create_a_shrinking_node_group_task_v2

        :param request: Request entity containing all parameters
        :type request: CceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateAShrinkingNodeGroupTaskV2Response data
        :rtype: CreateAShrinkingNodeGroupTaskV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CceClient.CONSTANT_V2,
            CceClient.CONSTANT_CLUSTER,
            request.cluster_id,
            CceClient.CONSTANT_INSTANCEGROUP,
            request.instance_group_id,
            CceClient.CONSTANT_SCALEDOWN,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateAShrinkingNodeGroupTaskV2Response,
        )

    def create_an_autoscaler_v2(self, request, config=None):
        """
        create_an_autoscaler_v2

        :param request: Request entity containing all parameters
        :type request: CceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateAnAutoscalerV2Response data
        :rtype: CreateAnAutoscalerV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', CceClient.CONSTANT_V2, CceClient.CONSTANT_AUTOSCALER, request.cluster_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, config=merged_config, model=CreateAnAutoscalerV2Response
        )

    def create_expansion_node_group_task_v2(self, request, config=None):
        """
        create_expansion_node_group_task_v2

        :param request: Request entity containing all parameters
        :type request: CceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateExpansionNodeGroupTaskV2Response data
        :rtype: CreateExpansionNodeGroupTaskV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CceClient.CONSTANT_V2,
            CceClient.CONSTANT_CLUSTER,
            request.cluster_id,
            CceClient.CONSTANT_INSTANCEGROUP,
            request.instance_group_id,
            CceClient.CONSTANT_SCALEUP,
        )
        headers = None
        params = {}
        if request.up_to_replicas is not None:
            params['upToReplicas'] = request.up_to_replicas
        if request.up_replicas is not None:
            params['upReplicas'] = request.up_replicas
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            params=params,
            config=merged_config,
            model=CreateExpansionNodeGroupTaskV2Response,
        )

    def create_node_group_v2(self, request, config=None):
        """
        create_node_group_v2

        :param request: Request entity containing all parameters
        :type request: CceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateNodeGroupV2Response data
        :rtype: CreateNodeGroupV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CceClient.CONSTANT_V2,
            CceClient.CONSTANT_CLUSTER,
            request.cluster_id,
            CceClient.CONSTANT_INSTANCEGROUP,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateNodeGroupV2Response,
        )

    def delete_node_group_v2(self, request, config=None):
        """
        delete_node_group_v2

        :param request: Request entity containing all parameters
        :type request: CceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DeleteNodeGroupV2Response data
        :rtype: DeleteNodeGroupV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CceClient.CONSTANT_V2,
            CceClient.CONSTANT_CLUSTER,
            request.cluster_id,
            CceClient.CONSTANT_INSTANCEGROUP,
            request.instance_group_id,
        )
        headers = None
        params = {}
        if request.delete_instances is not None:
            params['deleteInstances'] = request.delete_instances
        if request.release_all_resource is not None:
            params['releaseAllResource'] = request.release_all_resource
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.DELETE, path=path, params=params, config=merged_config, model=DeleteNodeGroupV2Response
        )

    def delete_nodes_cluster_scaling_v2(self, request, config=None):
        """
        delete_nodes_cluster_scaling_v2

        :param request: Request entity containing all parameters
        :type request: CceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DeleteNodesClusterScalingV2Response data
        :rtype: DeleteNodesClusterScalingV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/', CceClient.CONSTANT_V2, CceClient.CONSTANT_CLUSTER, request.cluster_id, CceClient.CONSTANT_INSTANCES
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=DeleteNodesClusterScalingV2Response,
        )

    def get_node_details_v2(self, request, config=None):
        """
        get_node_details_v2

        :param request: Request entity containing all parameters
        :type request: CceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetNodeDetailsV2Response data
        :rtype: GetNodeDetailsV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CceClient.CONSTANT_V2,
            CceClient.CONSTANT_CLUSTER,
            request.cluster_id,
            CceClient.CONSTANT_INSTANCE,
            request.instance_id,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetNodeDetailsV2Response)

    def get_node_group_details_v2(self, request, config=None):
        """
        get_node_group_details_v2

        :param request: Request entity containing all parameters
        :type request: CceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetNodeGroupDetailsV2Response data
        :rtype: GetNodeGroupDetailsV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CceClient.CONSTANT_V2,
            CceClient.CONSTANT_CLUSTER,
            request.cluster_id,
            CceClient.CONSTANT_INSTANCEGROUP,
            request.instance_group_id,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=GetNodeGroupDetailsV2Response
        )

    def get_package_list_v2(self, request, config=None):
        """
        get_package_list_v2

        :param request: Request entity containing all parameters
        :type request: CceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetPackageListV2Response data
        :rtype: GetPackageListV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CceClient.CONSTANT_API,
            CceClient.CONSTANT_CCE,
            CceClient.CONSTANT_ARTIFACT_SERVICE,
            CceClient.CONSTANT_V1,
            CceClient.CONSTANT_MACHINE_SPECS,
        )
        headers = None
        params = {}
        if request.type is not None:
            params['type'] = request.type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=GetPackageListV2Response,
        )

    def get_task_list_v2(self, request, config=None):
        """
        get_task_list_v2

        :param request: Request entity containing all parameters
        :type request: CceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetTaskListV2Response data
        :rtype: GetTaskListV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', CceClient.CONSTANT_V2, CceClient.CONSTANT_TASKS, request.task_type)
        headers = None
        params = {}
        if request.target_id is not None:
            params['targetID'] = request.target_id
        if request.operation_type is not None:
            params['operationType'] = request.operation_type
        if request.phase is not None:
            params['phase'] = request.phase
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
            http_methods.GET, path=path, params=params, config=merged_config, model=GetTaskListV2Response
        )

    def get_the_list_of_cluster_node_groups_v2(self, request, config=None):
        """
        get_the_list_of_cluster_node_groups_v2

        :param request: Request entity containing all parameters
        :type request: CceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetTheListOfClusterNodeGroupsV2Response data
        :rtype: GetTheListOfClusterNodeGroupsV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CceClient.CONSTANT_V2,
            CceClient.CONSTANT_CLUSTER,
            request.cluster_id,
            CceClient.CONSTANT_INSTANCEGROUPS,
        )
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
        if request.autoscaler_enabled is not None:
            params['autoscalerEnabled'] = request.autoscaler_enabled
        if request.charging_type is not None:
            params['chargingType'] = request.charging_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            params=params,
            config=merged_config,
            model=GetTheListOfClusterNodeGroupsV2Response,
        )

    def get_the_list_of_cluster_nodes_v2(self, request, config=None):
        """
        get_the_list_of_cluster_nodes_v2

        :param request: Request entity containing all parameters
        :type request: CceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetTheListOfClusterNodesV2Response data
        :rtype: GetTheListOfClusterNodesV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/', CceClient.CONSTANT_V2, CceClient.CONSTANT_CLUSTER, request.cluster_id, CceClient.CONSTANT_INSTANCES
        )
        headers = None
        params = {}
        if request.keyword_type is not None:
            params['keywordType'] = request.keyword_type
        if request.keyword is not None:
            params['keyword'] = request.keyword
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
            http_methods.GET, path=path, params=params, config=merged_config, model=GetTheListOfClusterNodesV2Response
        )

    def modify_ig_auto_scaler(self, request, config=None):
        """
        modify_ig_auto_scaler

        :param request: Request entity containing all parameters
        :type request: CceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ModifyIGAutoScalerResponse data
        :rtype: ModifyIGAutoScalerResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CceClient.CONSTANT_V2,
            CceClient.CONSTANT_CLUSTER,
            request.cluster_id,
            CceClient.CONSTANT_INSTANCEGROUP,
            request.instance_group_id,
            CceClient.CONSTANT_AUTOSCALER,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=ModifyIGAutoScalerResponse,
        )

    def modify_node_group_node_shrink_protection_status_v2(self, request, config=None):
        """
        modify_node_group_node_shrink_protection_status_v2

        :param request: Request entity containing all parameters
        :type request: CceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ModifyNodeGroupNodeShrinkProtectionStatusV2Response data
        :rtype: ModifyNodeGroupNodeShrinkProtectionStatusV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CceClient.CONSTANT_V2,
            CceClient.CONSTANT_CLUSTER,
            request.cluster_id,
            CceClient.CONSTANT_INSTANCE_SCALE_DOWN,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=ModifyNodeGroupNodeShrinkProtectionStatusV2Response,
        )

    def modify_the_number_of_node_replicas_in_a_node_group_v2(self, request, config=None):
        """
        modify_the_number_of_node_replicas_in_a_node_group_v2

        :param request: Request entity containing all parameters
        :type request: CceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ModifyTheNumberOfNodeReplicasInANodeGroupV2Response data
        :rtype: ModifyTheNumberOfNodeReplicasInANodeGroupV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CceClient.CONSTANT_V2,
            CceClient.CONSTANT_CLUSTER,
            request.cluster_id,
            CceClient.CONSTANT_INSTANCEGROUP,
            request.instance_group_id,
            CceClient.CONSTANT_REPLICAS,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=ModifyTheNumberOfNodeReplicasInANodeGroupV2Response,
        )

    def move_into_an_existing_node_v2(self, request, config=None):
        """
        move_into_an_existing_node_v2

        :param request: Request entity containing all parameters
        :type request: CceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing MoveIntoAnExistingNodeV2Response data
        :rtype: MoveIntoAnExistingNodeV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CceClient.CONSTANT_V2,
            CceClient.CONSTANT_CLUSTER,
            CceClient.CONSTANT_CLUSTER_I_D,
            CceClient.CONSTANT_INSTANCEGROUP,
            CceClient.CONSTANT_INSTANCE_GROUP_I_D,
            CceClient.CONSTANT_ATTACH_INSTANCES,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=MoveIntoAnExistingNodeV2Response,
        )

    def query_the_configuration_of_autoscaler_v2(self, request, config=None):
        """
        query_the_configuration_of_autoscaler_v2

        :param request: Request entity containing all parameters
        :type request: CceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryTheConfigurationOfAutoscalerV2Response data
        :rtype: QueryTheConfigurationOfAutoscalerV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', CceClient.CONSTANT_V2, CceClient.CONSTANT_AUTOSCALER, request.cluster_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=QueryTheConfigurationOfAutoscalerV2Response
        )

    def retrieve_the_node_group_node_list_v2(self, request, config=None):
        """
        retrieve_the_node_group_node_list_v2

        :param request: Request entity containing all parameters
        :type request: CceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing RetrieveTheNodeGroupNodeListV2Response data
        :rtype: RetrieveTheNodeGroupNodeListV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CceClient.CONSTANT_V2,
            CceClient.CONSTANT_CLUSTER,
            request.cluster_id,
            CceClient.CONSTANT_INSTANCEGROUP,
            request.instance_group_id,
            CceClient.CONSTANT_INSTANCES,
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
            model=RetrieveTheNodeGroupNodeListV2Response,
        )

    def steps_to_obtain_node_events_v2(self, request, config=None):
        """
        steps_to_obtain_node_events_v2

        :param request: Request entity containing all parameters
        :type request: CceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing StepsToObtainNodeEventsV2Response data
        :rtype: StepsToObtainNodeEventsV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/', CceClient.CONSTANT_V2, CceClient.CONSTANT_EVENT, CceClient.CONSTANT_INSTANCE, request.instance_id
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=StepsToObtainNodeEventsV2Response
        )

    def synchronize_node_metadata_v2(self, request, config=None):
        """
        synchronize_node_metadata_v2

        :param request: Request entity containing all parameters
        :type request: CceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing SynchronizeNodeMetadataV2Response data
        :rtype: SynchronizeNodeMetadataV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CceClient.CONSTANT_V2,
            CceClient.CONSTANT_SYNC,
            CceClient.CONSTANT_CLUSTER,
            request.cluster_id,
            CceClient.CONSTANT_INSTANCES,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, config=merged_config, model=SynchronizeNodeMetadataV2Response
        )

    def update_autoscaler_configuration_v2(self, request, config=None):
        """
        update_autoscaler_configuration_v2

        :param request: Request entity containing all parameters
        :type request: CceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UpdateAutoscalerConfigurationV2Response data
        :rtype: UpdateAutoscalerConfigurationV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', CceClient.CONSTANT_V2, CceClient.CONSTANT_AUTOSCALER, request.cluster_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=UpdateAutoscalerConfigurationV2Response,
        )

    def update_node_attributes_v2(self, request, config=None):
        """
        update_node_attributes_v2

        :param request: Request entity containing all parameters
        :type request: CceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UpdateNodeAttributesV2Response data
        :rtype: UpdateNodeAttributesV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CceClient.CONSTANT_V2,
            CceClient.CONSTANT_CLUSTER,
            request.cluster_id,
            CceClient.CONSTANT_INSTANCE,
            request.instance_id,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=UpdateNodeAttributesV2Response,
        )

    def view_task_details_v2(self, request, config=None):
        """
        view_task_details_v2

        :param request: Request entity containing all parameters
        :type request: CceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ViewTaskDetailsV2Response data
        :rtype: ViewTaskDetailsV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/', CceClient.CONSTANT_V2, CceClient.CONSTANT_TASK, request.task_type, request.task_id
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=ViewTaskDetailsV2Response)

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
