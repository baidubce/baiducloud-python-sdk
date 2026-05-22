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
from baiducloud_python_sdk_blb.models.create_blb_response import CreateBlbResponse
from baiducloud_python_sdk_blb.models.describe_app_blb_response import DescribeAppBlbResponse
from baiducloud_python_sdk_blb.models.describe_app_blb_http_listener_response import DescribeAppBlbHttpListenerResponse
from baiducloud_python_sdk_blb.models.describe_app_blb_https_listener_response import (
    DescribeAppBlbHttpsListenerResponse,
)
from baiducloud_python_sdk_blb.models.describe_app_blb_listener_response import DescribeAppBlbListenerResponse
from baiducloud_python_sdk_blb.models.describe_app_blb_policy_response import DescribeAppBlbPolicyResponse
from baiducloud_python_sdk_blb.models.describe_app_blb_ssl_listener_response import DescribeAppBlbSslListenerResponse
from baiducloud_python_sdk_blb.models.describe_app_blb_tcp_listener_response import DescribeAppBlbTcpListenerResponse
from baiducloud_python_sdk_blb.models.describe_app_blb_udp_listener_response import DescribeAppBlbUdpListenerResponse
from baiducloud_python_sdk_blb.models.describe_app_blbs_response import DescribeAppBlbsResponse
from baiducloud_python_sdk_blb.models.describe_blb_response import DescribeBlbResponse
from baiducloud_python_sdk_blb.models.describe_blbs_response import DescribeBlbsResponse
from baiducloud_python_sdk_blb.models.resize_blb_response import ResizeBlbResponse

_logger = logging.getLogger(__name__)


class BlbClient(BceBaseClient):
    """
    blb base sdk client
    """

    VERSION_V1 = b'/v1'

    CONSTANT_BLB = b'blb'

    CONSTANT_ACL = b'acl'

    CONSTANT_APPBLB = b'appblb'

    CONSTANT_H_T_T_P_SLISTENER = b'HTTPSlistener'

    CONSTANT_CHARGE = b'charge'

    CONSTANT_T_C_PLISTENER = b'TCPlistener'

    CONSTANT_LISTENER = b'listener'

    CONSTANT_U_D_PLISTENER = b'UDPlistener'

    CONSTANT_H_T_T_PLISTENER = b'HTTPlistener'

    CONSTANT_POLICYS = b'policys'

    CONSTANT_S_S_LLISTENER = b'SSLlistener'

    CONSTANT_REFUND = b'refund'

    CONSTANT_PRICE = b'price'

    CONSTANT_MODIFICATION_PROTECTION = b'modification_protection'

    def __init__(self, config=None):
        """
        Initialize the blb client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

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
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

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
