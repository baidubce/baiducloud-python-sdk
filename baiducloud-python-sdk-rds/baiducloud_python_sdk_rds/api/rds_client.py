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
from baiducloud_python_sdk_rds.models.cluster_status_check_response import ClusterStatusCheckResponse
from baiducloud_python_sdk_rds.models.create_a_primary_instance_response import CreateAPrimaryInstanceResponse
from baiducloud_python_sdk_rds.models.create_a_proxy_instance_response import CreateAProxyInstanceResponse
from baiducloud_python_sdk_rds.models.create_read_only_instance_response import CreateReadOnlyInstanceResponse
from baiducloud_python_sdk_rds.models.dial_test_interface_response import DialTestInterfaceResponse
from baiducloud_python_sdk_rds.models.does_the_instance_support_enabling_automatic_expansion_response import (
    DoesTheInstanceSupportEnablingAutomaticExpansionResponse,
)
from baiducloud_python_sdk_rds.models.query_instance_list_response import QueryInstanceListResponse
from baiducloud_python_sdk_rds.models.query_subnet_list_response import QuerySubnetListResponse
from baiducloud_python_sdk_rds.models.query_task_list_response import QueryTaskListResponse
from baiducloud_python_sdk_rds.models.query_the_list_of_available_zones_response import (
    QueryTheListOfAvailableZonesResponse,
)
from baiducloud_python_sdk_rds.models.release_instance_response import ReleaseInstanceResponse
from baiducloud_python_sdk_rds.models.renewal_example_response import RenewalExampleResponse
from baiducloud_python_sdk_rds.models.retrieve_instance_auto_scaling_config_response import (
    RetrieveInstanceAutoScalingConfigResponse,
)
from baiducloud_python_sdk_rds.models.transformation_example_response import TransformationExampleResponse

_logger = logging.getLogger(__name__)


class RdsClient(BceBaseClient):
    """
    rds base sdk client
    """

    VERSION_V1 = b'/v1'

    CONSTANT_INSTANCE = b'instance'

    CONSTANT_TAGS = b'tags'

    CONSTANT_STATUS = b'status'

    CONSTANT_DISK_AUTO_RESIZE = b'diskAutoResize'

    CONSTANT_CONFIG = b'config'

    CONSTANT_PROBE = b'probe'

    CONSTANT_V1 = b'v1'

    CONSTANT_TASK = b'task'

    CONSTANT_RENEW = b'renew'

    CONSTANT_AUTO_RESIZE_CONFIG = b'autoResizeConfig'

    CONSTANT_ZONE = b'zone'

    CONSTANT_SUBNET = b'subnet'

    CONSTANT_MAINTAINTIME = b'maintaintime'

    CONSTANT_AUTO_EXPANSION = b'autoExpansion'

    def __init__(self, config=None):
        """
        Initialize the rds client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

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
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config, model=ReleaseInstanceResponse)

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
