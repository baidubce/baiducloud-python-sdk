"""
Example for bcc client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.auth import bce_v1_signer
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_bcc.models.add_ipv6_response import AddIpv6Response
from baiducloud_python_sdk_bcc.models.attach_volume_response import AttachVolumeResponse
from baiducloud_python_sdk_bcc.models.authorize_server_event_response import AuthorizeServerEventResponse
from baiducloud_python_sdk_bcc.models.auto_renew_reserved_instance_response import AutoRenewReservedInstanceResponse
from baiducloud_python_sdk_bcc.models.batch_change_to_postpaid_response import BatchChangeToPostpaidResponse
from baiducloud_python_sdk_bcc.models.batch_change_to_prepaid_response import BatchChangeToPrepaidResponse
from baiducloud_python_sdk_bcc.models.batch_refund_resource_response import BatchRefundResourceResponse
from baiducloud_python_sdk_bcc.models.bind_instance_security_group_response import BindInstanceSecurityGroupResponse
from baiducloud_python_sdk_bcc.models.bind_role_response import BindRoleResponse
from baiducloud_python_sdk_bcc.models.cancel_auto_renew_reserved_instance_response import (
    CancelAutoRenewReservedInstanceResponse,
)
from baiducloud_python_sdk_bcc.models.cancel_bid_order_response import CancelBidOrderResponse
from baiducloud_python_sdk_bcc.models.cancel_snapshot_share_response import CancelSnapshotShareResponse
from baiducloud_python_sdk_bcc.models.change_to_prepaid_response import ChangeToPrepaidResponse
from baiducloud_python_sdk_bcc.models.check_server_event_response import CheckServerEventResponse
from baiducloud_python_sdk_bcc.models.create_asp_response import CreateAspResponse
from baiducloud_python_sdk_bcc.models.create_authorization_rule_response import CreateAuthorizationRuleResponse
from baiducloud_python_sdk_bcc.models.create_bid_instance_response import CreateBidInstanceResponse
from baiducloud_python_sdk_bcc.models.create_deploy_set_response import CreateDeploySetResponse
from baiducloud_python_sdk_bcc.models.create_ehc_cluster_response import CreateEhcClusterResponse
from baiducloud_python_sdk_bcc.models.create_image_response import CreateImageResponse
from baiducloud_python_sdk_bcc.models.create_instance_by_spec_response import CreateInstanceBySpecResponse
from baiducloud_python_sdk_bcc.models.create_keypair_response import CreateKeypairResponse
from baiducloud_python_sdk_bcc.models.create_reserved_instances_response import CreateReservedInstancesResponse
from baiducloud_python_sdk_bcc.models.create_security_group_response import CreateSecurityGroupResponse
from baiducloud_python_sdk_bcc.models.create_snapshot_response import CreateSnapshotResponse
from baiducloud_python_sdk_bcc.models.create_snapshot_share_response import CreateSnapshotShareResponse
from baiducloud_python_sdk_bcc.models.create_volume_response import CreateVolumeResponse
from baiducloud_python_sdk_bcc.models.create_volume_cluster_response import CreateVolumeClusterResponse
from baiducloud_python_sdk_bcc.models.delete_inst_user_op_authorize_rule_response import (
    DeleteInstUserOpAuthorizeRuleResponse,
)
from baiducloud_python_sdk_bcc.models.delete_prepay_instance_response import DeletePrepayInstanceResponse
from baiducloud_python_sdk_bcc.models.describe_authorize_rules_response import DescribeAuthorizeRulesResponse
from baiducloud_python_sdk_bcc.models.describe_planned_event_records_response import (
    DescribePlannedEventRecordsResponse,
)
from baiducloud_python_sdk_bcc.models.describe_planned_events_response import DescribePlannedEventsResponse
from baiducloud_python_sdk_bcc.models.describe_regions_response import DescribeRegionsResponse
from baiducloud_python_sdk_bcc.models.describe_unplanned_event_records_response import (
    DescribeUnplannedEventRecordsResponse,
)
from baiducloud_python_sdk_bcc.models.describe_unplanned_events_response import DescribeUnplannedEventsResponse
from baiducloud_python_sdk_bcc.models.ehc_cluster_list_response import EhcClusterListResponse
from baiducloud_python_sdk_bcc.models.enter_rescue_mode_response import EnterRescueModeResponse
from baiducloud_python_sdk_bcc.models.exit_rescue_mode_response import ExitRescueModeResponse
from baiducloud_python_sdk_bcc.models.get_asp_response import GetAspResponse
from baiducloud_python_sdk_bcc.models.get_available_images_by_spec_response import GetAvailableImagesBySpecResponse
from baiducloud_python_sdk_bcc.models.get_bid_instance_price_response import GetBidInstancePriceResponse
from baiducloud_python_sdk_bcc.models.get_cds_price_response import GetCdsPriceResponse
from baiducloud_python_sdk_bcc.models.get_deploy_set_response import GetDeploySetResponse
from baiducloud_python_sdk_bcc.models.get_disk_quota_response import GetDiskQuotaResponse
from baiducloud_python_sdk_bcc.models.get_image_response import GetImageResponse
from baiducloud_python_sdk_bcc.models.get_instance_response import GetInstanceResponse
from baiducloud_python_sdk_bcc.models.get_instance_no_charge_list_response import GetInstanceNoChargeListResponse
from baiducloud_python_sdk_bcc.models.get_instance_user_data_info_response import GetInstanceUserDataInfoResponse
from baiducloud_python_sdk_bcc.models.get_instance_vnc_response import GetInstanceVncResponse
from baiducloud_python_sdk_bcc.models.get_price_by_spec_response import GetPriceBySpecResponse
from baiducloud_python_sdk_bcc.models.get_reserved_instance_response import GetReservedInstanceResponse
from baiducloud_python_sdk_bcc.models.get_reserved_instance_price_response import GetReservedInstancePriceResponse
from baiducloud_python_sdk_bcc.models.get_role_list_response import GetRoleListResponse
from baiducloud_python_sdk_bcc.models.get_snapshot_response import GetSnapshotResponse
from baiducloud_python_sdk_bcc.models.get_task_response import GetTaskResponse
from baiducloud_python_sdk_bcc.models.get_volume_response import GetVolumeResponse
from baiducloud_python_sdk_bcc.models.get_volume_cluster_response import GetVolumeClusterResponse
from baiducloud_python_sdk_bcc.models.get_volume_resize_progress_response import GetVolumeResizeProgressResponse
from baiducloud_python_sdk_bcc.models.get_zone_by_spec_response import GetZoneBySpecResponse
from baiducloud_python_sdk_bcc.models.import_image_response import ImportImageResponse
from baiducloud_python_sdk_bcc.models.import_keypair_response import ImportKeypairResponse
from baiducloud_python_sdk_bcc.models.instance_batch_resize_by_spec_response import InstanceBatchResizeBySpecResponse
from baiducloud_python_sdk_bcc.models.keypair_detail_response import KeypairDetailResponse
from baiducloud_python_sdk_bcc.models.list_asps_response import ListAspsResponse
from baiducloud_python_sdk_bcc.models.list_available_resize_spec_response import ListAvailableResizeSpecResponse
from baiducloud_python_sdk_bcc.models.list_bid_flavor_response import ListBidFlavorResponse
from baiducloud_python_sdk_bcc.models.list_deploy_set_response import ListDeploySetResponse
from baiducloud_python_sdk_bcc.models.list_flavor_spec_response import ListFlavorSpecResponse
from baiducloud_python_sdk_bcc.models.list_images_response import ListImagesResponse
from baiducloud_python_sdk_bcc.models.list_instance_by_ids_response import ListInstanceByIdsResponse
from baiducloud_python_sdk_bcc.models.list_instance_enis_response import ListInstanceEnisResponse
from baiducloud_python_sdk_bcc.models.list_instances_response import ListInstancesResponse
from baiducloud_python_sdk_bcc.models.list_keypair_response import ListKeypairResponse
from baiducloud_python_sdk_bcc.models.list_os_response import ListOsResponse
from baiducloud_python_sdk_bcc.models.list_recycle_instance_response import ListRecycleInstanceResponse
from baiducloud_python_sdk_bcc.models.list_reserved_instance_transfer_in_response import (
    ListReservedInstanceTransferInResponse,
)
from baiducloud_python_sdk_bcc.models.list_reserved_instance_transfer_out_response import (
    ListReservedInstanceTransferOutResponse,
)
from baiducloud_python_sdk_bcc.models.list_security_groups_response import ListSecurityGroupsResponse
from baiducloud_python_sdk_bcc.models.list_shared_user_response import ListSharedUserResponse
from baiducloud_python_sdk_bcc.models.list_snapchain_response import ListSnapchainResponse
from baiducloud_python_sdk_bcc.models.list_snapshot_share_response import ListSnapshotShareResponse
from baiducloud_python_sdk_bcc.models.list_snapshots_response import ListSnapshotsResponse
from baiducloud_python_sdk_bcc.models.list_task_response import ListTaskResponse
from baiducloud_python_sdk_bcc.models.list_volume_clusters_response import ListVolumeClustersResponse
from baiducloud_python_sdk_bcc.models.list_volumes_response import ListVolumesResponse
from baiducloud_python_sdk_bcc.models.list_zones_response import ListZonesResponse
from baiducloud_python_sdk_bcc.models.modify_inst_user_op_authorize_rule_attribute_response import (
    ModifyInstUserOpAuthorizeRuleAttributeResponse,
)
from baiducloud_python_sdk_bcc.models.modify_reserved_instances_response import ModifyReservedInstancesResponse
from baiducloud_python_sdk_bcc.models.purchase_reserved_instance_response import PurchaseReservedInstanceResponse
from baiducloud_python_sdk_bcc.models.purchase_reserved_volume_response import PurchaseReservedVolumeResponse
from baiducloud_python_sdk_bcc.models.purchase_reserved_volume_cluster_response import (
    PurchaseReservedVolumeClusterResponse,
)
from baiducloud_python_sdk_bcc.models.remote_copy_image_response import RemoteCopyImageResponse
from baiducloud_python_sdk_bcc.models.remote_copy_snapshot_response import RemoteCopySnapshotResponse
from baiducloud_python_sdk_bcc.models.renew_reserved_instance_response import RenewReservedInstanceResponse
from baiducloud_python_sdk_bcc.models.replace_instance_security_group_response import (
    ReplaceInstanceSecurityGroupResponse,
)
from baiducloud_python_sdk_bcc.models.resize_volume_response import ResizeVolumeResponse
from baiducloud_python_sdk_bcc.models.resize_volume_cluster_response import ResizeVolumeClusterResponse
from baiducloud_python_sdk_bcc.models.unbind_instance_security_group_response import (
    UnbindInstanceSecurityGroupResponse,
)
from baiducloud_python_sdk_bcc.models.unbind_role_response import UnbindRoleResponse
from baiducloud_python_sdk_bcc.models.update_deploy_set_relation_response import UpdateDeploySetRelationResponse

_logger = logging.getLogger(__name__)


class BccClient(BceBaseClient):
    """
    bcc base sdk client
    """

    VERSION_V2 = b'/v2'

    VERSION_V1 = b'/v1'

    CONSTANT_VOLUME = b'volume'

    CONSTANT_CLUSTER = b'cluster'

    CONSTANT_TAG = b'tag'

    CONSTANT_INSTANCE = b'instance'

    CONSTANT_EHC = b'ehc'

    CONSTANT_CREATE = b'create'

    CONSTANT_IMAGE = b'image'

    CONSTANT_REGION = b'region'

    CONSTANT_DESCRIBE_REGIONS = b'describeRegions'

    CONSTANT_SNAPSHOT = b'snapshot'

    CONSTANT_DISK = b'disk'

    CONSTANT_QUOTA = b'quota'

    CONSTANT_RESERVED = b'reserved'

    CONSTANT_GET_PRICE = b'getPrice'

    CONSTANT_RECOVERY = b'recovery'

    CONSTANT_DEPLOYSET = b'deployset'

    CONSTANT_GET_AVAILABLE_IMAGES_BY_SPEC = b'getAvailableImagesBySpec'

    CONSTANT_ROLE = b'role'

    CONSTANT_MODIFY = b'modify'

    CONSTANT_DELETE_PROTECTION = b'deleteProtection'

    CONSTANT_BCC = b'bcc'

    CONSTANT_SECURITY_GROUP = b'securityGroup'

    CONSTANT_PRICE = b'price'

    CONSTANT_BATCH_CREATE_AUTO_RENEW_RULES = b'batchCreateAutoRenewRules'

    CONSTANT_TRANSFER = b'transfer'

    CONSTANT_ASP = b'asp'

    CONSTANT_UPDATE = b'update'

    CONSTANT_CHAIN = b'chain'

    CONSTANT_IN = b'in'

    CONSTANT_LIST = b'list'

    CONSTANT_AUTO_RENEW = b'autoRenew'

    CONSTANT_KEYPAIR = b'keypair'

    CONSTANT_VNC = b'vnc'

    CONSTANT_UN_SHARE = b'unShare'

    CONSTANT_RECYCLE = b'recycle'

    CONSTANT_ACCEPT = b'accept'

    CONSTANT_SHARED_USERS = b'sharedUsers'

    CONSTANT_NO_CHARGE = b'noCharge'

    CONSTANT_REBUILD = b'rebuild'

    CONSTANT_INSTANCE_BATCH_BY_SPEC = b'instanceBatchBySpec'

    CONSTANT_MODIFY_RELATED_DELETE_POLICY = b'modifyRelatedDeletePolicy'

    CONSTANT_DEL_RELATION = b'delRelation'

    CONSTANT_FLAVOR_SPEC = b'flavorSpec'

    CONSTANT_REVOKE = b'revoke'

    CONSTANT_CANCEL_BID_ORDER = b'cancelBidOrder'

    CONSTANT_BID_FLAVOR = b'bidFlavor'

    CONSTANT_INSTANCE_BY_SPEC = b'instanceBySpec'

    CONSTANT_BATCH_DELETE = b'batchDelete'

    CONSTANT_BATCH_REFUND_RESOURCE = b'batchRefundResource'

    CONSTANT_REFUSE = b'refuse'

    CONSTANT_LIST_BY_INSTANCE_ID = b'listByInstanceId'

    CONSTANT_OS = b'os'

    CONSTANT_SECURITYGROUP = b'securitygroup'

    CONSTANT_UNBIND = b'unbind'

    CONSTANT_BATCH_ACTION = b'batchAction'

    CONSTANT_TASK = b'task'

    CONSTANT_DETAIL = b'detail'

    CONSTANT_BIND = b'bind'

    CONSTANT_RULE = b'rule'

    CONSTANT_ATTRIBUTE = b'attribute'

    CONSTANT_GET_USERDATA = b'getUserdata'

    CONSTANT_RESERVED_INSTANCE = b'reservedInstance'

    CONSTANT_FLAVOR_ZONES = b'flavorZones'

    CONSTANT_ZONE = b'zone'

    CONSTANT_CANCEL_AUTO_RENEW = b'cancelAutoRenew'

    CONSTANT_BATCH_DEL_IP = b'batchDelIp'

    CONSTANT_PROGRESS = b'progress'

    CONSTANT_BATCH = b'batch'

    CONSTANT_CHARGING = b'charging'

    CONSTANT_BID_PRICE = b'bidPrice'

    CONSTANT_SNAPSHOT_SHARE = b'snapshotShare'

    CONSTANT_RENAME = b'rename'

    CONSTANT_SUBNET = b'subnet'

    CONSTANT_CHANGE_SUBNET = b'changeSubnet'

    CONSTANT_REPLACE = b'replace'

    CONSTANT_VPC = b'vpc'

    CONSTANT_CHANGE_VPC = b'changeVpc'

    CONSTANT_BATCH_DELETE_AUTO_RENEW_RULES = b'batchDeleteAutoRenewRules'

    CONSTANT_DELETE = b'delete'

    CONSTANT_ADD_IPV6 = b'addIpv6'

    CONSTANT_DELETION_PROTECTION = b'deletionProtection'

    CONSTANT_OUT = b'out'

    CONSTANT_SHARE = b'share'

    CONSTANT_UPDATE_RELATION = b'updateRelation'

    CONSTANT_DEL_IPV6 = b'delIpv6'

    CONSTANT_ENI = b'eni'

    CONSTANT_BATCH_ADD_IP = b'batchAddIp'

    CONSTANT_REMOTE_COPY = b'remote_copy'

    CONSTANT_IMPORT = b'import'

    CONSTANT_RESCUE = b'rescue'

    CONSTANT_MODE = b'mode'

    CONSTANT_EXIT = b'exit'

    CONSTANT_RENEW = b'renew'

    CONSTANT_ENTER = b'enter'

    def __init__(self, config=None):
        """
        Initialize the bcc client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def accept_reserved_instance_transfer(self, request, config=None):
        """
        accept_reserved_instance_transfer

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2,
            BccClient.CONSTANT_INSTANCE,
            BccClient.CONSTANT_RESERVED,
            BccClient.CONSTANT_TRANSFER,
            BccClient.CONSTANT_ACCEPT,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def add_ipv6(self, request, config=None):
        """
        add_ipv6

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing AddIpv6Response data
        :rtype: AddIpv6Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_ADD_IPV6)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), config=merged_config, model=AddIpv6Response
        )

    def attach_asp(self, request, config=None):
        """
        attach_asp

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_ASP, request.asp_id)
        headers = None
        params = {}
        params['attach'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def attach_keypair(self, request, config=None):
        """
        attach_keypair

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_KEYPAIR, request.keypair_id)
        headers = None
        params = {}
        params['attach'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def attach_volume(self, request, config=None):
        """
        attach_volume

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing AttachVolumeResponse data
        :rtype: AttachVolumeResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, request.volume_id)
        headers = None
        params = {}
        params['attach'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=AttachVolumeResponse,
        )

    def authorize_security_group_rule(self, request, config=None):
        """
        authorize_security_group_rule

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_SECURITY_GROUP, request.security_group_id)
        headers = None
        params = {}
        params['authorizeRule'] = None
        if request.sg_version is not None:
            params['sgVersion'] = request.sg_version
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def authorize_server_event(self, request, config=None):
        """
        authorize_server_event

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing AuthorizeServerEventResponse data
        :rtype: AuthorizeServerEventResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = None
        params = {}
        if request.action is not None:
            params['action'] = request.action
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=AuthorizeServerEventResponse,
        )

    def auto_release_instance(self, request, config=None):
        """
        auto_release_instance

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, request.instance_id)
        headers = None
        params = {}
        params['autorelease'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def auto_renew_reserved_instance(self, request, config=None):
        """
        auto_renew_reserved_instance

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing AutoRenewReservedInstanceResponse data
        :rtype: AutoRenewReservedInstanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2,
            BccClient.CONSTANT_INSTANCE,
            BccClient.CONSTANT_RESERVED,
            BccClient.CONSTANT_AUTO_RENEW,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=AutoRenewReservedInstanceResponse,
        )

    def auto_renew_volume_cluster(self, request, config=None):
        """
        auto_renew_volume_cluster

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, BccClient.CONSTANT_CLUSTER, BccClient.CONSTANT_AUTO_RENEW
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def batch_add_ip(self, request, config=None):
        """
        batch_add_ip

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_BATCH_ADD_IP)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def batch_change_to_postpaid(self, request, config=None):
        """
        batch_change_to_postpaid

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BatchChangeToPostpaidResponse data
        :rtype: BatchChangeToPostpaidResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_BATCH, BccClient.CONSTANT_CHARGING
        )
        headers = None
        params = {}
        params['toPostpay'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=BatchChangeToPostpaidResponse,
        )

    def batch_change_to_prepaid(self, request, config=None):
        """
        batch_change_to_prepaid

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BatchChangeToPrepaidResponse data
        :rtype: BatchChangeToPrepaidResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_BATCH, BccClient.CONSTANT_CHARGING
        )
        headers = None
        params = {}
        params['toPrepay'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=BatchChangeToPrepaidResponse,
        )

    def batch_delete_ip(self, request, config=None):
        """
        batch_delete_ip

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_BATCH_DEL_IP)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def batch_refund_resource(self, request, config=None):
        """
        batch_refund_resource

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BatchRefundResourceResponse data
        :rtype: BatchRefundResourceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_BATCH_REFUND_RESOURCE
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=BatchRefundResourceResponse,
        )

    def batch_start_instance(self, request, config=None):
        """
        batch_start_instance

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_BATCH_ACTION)
        headers = None
        params = {}
        params['start'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def batch_stop_instance(self, request, config=None):
        """
        batch_stop_instance

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_BATCH_ACTION)
        headers = None
        params = {}
        params['stop'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def bind_instance_security_group(self, request, config=None):
        """
        bind_instance_security_group

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BindInstanceSecurityGroupResponse data
        :rtype: BindInstanceSecurityGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_SECURITYGROUP, BccClient.CONSTANT_BIND)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=BindInstanceSecurityGroupResponse,
        )

    def bind_instance_to_security_group(self, request, config=None):
        """
        bind_instance_to_security_group

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, request.instance_id)
        headers = None
        params = {}
        params['bind'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def bind_instance_to_tags(self, request, config=None):
        """
        bind_instance_to_tags

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, request.instance_id, BccClient.CONSTANT_TAG
        )
        headers = None
        params = {}
        params['bind'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def bind_reserved_instance_to_tags(self, request, config=None):
        """
        bind_reserved_instance_to_tags

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_BCC, BccClient.CONSTANT_RESERVED, BccClient.CONSTANT_TAG
        )
        headers = None
        params = {}
        params['bind'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def bind_role(self, request, config=None):
        """
        bind_role

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BindRoleResponse data
        :rtype: BindRoleResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_ROLE)
        headers = None
        params = {}
        params['bind'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=BindRoleResponse,
        )

    def bind_tag_image(self, request, config=None):
        """
        bind_tag_image

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_IMAGE, request.image_id, BccClient.CONSTANT_TAG
        )
        headers = None
        params = {}
        params['bind'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def bind_tag_snapchain(self, request, config=None):
        """
        bind_tag_snapchain

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2,
            BccClient.CONSTANT_SNAPSHOT,
            BccClient.CONSTANT_CHAIN,
            request.chain_id,
            BccClient.CONSTANT_TAG,
        )
        headers = None
        params = {}
        params['bind'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def bind_tag_volume(self, request, config=None):
        """
        bind_tag_volume

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, request.volume_id, BccClient.CONSTANT_TAG
        )
        headers = None
        params = {}
        params['bind'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def bind_tag_volume_cluster(self, request, config=None):
        """
        bind_tag_volume_cluster

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2,
            BccClient.CONSTANT_VOLUME,
            BccClient.CONSTANT_CLUSTER,
            request.cluster_id,
            BccClient.CONSTANT_TAG,
        )
        headers = None
        params = {}
        params['bind'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def cancel_auto_renew_reserved_instance(self, request, config=None):
        """
        cancel_auto_renew_reserved_instance

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CancelAutoRenewReservedInstanceResponse data
        :rtype: CancelAutoRenewReservedInstanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2,
            BccClient.CONSTANT_INSTANCE,
            BccClient.CONSTANT_RESERVED,
            BccClient.CONSTANT_CANCEL_AUTO_RENEW,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CancelAutoRenewReservedInstanceResponse,
        )

    def cancel_auto_renew_volume_cluster(self, request, config=None):
        """
        cancel_auto_renew_volume_cluster

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2,
            BccClient.CONSTANT_VOLUME,
            BccClient.CONSTANT_CLUSTER,
            BccClient.CONSTANT_CANCEL_AUTO_RENEW,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def cancel_bid_order(self, request, config=None):
        """
        cancel_bid_order

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CancelBidOrderResponse data
        :rtype: CancelBidOrderResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_CANCEL_BID_ORDER)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CancelBidOrderResponse,
        )

    def cancel_remote_copy_image(self, request, config=None):
        """
        cancel_remote_copy_image

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_IMAGE, request.image_id)
        headers = None
        params = {}
        params['cancelRemoteCopy'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, params=params, config=merged_config)

    def cancel_snapshot_share(self, request, config=None):
        """
        cancel_snapshot_share

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CancelSnapshotShareResponse data
        :rtype: CancelSnapshotShareResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_SNAPSHOT, BccClient.CONSTANT_UN_SHARE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CancelSnapshotShareResponse,
        )

    def change_to_prepaid(self, request, config=None):
        """
        change_to_prepaid

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ChangeToPrepaidResponse data
        :rtype: ChangeToPrepaidResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, request.instance_id)
        headers = None
        params = {}
        params['toPrepay'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=ChangeToPrepaidResponse,
        )

    def change_vpc(self, request, config=None):
        """
        change_vpc

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_VPC, BccClient.CONSTANT_CHANGE_VPC)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def check_server_event(self, request, config=None):
        """
        check_server_event

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CheckServerEventResponse data
        :rtype: CheckServerEventResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = None
        params = {}
        if request.action is not None:
            params['action'] = request.action
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CheckServerEventResponse,
        )

    def create_asp(self, request, config=None):
        """
        create_asp

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateAspResponse data
        :rtype: CreateAspResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_ASP)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), config=merged_config, model=CreateAspResponse
        )

    def create_authorization_rule(self, request, config=None):
        """
        create_authorization_rule

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateAuthorizationRuleResponse data
        :rtype: CreateAuthorizationRuleResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = None
        params = {}
        if request.action is not None:
            params['action'] = request.action
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateAuthorizationRuleResponse,
        )

    def create_auto_renew_rule(self, request, config=None):
        """
        create_auto_renew_rule

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_BATCH_CREATE_AUTO_RENEW_RULES
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def create_bid_instance(self, request, config=None):
        """
        create_bid_instance

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateBidInstanceResponse data
        :rtype: CreateBidInstanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE_BY_SPEC)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateBidInstanceResponse,
        )

    def create_deploy_set(self, request, config=None):
        """
        create_deploy_set

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateDeploySetResponse data
        :rtype: CreateDeploySetResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_DEPLOYSET, BccClient.CONSTANT_CREATE
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateDeploySetResponse,
        )

    def create_ehc_cluster(self, request, config=None):
        """
        create_ehc_cluster

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateEhcClusterResponse data
        :rtype: CreateEhcClusterResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2,
            BccClient.CONSTANT_INSTANCE,
            BccClient.CONSTANT_EHC,
            BccClient.CONSTANT_CLUSTER,
            BccClient.CONSTANT_CREATE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateEhcClusterResponse,
        )

    def create_image(self, request, config=None):
        """
        create_image

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateImageResponse data
        :rtype: CreateImageResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_IMAGE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateImageResponse,
        )

    def create_instance_by_spec(self, request, config=None):
        """
        create_instance_by_spec

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateInstanceBySpecResponse data
        :rtype: CreateInstanceBySpecResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE_BY_SPEC)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateInstanceBySpecResponse,
        )

    def create_keypair(self, request, config=None):
        """
        create_keypair

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateKeypairResponse data
        :rtype: CreateKeypairResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_KEYPAIR)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateKeypairResponse,
        )

    def create_reserved_instance_transfer(self, request, config=None):
        """
        create_reserved_instance_transfer

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2,
            BccClient.CONSTANT_INSTANCE,
            BccClient.CONSTANT_RESERVED,
            BccClient.CONSTANT_TRANSFER,
            BccClient.CONSTANT_CREATE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def create_reserved_instances(self, request, config=None):
        """
        create_reserved_instances

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateReservedInstancesResponse data
        :rtype: CreateReservedInstancesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_RESERVED, BccClient.CONSTANT_CREATE
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateReservedInstancesResponse,
        )

    def create_security_group(self, request, config=None):
        """
        create_security_group

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateSecurityGroupResponse data
        :rtype: CreateSecurityGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_SECURITY_GROUP)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateSecurityGroupResponse,
        )

    def create_snapshot(self, request, config=None):
        """
        create_snapshot

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateSnapshotResponse data
        :rtype: CreateSnapshotResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_SNAPSHOT)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateSnapshotResponse,
        )

    def create_snapshot_share(self, request, config=None):
        """
        create_snapshot_share

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateSnapshotShareResponse data
        :rtype: CreateSnapshotShareResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_SNAPSHOT, BccClient.CONSTANT_SHARE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateSnapshotShareResponse,
        )

    def create_volume(self, request, config=None):
        """
        create_volume

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateVolumeResponse data
        :rtype: CreateVolumeResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateVolumeResponse,
        )

    def create_volume_cluster(self, request, config=None):
        """
        create_volume_cluster

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateVolumeClusterResponse data
        :rtype: CreateVolumeClusterResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, BccClient.CONSTANT_CLUSTER)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateVolumeClusterResponse,
        )

    def del_ipv6(self, request, config=None):
        """
        del_ipv6

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_DEL_IPV6)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def delete_asp(self, request, config=None):
        """
        delete_asp

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_ASP, request.asp_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def delete_auto_renew_rule(self, request, config=None):
        """
        delete_auto_renew_rule

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_BATCH_DELETE_AUTO_RENEW_RULES
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def delete_deploy_set(self, request, config=None):
        """
        delete_deploy_set

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_DEPLOYSET, request.deploy_id
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def delete_ehc_cluster(self, request, config=None):
        """
        delete_ehc_cluster

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2,
            BccClient.CONSTANT_INSTANCE,
            BccClient.CONSTANT_EHC,
            BccClient.CONSTANT_CLUSTER,
            BccClient.CONSTANT_DELETE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def delete_image(self, request, config=None):
        """
        delete_image

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_IMAGE, request.image_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def delete_inst_user_op_authorize_rule(self, request, config=None):
        """
        delete_inst_user_op_authorize_rule

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DeleteInstUserOpAuthorizeRuleResponse data
        :rtype: DeleteInstUserOpAuthorizeRuleResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = None
        params = {}
        if request.action is not None:
            params['action'] = request.action
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DeleteInstUserOpAuthorizeRuleResponse,
        )

    def delete_instance_deploy_set(self, request, config=None):
        """
        delete_instance_deploy_set

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2,
            BccClient.CONSTANT_INSTANCE,
            BccClient.CONSTANT_DEPLOYSET,
            BccClient.CONSTANT_DEL_RELATION,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def delete_keypair(self, request, config=None):
        """
        delete_keypair

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_KEYPAIR, request.keypair_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def delete_prepay_instance(self, request, config=None):
        """
        delete_prepay_instance

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DeletePrepayInstanceResponse data
        :rtype: DeletePrepayInstanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_DELETE)
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DeletePrepayInstanceResponse,
        )

    def delete_recycled_instance(self, request, config=None):
        """
        delete_recycled_instance

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_RECYCLE, BccClient.CONSTANT_INSTANCE, request.instance_id
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def delete_security_group(self, request, config=None):
        """
        delete_security_group

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_SECURITY_GROUP, request.security_group_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def delete_security_group_rule(self, request, config=None):
        """
        delete_security_group_rule

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2,
            BccClient.CONSTANT_SECURITY_GROUP,
            BccClient.CONSTANT_RULE,
            request.security_group_rule_id,
        )
        headers = None
        params = {}
        if request.sg_version is not None:
            params['sgVersion'] = request.sg_version
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_snapshot(self, request, config=None):
        """
        delete_snapshot

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_SNAPSHOT, request.snapshot_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def deletes_instance_deploy_set(self, request, config=None):
        """
        deletes_instance_deploy_set

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2,
            BccClient.CONSTANT_INSTANCE,
            BccClient.CONSTANT_DEPLOYSET,
            BccClient.CONSTANT_DEL_RELATION,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def describe_authorize_rules(self, request, config=None):
        """
        describe_authorize_rules

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeAuthorizeRulesResponse data
        :rtype: DescribeAuthorizeRulesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = None
        params = {}
        if request.action is not None:
            params['action'] = request.action
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeAuthorizeRulesResponse,
        )

    def describe_planned_event_records(self, request, config=None):
        """
        describe_planned_event_records

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribePlannedEventRecordsResponse data
        :rtype: DescribePlannedEventRecordsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = None
        params = {}
        if request.action is not None:
            params['action'] = request.action
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribePlannedEventRecordsResponse,
        )

    def describe_planned_events(self, request, config=None):
        """
        describe_planned_events

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribePlannedEventsResponse data
        :rtype: DescribePlannedEventsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = None
        params = {}
        if request.action is not None:
            params['action'] = request.action
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribePlannedEventsResponse,
        )

    def describe_regions(self, request, config=None):
        """
        describe_regions

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeRegionsResponse data
        :rtype: DescribeRegionsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_REGION, BccClient.CONSTANT_DESCRIBE_REGIONS)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=DescribeRegionsResponse,
        )

    def describe_unplanned_event_records(self, request, config=None):
        """
        describe_unplanned_event_records

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeUnplannedEventRecordsResponse data
        :rtype: DescribeUnplannedEventRecordsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = None
        params = {}
        if request.action is not None:
            params['action'] = request.action
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeUnplannedEventRecordsResponse,
        )

    def describe_unplanned_events(self, request, config=None):
        """
        describe_unplanned_events

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeUnplannedEventsResponse data
        :rtype: DescribeUnplannedEventsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = None
        params = {}
        if request.action is not None:
            params['action'] = request.action
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeUnplannedEventsResponse,
        )

    def detach_asp(self, request, config=None):
        """
        detach_asp

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_ASP, request.asp_id)
        headers = None
        params = {}
        params['detach'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def detach_keypair(self, request, config=None):
        """
        detach_keypair

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_KEYPAIR, request.keypair_id)
        headers = None
        params = {}
        params['detach'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def detach_volume(self, request, config=None):
        """
        detach_volume

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, request.volume_id)
        headers = None
        params = {}
        params['detach'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def ehc_cluster_list(self, request, config=None):
        """
        ehc_cluster_list

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing EhcClusterListResponse data
        :rtype: EhcClusterListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2,
            BccClient.CONSTANT_INSTANCE,
            BccClient.CONSTANT_EHC,
            BccClient.CONSTANT_CLUSTER,
            BccClient.CONSTANT_LIST,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=EhcClusterListResponse,
        )

    def enter_rescue_mode(self, request, config=None):
        """
        enter_rescue_mode

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing EnterRescueModeResponse data
        :rtype: EnterRescueModeResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2,
            BccClient.CONSTANT_INSTANCE,
            BccClient.CONSTANT_RESCUE,
            BccClient.CONSTANT_MODE,
            BccClient.CONSTANT_ENTER,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=EnterRescueModeResponse,
        )

    def exit_rescue_mode(self, request, config=None):
        """
        exit_rescue_mode

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ExitRescueModeResponse data
        :rtype: ExitRescueModeResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2,
            BccClient.CONSTANT_INSTANCE,
            BccClient.CONSTANT_RESCUE,
            BccClient.CONSTANT_MODE,
            BccClient.CONSTANT_EXIT,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=ExitRescueModeResponse,
        )

    def get_asp(self, request, config=None):
        """
        get_asp

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetAspResponse data
        :rtype: GetAspResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_ASP, request.asp_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetAspResponse)

    def get_available_images_by_spec(self, request, config=None):
        """
        get_available_images_by_spec

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetAvailableImagesBySpecResponse data
        :rtype: GetAvailableImagesBySpecResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_IMAGE, BccClient.CONSTANT_GET_AVAILABLE_IMAGES_BY_SPEC
        )
        headers = None
        params = {}
        if request.spec is not None:
            params['spec'] = request.spec
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.os_name is not None:
            params['osName'] = request.os_name
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetAvailableImagesBySpecResponse
        )

    def get_bid_instance_price(self, request, config=None):
        """
        get_bid_instance_price

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetBidInstancePriceResponse data
        :rtype: GetBidInstancePriceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_BID_PRICE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=GetBidInstancePriceResponse,
        )

    def get_cds_price(self, request, config=None):
        """
        get_cds_price

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetCdsPriceResponse data
        :rtype: GetCdsPriceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, BccClient.CONSTANT_GET_PRICE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=GetCdsPriceResponse,
        )

    def get_deploy_set(self, request, config=None):
        """
        get_deploy_set

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetDeploySetResponse data
        :rtype: GetDeploySetResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_DEPLOYSET, request.id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetDeploySetResponse)

    def get_disk_quota(self, request, config=None):
        """
        get_disk_quota

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetDiskQuotaResponse data
        :rtype: GetDiskQuotaResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, BccClient.CONSTANT_DISK, BccClient.CONSTANT_QUOTA
        )
        headers = None
        params = {}
        if request.zone_name is not None:
            params['zoneName'] = request.zone_name
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetDiskQuotaResponse
        )

    def get_image(self, request, config=None):
        """
        get_image

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetImageResponse data
        :rtype: GetImageResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_IMAGE, request.image_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetImageResponse)

    def get_instance(self, request, config=None):
        """
        get_instance

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetInstanceResponse data
        :rtype: GetInstanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, request.instance_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetInstanceResponse)

    def get_instance_no_charge_list(self, request, config=None):
        """
        get_instance_no_charge_list

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetInstanceNoChargeListResponse data
        :rtype: GetInstanceNoChargeListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_NO_CHARGE)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.internal_ip is not None:
            params['internalIp'] = request.internal_ip
        if request.keypair_id is not None:
            params['keypairId'] = request.keypair_id
        if request.zone_name is not None:
            params['zoneName'] = request.zone_name
        if request.instance_ids is not None:
            params['instanceIds'] = request.instance_ids
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetInstanceNoChargeListResponse
        )

    def get_instance_user_data_info(self, request, config=None):
        """
        get_instance_user_data_info

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetInstanceUserDataInfoResponse data
        :rtype: GetInstanceUserDataInfoResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2,
            BccClient.CONSTANT_INSTANCE,
            BccClient.CONSTANT_ATTRIBUTE,
            BccClient.CONSTANT_GET_USERDATA,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=GetInstanceUserDataInfoResponse,
        )

    def get_instance_vnc(self, request, config=None):
        """
        get_instance_vnc

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetInstanceVncResponse data
        :rtype: GetInstanceVncResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, request.instance_id, BccClient.CONSTANT_VNC
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetInstanceVncResponse)

    def get_price_by_spec(self, request, config=None):
        """
        get_price_by_spec

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetPriceBySpecResponse data
        :rtype: GetPriceBySpecResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_PRICE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=GetPriceBySpecResponse,
        )

    def get_reserved_instance(self, request, config=None):
        """
        get_reserved_instance

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetReservedInstanceResponse data
        :rtype: GetReservedInstanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_RESERVED, BccClient.CONSTANT_LIST
        )
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=GetReservedInstanceResponse,
        )

    def get_reserved_instance_price(self, request, config=None):
        """
        get_reserved_instance_price

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetReservedInstancePriceResponse data
        :rtype: GetReservedInstancePriceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_RESERVED_INSTANCE, BccClient.CONSTANT_PRICE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=GetReservedInstancePriceResponse,
        )

    def get_role_list(self, config=None):
        """
        get_role_list
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetRoleListResponse data
        :rtype: GetRoleListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_ROLE, BccClient.CONSTANT_LIST
        )
        headers = None
        return self._send_request(http_methods.GET, path=path, config=config, model=GetRoleListResponse)

    def get_snapshot(self, request, config=None):
        """
        get_snapshot

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetSnapshotResponse data
        :rtype: GetSnapshotResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_SNAPSHOT, request.snapshot_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetSnapshotResponse)

    def get_task(self, request, config=None):
        """
        get_task

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetTaskResponse data
        :rtype: GetTaskResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_TASK, BccClient.CONSTANT_DETAIL)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), config=merged_config, model=GetTaskResponse
        )

    def get_volume(self, request, config=None):
        """
        get_volume

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetVolumeResponse data
        :rtype: GetVolumeResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, request.volume_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetVolumeResponse)

    def get_volume_cluster(self, request, config=None):
        """
        get_volume_cluster

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetVolumeClusterResponse data
        :rtype: GetVolumeClusterResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, BccClient.CONSTANT_CLUSTER, request.cluster_id
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetVolumeClusterResponse)

    def get_volume_resize_progress(self, request, config=None):
        """
        get_volume_resize_progress

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetVolumeResizeProgressResponse data
        :rtype: GetVolumeResizeProgressResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, BccClient.CONSTANT_PROGRESS, request.volume_id
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=GetVolumeResizeProgressResponse
        )

    def get_zone_by_spec(self, request, config=None):
        """
        get_zone_by_spec

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetZoneBySpecResponse data
        :rtype: GetZoneBySpecResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V1, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_FLAVOR_ZONES)
        headers = None
        params = {}
        if request.instance_type is not None:
            params['instanceType'] = request.instance_type
        if request.product_type is not None:
            params['productType'] = request.product_type
        if request.spec is not None:
            params['spec'] = request.spec
        if request.spec_id is not None:
            params['specId'] = request.spec_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetZoneBySpecResponse
        )

    def import_image(self, request, config=None):
        """
        import_image

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ImportImageResponse data
        :rtype: ImportImageResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_IMAGE, BccClient.CONSTANT_IMPORT)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=ImportImageResponse,
        )

    def import_keypair(self, request, config=None):
        """
        import_keypair

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ImportKeypairResponse data
        :rtype: ImportKeypairResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_KEYPAIR)
        headers = None
        params = {}
        params['import'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=ImportKeypairResponse,
        )

    def instance_batch_resize_by_spec(self, request, config=None):
        """
        instance_batch_resize_by_spec

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing InstanceBatchResizeBySpecResponse data
        :rtype: InstanceBatchResizeBySpecResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE_BATCH_BY_SPEC)
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
            model=InstanceBatchResizeBySpecResponse,
        )

    def instance_deletion_protection(self, request, config=None):
        """
        instance_deletion_protection

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2,
            BccClient.CONSTANT_INSTANCE,
            request.instance_id,
            BccClient.CONSTANT_DELETION_PROTECTION,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def instance_recovery(self, request, config=None):
        """
        instance_recovery

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_RECOVERY)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def keypair_detail(self, request, config=None):
        """
        keypair_detail

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing KeypairDetailResponse data
        :rtype: KeypairDetailResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_KEYPAIR, request.keypair_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=KeypairDetailResponse)

    def list_asps(self, request, config=None):
        """
        list_asps

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListAspsResponse data
        :rtype: ListAspsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_ASP)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.asp_name is not None:
            params['aspName'] = request.asp_name
        if request.volume_name is not None:
            params['volumeName'] = request.volume_name
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListAspsResponse
        )

    def list_available_resize_spec(self, request, config=None):
        """
        list_available_resize_spec

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListAvailableResizeSpecResponse data
        :rtype: ListAvailableResizeSpecResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE)
        headers = None
        params = {}
        params['resizeList'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=ListAvailableResizeSpecResponse,
        )

    def list_bid_flavor(self, config=None):
        """
        list_bid_flavor
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListBidFlavorResponse data
        :rtype: ListBidFlavorResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_BID_FLAVOR)
        headers = None
        return self._send_request(http_methods.POST, path=path, config=config, model=ListBidFlavorResponse)

    def list_deploy_set(self, config=None):
        """
        list_deploy_set
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListDeploySetResponse data
        :rtype: ListDeploySetResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_DEPLOYSET, BccClient.CONSTANT_LIST
        )
        headers = None
        return self._send_request(http_methods.GET, path=path, config=config, model=ListDeploySetResponse)

    def list_flavor_spec(self, request, config=None):
        """
        list_flavor_spec

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListFlavorSpecResponse data
        :rtype: ListFlavorSpecResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_FLAVOR_SPEC)
        headers = None
        params = {}
        if request.zone_name is not None:
            params['zoneName'] = request.zone_name
        if request.specs is not None:
            params['specs'] = request.specs
        if request.spec_ids is not None:
            params['specIds'] = request.spec_ids
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListFlavorSpecResponse
        )

    def list_images(self, request, config=None):
        """
        list_images

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListImagesResponse data
        :rtype: ListImagesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_IMAGE)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.image_type is not None:
            params['imageType'] = request.image_type
        if request.image_name is not None:
            params['imageName'] = request.image_name
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListImagesResponse
        )

    def list_instance_by_ids(self, request, config=None):
        """
        list_instance_by_ids

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListInstanceByIdsResponse data
        :rtype: ListInstanceByIdsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_LIST_BY_INSTANCE_ID
        )
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=ListInstanceByIdsResponse,
        )

    def list_instance_enis(self, request, config=None):
        """
        list_instance_enis

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListInstanceEnisResponse data
        :rtype: ListInstanceEnisResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_ENI, request.instance_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=ListInstanceEnisResponse)

    def list_instances(self, request, config=None):
        """
        list_instances

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListInstancesResponse data
        :rtype: ListInstancesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.internal_ip is not None:
            params['internalIp'] = request.internal_ip
        if request.dedicated_host_id is not None:
            params['dedicatedHostId'] = request.dedicated_host_id
        if request.zone_name is not None:
            params['zoneName'] = request.zone_name
        if request.show_rdma_topo is not None:
            params['showRdmaTopo'] = request.show_rdma_topo
        if request.instance_ids is not None:
            params['instanceIds'] = request.instance_ids
        if request.instance_names is not None:
            params['instanceNames'] = request.instance_names
        if request.fuzzy_instance_name is not None:
            params['fuzzyInstanceName'] = request.fuzzy_instance_name
        if request.volume_ids is not None:
            params['volumeIds'] = request.volume_ids
        if request.deploy_set_ids is not None:
            params['deploySetIds'] = request.deploy_set_ids
        if request.security_group_ids is not None:
            params['securityGroupIds'] = request.security_group_ids
        if request.payment_timing is not None:
            params['paymentTiming'] = request.payment_timing
        if request.status is not None:
            params['status'] = request.status
        if request.tags is not None:
            params['tags'] = request.tags
        if request.vpc_id is not None:
            params['vpcId'] = request.vpc_id
        if request.private_ips is not None:
            params['privateIps'] = request.private_ips
        if request.ehc_cluster_id is not None:
            params['ehcClusterId'] = request.ehc_cluster_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListInstancesResponse
        )

    def list_keypair(self, request, config=None):
        """
        list_keypair

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListKeypairResponse data
        :rtype: ListKeypairResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_KEYPAIR)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListKeypairResponse
        )

    def list_os(self, request, config=None):
        """
        list_os

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListOsResponse data
        :rtype: ListOsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_IMAGE, BccClient.CONSTANT_OS)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), config=merged_config, model=ListOsResponse
        )

    def list_recycle_instance(self, request, config=None):
        """
        list_recycle_instance

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListRecycleInstanceResponse data
        :rtype: ListRecycleInstanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_RECYCLE, BccClient.CONSTANT_INSTANCE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=ListRecycleInstanceResponse,
        )

    def list_reserved_instance_transfer_in(self, request, config=None):
        """
        list_reserved_instance_transfer_in

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListReservedInstanceTransferInResponse data
        :rtype: ListReservedInstanceTransferInResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2,
            BccClient.CONSTANT_INSTANCE,
            BccClient.CONSTANT_RESERVED,
            BccClient.CONSTANT_TRANSFER,
            BccClient.CONSTANT_IN,
            BccClient.CONSTANT_LIST,
        )
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=ListReservedInstanceTransferInResponse,
        )

    def list_reserved_instance_transfer_out(self, request, config=None):
        """
        list_reserved_instance_transfer_out

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListReservedInstanceTransferOutResponse data
        :rtype: ListReservedInstanceTransferOutResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2,
            BccClient.CONSTANT_INSTANCE,
            BccClient.CONSTANT_RESERVED,
            BccClient.CONSTANT_TRANSFER,
            BccClient.CONSTANT_OUT,
            BccClient.CONSTANT_LIST,
        )
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=ListReservedInstanceTransferOutResponse,
        )

    def list_security_groups(self, request, config=None):
        """
        list_security_groups

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListSecurityGroupsResponse data
        :rtype: ListSecurityGroupsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_SECURITY_GROUP)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.vpc_id is not None:
            params['vpcId'] = request.vpc_id
        if request.security_group_id is not None:
            params['securityGroupId'] = request.security_group_id
        if request.security_group_ids is not None:
            params['securityGroupIds'] = request.security_group_ids
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListSecurityGroupsResponse
        )

    def list_shared_user(self, request, config=None):
        """
        list_shared_user

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListSharedUserResponse data
        :rtype: ListSharedUserResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_IMAGE, request.image_id, BccClient.CONSTANT_SHARED_USERS
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=ListSharedUserResponse)

    def list_snapchain(self, request, config=None):
        """
        list_snapchain

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListSnapchainResponse data
        :rtype: ListSnapchainResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_SNAPSHOT, BccClient.CONSTANT_CHAIN)
        headers = None
        params = {}
        if request.order_by is not None:
            params['orderBy'] = request.order_by
        if request.order is not None:
            params['order'] = request.order
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.volume_id is not None:
            params['volumeId'] = request.volume_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListSnapchainResponse
        )

    def list_snapshot_share(self, request, config=None):
        """
        list_snapshot_share

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListSnapshotShareResponse data
        :rtype: ListSnapshotShareResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2,
            BccClient.CONSTANT_SNAPSHOT,
            BccClient.CONSTANT_SNAPSHOT_SHARE,
            BccClient.CONSTANT_LIST,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=ListSnapshotShareResponse,
        )

    def list_snapshots(self, request, config=None):
        """
        list_snapshots

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListSnapshotsResponse data
        :rtype: ListSnapshotsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_SNAPSHOT)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.volume_id is not None:
            params['volumeId'] = request.volume_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListSnapshotsResponse
        )

    def list_task(self, request, config=None):
        """
        list_task

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListTaskResponse data
        :rtype: ListTaskResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_TASK, BccClient.CONSTANT_LIST)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), config=merged_config, model=ListTaskResponse
        )

    def list_volume_clusters(self, request, config=None):
        """
        list_volume_clusters

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListVolumeClustersResponse data
        :rtype: ListVolumeClustersResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, BccClient.CONSTANT_CLUSTER)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.zone_name is not None:
            params['zoneName'] = request.zone_name
        if request.cluster_name is not None:
            params['clusterName'] = request.cluster_name
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListVolumeClustersResponse
        )

    def list_volumes(self, request, config=None):
        """
        list_volumes

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListVolumesResponse data
        :rtype: ListVolumesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.zone_name is not None:
            params['zoneName'] = request.zone_name
        if request.cluster_id is not None:
            params['clusterId'] = request.cluster_id
        if request.charge_filter is not None:
            params['chargeFilter'] = request.charge_filter
        if request.usage_filter is not None:
            params['usageFilter'] = request.usage_filter
        if request.name is not None:
            params['name'] = request.name
        if request.product_category is not None:
            params['productCategory'] = request.product_category
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListVolumesResponse
        )

    def list_zones(self, config=None):
        """
        list_zones
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListZonesResponse data
        :rtype: ListZonesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_ZONE)
        headers = None
        return self._send_request(http_methods.GET, path=path, config=config, model=ListZonesResponse)

    def modify_cds_attribute(self, request, config=None):
        """
        modify_cds_attribute

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, request.volume_id)
        headers = None
        params = {}
        params['modify'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def modify_ehc_cluster(self, request, config=None):
        """
        modify_ehc_cluster

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2,
            BccClient.CONSTANT_INSTANCE,
            BccClient.CONSTANT_EHC,
            BccClient.CONSTANT_CLUSTER,
            BccClient.CONSTANT_MODIFY,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def modify_inst_user_op_authorize_rule_attribute(self, request, config=None):
        """
        modify_inst_user_op_authorize_rule_attribute

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ModifyInstUserOpAuthorizeRuleAttributeResponse data
        :rtype: ModifyInstUserOpAuthorizeRuleAttributeResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = None
        params = {}
        if request.action is not None:
            params['action'] = request.action
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=ModifyInstUserOpAuthorizeRuleAttributeResponse,
        )

    def modify_instance_attributes(self, request, config=None):
        """
        modify_instance_attributes

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, request.instance_id)
        headers = None
        params = {}
        params['modifyAttribute'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def modify_instance_desc(self, request, config=None):
        """
        modify_instance_desc

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, request.instance_id)
        headers = None
        params = {}
        params['modifyDesc'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def modify_instance_hostname(self, request, config=None):
        """
        modify_instance_hostname

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, request.instance_id)
        headers = None
        params = {}
        params['changeHostname'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def modify_instance_password(self, request, config=None):
        """
        modify_instance_password

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, request.instance_id)
        headers = None
        params = {}
        params['changePass'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def modify_related_delete_policy(self, request, config=None):
        """
        modify_related_delete_policy

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2,
            BccClient.CONSTANT_INSTANCE,
            request.instance_id,
            BccClient.CONSTANT_MODIFY_RELATED_DELETE_POLICY,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def modify_reserved_instances(self, request, config=None):
        """
        modify_reserved_instances

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ModifyReservedInstancesResponse data
        :rtype: ModifyReservedInstancesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_RESERVED, BccClient.CONSTANT_MODIFY
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=ModifyReservedInstancesResponse,
        )

    def modify_volume_charge_type(self, request, config=None):
        """
        modify_volume_charge_type

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, request.volume_id)
        headers = None
        params = {}
        params['modifyChargeType'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def modify_volume_delete_protection_v2(self, request, config=None):
        """
        modify_volume_delete_protection_v2

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2,
            BccClient.CONSTANT_VOLUME,
            BccClient.CONSTANT_MODIFY,
            BccClient.CONSTANT_DELETE_PROTECTION,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def purchase_reserved_instance(self, request, config=None):
        """
        purchase_reserved_instance

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing PurchaseReservedInstanceResponse data
        :rtype: PurchaseReservedInstanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, request.instance_id)
        headers = None
        params = {}
        params['purchaseReserved'] = None
        if request.related_renew_flag is not None:
            params['relatedRenewFlag'] = request.related_renew_flag
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=PurchaseReservedInstanceResponse,
        )

    def purchase_reserved_volume(self, request, config=None):
        """
        purchase_reserved_volume

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing PurchaseReservedVolumeResponse data
        :rtype: PurchaseReservedVolumeResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, request.volume_id)
        headers = None
        params = {}
        params['purchaseReserved'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=PurchaseReservedVolumeResponse,
        )

    def purchase_reserved_volume_cluster(self, request, config=None):
        """
        purchase_reserved_volume_cluster

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing PurchaseReservedVolumeClusterResponse data
        :rtype: PurchaseReservedVolumeClusterResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, BccClient.CONSTANT_CLUSTER, request.cluster_id
        )
        headers = None
        params = {}
        params['purchaseReserved'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=PurchaseReservedVolumeClusterResponse,
        )

    def reboot_instance(self, request, config=None):
        """
        reboot_instance

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, request.instance_id)
        headers = None
        params = {}
        params['reboot'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def rebuild_batch_instance(self, request, config=None):
        """
        rebuild_batch_instance

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_REBUILD)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def rebuild_instance(self, request, config=None):
        """
        rebuild_instance

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, request.instance_id)
        headers = None
        params = {}
        params['rebuild'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def refuse_reserved_instance_transfer(self, request, config=None):
        """
        refuse_reserved_instance_transfer

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2,
            BccClient.CONSTANT_INSTANCE,
            BccClient.CONSTANT_RESERVED,
            BccClient.CONSTANT_TRANSFER,
            BccClient.CONSTANT_REFUSE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def release_instance_by_post(self, request, config=None):
        """
        release_instance_by_post

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, request.instance_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def release_multiple_instance_by_post(self, request, config=None):
        """
        release_multiple_instance_by_post

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_BATCH_DELETE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def release_volume(self, request, config=None):
        """
        release_volume

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, request.volume_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def remote_copy_image(self, request, config=None):
        """
        remote_copy_image

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing RemoteCopyImageResponse data
        :rtype: RemoteCopyImageResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_IMAGE, request.image_id)
        headers = None
        params = {}
        params['remoteCopy'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=RemoteCopyImageResponse,
        )

    def remote_copy_snapshot(self, request, config=None):
        """
        remote_copy_snapshot

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing RemoteCopySnapshotResponse data
        :rtype: RemoteCopySnapshotResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_SNAPSHOT, BccClient.CONSTANT_REMOTE_COPY, request.snapshot_id
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=RemoteCopySnapshotResponse,
        )

    def rename_image(self, request, config=None):
        """
        rename_image

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_IMAGE, BccClient.CONSTANT_RENAME)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def rename_keypair(self, request, config=None):
        """
        rename_keypair

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_KEYPAIR, request.keypair_id)
        headers = None
        params = {}
        params['rename'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def rename_volume(self, request, config=None):
        """
        rename_volume

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, request.volume_id)
        headers = None
        params = {}
        params['rename'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def renew_reserved_instance(self, request, config=None):
        """
        renew_reserved_instance

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing RenewReservedInstanceResponse data
        :rtype: RenewReservedInstanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_RESERVED, BccClient.CONSTANT_RENEW
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=RenewReservedInstanceResponse,
        )

    def replace_instance_security_group(self, request, config=None):
        """
        replace_instance_security_group

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ReplaceInstanceSecurityGroupResponse data
        :rtype: ReplaceInstanceSecurityGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_SECURITYGROUP, BccClient.CONSTANT_REPLACE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=ReplaceInstanceSecurityGroupResponse,
        )

    def resize_instance_by_spec(self, request, config=None):
        """
        resize_instance_by_spec

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE_BY_SPEC, request.instance_id)
        headers = None
        params = {}
        params['resize'] = None
        if request.action is not None:
            params['action'] = request.action
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def resize_volume(self, request, config=None):
        """
        resize_volume

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ResizeVolumeResponse data
        :rtype: ResizeVolumeResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, request.volume_id)
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
            model=ResizeVolumeResponse,
        )

    def resize_volume_cluster(self, request, config=None):
        """
        resize_volume_cluster

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ResizeVolumeClusterResponse data
        :rtype: ResizeVolumeClusterResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, BccClient.CONSTANT_CLUSTER, request.cluster_id
        )
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
            model=ResizeVolumeClusterResponse,
        )

    def revoke_reserved_instance_transfer(self, request, config=None):
        """
        revoke_reserved_instance_transfer

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2,
            BccClient.CONSTANT_INSTANCE,
            BccClient.CONSTANT_RESERVED,
            BccClient.CONSTANT_TRANSFER,
            BccClient.CONSTANT_REVOKE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def revoke_security_group_rule(self, request, config=None):
        """
        revoke_security_group_rule

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_SECURITY_GROUP, request.security_group_id)
        headers = None
        params = {}
        params['revokeRule'] = None
        if request.sg_version is not None:
            params['sgVersion'] = request.sg_version
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def rollback_volume(self, request, config=None):
        """
        rollback_volume

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, request.volume_id)
        headers = None
        params = {}
        params['rollback'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def share_image(self, request, config=None):
        """
        share_image

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_IMAGE, request.image_id)
        headers = None
        params = {}
        params['share'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def start_instance(self, request, config=None):
        """
        start_instance

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, request.instance_id)
        headers = None
        params = {}
        params['start'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def stop_instance(self, request, config=None):
        """
        stop_instance

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, request.instance_id)
        headers = None
        params = {}
        params['stop'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def un_share_image(self, request, config=None):
        """
        un_share_image

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_IMAGE, request.image_id)
        headers = None
        params = {}
        params['unshare'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def unbind_instance_from_security_group(self, request, config=None):
        """
        unbind_instance_from_security_group

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, request.instance_id)
        headers = None
        params = {}
        params['unbind'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def unbind_instance_from_tags(self, request, config=None):
        """
        unbind_instance_from_tags

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, request.instance_id, BccClient.CONSTANT_TAG
        )
        headers = None
        params = {}
        params['unbind'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def unbind_instance_security_group(self, request, config=None):
        """
        unbind_instance_security_group

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UnbindInstanceSecurityGroupResponse data
        :rtype: UnbindInstanceSecurityGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_SECURITYGROUP, BccClient.CONSTANT_UNBIND)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=UnbindInstanceSecurityGroupResponse,
        )

    def unbind_reserved_instance_from_tags(self, request, config=None):
        """
        unbind_reserved_instance_from_tags

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_BCC, BccClient.CONSTANT_RESERVED, BccClient.CONSTANT_TAG
        )
        headers = None
        params = {}
        params['unbind'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def unbind_role(self, request, config=None):
        """
        unbind_role

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UnbindRoleResponse data
        :rtype: UnbindRoleResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_ROLE)
        headers = None
        params = {}
        params['unbind'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=UnbindRoleResponse,
        )

    def unbind_tag_image(self, request, config=None):
        """
        unbind_tag_image

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_IMAGE, request.image_id, BccClient.CONSTANT_TAG
        )
        headers = None
        params = {}
        params['unbind'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def unbind_tag_snapchain(self, request, config=None):
        """
        unbind_tag_snapchain

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2,
            BccClient.CONSTANT_SNAPSHOT,
            BccClient.CONSTANT_CHAIN,
            request.chain_id,
            BccClient.CONSTANT_TAG,
        )
        headers = None
        params = {}
        params['unbind'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def unbind_tag_volume(self, request, config=None):
        """
        unbind_tag_volume

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, request.volume_id, BccClient.CONSTANT_TAG
        )
        headers = None
        params = {}
        params['unbind'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def unbind_tag_volume_cluster(self, request, config=None):
        """
        unbind_tag_volume_cluster

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2,
            BccClient.CONSTANT_VOLUME,
            BccClient.CONSTANT_CLUSTER,
            request.cluster_id,
            BccClient.CONSTANT_TAG,
        )
        headers = None
        params = {}
        params['unbind'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_asp(self, request, config=None):
        """
        update_asp

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_ASP, BccClient.CONSTANT_UPDATE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def update_deploy_set(self, request, config=None):
        """
        update_deploy_set

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_INSTANCE, BccClient.CONSTANT_DEPLOYSET, request.deploy_id
        )
        headers = None
        params = {}
        params['modifyAttribute'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_deploy_set_relation(self, request, config=None):
        """
        update_deploy_set_relation

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UpdateDeploySetRelationResponse data
        :rtype: UpdateDeploySetRelationResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2,
            BccClient.CONSTANT_INSTANCE,
            BccClient.CONSTANT_DEPLOYSET,
            BccClient.CONSTANT_UPDATE_RELATION,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=UpdateDeploySetRelationResponse,
        )

    def update_instance_subnet(self, request, config=None):
        """
        update_instance_subnet

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_SUBNET, BccClient.CONSTANT_CHANGE_SUBNET)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def update_keypair_description(self, request, config=None):
        """
        update_keypair_description

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_KEYPAIR, request.keypair_id)
        headers = None
        params = {}
        params['updateDesc'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_security_group_rule(self, request, config=None):
        """
        update_security_group_rule

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_SECURITY_GROUP, BccClient.CONSTANT_RULE, BccClient.CONSTANT_UPDATE
        )
        headers = None
        params = {}
        if request.sg_version is not None:
            params['sgVersion'] = request.sg_version
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
