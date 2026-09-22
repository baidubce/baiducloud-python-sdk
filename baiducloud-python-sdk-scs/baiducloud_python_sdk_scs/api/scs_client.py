"""
Example for scs client.
"""
import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_core.util import request_body_utils
from baiducloud_python_sdk_scs.models.account_list_response import AccountListResponse
from baiducloud_python_sdk_scs.models.bind_security_group_response import BindSecurityGroupResponse
from baiducloud_python_sdk_scs.models.change_configuration_response import ChangeConfigurationResponse
from baiducloud_python_sdk_scs.models.cluster_status_check_response import ClusterStatusCheckResponse
from baiducloud_python_sdk_scs.models.cluster_type_upgrade_response import ClusterTypeUpgradeResponse
from baiducloud_python_sdk_scs.models.create_an_instance_response import CreateAnInstanceResponse
from baiducloud_python_sdk_scs.models.create_deployment_set_response import CreateDeploymentSetResponse
from baiducloud_python_sdk_scs.models.create_entrance_response import CreateEntranceResponse
from baiducloud_python_sdk_scs.models.create_hot_group_response import CreateHotGroupResponse
from baiducloud_python_sdk_scs.models.create_parameter_template_response import CreateParameterTemplateResponse
from baiducloud_python_sdk_scs.models.create_sync_group_response import CreateSyncGroupResponse
from baiducloud_python_sdk_scs.models.disconnect_entrance_response import DisconnectEntranceResponse
from baiducloud_python_sdk_scs.models.ge_price_for_resize_instance_response import GePriceForResizeInstanceResponse
from baiducloud_python_sdk_scs.models.get_application_parameter_template_records_response import GetApplicationParameterTemplateRecordsResponse
from baiducloud_python_sdk_scs.models.get_available_zones_response import GetAvailableZonesResponse
from baiducloud_python_sdk_scs.models.get_back_up_url_response import GetBackUpUrlResponse
from baiducloud_python_sdk_scs.models.get_back_up_usage_response import GetBackUpUsageResponse
from baiducloud_python_sdk_scs.models.get_backup_list_response import GetBackupListResponse
from baiducloud_python_sdk_scs.models.get_backup_strategy_response import GetBackupStrategyResponse
from baiducloud_python_sdk_scs.models.get_cluster_blb_status_response import GetClusterBlbStatusResponse
from baiducloud_python_sdk_scs.models.get_deployment_set_list_response import GetDeploymentSetListResponse
from baiducloud_python_sdk_scs.models.get_hot_group_detail_response import GetHotGroupDetailResponse
from baiducloud_python_sdk_scs.models.get_hot_group_list_response import GetHotGroupListResponse
from baiducloud_python_sdk_scs.models.get_instance_detail_response import GetInstanceDetailResponse
from baiducloud_python_sdk_scs.models.get_instance_list_response import GetInstanceListResponse
from baiducloud_python_sdk_scs.models.get_instance_spec_list_response import GetInstanceSpecListResponse
from baiducloud_python_sdk_scs.models.get_instance_white_group_response import GetInstanceWhiteGroupResponse
from baiducloud_python_sdk_scs.models.get_parameter_list_response import GetParameterListResponse
from baiducloud_python_sdk_scs.models.get_parameter_template_list_response import GetParameterTemplateListResponse
from baiducloud_python_sdk_scs.models.get_price_for_create_instance_response import GetPriceForCreateInstanceResponse
from baiducloud_python_sdk_scs.models.get_recycle_list_response import GetRecycleListResponse
from baiducloud_python_sdk_scs.models.get_subnet_list_response import GetSubnetListResponse
from baiducloud_python_sdk_scs.models.get_sync_group_status_response import GetSyncGroupStatusResponse
from baiducloud_python_sdk_scs.models.get_system_parameter_list_response import GetSystemParameterListResponse
from baiducloud_python_sdk_scs.models.get_time_window_response import GetTimeWindowResponse
from baiducloud_python_sdk_scs.models.get_tls_cert_response import GetTlsCertResponse
from baiducloud_python_sdk_scs.models.hot_group_pre_check_response import HotGroupPreCheckResponse
from baiducloud_python_sdk_scs.models.hot_group_sync_status_response import HotGroupSyncStatusResponse
from baiducloud_python_sdk_scs.models.log_details_response import LogDetailsResponse
from baiducloud_python_sdk_scs.models.log_list_response import LogListResponse
from baiducloud_python_sdk_scs.models.manually_modify_bandwidth_response import ManuallyModifyBandwidthResponse
from baiducloud_python_sdk_scs.models.parameter_template_details_response import ParameterTemplateDetailsResponse
from baiducloud_python_sdk_scs.models.post_paid_to_prepaid_response import PostPaidToPrepaidResponse
from baiducloud_python_sdk_scs.models.prepaid_to_postpaid_response import PrepaidToPostpaidResponse
from baiducloud_python_sdk_scs.models.query_ip_whitelist_response import QueryIpWhitelistResponse
from baiducloud_python_sdk_scs.models.query_memory_scaling_config_response import QueryMemoryScalingConfigResponse
from baiducloud_python_sdk_scs.models.renew_instance_response import RenewInstanceResponse
from baiducloud_python_sdk_scs.models.sync_group_delay_info_response import SyncGroupDelayInfoResponse
from baiducloud_python_sdk_scs.models.sync_group_detail_response import SyncGroupDetailResponse
from baiducloud_python_sdk_scs.models.sync_group_list_response import SyncGroupListResponse
from baiducloud_python_sdk_scs.models.sync_group_pre_check_response import SyncGroupPreCheckResponse
from baiducloud_python_sdk_scs.models.tde_encryption_response import TdeEncryptionResponse
from baiducloud_python_sdk_scs.models.unbind_security_group_response import UnbindSecurityGroupResponse
from baiducloud_python_sdk_scs.models.update_security_group_response import UpdateSecurityGroupResponse
from baiducloud_python_sdk_scs.models.view_security_group_response import ViewSecurityGroupResponse

