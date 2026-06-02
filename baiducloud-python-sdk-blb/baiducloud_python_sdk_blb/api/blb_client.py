"""
Example for blb client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.auth import bce_v1_signer
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_blb.models.billing_change_post_to_pre_blb_response import BillingChangePostToPreBlbResponse
from baiducloud_python_sdk_blb.models.billing_change_pre_to_post_blb_response import BillingChangePreToPostBlbResponse
from baiducloud_python_sdk_blb.models.blb_inquiry_response import BlbInquiryResponse
from baiducloud_python_sdk_blb.models.create_app_blb_response import CreateAppBlbResponse
from baiducloud_python_sdk_blb.models.create_app_blb_ip_group_response import CreateAppBlbIpGroupResponse
from baiducloud_python_sdk_blb.models.create_app_blb_server_group_response import CreateAppBlbServerGroupResponse
from baiducloud_python_sdk_blb.models.create_app_blb_server_group_port_response import (
    CreateAppBlbServerGroupPortResponse,
)
from baiducloud_python_sdk_blb.models.create_blb_response import CreateBlbResponse
from baiducloud_python_sdk_blb.models.create_lbdc_response import CreateLbdcResponse
from baiducloud_python_sdk_blb.models.create_service_response import CreateServiceResponse
from baiducloud_python_sdk_blb.models.describe_app_blb_response import DescribeAppBlbResponse
from baiducloud_python_sdk_blb.models.describe_app_blb_http_listener_response import DescribeAppBlbHttpListenerResponse
from baiducloud_python_sdk_blb.models.describe_app_blb_https_listener_response import (
    DescribeAppBlbHttpsListenerResponse,
)
from baiducloud_python_sdk_blb.models.describe_app_blb_ip_group_response import DescribeAppBlbIpGroupResponse
from baiducloud_python_sdk_blb.models.describe_app_blb_ip_group_member_response import (
    DescribeAppBlbIpGroupMemberResponse,
)
from baiducloud_python_sdk_blb.models.describe_app_blb_listener_response import DescribeAppBlbListenerResponse
from baiducloud_python_sdk_blb.models.describe_app_blb_policy_response import DescribeAppBlbPolicyResponse
from baiducloud_python_sdk_blb.models.describe_app_blb_server_group_response import DescribeAppBlbServerGroupResponse
from baiducloud_python_sdk_blb.models.describe_app_blb_server_group_mount_rs_response import (
    DescribeAppBlbServerGroupMountRsResponse,
)
from baiducloud_python_sdk_blb.models.describe_app_blb_server_group_rs_response import (
    DescribeAppBlbServerGroupRsResponse,
)
from baiducloud_python_sdk_blb.models.describe_app_blb_server_group_unmount_rs_response import (
    DescribeAppBlbServerGroupUnmountRsResponse,
)
from baiducloud_python_sdk_blb.models.describe_app_blb_ssl_listener_response import DescribeAppBlbSslListenerResponse
from baiducloud_python_sdk_blb.models.describe_app_blb_tcp_listener_response import DescribeAppBlbTcpListenerResponse
from baiducloud_python_sdk_blb.models.describe_app_blb_udp_listener_response import DescribeAppBlbUdpListenerResponse
from baiducloud_python_sdk_blb.models.describe_app_blbs_response import DescribeAppBlbsResponse
from baiducloud_python_sdk_blb.models.describe_blb_response import DescribeBlbResponse
from baiducloud_python_sdk_blb.models.describe_blb_enterprise_security_groups_response import (
    DescribeBlbEnterpriseSecurityGroupsResponse,
)
from baiducloud_python_sdk_blb.models.describe_blb_http_listener_response import DescribeBlbHttpListenerResponse
from baiducloud_python_sdk_blb.models.describe_blb_https_listener_response import DescribeBlbHttpsListenerResponse
from baiducloud_python_sdk_blb.models.describe_blb_listener_response import DescribeBlbListenerResponse
from baiducloud_python_sdk_blb.models.describe_blb_security_groups_response import DescribeBlbSecurityGroupsResponse
from baiducloud_python_sdk_blb.models.describe_blb_server_health_response import DescribeBlbServerHealthResponse
from baiducloud_python_sdk_blb.models.describe_blb_servers_response import DescribeBlbServersResponse
from baiducloud_python_sdk_blb.models.describe_blb_ssl_listener_response import DescribeBlbSslListenerResponse
from baiducloud_python_sdk_blb.models.describe_blb_tcp_listener_response import DescribeBlbTcpListenerResponse
from baiducloud_python_sdk_blb.models.describe_blb_udp_listener_response import DescribeBlbUdpListenerResponse
from baiducloud_python_sdk_blb.models.describe_blbs_response import DescribeBlbsResponse
from baiducloud_python_sdk_blb.models.describe_lbdc_response import DescribeLbdcResponse
from baiducloud_python_sdk_blb.models.describe_lbdc_blb_response import DescribeLbdcBlbResponse
from baiducloud_python_sdk_blb.models.describe_lbdcs_response import DescribeLbdcsResponse
from baiducloud_python_sdk_blb.models.describe_service_response import DescribeServiceResponse
from baiducloud_python_sdk_blb.models.describe_services_response import DescribeServicesResponse
from baiducloud_python_sdk_blb.models.resize_blb_response import ResizeBlbResponse

_logger = logging.getLogger(__name__)


class BlbClient(BceBaseClient):
    """
    blb base sdk client
    """

    VERSION_V1 = b'/v1'

    CONSTANT_BLB = b'blb'

    CONSTANT_SECURITYGROUP = b'securitygroup'

    CONSTANT_ENTERPRISE = b'enterprise'

    CONSTANT_APPBLB = b'appblb'

    CONSTANT_APPSERVERGROUP = b'appservergroup'

    CONSTANT_LBDC = b'lbdc'

    CONSTANT_SERVICE = b'service'

    CONSTANT_H_T_T_P_SLISTENER = b'HTTPSlistener'

    CONSTANT_BACKENDSERVER = b'backendserver'

    CONSTANT_IPGROUP = b'ipgroup'

    CONSTANT_MEMBER = b'member'

    CONSTANT_CHARGE = b'charge'

    CONSTANT_T_C_PLISTENER = b'TCPlistener'

    CONSTANT_U_D_PLISTENER = b'UDPlistener'

    CONSTANT_S_S_LLISTENER = b'SSLlistener'

    CONSTANT_LISTENER = b'listener'

    CONSTANT_BACKENDPOLICY = b'backendpolicy'

    CONSTANT_APPSERVERGROUPPORT = b'appservergroupport'

    CONSTANT_REFUND = b'refund'

    CONSTANT_BLBRS = b'blbrs'

    CONSTANT_H_T_T_PLISTENER = b'HTTPlistener'

    CONSTANT_MODIFICATION_PROTECTION = b'modification_protection'

    CONSTANT_ACL = b'acl'

    CONSTANT_POLICYS = b'policys'

    CONSTANT_PRICE = b'price'

    CONSTANT_BLBRSUNMOUNT = b'blbrsunmount'

    CONSTANT_BLBRSMOUNT = b'blbrsmount'

    def __init__(self, config=None):
        """
        Initialize the blb client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def add_app_blb_server_group_rs(self, request, config=None):
        """
        add_app_blb_server_group_rs

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_BLBRS
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def add_blb_server(self, request, config=None):
        """
        add_blb_server

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id, BlbClient.CONSTANT_BACKENDSERVER
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def add_service_auth(self, request, config=None):
        """
        add_service_auth

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_SERVICE, request.service)
        headers = None
        params = {}
        params['addAuth'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def billing_change_cancel_to_post_blb(self, request, config=None):
        """
        billing_change_cancel_to_post_blb

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id, BlbClient.CONSTANT_CHARGE
        )
        headers = None
        params = {}
        params['action'] = 'CANCEL_TO_POSTPAY'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, params=params, config=merged_config)

    def billing_change_post_to_pre_blb(self, request, config=None):
        """
        billing_change_post_to_pre_blb

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BillingChangePostToPreBlbResponse data
        :rtype: BillingChangePostToPreBlbResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id, BlbClient.CONSTANT_CHARGE
        )
        headers = None
        params = {}
        params['action'] = 'TO_PREPAY'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=BillingChangePostToPreBlbResponse,
        )

    def billing_change_pre_to_post_blb(self, request, config=None):
        """
        billing_change_pre_to_post_blb

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BillingChangePreToPostBlbResponse data
        :rtype: BillingChangePreToPostBlbResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id, BlbClient.CONSTANT_CHARGE
        )
        headers = None
        params = {}
        params['action'] = 'TO_POSTPAY'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=BillingChangePreToPostBlbResponse,
        )

    def bind_blb_enterprise_security_group(self, request, config=None):
        """
        bind_blb_enterprise_security_group

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1,
            BlbClient.CONSTANT_BLB,
            request.blb_id,
            BlbClient.CONSTANT_ENTERPRISE,
            BlbClient.CONSTANT_SECURITYGROUP,
        )
        headers = None
        params = {}
        params['bind'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def bind_blb_security_group(self, request, config=None):
        """
        bind_blb_security_group

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id, BlbClient.CONSTANT_SECURITYGROUP
        )
        headers = None
        params = {}
        params['bind'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def bind_instance_to_service(self, request, config=None):
        """
        bind_instance_to_service

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_SERVICE, request.service)
        headers = None
        params = {}
        params['bind'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def blb_inquiry(self, request, config=None):
        """
        blb_inquiry

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BlbInquiryResponse data
        :rtype: BlbInquiryResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, BlbClient.CONSTANT_PRICE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), config=merged_config, model=BlbInquiryResponse
        )

    def create_app_blb(self, request, config=None):
        """
        create_app_blb

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateAppBlbResponse data
        :rtype: CreateAppBlbResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB)
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
            model=CreateAppBlbResponse,
        )

    def create_app_blb_http_listener(self, request, config=None):
        """
        create_app_blb_http_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_H_T_T_PLISTENER
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def create_app_blb_https_listener(self, request, config=None):
        """
        create_app_blb_https_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_H_T_T_P_SLISTENER
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def create_app_blb_ip_group(self, request, config=None):
        """
        create_app_blb_ip_group

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateAppBlbIpGroupResponse data
        :rtype: CreateAppBlbIpGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_IPGROUP
        )
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
            model=CreateAppBlbIpGroupResponse,
        )

    def create_app_blb_ip_group_member(self, request, config=None):
        """
        create_app_blb_ip_group_member

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1,
            BlbClient.CONSTANT_APPBLB,
            request.blb_id,
            BlbClient.CONSTANT_IPGROUP,
            BlbClient.CONSTANT_MEMBER,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def create_app_blb_ip_group_protocol(self, request, config=None):
        """
        create_app_blb_ip_group_protocol

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1,
            BlbClient.CONSTANT_APPBLB,
            request.blb_id,
            BlbClient.CONSTANT_IPGROUP,
            BlbClient.CONSTANT_BACKENDPOLICY,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def create_app_blb_policy(self, request, config=None):
        """
        create_app_blb_policy

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_POLICYS
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def create_app_blb_server_group(self, request, config=None):
        """
        create_app_blb_server_group

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateAppBlbServerGroupResponse data
        :rtype: CreateAppBlbServerGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_APPSERVERGROUP
        )
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
            model=CreateAppBlbServerGroupResponse,
        )

    def create_app_blb_server_group_port(self, request, config=None):
        """
        create_app_blb_server_group_port

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateAppBlbServerGroupPortResponse data
        :rtype: CreateAppBlbServerGroupPortResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_APPSERVERGROUPPORT
        )
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
            model=CreateAppBlbServerGroupPortResponse,
        )

    def create_app_blb_ssl_listener(self, request, config=None):
        """
        create_app_blb_ssl_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_S_S_LLISTENER
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def create_app_blb_tcp_listener(self, request, config=None):
        """
        create_app_blb_tcp_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_T_C_PLISTENER
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def create_app_blb_udp_listener(self, request, config=None):
        """
        create_app_blb_udp_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_U_D_PLISTENER
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def create_blb(self, request, config=None):
        """
        create_blb

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateBlbResponse data
        :rtype: CreateBlbResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB)
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
            model=CreateBlbResponse,
        )

    def create_blb_http_listener(self, request, config=None):
        """
        create_blb_http_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id, BlbClient.CONSTANT_H_T_T_PLISTENER
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def create_blb_https_listener(self, request, config=None):
        """
        create_blb_https_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id, BlbClient.CONSTANT_H_T_T_P_SLISTENER
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def create_blb_ssl_listener(self, request, config=None):
        """
        create_blb_ssl_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id, BlbClient.CONSTANT_S_S_LLISTENER
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def create_blb_tcp_listener(self, request, config=None):
        """
        create_blb_tcp_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id, BlbClient.CONSTANT_T_C_PLISTENER
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def create_blb_udp_listener(self, request, config=None):
        """
        create_blb_udp_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id, BlbClient.CONSTANT_U_D_PLISTENER
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def create_lbdc(self, request, config=None):
        """
        create_lbdc

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateLbdcResponse data
        :rtype: CreateLbdcResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_LBDC)
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
            model=CreateLbdcResponse,
        )

    def create_service(self, request, config=None):
        """
        create_service

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateServiceResponse data
        :rtype: CreateServiceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_SERVICE)
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
            model=CreateServiceResponse,
        )

    def delete_app_blb_ip_group(self, request, config=None):
        """
        delete_app_blb_ip_group

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_IPGROUP
        )
        headers = None
        params = {}
        params['delete'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def delete_app_blb_ip_group_member(self, request, config=None):
        """
        delete_app_blb_ip_group_member

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1,
            BlbClient.CONSTANT_APPBLB,
            request.blb_id,
            BlbClient.CONSTANT_IPGROUP,
            BlbClient.CONSTANT_MEMBER,
        )
        headers = None
        params = {}
        params['delete'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def delete_app_blb_ip_group_protocol(self, request, config=None):
        """
        delete_app_blb_ip_group_protocol

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1,
            BlbClient.CONSTANT_APPBLB,
            request.blb_id,
            BlbClient.CONSTANT_IPGROUP,
            BlbClient.CONSTANT_BACKENDPOLICY,
        )
        headers = None
        params = {}
        params['delete'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def delete_app_blb_listener(self, request, config=None):
        """
        delete_app_blb_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_LISTENER
        )
        headers = None
        params = {}
        params['batchdelete'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def delete_app_blb_policy(self, request, config=None):
        """
        delete_app_blb_policy

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_POLICYS
        )
        headers = None
        params = {}
        params['batchdelete'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def delete_app_blb_server_group(self, request, config=None):
        """
        delete_app_blb_server_group

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_APPSERVERGROUP
        )
        headers = None
        params = {}
        params['delete'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def delete_app_blb_server_group_port(self, request, config=None):
        """
        delete_app_blb_server_group_port

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_APPSERVERGROUPPORT
        )
        headers = None
        params = {}
        params['batchdelete'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def delete_app_blb_server_group_rs(self, request, config=None):
        """
        delete_app_blb_server_group_rs

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_BLBRS
        )
        headers = None
        params = {}
        params['batchdelete'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def delete_blb_listener(self, request, config=None):
        """
        delete_blb_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id, BlbClient.CONSTANT_LISTENER
        )
        headers = None
        params = {}
        params['batchdelete'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def delete_blb_server(self, request, config=None):
        """
        delete_blb_server

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id, BlbClient.CONSTANT_BACKENDSERVER
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def delete_service(self, request, config=None):
        """
        delete_service

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_SERVICE, request.service)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_service_auth(self, request, config=None):
        """
        delete_service_auth

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_SERVICE, request.service)
        headers = None
        params = {}
        params['removeAuth'] = None
        if request.action is not None:
            params['action'] = request.action
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def describe_app_blb(self, request, config=None):
        """
        describe_app_blb

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeAppBlbResponse data
        :rtype: DescribeAppBlbResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=DescribeAppBlbResponse)

    def describe_app_blb_http_listener(self, request, config=None):
        """
        describe_app_blb_http_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeAppBlbHttpListenerResponse data
        :rtype: DescribeAppBlbHttpListenerResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_H_T_T_PLISTENER
        )
        headers = None
        params = {}
        if request.listener_port is not None:
            params['listenerPort'] = request.listener_port
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=DescribeAppBlbHttpListenerResponse
        )

    def describe_app_blb_https_listener(self, request, config=None):
        """
        describe_app_blb_https_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeAppBlbHttpsListenerResponse data
        :rtype: DescribeAppBlbHttpsListenerResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_H_T_T_P_SLISTENER
        )
        headers = None
        params = {}
        if request.listener_port is not None:
            params['listenerPort'] = request.listener_port
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=DescribeAppBlbHttpsListenerResponse
        )

    def describe_app_blb_ip_group(self, request, config=None):
        """
        describe_app_blb_ip_group

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeAppBlbIpGroupResponse data
        :rtype: DescribeAppBlbIpGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_IPGROUP
        )
        headers = None
        params = {}
        if request.name is not None:
            params['name'] = request.name
        if request.exactly_match is not None:
            params['exactlyMatch'] = request.exactly_match
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=DescribeAppBlbIpGroupResponse
        )

    def describe_app_blb_ip_group_member(self, request, config=None):
        """
        describe_app_blb_ip_group_member

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeAppBlbIpGroupMemberResponse data
        :rtype: DescribeAppBlbIpGroupMemberResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1,
            BlbClient.CONSTANT_APPBLB,
            request.blb_id,
            BlbClient.CONSTANT_IPGROUP,
            BlbClient.CONSTANT_MEMBER,
        )
        headers = None
        params = {}
        if request.ip_group_id is not None:
            params['ipGroupId'] = request.ip_group_id
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=DescribeAppBlbIpGroupMemberResponse
        )

    def describe_app_blb_listener(self, request, config=None):
        """
        describe_app_blb_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeAppBlbListenerResponse data
        :rtype: DescribeAppBlbListenerResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_LISTENER
        )
        headers = None
        params = {}
        if request.listener_port is not None:
            params['listenerPort'] = request.listener_port
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=DescribeAppBlbListenerResponse
        )

    def describe_app_blb_policy(self, request, config=None):
        """
        describe_app_blb_policy

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeAppBlbPolicyResponse data
        :rtype: DescribeAppBlbPolicyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_POLICYS
        )
        headers = None
        params = {}
        if request.port is not None:
            params['port'] = request.port
        if request.type is not None:
            params['type'] = request.type
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=DescribeAppBlbPolicyResponse
        )

    def describe_app_blb_server_group(self, request, config=None):
        """
        describe_app_blb_server_group

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeAppBlbServerGroupResponse data
        :rtype: DescribeAppBlbServerGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_APPSERVERGROUP
        )
        headers = None
        params = {}
        if request.name is not None:
            params['name'] = request.name
        if request.exactly_match is not None:
            params['exactlyMatch'] = request.exactly_match
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=DescribeAppBlbServerGroupResponse
        )

    def describe_app_blb_server_group_mount_rs(self, request, config=None):
        """
        describe_app_blb_server_group_mount_rs

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeAppBlbServerGroupMountRsResponse data
        :rtype: DescribeAppBlbServerGroupMountRsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_BLBRSMOUNT
        )
        headers = None
        params = {}
        if request.sg_id is not None:
            params['sgId'] = request.sg_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            params=params,
            config=merged_config,
            model=DescribeAppBlbServerGroupMountRsResponse,
        )

    def describe_app_blb_server_group_rs(self, request, config=None):
        """
        describe_app_blb_server_group_rs

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeAppBlbServerGroupRsResponse data
        :rtype: DescribeAppBlbServerGroupRsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_BLBRS
        )
        headers = None
        params = {}
        if request.sg_id is not None:
            params['sgId'] = request.sg_id
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=DescribeAppBlbServerGroupRsResponse
        )

    def describe_app_blb_server_group_unmount_rs(self, request, config=None):
        """
        describe_app_blb_server_group_unmount_rs

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeAppBlbServerGroupUnmountRsResponse data
        :rtype: DescribeAppBlbServerGroupUnmountRsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_BLBRSUNMOUNT
        )
        headers = None
        params = {}
        if request.sg_id is not None:
            params['sgId'] = request.sg_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            params=params,
            config=merged_config,
            model=DescribeAppBlbServerGroupUnmountRsResponse,
        )

    def describe_app_blb_ssl_listener(self, request, config=None):
        """
        describe_app_blb_ssl_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeAppBlbSslListenerResponse data
        :rtype: DescribeAppBlbSslListenerResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_S_S_LLISTENER
        )
        headers = None
        params = {}
        if request.listener_port is not None:
            params['listenerPort'] = request.listener_port
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=DescribeAppBlbSslListenerResponse
        )

    def describe_app_blb_tcp_listener(self, request, config=None):
        """
        describe_app_blb_tcp_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeAppBlbTcpListenerResponse data
        :rtype: DescribeAppBlbTcpListenerResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_T_C_PLISTENER
        )
        headers = None
        params = {}
        if request.listener_port is not None:
            params['listenerPort'] = request.listener_port
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=DescribeAppBlbTcpListenerResponse
        )

    def describe_app_blb_udp_listener(self, request, config=None):
        """
        describe_app_blb_udp_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeAppBlbUdpListenerResponse data
        :rtype: DescribeAppBlbUdpListenerResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_U_D_PLISTENER
        )
        headers = None
        params = {}
        if request.listener_port is not None:
            params['listenerPort'] = request.listener_port
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=DescribeAppBlbUdpListenerResponse
        )

    def describe_app_blbs(self, request, config=None):
        """
        describe_app_blbs

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeAppBlbsResponse data
        :rtype: DescribeAppBlbsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB)
        headers = None
        params = {}
        if request.address is not None:
            params['address'] = request.address
        if request.name is not None:
            params['name'] = request.name
        if request.blb_id is not None:
            params['blbId'] = request.blb_id
        if request.bcc_id is not None:
            params['bccId'] = request.bcc_id
        if request.exactly_match is not None:
            params['exactlyMatch'] = request.exactly_match
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=DescribeAppBlbsResponse
        )

    def describe_blb(self, request, config=None):
        """
        describe_blb

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeBlbResponse data
        :rtype: DescribeBlbResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id)
        headers = None
        params = {}
        if request.type is not None:
            params['type'] = request.type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=DescribeBlbResponse
        )

    def describe_blb_enterprise_security_groups(self, request, config=None):
        """
        describe_blb_enterprise_security_groups

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeBlbEnterpriseSecurityGroupsResponse data
        :rtype: DescribeBlbEnterpriseSecurityGroupsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1,
            BlbClient.CONSTANT_BLB,
            request.blb_id,
            BlbClient.CONSTANT_ENTERPRISE,
            BlbClient.CONSTANT_SECURITYGROUP,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=DescribeBlbEnterpriseSecurityGroupsResponse
        )

    def describe_blb_http_listener(self, request, config=None):
        """
        describe_blb_http_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeBlbHttpListenerResponse data
        :rtype: DescribeBlbHttpListenerResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id, BlbClient.CONSTANT_H_T_T_PLISTENER
        )
        headers = None
        params = {}
        if request.listener_port is not None:
            params['listenerPort'] = request.listener_port
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=DescribeBlbHttpListenerResponse
        )

    def describe_blb_https_listener(self, request, config=None):
        """
        describe_blb_https_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeBlbHttpsListenerResponse data
        :rtype: DescribeBlbHttpsListenerResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id, BlbClient.CONSTANT_H_T_T_P_SLISTENER
        )
        headers = None
        params = {}
        if request.listener_port is not None:
            params['listenerPort'] = request.listener_port
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=DescribeBlbHttpsListenerResponse
        )

    def describe_blb_listener(self, request, config=None):
        """
        describe_blb_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeBlbListenerResponse data
        :rtype: DescribeBlbListenerResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id, BlbClient.CONSTANT_LISTENER
        )
        headers = None
        params = {}
        if request.listener_port is not None:
            params['listenerPort'] = request.listener_port
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=DescribeBlbListenerResponse
        )

    def describe_blb_security_groups(self, request, config=None):
        """
        describe_blb_security_groups

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeBlbSecurityGroupsResponse data
        :rtype: DescribeBlbSecurityGroupsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id, BlbClient.CONSTANT_SECURITYGROUP
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=DescribeBlbSecurityGroupsResponse
        )

    def describe_blb_server_health(self, request, config=None):
        """
        describe_blb_server_health

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeBlbServerHealthResponse data
        :rtype: DescribeBlbServerHealthResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id, BlbClient.CONSTANT_BACKENDSERVER
        )
        headers = None
        params = {}
        if request.listener_port is not None:
            params['listenerPort'] = request.listener_port
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=DescribeBlbServerHealthResponse
        )

    def describe_blb_servers(self, request, config=None):
        """
        describe_blb_servers

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeBlbServersResponse data
        :rtype: DescribeBlbServersResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id, BlbClient.CONSTANT_BACKENDSERVER
        )
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=DescribeBlbServersResponse
        )

    def describe_blb_ssl_listener(self, request, config=None):
        """
        describe_blb_ssl_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeBlbSslListenerResponse data
        :rtype: DescribeBlbSslListenerResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id, BlbClient.CONSTANT_S_S_LLISTENER
        )
        headers = None
        params = {}
        if request.listener_port is not None:
            params['listenerPort'] = request.listener_port
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=DescribeBlbSslListenerResponse
        )

    def describe_blb_tcp_listener(self, request, config=None):
        """
        describe_blb_tcp_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeBlbTcpListenerResponse data
        :rtype: DescribeBlbTcpListenerResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id, BlbClient.CONSTANT_T_C_PLISTENER
        )
        headers = None
        params = {}
        if request.listener_port is not None:
            params['listenerPort'] = request.listener_port
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=DescribeBlbTcpListenerResponse
        )

    def describe_blb_udp_listener(self, request, config=None):
        """
        describe_blb_udp_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeBlbUdpListenerResponse data
        :rtype: DescribeBlbUdpListenerResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id, BlbClient.CONSTANT_U_D_PLISTENER
        )
        headers = None
        params = {}
        if request.listener_port is not None:
            params['listenerPort'] = request.listener_port
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=DescribeBlbUdpListenerResponse
        )

    def describe_blbs(self, request, config=None):
        """
        describe_blbs

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeBlbsResponse data
        :rtype: DescribeBlbsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB)
        headers = None
        params = {}
        if request.address is not None:
            params['address'] = request.address
        if request.name is not None:
            params['name'] = request.name
        if request.blb_id is not None:
            params['blbId'] = request.blb_id
        if request.bcc_id is not None:
            params['bccId'] = request.bcc_id
        if request.exactly_match is not None:
            params['exactlyMatch'] = request.exactly_match
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.type is not None:
            params['type'] = request.type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=DescribeBlbsResponse
        )

    def describe_lbdc(self, request, config=None):
        """
        describe_lbdc

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeLbdcResponse data
        :rtype: DescribeLbdcResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_LBDC, request.id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=DescribeLbdcResponse)

    def describe_lbdc_blb(self, request, config=None):
        """
        describe_lbdc_blb

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeLbdcBlbResponse data
        :rtype: DescribeLbdcBlbResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_LBDC, request.id, BlbClient.CONSTANT_BLB)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=DescribeLbdcBlbResponse)

    def describe_lbdcs(self, request, config=None):
        """
        describe_lbdcs

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeLbdcsResponse data
        :rtype: DescribeLbdcsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_LBDC)
        headers = None
        params = {}
        if request.id is not None:
            params['id'] = request.id
        if request.name is not None:
            params['name'] = request.name
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=DescribeLbdcsResponse
        )

    def describe_service(self, request, config=None):
        """
        describe_service

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeServiceResponse data
        :rtype: DescribeServiceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_SERVICE, request.service)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=DescribeServiceResponse)

    def describe_services(self, request, config=None):
        """
        describe_services

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeServicesResponse data
        :rtype: DescribeServicesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_SERVICE)
        headers = None
        params = {}
        params['maxKeys'] = '1'
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=DescribeServicesResponse
        )

    def refund_blb(self, request, config=None):
        """
        refund_blb

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, BlbClient.CONSTANT_REFUND, request.blb_id
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def release_app_blb(self, request, config=None):
        """
        release_app_blb

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def release_blb(self, request, config=None):
        """
        release_blb

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def renew_lbdc(self, request, config=None):
        """
        renew_lbdc

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_LBDC, request.id)
        headers = None
        params = {}
        params['purchaseReserved'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def resize_blb(self, request, config=None):
        """
        resize_blb

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ResizeBlbResponse data
        :rtype: ResizeBlbResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id)
        headers = None
        params = {}
        params['action'] = 'RESIZE'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=ResizeBlbResponse,
        )

    def unbind_blb_enterprise_security_group(self, request, config=None):
        """
        unbind_blb_enterprise_security_group

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1,
            BlbClient.CONSTANT_BLB,
            request.blb_id,
            BlbClient.CONSTANT_ENTERPRISE,
            BlbClient.CONSTANT_SECURITYGROUP,
        )
        headers = None
        params = {}
        params['unbind'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def unbind_blb_security_group(self, request, config=None):
        """
        unbind_blb_security_group

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id, BlbClient.CONSTANT_SECURITYGROUP
        )
        headers = None
        params = {}
        params['unbind'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def unbind_instance_from_service(self, request, config=None):
        """
        unbind_instance_from_service

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_SERVICE, request.service)
        headers = None
        params = {}
        params['unbind'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def update_app_blb(self, request, config=None):
        """
        update_app_blb

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_app_blb_http_listener(self, request, config=None):
        """
        update_app_blb_http_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_H_T_T_PLISTENER
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        if request.listener_port is not None:
            params['listenerPort'] = request.listener_port
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_app_blb_https_listener(self, request, config=None):
        """
        update_app_blb_https_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_H_T_T_P_SLISTENER
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        if request.listener_port is not None:
            params['listenerPort'] = request.listener_port
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_app_blb_ip_group(self, request, config=None):
        """
        update_app_blb_ip_group

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_IPGROUP
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_app_blb_ip_group_member(self, request, config=None):
        """
        update_app_blb_ip_group_member

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1,
            BlbClient.CONSTANT_APPBLB,
            request.blb_id,
            BlbClient.CONSTANT_IPGROUP,
            BlbClient.CONSTANT_MEMBER,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_app_blb_ip_group_protocol(self, request, config=None):
        """
        update_app_blb_ip_group_protocol

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1,
            BlbClient.CONSTANT_APPBLB,
            request.blb_id,
            BlbClient.CONSTANT_IPGROUP,
            BlbClient.CONSTANT_BACKENDPOLICY,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_app_blb_policy(self, request, config=None):
        """
        update_app_blb_policy

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_POLICYS
        )
        headers = None
        params = {}
        params['batchupdate'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_app_blb_server_group(self, request, config=None):
        """
        update_app_blb_server_group

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_APPSERVERGROUP
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_app_blb_server_group_port(self, request, config=None):
        """
        update_app_blb_server_group_port

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_APPSERVERGROUPPORT
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_app_blb_server_group_rs(self, request, config=None):
        """
        update_app_blb_server_group_rs

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_BLBRS
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_app_blb_ssl_listener(self, request, config=None):
        """
        update_app_blb_ssl_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_S_S_LLISTENER
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        if request.listener_port is not None:
            params['listenerPort'] = request.listener_port
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_app_blb_tcp_listener(self, request, config=None):
        """
        update_app_blb_tcp_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_T_C_PLISTENER
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        if request.listener_port is not None:
            params['listenerPort'] = request.listener_port
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_app_blb_udp_listener(self, request, config=None):
        """
        update_app_blb_udp_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_APPBLB, request.blb_id, BlbClient.CONSTANT_U_D_PLISTENER
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        if request.listener_port is not None:
            params['listenerPort'] = request.listener_port
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_blb(self, request, config=None):
        """
        update_blb

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_blb_acl(self, request, config=None):
        """
        update_blb_acl

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, BlbClient.CONSTANT_ACL, request.blb_id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_blb_http_listener(self, request, config=None):
        """
        update_blb_http_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id, BlbClient.CONSTANT_H_T_T_PLISTENER
        )
        headers = None
        params = {}
        if request.listener_port is not None:
            params['listenerPort'] = request.listener_port
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_blb_https_listener(self, request, config=None):
        """
        update_blb_https_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id, BlbClient.CONSTANT_H_T_T_P_SLISTENER
        )
        headers = None
        params = {}
        if request.listener_port is not None:
            params['listenerPort'] = request.listener_port
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_blb_modify_protection(self, request, config=None):
        """
        update_blb_modify_protection

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, BlbClient.CONSTANT_MODIFICATION_PROTECTION, request.blb_id
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_blb_server(self, request, config=None):
        """
        update_blb_server

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id, BlbClient.CONSTANT_BACKENDSERVER
        )
        headers = None
        params = {}
        params['update'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_blb_ssl_listener(self, request, config=None):
        """
        update_blb_ssl_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id, BlbClient.CONSTANT_S_S_LLISTENER
        )
        headers = None
        params = {}
        if request.listener_port is not None:
            params['listenerPort'] = request.listener_port
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_blb_tcp_listener(self, request, config=None):
        """
        update_blb_tcp_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id, BlbClient.CONSTANT_T_C_PLISTENER
        )
        headers = None
        params = {}
        if request.listener_port is not None:
            params['listenerPort'] = request.listener_port
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_blb_udp_listener(self, request, config=None):
        """
        update_blb_udp_listener

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, request.blb_id, BlbClient.CONSTANT_U_D_PLISTENER
        )
        headers = None
        params = {}
        if request.listener_port is not None:
            params['listenerPort'] = request.listener_port
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_lbdc(self, request, config=None):
        """
        update_lbdc

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_LBDC, request.id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_service(self, request, config=None):
        """
        update_service

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_SERVICE, request.service)
        headers = None
        params = {}
        params['modifyAttribute'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_service_auth(self, request, config=None):
        """
        update_service_auth

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_SERVICE, request.service)
        headers = None
        params = {}
        params['editAuth'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def upgrade_lbdc(self, request, config=None):
        """
        upgrade_lbdc

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_LBDC, request.id)
        headers = None
        params = {}
        params['resize'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
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
