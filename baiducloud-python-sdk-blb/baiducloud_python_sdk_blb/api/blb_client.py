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
from baiducloud_python_sdk_blb.models.resize_blb_response import ResizeBlbResponse

_logger = logging.getLogger(__name__)


class BlbClient(BceBaseClient):
    """
    blb base sdk client
    """

    VERSION_V1 = b'/v1'

    CONSTANT_BLB = b'blb'

    CONSTANT_CHARGE = b'charge'

    CONSTANT_PRICE = b'price'

    CONSTANT_REFUND = b'refund'

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
        params = {}
        params['action'] = 'CANCEL_TO_POSTPAY'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.POST, path=path, params=params, config=config)

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
        params = {}
        params['action'] = 'TO_PREPAY'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=config,
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
        params = {}
        params['action'] = 'TO_POSTPAY'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=config,
            model=BillingChangePreToPostBlbResponse,
        )

    def blb_inquiry(self, request, config=None):
        """
        blb_inquiry

        :param request: Request entity containing all parameters
        :type request: BlbClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BlbClient.VERSION_V1, BlbClient.CONSTANT_BLB, BlbClient.CONSTANT_PRICE)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=config)

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
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.PUT, path=path, params=params, config=config)

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
        params = {}
        params['action'] = 'RESIZE'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=config,
            model=ResizeBlbResponse,
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