_logger = logging.getLogger(__name__)


class ScsClient(BceBaseClient):
    """
    scs base sdk client
    """

    VERSION_V1 = b'/v1'

    CONSTANT_V2 = b'v2'

    CONSTANT_INSTANCE = b'instance'

    CONSTANT_V1 = b'v1'

    CONSTANT_BACKUP = b'backup'

    CONSTANT_URL = b'url'

    CONSTANT_TLS = b'tls'

    CONSTANT_BIND_TAG = b'bindTag'

    CONSTANT_ACL_USER_ACTIONS = b'aclUserActions'

    CONSTANT_AUTHORITY = b'authority'

    CONSTANT_LOG = b'log'

    CONSTANT_RECYCLER = b'recycler'

    CONSTANT_LIST = b'list'

    CONSTANT_ENTRANCE = b'entrance'

    CONSTANT_DISCONNECT = b'disconnect'

    CONSTANT_WHITELIST = b'whitelist'

    CONSTANT_POLICY = b'policy'

    CONSTANT_TEMPLATE = b'template'

    CONSTANT_FLUSH = b'flush'

    CONSTANT_GROUP = b'group'

    CONSTANT_CREATE = b'create'

    CONSTANT_SWAP_DOMAIN = b'swapDomain'

    CONSTANT_ZONE = b'zone'

    CONSTANT_SYNC_GROUP = b'syncGroup'

    CONSTANT_MODIFY_BNS_GROUP = b'modifyBnsGroup'

    CONSTANT_SUBNET = b'subnet'

    CONSTANT_RESTART = b'restart'

    CONSTANT_DEPLOY_SET = b'deploySet'

    CONSTANT_RELEASE = b'release'

    CONSTANT_RENEW = b'renew'

    CONSTANT_APPLY = b'apply'

    CONSTANT_MODIFY_PARAMS = b'modifyParams'

    CONSTANT_RECOVER__H_T_T_P = b'recover HTTP'

    CONSTANT_1_1 = b'1.1'

    CONSTANT_QPS = b'qps'

    CONSTANT_RENAME = b'rename'

    CONSTANT_MODIFY_BANDWIDTH = b'modifyBandwidth'

    CONSTANT_SECURITY_GROUP = b'securityGroup'

    CONSTANT_UPDATE = b'update'

    CONSTANT_DELETE__H_T_T_P = b'delete HTTP'

    CONSTANT_SECURITY_IP = b'securityIp'

    CONSTANT_MODIFY_POLICY = b'modifyPolicy'

    CONSTANT_ADD_PARAMS = b'addParams'

    CONSTANT_DELETE_AUTO_SCALING_CONFIG = b'deleteAutoScalingConfig'

    CONSTANT_REMOVE_CLUSTER = b'removeCluster'

    CONSTANT_CHECK = b'check'

    CONSTANT_PRICE = b'price'

    CONSTANT_STALE_READABLE = b'stale_readable'

    CONSTANT_FORBID_WRITE = b'forbidWrite'

    CONSTANT_BLB_STATUS = b'blbStatus'

    CONSTANT_UN_BIND_TAG = b'unBindTag'

    CONSTANT_TO_PREPAY = b'toPrepay'

    CONSTANT_SET_AS_MASTER = b'setAsMaster'

    CONSTANT_AZONE_MIGRATION = b'azoneMigration'

    CONSTANT_MODIFY_ENTRANCE = b'modifyEntrance'

    CONSTANT_STATUS = b'status'

    CONSTANT_PARAMETER = b'parameter'

    CONSTANT_USAGE = b'usage'

    CONSTANT_DELETE = b'delete'

    CONSTANT_RENAME_DOMAIN = b'renameDomain'

    CONSTANT_RECORD = b'record'

    CONSTANT_PROXY_NODE = b'proxyNode'

    CONSTANT_TIME_WINDOW = b'timeWindow'

    CONSTANT_AUDIT = b'audit'

    CONSTANT_SWITCH = b'switch'

    CONSTANT_MODIFY_PASSWD = b'modifyPasswd'

    CONSTANT_SET_AS_LEADER = b'setAsLeader'

    CONSTANT_SWITCH_MASTER_SLAVE = b'switchMasterSlave'

    CONSTANT_MODIFY_PASSWORD = b'modifyPassword'

    CONSTANT_UPGRADE_PROXY = b'upgradeProxy'

    CONSTANT_COMMENT = b'comment'

    CONSTANT_CLUSTER_TYPE_CHANGE = b'clusterTypeChange'

    CONSTANT_NODETYPES = b'nodetypes'

    CONSTANT_CANCEL_TO_POSTPAY = b'cancelToPostpay'

    CONSTANT_DELETE_PARAMS = b'deleteParams'

    CONSTANT_QUIT = b'quit'

    CONSTANT_AUTO_SCALING_CONFIG = b'autoScalingConfig'

    CONSTANT_UNBIND = b'unbind'

    CONSTANT_SYSTEM = b'system'

    CONSTANT_JOIN = b'join'

    CONSTANT_TO_POSTPAY = b'toPostpay'

    CONSTANT_DELAY_INFO = b'delayInfo'

    CONSTANT_UPGRADE_VERSION = b'upgradeVersion'

    CONSTANT_SET_AS_SLAVE = b'setAsSlave'

    CONSTANT_SYNC_STATUS = b'syncStatus'

    CONSTANT_ADD_CLUSTER = b'addCluster'

    CONSTANT_CHANGE = b'change'

    CONSTANT_BIND = b'bind'

    CONSTANT_TDE = b'tde'

    def __init__(self, config=None):
        """
        Initialize the scs client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def account_list(self, request, config=None):
        """
        account_list

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing AccountListResponse data
        :rtype: AccountListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(ScsClient.VERSION_V1, ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_ACL_USER_ACTIONS)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , config=merged_config, model=AccountListResponse)

    def add_ip_whitelist(self, request, config=None):
        """
        add_ip_whitelist

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_SECURITY_IP)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), config=merged_config)

    def add_parameters_to_parameter_template(self, request, config=None):
        """
        add_parameters_to_parameter_template

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_TEMPLATE,
                                ScsClient.CONSTANT_ADD_PARAMS,
                                request.template_show_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config)

    def application_parameter_template(self, request, config=None):
        """
        application_parameter_template

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_TEMPLATE,
                                ScsClient.CONSTANT_APPLY,
                                request.template_show_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config)

    def audit_log_switch(self, request, config=None):
        """
        audit_log_switch

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_LOG,
                                ScsClient.CONSTANT_AUDIT,
                                ScsClient.CONSTANT_SWITCH)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), config=merged_config)

    def batch_restore_instances(self, request, config=None):
        """
        batch_restore_instances

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_RECYCLER,
                                ScsClient.CONSTANT_RECOVER__H_T_T_P,
                                ScsClient.CONSTANT_1_1)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config)

    def bind_security_group(self, request, config=None):
        """
        bind_security_group

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BindSecurityGroupResponse data
        :rtype: BindSecurityGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_SECURITY_GROUP,
                                ScsClient.CONSTANT_BIND)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config, model=BindSecurityGroupResponse)

    def bind_tags(self, request, config=None):
        """
        bind_tags

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_BIND_TAG)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), config=merged_config)

    def cancel_prepaid_to_postpaid(self, request, config=None):
        """
        cancel_prepaid_to_postpaid

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                ScsClient.CONSTANT_CANCEL_TO_POSTPAY)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config)

    def change_access_password(self, request, config=None):
        """
        change_access_password

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_MODIFY_PASSWORD)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), config=merged_config)

    def change_account_password(self, request, config=None):
        """
        change_account_password

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(ScsClient.VERSION_V1, request.instance_id,
                                ScsClient.CONSTANT_ACL_USER_ACTIONS,
                                ScsClient.CONSTANT_MODIFY_PASSWD)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config)

    def change_configuration(self, request, config=None):
        """
        change_configuration

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ChangeConfigurationResponse data
        :rtype: ChangeConfigurationResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_CHANGE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), config=merged_config, model=ChangeConfigurationResponse)

    def clear_instance(self, request, config=None):
        """
        clear_instance

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_FLUSH)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), config=merged_config)

    def cluster_status_check(self, request, config=None):
        """
        cluster_status_check

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ClusterStatusCheckResponse data
        :rtype: ClusterStatusCheckResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(ScsClient.VERSION_V1, ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_STATUS)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path
                                , config=merged_config, model=ClusterStatusCheckResponse)

    def cluster_type_upgrade(self, request, config=None):
        """
        cluster_type_upgrade

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ClusterTypeUpgradeResponse data
        :rtype: ClusterTypeUpgradeResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_CLUSTER_TYPE_CHANGE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), config=merged_config, model=ClusterTypeUpgradeResponse)

    def create_account(self, request, config=None):
        """
        create_account

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(ScsClient.VERSION_V1, ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_ACL_USER_ACTIONS)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config)

    def create_an_instance(self, request, config=None):
        """
        create_an_instance

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateAnInstanceResponse data
        :rtype: CreateAnInstanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_INSTANCE)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), params=params, config=merged_config, model=CreateAnInstanceResponse)

    def create_deployment_set(self, request, config=None):
        """
        create_deployment_set

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateDeploymentSetResponse data
        :rtype: CreateDeploymentSetResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_DEPLOY_SET)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config, model=CreateDeploymentSetResponse)

    def create_entrance(self, request, config=None):
        """
        create_entrance

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateEntranceResponse data
        :rtype: CreateEntranceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(ScsClient.VERSION_V1, ScsClient.CONSTANT_ENTRANCE,
                                ScsClient.CONSTANT_CREATE,
                                request.instance_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , config=merged_config, model=CreateEntranceResponse)

    def create_hot_group(self, request, config=None):
        """
        create_hot_group

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateHotGroupResponse data
        :rtype: CreateHotGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_GROUP,
                                ScsClient.CONSTANT_CREATE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config, model=CreateHotGroupResponse)

    def create_instance_white_group(self, request, config=None):
        """
        create_instance_white_group

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(ScsClient.VERSION_V1, ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_WHITELIST)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config)

    def create_parameter_template(self, request, config=None):
        """
        create_parameter_template

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateParameterTemplateResponse data
        :rtype: CreateParameterTemplateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_TEMPLATE,
                                ScsClient.CONSTANT_CREATE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config, model=CreateParameterTemplateResponse)

    def create_sync_group(self, request, config=None):
        """
        create_sync_group

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateSyncGroupResponse data
        :rtype: CreateSyncGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(ScsClient.VERSION_V1, ScsClient.CONSTANT_SYNC_GROUP,
                                ScsClient.CONSTANT_CREATE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config, model=CreateSyncGroupResponse)

    def delete_account(self, request, config=None):
        """
        delete_account

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(ScsClient.VERSION_V1, request.instance_id,
                                ScsClient.CONSTANT_ACL_USER_ACTIONS,
                                ScsClient.CONSTANT_DELETE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config)

    def delete_deployment_set(self, request, config=None):
        """
        delete_deployment_set

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_DEPLOY_SET,
                                request.deploy_set_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path
                                , config=merged_config)

    def delete_instance_white_group(self, request, config=None):
        """
        delete_instance_white_group

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(ScsClient.VERSION_V1, ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_WHITELIST)
        headers = None
        params = {}
        if request.group_name is not None:
            params['groupName'] = request.group_name
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path
                                , params=params, config=merged_config)

    def delete_instances(self, request, config=None):
        """
        delete_instances

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_RECYCLER,
                                ScsClient.CONSTANT_DELETE__H_T_T_P,
                                ScsClient.CONSTANT_1_1)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config)

    def delete_ip_whitelist(self, request, config=None):
        """
        delete_ip_whitelist

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_SECURITY_IP)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config)

    def delete_manual_backup(self, request, config=None):
        """
        delete_manual_backup

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_BACKUP,
                                request.batch_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path
                                , config=merged_config)

    def delete_memory_scaling_config(self, request, config=None):
        """
        delete_memory_scaling_config

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_DELETE_AUTO_SCALING_CONFIG)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , config=merged_config)

    def delete_parameter_template(self, request, config=None):
        """
        delete_parameter_template

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_TEMPLATE,
                                ScsClient.CONSTANT_DELETE,
                                request.template_show_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path
                                , config=merged_config)

    def delete_sync_group(self, request, config=None):
        """
        delete_sync_group

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(ScsClient.VERSION_V1, ScsClient.CONSTANT_SYNC_GROUP,
                                request.sync_group_show_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path
                                , config=merged_config)

    def disconnect_entrance(self, request, config=None):
        """
        disconnect_entrance

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DisconnectEntranceResponse data
        :rtype: DisconnectEntranceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(ScsClient.VERSION_V1, ScsClient.CONSTANT_ENTRANCE,
                                ScsClient.CONSTANT_DISCONNECT,
                                request.instance_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , config=merged_config, model=DisconnectEntranceResponse)

    def domain_name_exchange(self, request, config=None):
        """
        domain_name_exchange

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_INSTANCE,
                                ScsClient.CONSTANT_SWAP_DOMAIN)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config)

    def ge_price_for_resize_instance(self, request, config=None):
        """
        ge_price_for_resize_instance

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GePriceForResizeInstanceResponse data
        :rtype: GePriceForResizeInstanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_PRICE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config, model=GePriceForResizeInstanceResponse)

    def get_application_parameter_template_records(self, request, config=None):
        """
        get_application_parameter_template_records

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetApplicationParameterTemplateRecordsResponse data
        :rtype: GetApplicationParameterTemplateRecordsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_TEMPLATE,
                                ScsClient.CONSTANT_RECORD,
                                request.template_show_id)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path
                                , params=params, config=merged_config, model=GetApplicationParameterTemplateRecordsResponse)

    def get_available_zones(self, config=None):
        """
        get_available_zones
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetAvailableZonesResponse data
        :rtype: GetAvailableZonesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_ZONE)
        headers = None
        return self._send_request(http_methods.GET, path=path
                                , config=config, model=GetAvailableZonesResponse)

    def get_back_up_url(self, request, config=None):
        """
        get_back_up_url

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetBackUpUrlResponse data
        :rtype: GetBackUpUrlResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_BACKUP,
                                request.backup_id,
                                ScsClient.CONSTANT_URL)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path
                                , config=merged_config, model=GetBackUpUrlResponse)

    def get_back_up_usage(self, request, config=None):
        """
        get_back_up_usage

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetBackUpUsageResponse data
        :rtype: GetBackUpUsageResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(ScsClient.VERSION_V1, ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_BACKUP,
                                ScsClient.CONSTANT_USAGE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path
                                , config=merged_config, model=GetBackUpUsageResponse)

    def get_backup_list(self, request, config=None):
        """
        get_backup_list

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetBackupListResponse data
        :rtype: GetBackupListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_BACKUP)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path
                                , config=merged_config, model=GetBackupListResponse)

    def get_backup_strategy(self, request, config=None):
        """
        get_backup_strategy

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetBackupStrategyResponse data
        :rtype: GetBackupStrategyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_BACKUP,
                                ScsClient.CONSTANT_POLICY)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path
                                , config=merged_config, model=GetBackupStrategyResponse)

    def get_cluster_blb_status(self, request, config=None):
        """
        get_cluster_blb_status

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetClusterBlbStatusResponse data
        :rtype: GetClusterBlbStatusResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(ScsClient.VERSION_V1, ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_BLB_STATUS)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path
                                , config=merged_config, model=GetClusterBlbStatusResponse)

    def get_deployment_set_list(self, request, config=None):
        """
        get_deployment_set_list

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetDeploymentSetListResponse data
        :rtype: GetDeploymentSetListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_DEPLOY_SET)
        headers = None
        params = {}
        params['maxKeys'] = '1'
        params['marker'] = '-1'
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path
                                , params=params, config=merged_config, model=GetDeploymentSetListResponse)

    def get_hot_group_detail(self, request, config=None):
        """
        get_hot_group_detail

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetHotGroupDetailResponse data
        :rtype: GetHotGroupDetailResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_GROUP,
                                request.group_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path
                                , config=merged_config, model=GetHotGroupDetailResponse)

    def get_hot_group_list(self, request, config=None):
        """
        get_hot_group_list

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetHotGroupListResponse data
        :rtype: GetHotGroupListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_GROUP,
                                ScsClient.CONSTANT_LIST)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config, model=GetHotGroupListResponse)

    def get_instance_detail(self, request, config=None):
        """
        get_instance_detail

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetInstanceDetailResponse data
        :rtype: GetInstanceDetailResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path
                                , config=merged_config, model=GetInstanceDetailResponse)

    def get_instance_list(self, request, config=None):
        """
        get_instance_list

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetInstanceListResponse data
        :rtype: GetInstanceListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_INSTANCE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path
                                , config=merged_config, model=GetInstanceListResponse)

    def get_instance_spec_list(self, config=None):
        """
        get_instance_spec_list
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetInstanceSpecListResponse data
        :rtype: GetInstanceSpecListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_NODETYPES)
        headers = None
        return self._send_request(http_methods.GET, path=path
                                , config=config, model=GetInstanceSpecListResponse)

    def get_instance_white_group(self, request, config=None):
        """
        get_instance_white_group

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetInstanceWhiteGroupResponse data
        :rtype: GetInstanceWhiteGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(ScsClient.VERSION_V1, ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_WHITELIST)
        headers = None
        params = {}
        if request.group_name is not None:
            params['groupName'] = request.group_name
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path
                                , params=params, config=merged_config, model=GetInstanceWhiteGroupResponse)

    def get_parameter_list(self, request, config=None):
        """
        get_parameter_list

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetParameterListResponse data
        :rtype: GetParameterListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_PARAMETER)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path
                                , config=merged_config, model=GetParameterListResponse)

    def get_parameter_template_list(self, request, config=None):
        """
        get_parameter_template_list

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetParameterTemplateListResponse data
        :rtype: GetParameterTemplateListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_TEMPLATE,
                                ScsClient.CONSTANT_LIST)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path
                                , params=params, config=merged_config, model=GetParameterTemplateListResponse)

    def get_price_for_create_instance(self, request, config=None):
        """
        get_price_for_create_instance

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetPriceForCreateInstanceResponse data
        :rtype: GetPriceForCreateInstanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_PRICE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config, model=GetPriceForCreateInstanceResponse)

    def get_recycle_list(self, request, config=None):
        """
        get_recycle_list

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetRecycleListResponse data
        :rtype: GetRecycleListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_RECYCLER,
                                ScsClient.CONSTANT_LIST)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path
                                , params=params, config=merged_config, model=GetRecycleListResponse)

    def get_subnet_list(self, request, config=None):
        """
        get_subnet_list

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetSubnetListResponse data
        :rtype: GetSubnetListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_SUBNET)
        headers = None
        params = {}
        if request.vpc_id is not None:
            params['vpcId'] = request.vpc_id
        if request.zone_name is not None:
            params['zoneName'] = request.zone_name
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path
                                , params=params, config=merged_config, model=GetSubnetListResponse)

    def get_sync_group_status(self, request, config=None):
        """
        get_sync_group_status

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetSyncGroupStatusResponse data
        :rtype: GetSyncGroupStatusResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(ScsClient.VERSION_V1, ScsClient.CONSTANT_SYNC_GROUP,
                                request.sync_group_show_id,
                                ScsClient.CONSTANT_SYNC_STATUS)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path
                                , config=merged_config, model=GetSyncGroupStatusResponse)

    def get_system_parameter_list(self, request, config=None):
        """
        get_system_parameter_list

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetSystemParameterListResponse data
        :rtype: GetSystemParameterListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_TEMPLATE,
                                ScsClient.CONSTANT_SYSTEM)
        headers = None
        params = {}
        if request.engine is not None:
            params['engine'] = request.engine
        if request.engine_version is not None:
            params['engineVersion'] = request.engine_version
        if request.cluster_type is not None:
            params['clusterType'] = request.cluster_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path
                                , params=params, config=merged_config, model=GetSystemParameterListResponse)

    def get_time_window(self, request, config=None):
        """
        get_time_window

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetTimeWindowResponse data
        :rtype: GetTimeWindowResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_TIME_WINDOW)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path
                                , config=merged_config, model=GetTimeWindowResponse)

    def get_tls_cert(self, request, config=None):
        """
        get_tls_cert

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetTlsCertResponse data
        :rtype: GetTlsCertResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_TLS)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path
                                , config=merged_config, model=GetTlsCertResponse)

    def hot_group_add_cluster(self, request, config=None):
        """
        hot_group_add_cluster

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_GROUP,
                                request.group_id,
                                ScsClient.CONSTANT_JOIN)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config)

    def hot_group_change_master_role(self, request, config=None):
        """
        hot_group_change_master_role

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_GROUP,
                                request.group_id,
                                ScsClient.CONSTANT_SET_AS_LEADER,
                                request.instance_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , config=merged_config)

    def hot_group_forbid_write(self, request, config=None):
        """
        hot_group_forbid_write

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_GROUP,
                                request.group_id,
                                ScsClient.CONSTANT_FORBID_WRITE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), config=merged_config)

    def hot_group_modify_name(self, request, config=None):
        """
        hot_group_modify_name

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_GROUP,
                                request.group_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), config=merged_config)

    def hot_group_pre_check(self, request, config=None):
        """
        hot_group_pre_check

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing HotGroupPreCheckResponse data
        :rtype: HotGroupPreCheckResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_GROUP,
                                ScsClient.CONSTANT_CHECK)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config, model=HotGroupPreCheckResponse)

    def hot_group_remove_cluster(self, request, config=None):
        """
        hot_group_remove_cluster

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_GROUP,
                                request.group_id,
                                ScsClient.CONSTANT_QUIT,
                                request.instance_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , config=merged_config)

    def hot_group_set_flow_control_rules(self, request, config=None):
        """
        hot_group_set_flow_control_rules

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_GROUP,
                                request.group_id,
                                ScsClient.CONSTANT_QPS)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), config=merged_config)

    def hot_group_stale_readable(self, request, config=None):
        """
        hot_group_stale_readable

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_GROUP,
                                request.group_id,
                                ScsClient.CONSTANT_STALE_READABLE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), config=merged_config)

    def hot_group_sync_status(self, request, config=None):
        """
        hot_group_sync_status

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing HotGroupSyncStatusResponse data
        :rtype: HotGroupSyncStatusResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_GROUP,
                                request.group_id,
                                ScsClient.CONSTANT_SYNC_STATUS)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path
                                , config=merged_config, model=HotGroupSyncStatusResponse)

    def instance_version_upgrade(self, request, config=None):
        """
        instance_version_upgrade

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_UPGRADE_VERSION)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config)

    def log_details(self, request, config=None):
        """
        log_details

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing LogDetailsResponse data
        :rtype: LogDetailsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_LOG,
                                request.log_id)
        headers = None
        params = {}
        if request.valid_seconds is not None:
            params['validSeconds'] = request.valid_seconds
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path
                                , params=params, config=merged_config, model=LogDetailsResponse)

    def log_list(self, request, config=None):
        """
        log_list

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing LogListResponse data
        :rtype: LogListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_LOG,
                                ScsClient.CONSTANT_LIST)
        headers = None
        params = {}
        params['fileType'] = 'runlog'
        if request.file_type is not None:
            params['fileType'] = request.file_type
        if request.start_time is not None:
            params['startTime'] = request.start_time
        if request.end_time is not None:
            params['endTime'] = request.end_time
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path
                                , params=params, config=merged_config, model=LogListResponse)

    def manual_backup(self, request, config=None):
        """
        manual_backup

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_BACKUP)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config)

    def manually_modify_bandwidth(self, request, config=None):
        """
        manually_modify_bandwidth

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ManuallyModifyBandwidthResponse data
        :rtype: ManuallyModifyBandwidthResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_MODIFY_BANDWIDTH)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config, model=ManuallyModifyBandwidthResponse)

    def master_slave_switch(self, request, config=None):
        """
        master_slave_switch

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_SWITCH_MASTER_SLAVE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), config=merged_config)

    def modify_backup_comment(self, request, config=None):
        """
        modify_backup_comment

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_BACKUP,
                                request.batch_id,
                                ScsClient.CONSTANT_COMMENT)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), config=merged_config)

    def modify_deployment_set(self, request, config=None):
        """
        modify_deployment_set

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_DEPLOY_SET,
                                request.deploy_set_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), config=merged_config)

    def modify_entrance(self, request, config=None):
        """
        modify_entrance

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_AZONE_MIGRATION,
                                ScsClient.CONSTANT_MODIFY_ENTRANCE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config)

    def modify_instance_domain_name(self, request, config=None):
        """
        modify_instance_domain_name

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_RENAME_DOMAIN)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), config=merged_config)

    def modify_instance_name(self, request, config=None):
        """
        modify_instance_name

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_RENAME)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), config=merged_config)

    def modify_parameter_template_name(self, request, config=None):
        """
        modify_parameter_template_name

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_TEMPLATE,
                                ScsClient.CONSTANT_RENAME,
                                request.template_show_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), config=merged_config)

    def modify_parameters(self, request, config=None):
        """
        modify_parameters

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_PARAMETER)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), config=merged_config)

    def modify_replication_zone(self, request, config=None):
        """
        modify_replication_zone

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_AZONE_MIGRATION)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config)

    def modify_sync_group_name(self, request, config=None):
        """
        modify_sync_group_name

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(ScsClient.VERSION_V1, ScsClient.CONSTANT_SYNC_GROUP,
                                request.sync_group_show_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), config=merged_config)

    def modify_time_window(self, request, config=None):
        """
        modify_time_window

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_TIME_WINDOW)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), config=merged_config)

    def parameter_template_delete_parameters(self, request, config=None):
        """
        parameter_template_delete_parameters

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_TEMPLATE,
                                ScsClient.CONSTANT_DELETE_PARAMS,
                                request.template_show_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config)

    def parameter_template_details(self, request, config=None):
        """
        parameter_template_details

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ParameterTemplateDetailsResponse data
        :rtype: ParameterTemplateDetailsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_TEMPLATE,
                                request.template_show_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path
                                , config=merged_config, model=ParameterTemplateDetailsResponse)

    def parameter_template_modify_parameters(self, request, config=None):
        """
        parameter_template_modify_parameters

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_TEMPLATE,
                                ScsClient.CONSTANT_MODIFY_PARAMS,
                                request.template_show_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), config=merged_config)

    def post_paid_to_prepaid(self, request, config=None):
        """
        post_paid_to_prepaid

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing PostPaidToPrepaidResponse data
        :rtype: PostPaidToPrepaidResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                ScsClient.CONSTANT_TO_PREPAY)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config, model=PostPaidToPrepaidResponse)

    def prepaid_to_postpaid(self, request, config=None):
        """
        prepaid_to_postpaid

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing PrepaidToPostpaidResponse data
        :rtype: PrepaidToPostpaidResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                ScsClient.CONSTANT_TO_POSTPAY)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config, model=PrepaidToPostpaidResponse)

    def proxy_node_replace(self, request, config=None):
        """
        proxy_node_replace

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_PROXY_NODE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), config=merged_config)

    def proxy_version_upgrade_or_restart(self, request, config=None):
        """
        proxy_version_upgrade_or_restart

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_UPGRADE_PROXY)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), config=merged_config)

    def query_ip_whitelist(self, request, config=None):
        """
        query_ip_whitelist

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryIpWhitelistResponse data
        :rtype: QueryIpWhitelistResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_SECURITY_IP)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path
                                , config=merged_config, model=QueryIpWhitelistResponse)

    def query_memory_scaling_config(self, request, config=None):
        """
        query_memory_scaling_config

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryMemoryScalingConfigResponse data
        :rtype: QueryMemoryScalingConfigResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_AUTO_SCALING_CONFIG)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path
                                , config=merged_config, model=QueryMemoryScalingConfigResponse)

    def release_hot_group(self, request, config=None):
        """
        release_hot_group

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_GROUP,
                                request.group_id,
                                ScsClient.CONSTANT_RELEASE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path
                                , config=merged_config)

    def release_instance(self, request, config=None):
        """
        release_instance

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_1_1)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path
                                , config=merged_config)

    def renew_instance(self, request, config=None):
        """
        renew_instance

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing RenewInstanceResponse data
        :rtype: RenewInstanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                ScsClient.CONSTANT_RENEW)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config, model=RenewInstanceResponse)

    def restart_instance(self, request, config=None):
        """
        restart_instance

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_RESTART)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), config=merged_config)

    def set_backup_policy(self, request, config=None):
        """
        set_backup_policy

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_BACKUP,
                                ScsClient.CONSTANT_MODIFY_POLICY)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), config=merged_config)

    def set_cluster_as_master(self, request, config=None):
        """
        set_cluster_as_master

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_SET_AS_MASTER)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path
                                , config=merged_config)

    def set_cluster_as_slave(self, request, config=None):
        """
        set_cluster_as_slave

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V2,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_SET_AS_SLAVE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), config=merged_config)

    def set_memory_scaling_config(self, request, config=None):
        """
        set_memory_scaling_config

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_AUTO_SCALING_CONFIG)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config)

    def set_permissions(self, request, config=None):
        """
        set_permissions

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(ScsClient.VERSION_V1, request.instance_id,
                                ScsClient.CONSTANT_ACL_USER_ACTIONS,
                                ScsClient.CONSTANT_AUTHORITY)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config)

    def sync_group_add_instance(self, request, config=None):
        """
        sync_group_add_instance

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_SYNC_GROUP,
                                request.group_id,
                                ScsClient.CONSTANT_ADD_CLUSTER)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config)

    def sync_group_delay_info(self, request, config=None):
        """
        sync_group_delay_info

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing SyncGroupDelayInfoResponse data
        :rtype: SyncGroupDelayInfoResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_SYNC_GROUP,
                                request.group_id,
                                ScsClient.CONSTANT_DELAY_INFO)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path
                                , config=merged_config, model=SyncGroupDelayInfoResponse)

    def sync_group_detail(self, request, config=None):
        """
        sync_group_detail

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing SyncGroupDetailResponse data
        :rtype: SyncGroupDetailResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(ScsClient.VERSION_V1, ScsClient.CONSTANT_SYNC_GROUP,
                                request.sync_group_show_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path
                                , config=merged_config, model=SyncGroupDetailResponse)

    def sync_group_list(self, request, config=None):
        """
        sync_group_list

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing SyncGroupListResponse data
        :rtype: SyncGroupListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(ScsClient.VERSION_V1, ScsClient.CONSTANT_SYNC_GROUP,
                                ScsClient.CONSTANT_LIST)
        headers = None
        params = {}
        params['page'] = '1'
        params['pageSize'] = '10'
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path
                                , params=params, config=merged_config, model=SyncGroupListResponse)

    def sync_group_modify_bnsgroup(self, request, config=None):
        """
        sync_group_modify_bnsgroup

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_SYNC_GROUP,
                                request.group_id,
                                ScsClient.CONSTANT_MODIFY_BNS_GROUP)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), config=merged_config)

    def sync_group_pre_check(self, request, config=None):
        """
        sync_group_pre_check

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing SyncGroupPreCheckResponse data
        :rtype: SyncGroupPreCheckResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_SYNC_GROUP,
                                ScsClient.CONSTANT_CHECK)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config, model=SyncGroupPreCheckResponse)

    def sync_group_remove_instance(self, request, config=None):
        """
        sync_group_remove_instance

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_SYNC_GROUP,
                                request.group_id,
                                ScsClient.CONSTANT_REMOVE_CLUSTER)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config)

    def tde_encryption(self, request, config=None):
        """
        tde_encryption

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing TdeEncryptionResponse data
        :rtype: TdeEncryptionResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(ScsClient.VERSION_V1, ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_TDE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config, model=TdeEncryptionResponse)

    def unbind_security_group(self, request, config=None):
        """
        unbind_security_group

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UnbindSecurityGroupResponse data
        :rtype: UnbindSecurityGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_SECURITY_GROUP,
                                ScsClient.CONSTANT_UNBIND)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config, model=UnbindSecurityGroupResponse)

    def unbind_tags(self, request, config=None):
        """
        unbind_tags

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_UN_BIND_TAG)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), config=merged_config)

    def update_instance_white_group(self, request, config=None):
        """
        update_instance_white_group

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(ScsClient.VERSION_V1, ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_WHITELIST)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), config=merged_config)

    def update_security_group(self, request, config=None):
        """
        update_security_group

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UpdateSecurityGroupResponse data
        :rtype: UpdateSecurityGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_SECURITY_GROUP,
                                ScsClient.CONSTANT_UPDATE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config, model=UpdateSecurityGroupResponse)

    def update_tls_encryption(self, request, config=None):
        """
        update_tls_encryption

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_TLS)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=merged_config)

    def view_security_group(self, request, config=None):
        """
        view_security_group

        :param request: Request entity containing all parameters
        :type request: ScsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ViewSecurityGroupResponse data
        :rtype: ViewSecurityGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ScsClient.CONSTANT_V1,
                                ScsClient.CONSTANT_INSTANCE,
                                request.instance_id,
                                ScsClient.CONSTANT_SECURITY_GROUP)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path
                                , config=merged_config, model=ViewSecurityGroupResponse)


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

    def _send_request(self, http_method, path,
                      body=None, headers=None, params=None,
                      config=None, body_parser=None, model=None):
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
            headers = {b'Accept': b'*/*', b'Content-Type':
                b'application/json;charset=utf-8'}
        sign_fn, params = self._choose_signer(config, params)
        return bce_http_client.send_request(
            config, sign_fn, [handler.parse_error, body_parser],
            http_method, path, body, headers, params, model=model)
