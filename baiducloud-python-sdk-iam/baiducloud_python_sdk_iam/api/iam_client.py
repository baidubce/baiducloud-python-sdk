"""
Example for iam client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.auth import bce_v1_signer
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_iam.models.list_access_key_response import ListAccessKeyResponse
from baiducloud_python_sdk_iam.models.list_all_subjects_granted_permissions_response import (
    ListAllSubjectsGrantedPermissionsResponse,
)
from baiducloud_python_sdk_iam.models.list_groups_response import ListGroupsResponse
from baiducloud_python_sdk_iam.models.list_roles_response import ListRolesResponse
from baiducloud_python_sdk_iam.models.list_strategies_response import ListStrategiesResponse
from baiducloud_python_sdk_iam.models.list_the_permissions_of_roles_response import ListThePermissionsOfRolesResponse
from baiducloud_python_sdk_iam.models.list_the_permissions_of_the_group_response import (
    ListThePermissionsOfTheGroupResponse,
)
from baiducloud_python_sdk_iam.models.list_the_subjects_granted_permissions_response import (
    ListTheSubjectsGrantedPermissionsResponse,
)
from baiducloud_python_sdk_iam.models.list_the_user_s_permissions_response import ListTheUserSPermissionsResponse
from baiducloud_python_sdk_iam.models.list_user_response import ListUserResponse
from baiducloud_python_sdk_iam.models.list_user_groups_response import ListUserGroupsResponse
from baiducloud_python_sdk_iam.models.list_users_within_the_group_response import ListUsersWithinTheGroupResponse
from baiducloud_python_sdk_iam.models.query_sub_user_idp_response import QuerySubUserIdpResponse
from baiducloud_python_sdk_iam.models.query_summary_of_main_account_response import QuerySummaryOfMainAccountResponse
from baiducloud_python_sdk_iam.models.query_the_last_usage_time_of_accesskey_response import (
    QueryTheLastUsageTimeOfAccesskeyResponse,
)
from baiducloud_python_sdk_iam.models.update_sub_user_idp_response import UpdateSubUserIdpResponse
from baiducloud_python_sdk_iam.models.update_sub_user_idp_status_response import UpdateSubUserIdpStatusResponse

_logger = logging.getLogger(__name__)


class IamClient(BceBaseClient):
    """
    iam base sdk client
    """

    VERSION_V1 = b'/v1'

    CONSTANT_ACCOUNT = b'account'

    CONSTANT_SUMMARY = b'summary'

    CONSTANT_POLICY = b'policy'

    CONSTANT_ROLE = b'role'

    CONSTANT_APIKEY = b'apikey'

    CONSTANT_CREATE = b'create'

    CONSTANT_ENTITY = b'entity'

    CONSTANT_SUB_USER = b'subUser'

    CONSTANT_IDP = b'idp'

    CONSTANT_UPDATE_STATUS = b'updateStatus'

    CONSTANT_LIST = b'list'

    CONSTANT_ACCESSKEY = b'accesskey'

    CONSTANT_LASTUSEDTIME = b'lastusedtime'

    CONSTANT_USER = b'user'

    CONSTANT_LOGIN_PROFILE = b'loginProfile'

    CONSTANT_B_C_E__B_E_A_R_E_R = b'BCE-BEARER'

    CONSTANT_TOKEN = b'token'

    CONSTANT_GROUP = b'group'

    CONSTANT_OPERATION = b'operation'

    CONSTANT_MFA = b'mfa'

    CONSTANT_SWITCH = b'switch'

    CONSTANT_DELETE = b'delete'

    CONSTANT_QUERY = b'query'

    CONSTANT_GRANT = b'grant'

    CONSTANT_UPDATE = b'update'

    CONSTANT_DETAIL = b'detail'

    CONSTANT_MFA_TYPE = b'mfaType'

    CONSTANT_DECRYPT = b'decrypt'

    def __init__(self, config=None):
        """
        Initialize the iam client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def add_user_to_group(self, request, config=None):
        """
        add_user_to_group

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1,
            IamClient.CONSTANT_GROUP,
            request.group_name,
            IamClient.CONSTANT_USER,
            request.user_name,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, config=merged_config)

    def associate_group_permissions(self, request, config=None):
        """
        associate_group_permissions

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1,
            IamClient.CONSTANT_GROUP,
            request.group_name,
            IamClient.CONSTANT_POLICY,
            request.policy_name,
        )
        headers = None
        params = {}
        if request.policy_type is not None:
            params['policyType'] = request.policy_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def associate_role_permissions(self, request, config=None):
        """
        associate_role_permissions

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1,
            IamClient.CONSTANT_ROLE,
            request.role_name,
            IamClient.CONSTANT_POLICY,
            request.policy_name,
        )
        headers = None
        params = {}
        if request.policy_type is not None:
            params['policyType'] = request.policy_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def associate_user_permissions(self, request, config=None):
        """
        associate_user_permissions

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1,
            IamClient.CONSTANT_USER,
            request.user_name,
            IamClient.CONSTANT_POLICY,
            request.policy_name,
        )
        headers = None
        params = {}
        if request.policy_type is not None:
            params['policyType'] = request.policy_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def change_sub_user_password(self, request, config=None):
        """
        change_sub_user_password

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1, IamClient.CONSTANT_SUB_USER, request.user_name, IamClient.CONSTANT_UPDATE
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def create_access_key(self, request, config=None):
        """
        create_access_key

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1, IamClient.CONSTANT_USER, request.user_name, IamClient.CONSTANT_ACCESSKEY
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, config=merged_config)

    def create_apikey_permanently_valid(self, request, config=None):
        """
        create_apikey_permanently_valid

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(IamClient.VERSION_V1, IamClient.CONSTANT_APIKEY, IamClient.CONSTANT_CREATE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def create_group(self, request, config=None):
        """
        create_group

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(IamClient.VERSION_V1, IamClient.CONSTANT_GROUP)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def create_role(self, request, config=None):
        """
        create_role

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(IamClient.VERSION_V1, IamClient.CONSTANT_ROLE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def create_strategy(self, request, config=None):
        """
        create_strategy

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(IamClient.VERSION_V1, IamClient.CONSTANT_POLICY)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def create_user(self, request, config=None):
        """
        create_user

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(IamClient.VERSION_V1, IamClient.CONSTANT_USER)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def decoding_apikey_permanently_valid(self, request, config=None):
        """
        decoding_apikey_permanently_valid

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(IamClient.VERSION_V1, IamClient.CONSTANT_APIKEY, IamClient.CONSTANT_DECRYPT)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def delete_access_key(self, request, config=None):
        """
        delete_access_key

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1,
            IamClient.CONSTANT_USER,
            request.user_name,
            IamClient.CONSTANT_ACCESSKEY,
            request.access_key_id,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def delete_apikey_permanently_valid(self, request, config=None):
        """
        delete_apikey_permanently_valid

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(IamClient.VERSION_V1, IamClient.CONSTANT_APIKEY, IamClient.CONSTANT_DELETE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def delete_group(self, request, config=None):
        """
        delete_group

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(IamClient.VERSION_V1, IamClient.CONSTANT_GROUP, request.group_name)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def delete_login_profile(self, request, config=None):
        """
        delete_login_profile

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1, IamClient.CONSTANT_USER, request.user_name, IamClient.CONSTANT_LOGIN_PROFILE
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def delete_role(self, request, config=None):
        """
        delete_role

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(IamClient.VERSION_V1, IamClient.CONSTANT_ROLE, request.role_name)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def delete_strategy(self, request, config=None):
        """
        delete_strategy

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(IamClient.VERSION_V1, IamClient.CONSTANT_POLICY, request.policy_name)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def delete_sub_user_idp(self, config=None):
        """
        delete_sub_user_idp
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1, IamClient.CONSTANT_SUB_USER, IamClient.CONSTANT_IDP, IamClient.CONSTANT_DELETE
        )
        headers = None
        return self._send_request(http_methods.POST, path=path, config=config)

    def delete_user(self, request, config=None):
        """
        delete_user

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(IamClient.VERSION_V1, IamClient.CONSTANT_USER, request.user_name)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def disable_access_key(self, request, config=None):
        """
        disable_access_key

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1,
            IamClient.CONSTANT_USER,
            request.user_name,
            IamClient.CONSTANT_ACCESSKEY,
            request.access_key_id,
        )
        headers = None
        params = {}
        params['disable'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def enable_access_key(self, request, config=None):
        """
        enable_access_key

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1,
            IamClient.CONSTANT_USER,
            request.user_name,
            IamClient.CONSTANT_ACCESSKEY,
            request.access_key_id,
        )
        headers = None
        params = {}
        params['enable'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def get_login_profile(self, request, config=None):
        """
        get_login_profile

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1, IamClient.CONSTANT_USER, request.user_name, IamClient.CONSTANT_LOGIN_PROFILE
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config)

    def get_session_api_key(self, request, config=None):
        """
        get_session_api_key

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(IamClient.VERSION_V1, IamClient.CONSTANT_B_C_E__B_E_A_R_E_R, IamClient.CONSTANT_TOKEN)
        headers = None
        params = {}
        if request.expire_in_seconds is not None:
            params['expireInSeconds'] = request.expire_in_seconds
        if request.acl is not None:
            params['acl'] = request.acl
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, params=params, config=merged_config)

    def get_user(self, request, config=None):
        """
        get_user

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(IamClient.VERSION_V1, IamClient.CONSTANT_USER, request.user_name)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config)

    def list_access_key(self, request, config=None):
        """
        list_access_key

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListAccessKeyResponse data
        :rtype: ListAccessKeyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1, IamClient.CONSTANT_USER, request.user_name, IamClient.CONSTANT_ACCESSKEY
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=ListAccessKeyResponse)

    def list_all_subjects_granted_permissions(self, request, config=None):
        """
        list_all_subjects_granted_permissions

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListAllSubjectsGrantedPermissionsResponse data
        :rtype: ListAllSubjectsGrantedPermissionsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1, IamClient.CONSTANT_POLICY, request.policy_id, IamClient.CONSTANT_ENTITY
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=ListAllSubjectsGrantedPermissionsResponse
        )

    def list_groups(self, config=None):
        """
        list_groups
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListGroupsResponse data
        :rtype: ListGroupsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(IamClient.VERSION_V1, IamClient.CONSTANT_GROUP)
        headers = None
        return self._send_request(http_methods.GET, path=path, config=config, model=ListGroupsResponse)

    def list_roles(self, config=None):
        """
        list_roles
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListRolesResponse data
        :rtype: ListRolesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(IamClient.VERSION_V1, IamClient.CONSTANT_ROLE)
        headers = None
        return self._send_request(http_methods.GET, path=path, config=config, model=ListRolesResponse)

    def list_strategies(self, request, config=None):
        """
        list_strategies

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListStrategiesResponse data
        :rtype: ListStrategiesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(IamClient.VERSION_V1, IamClient.CONSTANT_POLICY)
        headers = None
        params = {}
        if request.policy_type is not None:
            params['policyType'] = request.policy_type
        if request.name_filter is not None:
            params['nameFilter'] = request.name_filter
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListStrategiesResponse
        )

    def list_the_permissions_of_roles(self, request, config=None):
        """
        list_the_permissions_of_roles

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListThePermissionsOfRolesResponse data
        :rtype: ListThePermissionsOfRolesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1, IamClient.CONSTANT_ROLE, request.role_name, IamClient.CONSTANT_POLICY
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=ListThePermissionsOfRolesResponse
        )

    def list_the_permissions_of_the_group(self, request, config=None):
        """
        list_the_permissions_of_the_group

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListThePermissionsOfTheGroupResponse data
        :rtype: ListThePermissionsOfTheGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1, IamClient.CONSTANT_GROUP, request.group_name, IamClient.CONSTANT_POLICY
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=ListThePermissionsOfTheGroupResponse
        )

    def list_the_subjects_granted_permissions(self, request, config=None):
        """
        list_the_subjects_granted_permissions

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListTheSubjectsGrantedPermissionsResponse data
        :rtype: ListTheSubjectsGrantedPermissionsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1,
            IamClient.CONSTANT_POLICY,
            request.policy_id,
            IamClient.CONSTANT_GRANT,
            request.grant_type,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=ListTheSubjectsGrantedPermissionsResponse
        )

    def list_the_user_s_permissions(self, request, config=None):
        """
        list_the_user_s_permissions

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListTheUserSPermissionsResponse data
        :rtype: ListTheUserSPermissionsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1, IamClient.CONSTANT_USER, request.user_name, IamClient.CONSTANT_POLICY
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=ListTheUserSPermissionsResponse
        )

    def list_user(self, config=None):
        """
        list_user
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListUserResponse data
        :rtype: ListUserResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(IamClient.VERSION_V1, IamClient.CONSTANT_USER)
        headers = None
        return self._send_request(http_methods.GET, path=path, config=config, model=ListUserResponse)

    def list_user_groups(self, request, config=None):
        """
        list_user_groups

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListUserGroupsResponse data
        :rtype: ListUserGroupsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1, IamClient.CONSTANT_USER, request.user_name, IamClient.CONSTANT_GROUP
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=ListUserGroupsResponse)

    def list_users_within_the_group(self, request, config=None):
        """
        list_users_within_the_group

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListUsersWithinTheGroupResponse data
        :rtype: ListUsersWithinTheGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1, IamClient.CONSTANT_GROUP, request.group_name, IamClient.CONSTANT_USER
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=ListUsersWithinTheGroupResponse
        )

    def modify_sub_user_operation_protection(self, request, config=None):
        """
        modify_sub_user_operation_protection

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1,
            IamClient.CONSTANT_USER,
            IamClient.CONSTANT_OPERATION,
            IamClient.CONSTANT_MFA,
            IamClient.CONSTANT_SWITCH,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def obtain_a_list_of_permanently_valid_apikeys(self, request, config=None):
        """
        obtain_a_list_of_permanently_valid_apikeys

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(IamClient.VERSION_V1, IamClient.CONSTANT_APIKEY, IamClient.CONSTANT_LIST)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def query_apikey_details_permanently_valid(self, request, config=None):
        """
        query_apikey_details_permanently_valid

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(IamClient.VERSION_V1, IamClient.CONSTANT_APIKEY, IamClient.CONSTANT_DETAIL)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def query_group(self, request, config=None):
        """
        query_group

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(IamClient.VERSION_V1, IamClient.CONSTANT_GROUP, request.group_name)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config)

    def query_role(self, request, config=None):
        """
        query_role

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(IamClient.VERSION_V1, IamClient.CONSTANT_ROLE, request.role_name)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config)

    def query_strategy(self, request, config=None):
        """
        query_strategy

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(IamClient.VERSION_V1, IamClient.CONSTANT_POLICY, request.policy_name)
        headers = None
        params = {}
        if request.policy_type is not None:
            params['policyType'] = request.policy_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, params=params, config=merged_config)

    def query_sub_user_idp(self, config=None):
        """
        query_sub_user_idp
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QuerySubUserIdpResponse data
        :rtype: QuerySubUserIdpResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1, IamClient.CONSTANT_SUB_USER, IamClient.CONSTANT_IDP, IamClient.CONSTANT_QUERY
        )
        headers = None
        return self._send_request(http_methods.GET, path=path, config=config, model=QuerySubUserIdpResponse)

    def query_summary_of_main_account(self, config=None):
        """
        query_summary_of_main_account
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QuerySummaryOfMainAccountResponse data
        :rtype: QuerySummaryOfMainAccountResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(IamClient.VERSION_V1, IamClient.CONSTANT_ACCOUNT, IamClient.CONSTANT_SUMMARY)
        headers = None
        return self._send_request(http_methods.GET, path=path, config=config, model=QuerySummaryOfMainAccountResponse)

    def query_the_last_usage_time_of_accesskey(self, request, config=None):
        """
        query_the_last_usage_time_of_accesskey

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryTheLastUsageTimeOfAccesskeyResponse data
        :rtype: QueryTheLastUsageTimeOfAccesskeyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1, IamClient.CONSTANT_ACCESSKEY, request.access_key_id, IamClient.CONSTANT_LASTUSEDTIME
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=QueryTheLastUsageTimeOfAccesskeyResponse
        )

    def remove_group_permissions(self, request, config=None):
        """
        remove_group_permissions

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1,
            IamClient.CONSTANT_GROUP,
            request.group_name,
            IamClient.CONSTANT_POLICY,
            request.policy_name,
        )
        headers = None
        params = {}
        if request.policy_type is not None:
            params['policyType'] = request.policy_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def remove_role_permissions(self, request, config=None):
        """
        remove_role_permissions

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1,
            IamClient.CONSTANT_ROLE,
            request.role_name,
            IamClient.CONSTANT_POLICY,
            request.policy_name,
        )
        headers = None
        params = {}
        if request.policy_type is not None:
            params['policyType'] = request.policy_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def remove_user_from_the_group(self, request, config=None):
        """
        remove_user_from_the_group

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1,
            IamClient.CONSTANT_GROUP,
            request.group_name,
            IamClient.CONSTANT_USER,
            request.user_name,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def remove_user_permissions(self, request, config=None):
        """
        remove_user_permissions

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1,
            IamClient.CONSTANT_USER,
            request.user_name,
            IamClient.CONSTANT_POLICY,
            request.policy_name,
        )
        headers = None
        params = {}
        if request.policy_type is not None:
            params['policyType'] = request.policy_type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def unbind_sub_user_virtual_mfa(self, request, config=None):
        """
        unbind_sub_user_virtual_mfa

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1,
            IamClient.CONSTANT_USER,
            request.user_name,
            IamClient.CONSTANT_MFA_TYPE,
            request.mfa_type,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def update_apikey_permanently_valid(self, request, config=None):
        """
        update_apikey_permanently_valid

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(IamClient.VERSION_V1, IamClient.CONSTANT_APIKEY, IamClient.CONSTANT_UPDATE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def update_group(self, request, config=None):
        """
        update_group

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(IamClient.VERSION_V1, IamClient.CONSTANT_GROUP, request.group_name)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def update_login_profile(self, request, config=None):
        """
        update_login_profile

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1, IamClient.CONSTANT_USER, request.user_name, IamClient.CONSTANT_LOGIN_PROFILE
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def update_role(self, request, config=None):
        """
        update_role

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(IamClient.VERSION_V1, IamClient.CONSTANT_ROLE, request.role_name)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def update_strategy(self, request, config=None):
        """
        update_strategy

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(IamClient.VERSION_V1, IamClient.CONSTANT_POLICY, request.policy_name)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def update_sub_user_idp(self, request, config=None):
        """
        update_sub_user_idp

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UpdateSubUserIdpResponse data
        :rtype: UpdateSubUserIdpResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1, IamClient.CONSTANT_SUB_USER, IamClient.CONSTANT_IDP, IamClient.CONSTANT_UPDATE
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=UpdateSubUserIdpResponse,
        )

    def update_sub_user_idp_status(self, request, config=None):
        """
        update_sub_user_idp_status

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UpdateSubUserIdpStatusResponse data
        :rtype: UpdateSubUserIdpStatusResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            IamClient.VERSION_V1, IamClient.CONSTANT_SUB_USER, IamClient.CONSTANT_IDP, IamClient.CONSTANT_UPDATE_STATUS
        )
        headers = None
        params = {}
        if request.status is not None:
            params['status'] = request.status
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, params=params, config=merged_config, model=UpdateSubUserIdpStatusResponse
        )

    def update_user(self, request, config=None):
        """
        update_user

        :param request: Request entity containing all parameters
        :type request: IamClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(IamClient.VERSION_V1, IamClient.CONSTANT_USER, request.user_name)
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
