"""
Example for bci client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.auth import bce_v1_signer
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_bci.models.create_image_cache_response import CreateImageCacheResponse
from baiducloud_python_sdk_bci.models.create_instance_response import CreateInstanceResponse
from baiducloud_python_sdk_bci.models.get_instance_response import GetInstanceResponse
from baiducloud_python_sdk_bci.models.list_image_caches_response import ListImageCachesResponse
from baiducloud_python_sdk_bci.models.list_instances_response import ListInstancesResponse

_logger = logging.getLogger(__name__)


class BciClient(BceBaseClient):
    """
    bci base sdk client
    """

    VERSION_V1 = b'/v1'

    CONSTANT_INSTANCE = b'instance'

    CONSTANT_BATCH_DEL = b'batchDel'

    CONSTANT_IMAGE_CACHE = b'imageCache'

    def __init__(self, config=None):
        """
        Initialize the bci client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def batch_delete_image_caches(self, request, config=None):
        """
        batch_delete_image_caches

        :param request: Request entity containing all parameters
        :type request: BciClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BciClient.VERSION_V1, BciClient.CONSTANT_IMAGE_CACHE, BciClient.CONSTANT_BATCH_DEL)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def batch_delete_instances(self, request, config=None):
        """
        batch_delete_instances

        :param request: Request entity containing all parameters
        :type request: BciClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BciClient.VERSION_V1, BciClient.CONSTANT_INSTANCE, BciClient.CONSTANT_BATCH_DEL)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def create_image_cache(self, request, config=None):
        """
        create_image_cache

        :param request: Request entity containing all parameters
        :type request: BciClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateImageCacheResponse data
        :rtype: CreateImageCacheResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BciClient.VERSION_V1, BciClient.CONSTANT_IMAGE_CACHE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateImageCacheResponse,
        )

    def create_instance(self, request, config=None):
        """
        create_instance

        :param request: Request entity containing all parameters
        :type request: BciClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateInstanceResponse data
        :rtype: CreateInstanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BciClient.VERSION_V1, BciClient.CONSTANT_INSTANCE)
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
            model=CreateInstanceResponse,
        )

    def delete_instance(self, request, config=None):
        """
        delete_instance

        :param request: Request entity containing all parameters
        :type request: BciClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BciClient.VERSION_V1, BciClient.CONSTANT_INSTANCE, request.instance_id)
        headers = None
        params = {}
        if request.related_release_flag is not None:
            params['relatedReleaseFlag'] = request.related_release_flag
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def get_instance(self, request, config=None):
        """
        get_instance

        :param request: Request entity containing all parameters
        :type request: BciClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetInstanceResponse data
        :rtype: GetInstanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BciClient.VERSION_V1, BciClient.CONSTANT_INSTANCE, request.instance_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetInstanceResponse)

    def list_image_caches(self, request, config=None):
        """
        list_image_caches

        :param request: Request entity containing all parameters
        :type request: BciClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListImageCachesResponse data
        :rtype: ListImageCachesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BciClient.VERSION_V1, BciClient.CONSTANT_IMAGE_CACHE)
        headers = None
        params = {}
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListImageCachesResponse
        )

    def list_instances(self, request, config=None):
        """
        list_instances

        :param request: Request entity containing all parameters
        :type request: BciClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListInstancesResponse data
        :rtype: ListInstancesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BciClient.VERSION_V1, BciClient.CONSTANT_INSTANCE)
        headers = None
        params = {}
        if request.keyword_type is not None:
            params['keywordType'] = request.keyword_type
        if request.keyword is not None:
            params['keyword'] = request.keyword
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListInstancesResponse
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
