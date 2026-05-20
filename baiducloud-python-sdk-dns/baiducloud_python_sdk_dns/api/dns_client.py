"""
Example for dns client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.auth import bce_v1_signer
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_dns.models.query_and_parse_record_list_response import QueryAndParseRecordListResponse
from baiducloud_python_sdk_dns.models.query_domain_name_list_response import QueryDomainNameListResponse
from baiducloud_python_sdk_dns.models.query_the_list_of_line_groups_response import QueryTheListOfLineGroupsResponse

_logger = logging.getLogger(__name__)


class DnsClient(BceBaseClient):
    """
    dns base sdk client
    """

    VERSION_V1 = b'/v1'

    CONSTANT_DNS = b'dns'

    CONSTANT_ZONE = b'zone'

    CONSTANT_RECORD = b'record'

    CONSTANT_CUSTOMLINE = b'customline'

    CONSTANT_ORDER = b'order'

    def __init__(self, config=None):
        """
        Initialize the dns client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def add_domain_name(self, request, config=None):
        """
        add_domain_name

        :param request: Request entity containing all parameters
        :type request: DnsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(DnsClient.VERSION_V1, DnsClient.CONSTANT_DNS, DnsClient.CONSTANT_ZONE)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def add_line_group(self, request, config=None):
        """
        add_line_group

        :param request: Request entity containing all parameters
        :type request: DnsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(DnsClient.VERSION_V1, DnsClient.CONSTANT_DNS, DnsClient.CONSTANT_CUSTOMLINE)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def add_parsing_records(self, request, config=None):
        """
        add_parsing_records

        :param request: Request entity containing all parameters
        :type request: DnsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DnsClient.VERSION_V1,
            DnsClient.CONSTANT_DNS,
            DnsClient.CONSTANT_ZONE,
            request.zone_name,
            DnsClient.CONSTANT_RECORD,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def delete_line_group(self, request, config=None):
        """
        delete_line_group

        :param request: Request entity containing all parameters
        :type request: DnsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DnsClient.VERSION_V1, DnsClient.CONSTANT_DNS, DnsClient.CONSTANT_CUSTOMLINE, request.line_id
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_parsing_records(self, request, config=None):
        """
        delete_parsing_records

        :param request: Request entity containing all parameters
        :type request: DnsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DnsClient.VERSION_V1,
            DnsClient.CONSTANT_DNS,
            DnsClient.CONSTANT_ZONE,
            request.zone_name,
            DnsClient.CONSTANT_RECORD,
            request.record_id,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def domain_name_renewal(self, request, config=None):
        """
        domain_name_renewal

        :param request: Request entity containing all parameters
        :type request: DnsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DnsClient.VERSION_V1,
            DnsClient.CONSTANT_DNS,
            DnsClient.CONSTANT_ZONE,
            DnsClient.CONSTANT_ORDER,
            request.name,
        )
        headers = None
        params = {}
        params[request.action] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def modify_parsing_records(self, request, config=None):
        """
        modify_parsing_records

        :param request: Request entity containing all parameters
        :type request: DnsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DnsClient.VERSION_V1,
            DnsClient.CONSTANT_DNS,
            DnsClient.CONSTANT_ZONE,
            request.zone_name,
            DnsClient.CONSTANT_RECORD,
            request.record_id,
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def modify_the_parsing_record_status(self, request, config=None):
        """
        modify_the_parsing_record_status

        :param request: Request entity containing all parameters
        :type request: DnsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DnsClient.VERSION_V1,
            DnsClient.CONSTANT_DNS,
            DnsClient.CONSTANT_ZONE,
            request.zone_name,
            DnsClient.CONSTANT_RECORD,
            request.record_id,
        )
        headers = None
        params = {}
        params[request.action] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def purchase_a_paid_domain_name(self, request, config=None):
        """
        purchase_a_paid_domain_name

        :param request: Request entity containing all parameters
        :type request: DnsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DnsClient.VERSION_V1, DnsClient.CONSTANT_DNS, DnsClient.CONSTANT_ZONE, DnsClient.CONSTANT_ORDER
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def query_and_parse_record_list(self, request, config=None):
        """
        query_and_parse_record_list

        :param request: Request entity containing all parameters
        :type request: DnsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryAndParseRecordListResponse data
        :rtype: QueryAndParseRecordListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DnsClient.VERSION_V1,
            DnsClient.CONSTANT_DNS,
            DnsClient.CONSTANT_ZONE,
            request.zone_name,
            DnsClient.CONSTANT_RECORD,
        )
        headers = None
        params = {}
        if request.rr is not None:
            params['rr'] = request.rr
        if request.id is not None:
            params['id'] = request.id
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryAndParseRecordListResponse
        )

    def query_domain_name_list(self, request, config=None):
        """
        query_domain_name_list

        :param request: Request entity containing all parameters
        :type request: DnsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryDomainNameListResponse data
        :rtype: QueryDomainNameListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(DnsClient.VERSION_V1, DnsClient.CONSTANT_DNS, DnsClient.CONSTANT_ZONE)
        headers = None
        params = {}
        if request.name is not None:
            params['name'] = request.name
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryDomainNameListResponse
        )

    def query_the_list_of_line_groups(self, request, config=None):
        """
        query_the_list_of_line_groups

        :param request: Request entity containing all parameters
        :type request: DnsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryTheListOfLineGroupsResponse data
        :rtype: QueryTheListOfLineGroupsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(DnsClient.VERSION_V1, DnsClient.CONSTANT_DNS, DnsClient.CONSTANT_CUSTOMLINE)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryTheListOfLineGroupsResponse
        )

    def remove_domain_name(self, request, config=None):
        """
        remove_domain_name

        :param request: Request entity containing all parameters
        :type request: DnsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DnsClient.VERSION_V1, DnsClient.CONSTANT_DNS, DnsClient.CONSTANT_ZONE, request.zone_name
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def update_line_group(self, request, config=None):
        """
        update_line_group

        :param request: Request entity containing all parameters
        :type request: DnsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DnsClient.VERSION_V1, DnsClient.CONSTANT_DNS, DnsClient.CONSTANT_CUSTOMLINE, request.line_id
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def upgrade_the_free_domain_name_to_the_universal_version(self, request, config=None):
        """
        upgrade_the_free_domain_name_to_the_universal_version

        :param request: Request entity containing all parameters
        :type request: DnsClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            DnsClient.VERSION_V1, DnsClient.CONSTANT_DNS, DnsClient.CONSTANT_ZONE, DnsClient.CONSTANT_ORDER
        )
        headers = None
        params = {}
        params[request.action] = None
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
