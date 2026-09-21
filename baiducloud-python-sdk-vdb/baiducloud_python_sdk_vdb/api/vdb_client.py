"""
Example for vdb client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_core.util import request_body_utils
from baiducloud_python_sdk_vdb.models.account_list_using_get_response import AccountListUsingGETResponse
from baiducloud_python_sdk_vdb.models.create_instance_using_post_response import CreateInstanceUsingPOSTResponse
from baiducloud_python_sdk_vdb.models.get_config_using_get_response import GetConfigUsingGETResponse
from baiducloud_python_sdk_vdb.models.get_free_instance_quota_response import GetFreeInstanceQuotaResponse
from baiducloud_python_sdk_vdb.models.get_free_instance_quota_using_get_response import (
    GetFreeInstanceQuotaUsingGETResponse,
)
from baiducloud_python_sdk_vdb.models.get_instance_list_using_get_response import GetInstanceListUsingGETResponse
from baiducloud_python_sdk_vdb.models.get_price_using_post_response import GetPriceUsingPOSTResponse
from baiducloud_python_sdk_vdb.models.get_quota_using_get_response import GetQuotaUsingGETResponse
from baiducloud_python_sdk_vdb.models.get_tls_certificate_using_get_response import GetTLSCertificateUsingGETResponse
from baiducloud_python_sdk_vdb.models.get_tls_info_using_get_response import GetTLSInfoUsingGETResponse
from baiducloud_python_sdk_vdb.models.getinstancelistusingget1_response import Getinstancelistusingget1Response
from baiducloud_python_sdk_vdb.models.instance_detail_using_get_response import InstanceDetailUsingGETResponse
from baiducloud_python_sdk_vdb.models.list_records_using_get_response import ListRecordsUsingGETResponse
from baiducloud_python_sdk_vdb.models.password_using_get_response import PasswordUsingGETResponse
from baiducloud_python_sdk_vdb.models.resize_instance_using_post_response import ResizeInstanceUsingPOSTResponse
from baiducloud_python_sdk_vdb.models.zone_list_using_get_response import ZoneListUsingGETResponse

_logger = logging.getLogger(__name__)


class VdbClient(BceBaseClient):
    """
    vdb base sdk client
    """

    VERSION_V1 = b'/v1'

    CONSTANT_VDB = b'vdb'

    CONSTANT_INSTANCE = b'instance'

    CONSTANT_PRICE = b'price'

    CONSTANT_ACCOUNT = b'account'

    CONSTANT_RESET_PASSWORD = b'resetPassword'

    CONSTANT_MODIFY_PUBLIC_ACCESS = b'modifyPublicAccess'

    CONSTANT_DETAIL = b'detail'

    CONSTANT_DESCRIBE_INSTANCE_CONFIGS = b'describeInstanceConfigs'

    CONSTANT_RECYCLER = b'recycler'

    CONSTANT_DELETE = b'delete'

    CONSTANT_MODIFY_NAME = b'modifyName'

    CONSTANT_MODIFY_INSTANCE_CONFIG = b'modifyInstanceConfig'

    CONSTANT_LIST = b'list'

    CONSTANT_PASSWORD = b'password'

    CONSTANT_BACKUP = b'backup'

    CONSTANT_SET_COMMENT = b'setComment'

    CONSTANT_MODIFY_DOMAIN = b'modifyDomain'

    CONSTANT_RECOVER = b'recover'

    CONSTANT_BIND_EIP = b'bindEip'

    CONSTANT_MANUAL_BACKUP = b'manualBackup'

    CONSTANT_SECURITY = b'security'

    CONSTANT_MODIFY_T_L_S = b'modifyTLS'

    CONSTANT_CREATE = b'create'

    CONSTANT_RESIZE = b'resize'

    CONSTANT_GET_T_L_S_CERTIFICATE = b'getTLSCertificate'

    CONSTANT_FREE_QUOTA = b'freeQuota'

    CONSTANT_DELETE_RECORD = b'deleteRecord'

    CONSTANT_LIST_RECORDS = b'listRecords'

    CONSTANT_GET_CONFIG = b'getConfig'

    CONSTANT_GET_NODE_SPEC_LIST = b'getNodeSpecList'

    CONSTANT_UNBIND_EIP = b'unbindEip'

    CONSTANT_QUOTA = b'quota'

    CONSTANT_ZONE = b'zone'

    CONSTANT_GET_T_L_S_INFO = b'getTLSInfo'

    CONSTANT_SET_CONFIG = b'setConfig'

    def __init__(self, config=None):
        """
        Initialize the vdb client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def account_list_using_get(self, request, config=None):
        """
        account_list_using_get

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing AccountListUsingGETResponse data
        :rtype: AccountListUsingGETResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1, VdbClient.CONSTANT_VDB, VdbClient.CONSTANT_ACCOUNT, VdbClient.CONSTANT_LIST
        )
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=AccountListUsingGETResponse
        )

    def bind_eip_using_post(self, request, config=None):
        """
        bind_eip_using_post

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1,
            VdbClient.CONSTANT_VDB,
            VdbClient.CONSTANT_INSTANCE,
            request.instance_id,
            VdbClient.CONSTANT_BIND_EIP,
        )
        headers = None
        params = {}
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def create_instance_using_post(self, request, config=None):
        """
        create_instance_using_post

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateInstanceUsingPOSTResponse data
        :rtype: CreateInstanceUsingPOSTResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1, VdbClient.CONSTANT_VDB, VdbClient.CONSTANT_INSTANCE, VdbClient.CONSTANT_CREATE
        )
        headers = None
        params = {}
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateInstanceUsingPOSTResponse,
        )

    def delete_instance_using_delete(self, request, config=None):
        """
        delete_instance_using_delete

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1, VdbClient.CONSTANT_VDB, VdbClient.CONSTANT_INSTANCE, VdbClient.CONSTANT_DELETE
        )
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_record_using_delete(self, request, config=None):
        """
        delete_record_using_delete

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1, VdbClient.CONSTANT_VDB, VdbClient.CONSTANT_BACKUP, VdbClient.CONSTANT_DELETE_RECORD
        )
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        if request.batch_id is not None:
            params['batchId'] = request.batch_id
        if request.backup_id is not None:
            params['backupId'] = request.backup_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_recycler_instance(self, request, config=None):
        """
        delete_recycler_instance

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1,
            VdbClient.CONSTANT_VDB,
            VdbClient.CONSTANT_RECYCLER,
            VdbClient.CONSTANT_INSTANCE,
            VdbClient.CONSTANT_DELETE,
        )
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def deleteinstanceusingdelete1(self, request, config=None):
        """
        deleteinstanceusingdelete1

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1,
            VdbClient.CONSTANT_VDB,
            VdbClient.CONSTANT_RECYCLER,
            VdbClient.CONSTANT_INSTANCE,
            VdbClient.CONSTANT_DELETE,
        )
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def describe_instance_configs(self, request, config=None):
        """
        describe_instance_configs

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1,
            VdbClient.CONSTANT_VDB,
            VdbClient.CONSTANT_INSTANCE,
            VdbClient.CONSTANT_DESCRIBE_INSTANCE_CONFIGS,
        )
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, params=params, config=merged_config)

    def describe_instance_configs_using_get(self, request, config=None):
        """
        describe_instance_configs_using_get

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1,
            VdbClient.CONSTANT_VDB,
            VdbClient.CONSTANT_INSTANCE,
            VdbClient.CONSTANT_DESCRIBE_INSTANCE_CONFIGS,
        )
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, params=params, config=merged_config)

    def get_config_using_get(self, request, config=None):
        """
        get_config_using_get

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetConfigUsingGETResponse data
        :rtype: GetConfigUsingGETResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1, VdbClient.CONSTANT_VDB, VdbClient.CONSTANT_BACKUP, VdbClient.CONSTANT_GET_CONFIG
        )
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetConfigUsingGETResponse
        )

    def get_free_instance_quota(self, config=None):
        """
        get_free_instance_quota
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetFreeInstanceQuotaResponse data
        :rtype: GetFreeInstanceQuotaResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1, VdbClient.CONSTANT_VDB, VdbClient.CONSTANT_INSTANCE, VdbClient.CONSTANT_FREE_QUOTA
        )
        headers = None
        return self._send_request(http_methods.GET, path=path, config=config, model=GetFreeInstanceQuotaResponse)

    def get_free_instance_quota_using_get(self, config=None):
        """
        get_free_instance_quota_using_get
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetFreeInstanceQuotaUsingGETResponse data
        :rtype: GetFreeInstanceQuotaUsingGETResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1, VdbClient.CONSTANT_VDB, VdbClient.CONSTANT_INSTANCE, VdbClient.CONSTANT_FREE_QUOTA
        )
        headers = None
        return self._send_request(
            http_methods.GET, path=path, config=config, model=GetFreeInstanceQuotaUsingGETResponse
        )

    def get_instance_list_using_get(self, request, config=None):
        """
        get_instance_list_using_get

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetInstanceListUsingGETResponse data
        :rtype: GetInstanceListUsingGETResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1, VdbClient.CONSTANT_VDB, VdbClient.CONSTANT_INSTANCE, VdbClient.CONSTANT_LIST
        )
        headers = None
        params = {}
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        if request.instance_type is not None:
            params['instanceType'] = request.instance_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetInstanceListUsingGETResponse
        )

    def get_node_spec_list_using_get(self, request, config=None):
        """
        get_node_spec_list_using_get

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1,
            VdbClient.CONSTANT_VDB,
            VdbClient.CONSTANT_INSTANCE,
            VdbClient.CONSTANT_GET_NODE_SPEC_LIST,
        )
        headers = None
        params = {}
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, params=params, config=merged_config)

    def get_price_using_post(self, request, config=None):
        """
        get_price_using_post

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetPriceUsingPOSTResponse data
        :rtype: GetPriceUsingPOSTResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1, VdbClient.CONSTANT_VDB, VdbClient.CONSTANT_INSTANCE, VdbClient.CONSTANT_PRICE
        )
        headers = None
        params = {}
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=GetPriceUsingPOSTResponse,
        )

    def get_quota_using_get(self, request, config=None):
        """
        get_quota_using_get

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetQuotaUsingGETResponse data
        :rtype: GetQuotaUsingGETResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1, VdbClient.CONSTANT_VDB, VdbClient.CONSTANT_BACKUP, VdbClient.CONSTANT_QUOTA
        )
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetQuotaUsingGETResponse
        )

    def get_tls_certificate_using_get(self, request, config=None):
        """
        get_tls_certificate_using_get

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetTLSCertificateUsingGETResponse data
        :rtype: GetTLSCertificateUsingGETResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1,
            VdbClient.CONSTANT_VDB,
            VdbClient.CONSTANT_SECURITY,
            VdbClient.CONSTANT_GET_T_L_S_CERTIFICATE,
        )
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetTLSCertificateUsingGETResponse
        )

    def get_tls_info_using_get(self, request, config=None):
        """
        get_tls_info_using_get

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetTLSInfoUsingGETResponse data
        :rtype: GetTLSInfoUsingGETResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1,
            VdbClient.CONSTANT_VDB,
            VdbClient.CONSTANT_SECURITY,
            VdbClient.CONSTANT_GET_T_L_S_INFO,
        )
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetTLSInfoUsingGETResponse
        )

    def getinstancelistusingget1(self, request, config=None):
        """
        getinstancelistusingget1

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing Getinstancelistusingget1Response data
        :rtype: Getinstancelistusingget1Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1,
            VdbClient.CONSTANT_VDB,
            VdbClient.CONSTANT_RECYCLER,
            VdbClient.CONSTANT_INSTANCE,
            VdbClient.CONSTANT_LIST,
        )
        headers = None
        params = {}
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=Getinstancelistusingget1Response
        )

    def instance_detail_using_get(self, request, config=None):
        """
        instance_detail_using_get

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing InstanceDetailUsingGETResponse data
        :rtype: InstanceDetailUsingGETResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1, VdbClient.CONSTANT_VDB, VdbClient.CONSTANT_INSTANCE, VdbClient.CONSTANT_DETAIL
        )
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=InstanceDetailUsingGETResponse
        )

    def list_records_using_get(self, request, config=None):
        """
        list_records_using_get

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListRecordsUsingGETResponse data
        :rtype: ListRecordsUsingGETResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1, VdbClient.CONSTANT_VDB, VdbClient.CONSTANT_BACKUP, VdbClient.CONSTANT_LIST_RECORDS
        )
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        if request.list_order is not None:
            params['listOrder'] = request.list_order
        if request.page is not None:
            params['page'] = request.page
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListRecordsUsingGETResponse
        )

    def manual_backup_using_post(self, request, config=None):
        """
        manual_backup_using_post

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1, VdbClient.CONSTANT_VDB, VdbClient.CONSTANT_BACKUP, VdbClient.CONSTANT_MANUAL_BACKUP
        )
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def modify_instance_config(self, request, config=None):
        """
        modify_instance_config

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1,
            VdbClient.CONSTANT_VDB,
            VdbClient.CONSTANT_INSTANCE,
            VdbClient.CONSTANT_MODIFY_INSTANCE_CONFIG,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def modify_instance_config_using_post(self, request, config=None):
        """
        modify_instance_config_using_post

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1,
            VdbClient.CONSTANT_VDB,
            VdbClient.CONSTANT_INSTANCE,
            VdbClient.CONSTANT_MODIFY_INSTANCE_CONFIG,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def modify_password_using_post(self, request, config=None):
        """
        modify_password_using_post

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1, VdbClient.CONSTANT_VDB, VdbClient.CONSTANT_ACCOUNT, VdbClient.CONSTANT_RESET_PASSWORD
        )
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def modify_public_access(self, request, config=None):
        """
        modify_public_access

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1,
            VdbClient.CONSTANT_VDB,
            VdbClient.CONSTANT_INSTANCE,
            request.instance_id,
            VdbClient.CONSTANT_MODIFY_PUBLIC_ACCESS,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def modify_public_access_using_put(self, request, config=None):
        """
        modify_public_access_using_put

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1,
            VdbClient.CONSTANT_VDB,
            VdbClient.CONSTANT_INSTANCE,
            request.instance_id,
            VdbClient.CONSTANT_MODIFY_PUBLIC_ACCESS,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def modify_tls_using_put(self, request, config=None):
        """
        modify_tls_using_put

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1, VdbClient.CONSTANT_VDB, VdbClient.CONSTANT_SECURITY, VdbClient.CONSTANT_MODIFY_T_L_S
        )
        headers = None
        params = {}
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def password_using_get(self, request, config=None):
        """
        password_using_get

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing PasswordUsingGETResponse data
        :rtype: PasswordUsingGETResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1, VdbClient.CONSTANT_VDB, VdbClient.CONSTANT_ACCOUNT, VdbClient.CONSTANT_PASSWORD
        )
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.username is not None:
            params['username'] = request.username
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=PasswordUsingGETResponse
        )

    def recover_instance_using_post(self, request, config=None):
        """
        recover_instance_using_post

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1,
            VdbClient.CONSTANT_VDB,
            VdbClient.CONSTANT_RECYCLER,
            VdbClient.CONSTANT_INSTANCE,
            VdbClient.CONSTANT_RECOVER,
        )
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, params=params, config=merged_config)

    def recover_using_post(self, request, config=None):
        """
        recover_using_post

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1, VdbClient.CONSTANT_VDB, VdbClient.CONSTANT_BACKUP, VdbClient.CONSTANT_RECOVER
        )
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def resize_instance_using_post(self, request, config=None):
        """
        resize_instance_using_post

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ResizeInstanceUsingPOSTResponse data
        :rtype: ResizeInstanceUsingPOSTResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1, VdbClient.CONSTANT_VDB, VdbClient.CONSTANT_INSTANCE, VdbClient.CONSTANT_RESIZE
        )
        headers = None
        params = {}
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=ResizeInstanceUsingPOSTResponse,
        )

    def set_comment_using_post(self, request, config=None):
        """
        set_comment_using_post

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1, VdbClient.CONSTANT_VDB, VdbClient.CONSTANT_BACKUP, VdbClient.CONSTANT_SET_COMMENT
        )
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def set_config_using_post(self, request, config=None):
        """
        set_config_using_post

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1, VdbClient.CONSTANT_VDB, VdbClient.CONSTANT_BACKUP, VdbClient.CONSTANT_SET_CONFIG
        )
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def unbind_eip_using_post(self, request, config=None):
        """
        unbind_eip_using_post

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1,
            VdbClient.CONSTANT_VDB,
            VdbClient.CONSTANT_INSTANCE,
            request.instance_id,
            VdbClient.CONSTANT_UNBIND_EIP,
        )
        headers = None
        params = {}
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, params=params, config=merged_config)

    def update_instance_domain(self, request, config=None):
        """
        update_instance_domain

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1,
            VdbClient.CONSTANT_VDB,
            VdbClient.CONSTANT_INSTANCE,
            request.instance_id,
            VdbClient.CONSTANT_MODIFY_DOMAIN,
        )
        headers = None
        params = {}
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_instance_domain_using_post(self, request, config=None):
        """
        update_instance_domain_using_post

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1,
            VdbClient.CONSTANT_VDB,
            VdbClient.CONSTANT_INSTANCE,
            request.instance_id,
            VdbClient.CONSTANT_MODIFY_DOMAIN,
        )
        headers = None
        params = {}
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_instance_name(self, request, config=None):
        """
        update_instance_name

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1,
            VdbClient.CONSTANT_VDB,
            VdbClient.CONSTANT_INSTANCE,
            request.instance_id,
            VdbClient.CONSTANT_MODIFY_NAME,
        )
        headers = None
        params = {}
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_instance_name_using_post(self, request, config=None):
        """
        update_instance_name_using_post

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            VdbClient.VERSION_V1,
            VdbClient.CONSTANT_VDB,
            VdbClient.CONSTANT_INSTANCE,
            request.instance_id,
            VdbClient.CONSTANT_MODIFY_NAME,
        )
        headers = None
        params = {}
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def zone_list_using_get(self, request, config=None):
        """
        zone_list_using_get

        :param request: Request entity containing all parameters
        :type request: VdbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ZoneListUsingGETResponse data
        :rtype: ZoneListUsingGETResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(VdbClient.VERSION_V1, VdbClient.CONSTANT_VDB, VdbClient.CONSTANT_ZONE)
        headers = None
        params = {}
        if request.var_from is not None:
            params['from'] = request.var_from
        if request.engine_type is not None:
            params['engineType'] = request.engine_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ZoneListUsingGETResponse
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
