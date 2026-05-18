"""
Example for eip client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.auth import bce_v1_signer
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_eip.models.apply_for_eip_response import ApplyForEipResponse
from baiducloud_python_sdk_eip.models.bandwidth_package_inquiry_response import BandwidthPackageInquiryResponse
from baiducloud_python_sdk_eip.models.create_a_shared_traffic_package_response import (
    CreateASharedTrafficPackageResponse,
)
from baiducloud_python_sdk_eip.models.create_eip_bp_response import CreateEipBpResponse
from baiducloud_python_sdk_eip.models.create_eip_group_response import CreateEipGroupResponse
from baiducloud_python_sdk_eip.models.create_eip_transfer_response import CreateEipTransferResponse
from baiducloud_python_sdk_eip.models.create_tbsp_response import CreateTbspResponse
from baiducloud_python_sdk_eip.models.detail_tbsp_response import DetailTbspResponse
from baiducloud_python_sdk_eip.models.eip_inquiry_response import EipInquiryResponse
from baiducloud_python_sdk_eip.models.get_eip_bp_response import GetEipBpResponse
from baiducloud_python_sdk_eip.models.get_eip_group_response import GetEipGroupResponse
from baiducloud_python_sdk_eip.models.list_base_ddos_response import ListBaseDdosResponse
from baiducloud_python_sdk_eip.models.list_base_ddos_attack_record_response import ListBaseDdosAttackRecordResponse
from baiducloud_python_sdk_eip.models.list_eip_bp_response import ListEipBpResponse
from baiducloud_python_sdk_eip.models.list_eip_group_response import ListEipGroupResponse
from baiducloud_python_sdk_eip.models.list_eip_transfer_response import ListEipTransferResponse
from baiducloud_python_sdk_eip.models.list_recycle_eips_response import ListRecycleEipsResponse
from baiducloud_python_sdk_eip.models.list_tbsp_response import ListTbspResponse
from baiducloud_python_sdk_eip.models.list_tbsp_area_blocking_response import ListTbspAreaBlockingResponse
from baiducloud_python_sdk_eip.models.list_tbsp_ip_clean_response import ListTbspIpCleanResponse
from baiducloud_python_sdk_eip.models.list_tbsp_ip_whitelist_response import ListTbspIpWhitelistResponse
from baiducloud_python_sdk_eip.models.list_tbsp_protocol_blocking_response import ListTbspProtocolBlockingResponse
from baiducloud_python_sdk_eip.models.list_unban_response import ListUnbanResponse
from baiducloud_python_sdk_eip.models.query_eip_list_response import QueryEipListResponse
from baiducloud_python_sdk_eip.models.query_the_details_of_shared_traffic_packages_response import (
    QueryTheDetailsOfSharedTrafficPackagesResponse,
)
from baiducloud_python_sdk_eip.models.query_the_list_of_shared_traffic_packages_response import (
    QueryTheListOfSharedTrafficPackagesResponse,
)
from baiducloud_python_sdk_eip.models.shared_bandwidth_inquiry_response import SharedBandwidthInquiryResponse
from baiducloud_python_sdk_eip.models.shared_data_package_inquiry_response import SharedDataPackageInquiryResponse

_logger = logging.getLogger(__name__)


class EipClient(BceBaseClient):
    """
    eip base sdk client
    """

    VERSION_V1 = b'/v1'

    CONSTANT_EIP = b'eip'

    CONSTANT_PRICE = b'price'

    CONSTANT_TBSP = b'tbsp'

    CONSTANT_TRANSFER = b'transfer'

    CONSTANT_EIPGROUP = b'eipgroup'

    CONSTANT_EIPBP = b'eipbp'

    CONSTANT_PROTOCOL_BLOCKING = b'protocolBlocking'

    CONSTANT_AREA_BLOCKING = b'areaBlocking'

    CONSTANT_DDOS = b'ddos'

    CONSTANT_RECYCLE = b'recycle'

    CONSTANT_UNBAN = b'unban'

    CONSTANT_RECORD = b'record'

    CONSTANT_IP_CLEAN = b'ipClean'

    CONSTANT_EIPTP = b'eiptp'

    CONSTANT_IP_WHITELIST = b'ipWhitelist'

    CONSTANT_REFUND = b'refund'

    CONSTANT_IP_PROTECT_LEVEL = b'ipProtectLevel'

    CONSTANT_DELETE_PROTECT = b'deleteProtect'

    def __init__(self, config=None):
        """
        Initialize the eip client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def add_eip_group_count(self, request, config=None):
        """
        add_eip_group_count

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIPGROUP, request.id)
        headers = None
        params = {}
        params['resize'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def add_tbsp_area_blocking(self, request, config=None):
        """
        add_tbsp_area_blocking

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id, EipClient.CONSTANT_AREA_BLOCKING
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def add_tbsp_ip_whitelist(self, request, config=None):
        """
        add_tbsp_ip_whitelist

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id, EipClient.CONSTANT_IP_WHITELIST
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def add_tbsp_protocol_blocking(self, request, config=None):
        """
        add_tbsp_protocol_blocking

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id, EipClient.CONSTANT_PROTOCOL_BLOCKING
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def apply_for_eip(self, request, config=None):
        """
        apply_for_eip

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ApplyForEipResponse data
        :rtype: ApplyForEipResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIP)
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
            model=ApplyForEipResponse,
        )

    def bandwidth_package_inquiry(self, request, config=None):
        """
        bandwidth_package_inquiry

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BandwidthPackageInquiryResponse data
        :rtype: BandwidthPackageInquiryResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIPBP, EipClient.CONSTANT_PRICE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=BandwidthPackageInquiryResponse,
        )

    def bind_eip(self, request, config=None):
        """
        bind_eip

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIP, request.eip)
        headers = None
        params = {}
        params['bind'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def bind_tbsp_protection_object(self, request, config=None):
        """
        bind_tbsp_protection_object

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id)
        headers = None
        params = {}
        params['bind'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def cancel_eip_transfer(self, request, config=None):
        """
        cancel_eip_transfer

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TRANSFER)
        headers = None
        params = {}
        params['cancel'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def create_a_shared_traffic_package(self, request, config=None):
        """
        create_a_shared_traffic_package

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateASharedTrafficPackageResponse data
        :rtype: CreateASharedTrafficPackageResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIPTP)
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
            model=CreateASharedTrafficPackageResponse,
        )

    def create_eip_bp(self, request, config=None):
        """
        create_eip_bp

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateEipBpResponse data
        :rtype: CreateEipBpResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIPBP)
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
            model=CreateEipBpResponse,
        )

    def create_eip_group(self, request, config=None):
        """
        create_eip_group

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateEipGroupResponse data
        :rtype: CreateEipGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIPGROUP)
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
            model=CreateEipGroupResponse,
        )

    def create_eip_transfer(self, request, config=None):
        """
        create_eip_transfer

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateEipTransferResponse data
        :rtype: CreateEipTransferResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TRANSFER)
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
            model=CreateEipTransferResponse,
        )

    def create_tbsp(self, request, config=None):
        """
        create_tbsp

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateTbspResponse data
        :rtype: CreateTbspResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP)
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
            model=CreateTbspResponse,
        )

    def detail_tbsp(self, request, config=None):
        """
        detail_tbsp

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DetailTbspResponse data
        :rtype: DetailTbspResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=DetailTbspResponse)

    def direct_eip(self, request, config=None):
        """
        direct_eip

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIP, request.eip)
        headers = None
        params = {}
        params['direct'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def disable_tbsp_ip_clean(self, request, config=None):
        """
        disable_tbsp_ip_clean

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id, EipClient.CONSTANT_IP_CLEAN)
        headers = None
        params = {}
        params['turnOffClean'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def eip_bandwidth_scaling_capacity(self, request, config=None):
        """
        eip_bandwidth_scaling_capacity

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIP, request.eip)
        headers = None
        params = {}
        params['resize'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def eip_inquiry(self, request, config=None):
        """
        eip_inquiry

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing EipInquiryResponse data
        :rtype: EipInquiryResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIP, EipClient.CONSTANT_PRICE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), config=merged_config, model=EipInquiryResponse
        )

    def eip_postpaid_to_prepaid(self, request, config=None):
        """
        eip_postpaid_to_prepaid

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIP, request.eip)
        headers = None
        params = {}
        params['action'] = 'TO_PREPAY'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def eip_renewal(self, request, config=None):
        """
        eip_renewal

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIP, request.eip)
        headers = None
        params = {}
        params['purchaseReserved'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def enable_tbsp_ip_clean(self, request, config=None):
        """
        enable_tbsp_ip_clean

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id, EipClient.CONSTANT_IP_CLEAN)
        headers = None
        params = {}
        params['turnOnClean'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        if request.ip is not None:
            params['ip'] = request.ip
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def get_eip_bp(self, request, config=None):
        """
        get_eip_bp

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetEipBpResponse data
        :rtype: GetEipBpResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIPBP, request.id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetEipBpResponse
        )

    def get_eip_group(self, request, config=None):
        """
        get_eip_group

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetEipGroupResponse data
        :rtype: GetEipGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIPGROUP, request.id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetEipGroupResponse)

    def list_base_ddos(self, request, config=None):
        """
        list_base_ddos

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListBaseDdosResponse data
        :rtype: ListBaseDdosResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_DDOS)
        headers = None
        params = {}
        if request.ips is not None:
            params['ips'] = request.ips
        if request.type is not None:
            params['type'] = request.type
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListBaseDdosResponse
        )

    def list_base_ddos_attack_record(self, request, config=None):
        """
        list_base_ddos_attack_record

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListBaseDdosAttackRecordResponse data
        :rtype: ListBaseDdosAttackRecordResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_DDOS, request.ip, EipClient.CONSTANT_RECORD)
        headers = None
        params = {}
        if request.start_time is not None:
            params['startTime'] = request.start_time
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListBaseDdosAttackRecordResponse
        )

    def list_eip_bp(self, request, config=None):
        """
        list_eip_bp

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListEipBpResponse data
        :rtype: ListEipBpResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIPBP)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.id is not None:
            params['id'] = request.id
        if request.name is not None:
            params['name'] = request.name
        if request.bind_type is not None:
            params['bindType'] = request.bind_type
        if request.type is not None:
            params['type'] = request.type
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListEipBpResponse
        )

    def list_eip_group(self, request, config=None):
        """
        list_eip_group

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListEipGroupResponse data
        :rtype: ListEipGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIPGROUP)
        headers = None
        params = {}
        if request.id is not None:
            params['id'] = request.id
        if request.name is not None:
            params['name'] = request.name
        if request.status is not None:
            params['status'] = request.status
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListEipGroupResponse
        )

    def list_eip_transfer(self, request, config=None):
        """
        list_eip_transfer

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListEipTransferResponse data
        :rtype: ListEipTransferResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TRANSFER)
        headers = None
        params = {}
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.marker is not None:
            params['marker'] = request.marker
        if request.direction is not None:
            params['direction'] = request.direction
        if request.transfer_id is not None:
            params['transferId'] = request.transfer_id
        if request.status is not None:
            params['status'] = request.status
        if request.fuzzy_transfer_id is not None:
            params['fuzzyTransferId'] = request.fuzzy_transfer_id
        if request.fuzzy_instance_id is not None:
            params['fuzzyInstanceId'] = request.fuzzy_instance_id
        if request.fuzzy_instance_name is not None:
            params['fuzzyInstanceName'] = request.fuzzy_instance_name
        if request.fuzzy_instance_ip is not None:
            params['fuzzyInstanceIp'] = request.fuzzy_instance_ip
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListEipTransferResponse
        )

    def list_recycle_eips(self, request, config=None):
        """
        list_recycle_eips

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListRecycleEipsResponse data
        :rtype: ListRecycleEipsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIP, EipClient.CONSTANT_RECYCLE)
        headers = None
        params = {}
        if request.eip is not None:
            params['eip'] = request.eip
        if request.name is not None:
            params['name'] = request.name
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListRecycleEipsResponse
        )

    def list_tbsp(self, request, config=None):
        """
        list_tbsp

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListTbspResponse data
        :rtype: ListTbspResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP)
        headers = None
        params = {}
        if request.id is not None:
            params['id'] = request.id
        if request.name is not None:
            params['name'] = request.name
        if request.status is not None:
            params['status'] = request.status
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListTbspResponse
        )

    def list_tbsp_area_blocking(self, request, config=None):
        """
        list_tbsp_area_blocking

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListTbspAreaBlockingResponse data
        :rtype: ListTbspAreaBlockingResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id, EipClient.CONSTANT_AREA_BLOCKING
        )
        headers = None
        params = {}
        if request.ip is not None:
            params['ip'] = request.ip
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListTbspAreaBlockingResponse
        )

    def list_tbsp_ip_clean(self, request, config=None):
        """
        list_tbsp_ip_clean

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListTbspIpCleanResponse data
        :rtype: ListTbspIpCleanResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id, EipClient.CONSTANT_IP_CLEAN)
        headers = None
        params = {}
        if request.ip is not None:
            params['ip'] = request.ip
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListTbspIpCleanResponse
        )

    def list_tbsp_ip_whitelist(self, request, config=None):
        """
        list_tbsp_ip_whitelist

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListTbspIpWhitelistResponse data
        :rtype: ListTbspIpWhitelistResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id, EipClient.CONSTANT_IP_WHITELIST
        )
        headers = None
        params = {}
        if request.ip is not None:
            params['ip'] = request.ip
        if request.ip_cidr is not None:
            params['ipCidr'] = request.ip_cidr
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListTbspIpWhitelistResponse
        )

    def list_tbsp_protocol_blocking(self, request, config=None):
        """
        list_tbsp_protocol_blocking

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListTbspProtocolBlockingResponse data
        :rtype: ListTbspProtocolBlockingResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id, EipClient.CONSTANT_PROTOCOL_BLOCKING
        )
        headers = None
        params = {}
        if request.ip is not None:
            params['ip'] = request.ip
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListTbspProtocolBlockingResponse
        )

    def list_unban(self, request, config=None):
        """
        list_unban

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListUnbanResponse data
        :rtype: ListUnbanResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_UNBAN, EipClient.CONSTANT_RECORD)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.ip is not None:
            params['ip'] = request.ip
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListUnbanResponse
        )

    def modify_tbsp_ip_clean_threshold(self, request, config=None):
        """
        modify_tbsp_ip_clean_threshold

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id, EipClient.CONSTANT_IP_CLEAN)
        headers = None
        params = {}
        params['modifyThreshold'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def modify_tbsp_ip_protect_level(self, request, config=None):
        """
        modify_tbsp_ip_protect_level

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id, EipClient.CONSTANT_IP_PROTECT_LEVEL
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def move_in_eips(self, request, config=None):
        """
        move_in_eips

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIPGROUP, request.id)
        headers = None
        params = {}
        params['move_in'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def move_out_eips(self, request, config=None):
        """
        move_out_eips

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIPGROUP, request.id)
        headers = None
        params = {}
        params['move_out'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def optional_release_eip(self, request, config=None):
        """
        optional_release_eip

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIP, request.eip)
        headers = None
        params = {}
        if request.release_to_recycle is not None:
            params['releaseToRecycle'] = request.release_to_recycle
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def purchase_reserved_eip_group(self, request, config=None):
        """
        purchase_reserved_eip_group

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIPGROUP, request.id)
        headers = None
        params = {}
        params['purchaseReserved'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def query_eip_list(self, request, config=None):
        """
        query_eip_list

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryEipListResponse data
        :rtype: QueryEipListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIP)
        headers = None
        params = {}
        if request.ip_version is not None:
            params['ipVersion'] = request.ip_version
        if request.eip is not None:
            params['eip'] = request.eip
        if request.instance_type is not None:
            params['instanceType'] = request.instance_type
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.name is not None:
            params['name'] = request.name
        if request.status is not None:
            params['status'] = request.status
        if request.eip_ids is not None:
            params['eipIds'] = ','.join(request.eip_ids)
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=QueryEipListResponse
        )

    def query_the_details_of_shared_traffic_packages(self, request, config=None):
        """
        query_the_details_of_shared_traffic_packages

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryTheDetailsOfSharedTrafficPackagesResponse data
        :rtype: QueryTheDetailsOfSharedTrafficPackagesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIPTP, request.id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            params=params,
            config=merged_config,
            model=QueryTheDetailsOfSharedTrafficPackagesResponse,
        )

    def query_the_list_of_shared_traffic_packages(self, request, config=None):
        """
        query_the_list_of_shared_traffic_packages

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QueryTheListOfSharedTrafficPackagesResponse data
        :rtype: QueryTheListOfSharedTrafficPackagesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIPTP)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.id is not None:
            params['id'] = request.id
        if request.status is not None:
            params['status'] = request.status
        if request.deduct_policy is not None:
            params['deductPolicy'] = request.deduct_policy
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            params=params,
            config=merged_config,
            model=QueryTheListOfSharedTrafficPackagesResponse,
        )

    def receive_eip_transfer(self, request, config=None):
        """
        receive_eip_transfer

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TRANSFER)
        headers = None
        params = {}
        params['accept'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def refund_eip(self, request, config=None):
        """
        refund_eip

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIP, EipClient.CONSTANT_REFUND, request.eip)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def refund_eip_group(self, request, config=None):
        """
        refund_eip_group

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            EipClient.VERSION_V1, EipClient.CONSTANT_EIPGROUP, EipClient.CONSTANT_REFUND, request.id
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def reject_eip_transfer(self, request, config=None):
        """
        reject_eip_transfer

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TRANSFER)
        headers = None
        params = {}
        params['reject'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def release_eip(self, request, config=None):
        """
        release_eip

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIP, request.eip)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        if request.release_to_recycle is not None:
            params['releaseToRecycle'] = request.release_to_recycle
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def release_eip_bp(self, request, config=None):
        """
        release_eip_bp

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIPBP, request.id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def release_eip_from_recycle(self, request, config=None):
        """
        release_eip_from_recycle

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIP, EipClient.CONSTANT_RECYCLE, request.eip)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def release_eip_group(self, request, config=None):
        """
        release_eip_group

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIPGROUP, request.id)
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def remove_tbsp_area_blocking(self, request, config=None):
        """
        remove_tbsp_area_blocking

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id, EipClient.CONSTANT_AREA_BLOCKING
        )
        headers = None
        params = {}
        if request.ip is not None:
            params['ip'] = request.ip
        if request.block_type is not None:
            params['blockType'] = request.block_type
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def remove_tbsp_ip_whitelist(self, request, config=None):
        """
        remove_tbsp_ip_whitelist

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id, EipClient.CONSTANT_IP_WHITELIST
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        if request.ip is not None:
            params['ip'] = request.ip
        if request.whitelist_id is not None:
            params['whitelistId'] = request.whitelist_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def remove_tbsp_protocol_blocking(self, request, config=None):
        """
        remove_tbsp_protocol_blocking

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id, EipClient.CONSTANT_PROTOCOL_BLOCKING
        )
        headers = None
        params = {}
        if request.ip is not None:
            params['ip'] = request.ip
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def renew_tbsp(self, request, config=None):
        """
        renew_tbsp

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id)
        headers = None
        params = {}
        params['purchaseReserved'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def resize_eip_bp_bandwidth(self, request, config=None):
        """
        resize_eip_bp_bandwidth

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIPBP, request.id)
        headers = None
        params = {}
        params['resize'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def resize_eip_group_bandwidth(self, request, config=None):
        """
        resize_eip_group_bandwidth

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIPGROUP, request.id)
        headers = None
        params = {}
        params['resize'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def resize_tbsp(self, request, config=None):
        """
        resize_tbsp

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id)
        headers = None
        params = {}
        params['resize'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def restore_eip_from_recycle(self, request, config=None):
        """
        restore_eip_from_recycle

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIP, EipClient.CONSTANT_RECYCLE, request.eip)
        headers = None
        params = {}
        params['restore'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def shared_bandwidth_inquiry(self, request, config=None):
        """
        shared_bandwidth_inquiry

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing SharedBandwidthInquiryResponse data
        :rtype: SharedBandwidthInquiryResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIPGROUP, EipClient.CONSTANT_PRICE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=SharedBandwidthInquiryResponse,
        )

    def shared_data_package_inquiry(self, request, config=None):
        """
        shared_data_package_inquiry

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing SharedDataPackageInquiryResponse data
        :rtype: SharedDataPackageInquiryResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIPTP, EipClient.CONSTANT_PRICE)
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
            model=SharedDataPackageInquiryResponse,
        )

    def start_eip_auto_renew(self, request, config=None):
        """
        start_eip_auto_renew

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIP, request.eip)
        headers = None
        params = {}
        params['startAutoRenew'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def stop_eip_auto_renew(self, request, config=None):
        """
        stop_eip_auto_renew

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIP, request.eip)
        headers = None
        params = {}
        params['stopAutoRenew'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def un_direct_eip(self, request, config=None):
        """
        un_direct_eip

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIP, request.eip)
        headers = None
        params = {}
        params['unDirect'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def unbind_eip(self, request, config=None):
        """
        unbind_eip

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIP, request.eip)
        headers = None
        params = {}
        params['unbind'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def unbind_tbsp_protection_object(self, request, config=None):
        """
        unbind_tbsp_protection_object

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id)
        headers = None
        params = {}
        params['unbind'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_base_ddos_threshold(self, request, config=None):
        """
        update_base_ddos_threshold

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_DDOS, request.ip)
        headers = None
        params = {}
        params['modifyThreshold'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_eip_bp_auto_release_time(self, request, config=None):
        """
        update_eip_bp_auto_release_time

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIPBP, request.id)
        headers = None
        params = {}
        params['retime'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_eip_bp_name(self, request, config=None):
        """
        update_eip_bp_name

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIPBP, request.id)
        headers = None
        params = {}
        params['rename'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_eip_delete_protect(self, request, config=None):
        """
        update_eip_delete_protect

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            EipClient.VERSION_V1, EipClient.CONSTANT_EIP, request.eip, EipClient.CONSTANT_DELETE_PROTECT
        )
        headers = None
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_eip_group(self, request, config=None):
        """
        update_eip_group

        :param request: Request entity containing all parameters
        :type request: EipClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIPGROUP, request.id)
        headers = None
        params = {}
        params['update'] = None
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
