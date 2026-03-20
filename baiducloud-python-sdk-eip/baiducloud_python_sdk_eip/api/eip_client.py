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
from baiducloud_python_sdk_eip.models.create_eip_transfer_response import CreateEipTransferResponse
from baiducloud_python_sdk_eip.models.create_tbsp_response import CreateTbspResponse
from baiducloud_python_sdk_eip.models.detail_tbsp_response import DetailTbspResponse
from baiducloud_python_sdk_eip.models.eip_inquiry_response import EipInquiryResponse
from baiducloud_python_sdk_eip.models.list_eip_transfer_response import ListEipTransferResponse
from baiducloud_python_sdk_eip.models.list_recycle_eips_response import ListRecycleEipsResponse
from baiducloud_python_sdk_eip.models.list_tbsp_response import ListTbspResponse
from baiducloud_python_sdk_eip.models.list_tbsp_area_blocking_response import ListTbspAreaBlockingResponse
from baiducloud_python_sdk_eip.models.list_tbsp_ip_clean_response import ListTbspIpCleanResponse
from baiducloud_python_sdk_eip.models.list_tbsp_ip_whitelist_response import ListTbspIpWhitelistResponse
from baiducloud_python_sdk_eip.models.list_tbsp_protocol_blocking_response import ListTbspProtocolBlockingResponse
from baiducloud_python_sdk_eip.models.query_eip_list_response import QueryEipListResponse
from baiducloud_python_sdk_eip.models.shared_bandwidth_inquiry_response import SharedBandwidthInquiryResponse
from baiducloud_python_sdk_eip.models.shared_data_package_inquiry_response import SharedDataPackageInquiryResponse

_logger = logging.getLogger(__name__)


class EipClient(BceBaseClient):
    """
    eip base sdk client
    """

    VERSION_V1 = b'/v1'

    CONSTANT_TBSP = b'tbsp'

    CONSTANT_AREA_BLOCKING = b'areaBlocking'

    CONSTANT_EIP = b'eip'

    CONSTANT_PRICE = b'price'

    CONSTANT_PROTOCOL_BLOCKING = b'protocolBlocking'

    CONSTANT_EIPBP = b'eipbp'

    CONSTANT_IP_PROTECT_LEVEL = b'ipProtectLevel'

    CONSTANT_TRANSFER = b'transfer'

    CONSTANT_IP_CLEAN = b'ipClean'

    CONSTANT_RECYCLE = b'recycle'

    CONSTANT_IP_WHITELIST = b'ipWhitelist'

    CONSTANT_REFUND = b'refund'

    CONSTANT_DELETE_PROTECT = b'deleteProtect'

    CONSTANT_EIPTP = b'eiptp'

    CONSTANT_EIPGROUP = b'eipgroup'

    def __init__(self, config=None):
        """
        Initialize the eip client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

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
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=config
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
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=config
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
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=config
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
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=config,
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
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=config,
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
        params = {}
        params['bind'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=config
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
        params = {}
        params['bind'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=config
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
        params = {}
        params['cancel'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=config
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
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=config,
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
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=config,
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
        return self._send_request(http_methods.GET, path=path, config=config, model=DetailTbspResponse)

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
        params = {}
        params['direct'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.PUT, path=path, params=params, config=config)

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
        params = {}
        params['turnOffClean'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=config
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
        params = {}
        params['resize'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=config
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
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), config=config, model=EipInquiryResponse
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
        params = {}
        params['action'] = 'TO_PREPAY'
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=config
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
        params = {}
        params['purchaseReserved'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=config
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
        params = {}
        params['turnOnClean'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        if request.ip is not None:
            params['ip'] = request.ip
        return self._send_request(http_methods.PUT, path=path, params=params, config=config)

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
        return self._send_request(
            http_methods.GET, path=path, params=params, config=config, model=ListEipTransferResponse
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
        params = {}
        if request.eip is not None:
            params['eip'] = request.eip
        if request.name is not None:
            params['name'] = request.name
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        return self._send_request(
            http_methods.GET, path=path, params=params, config=config, model=ListRecycleEipsResponse
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
        return self._send_request(http_methods.GET, path=path, params=params, config=config, model=ListTbspResponse)

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
        params = {}
        if request.ip is not None:
            params['ip'] = request.ip
        return self._send_request(
            http_methods.GET, path=path, params=params, config=config, model=ListTbspAreaBlockingResponse
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
        params = {}
        if request.ip is not None:
            params['ip'] = request.ip
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        return self._send_request(
            http_methods.GET, path=path, params=params, config=config, model=ListTbspIpCleanResponse
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
        params = {}
        if request.ip is not None:
            params['ip'] = request.ip
        if request.ip_cidr is not None:
            params['ipCidr'] = request.ip_cidr
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        return self._send_request(
            http_methods.GET, path=path, params=params, config=config, model=ListTbspIpWhitelistResponse
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
        params = {}
        if request.ip is not None:
            params['ip'] = request.ip
        return self._send_request(
            http_methods.GET, path=path, params=params, config=config, model=ListTbspProtocolBlockingResponse
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
        params = {}
        params['modifyThreshold'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=config
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
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=config
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
        params = {}
        if request.release_to_recycle is not None:
            params['releaseToRecycle'] = request.release_to_recycle
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.DELETE, path=path, params=params, config=config)

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
        return self._send_request(
            http_methods.GET, path=path, params=params, config=config, model=QueryEipListResponse
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
        params = {}
        params['accept'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=config
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
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.PUT, path=path, params=params, config=config)

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
        params = {}
        params['reject'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=config
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
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        if request.release_to_recycle is not None:
            params['releaseToRecycle'] = request.release_to_recycle
        return self._send_request(http_methods.DELETE, path=path, params=params, config=config)

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
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.DELETE, path=path, params=params, config=config)

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
        params = {}
        if request.ip is not None:
            params['ip'] = request.ip
        if request.block_type is not None:
            params['blockType'] = request.block_type
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.DELETE, path=path, params=params, config=config)

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
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        if request.ip is not None:
            params['ip'] = request.ip
        if request.whitelist_id is not None:
            params['whitelistId'] = request.whitelist_id
        return self._send_request(http_methods.DELETE, path=path, params=params, config=config)

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
        params = {}
        if request.ip is not None:
            params['ip'] = request.ip
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.DELETE, path=path, params=params, config=config)

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
        params = {}
        params['purchaseReserved'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=config
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
        params = {}
        params['resize'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=config
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
        params = {}
        params['restore'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.PUT, path=path, params=params, config=config)

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
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=config,
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
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=config,
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
        params = {}
        params['startAutoRenew'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=config
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
        params = {}
        params['stopAutoRenew'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.PUT, path=path, params=params, config=config)

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
        params = {}
        params['unDirect'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.PUT, path=path, params=params, config=config)

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
        params = {}
        params['unbind'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(http_methods.PUT, path=path, params=params, config=config)

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
        params = {}
        params['unbind'] = None
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=config
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
        params = {}
        if request.client_token is not None:
            params['clientToken'] = request.client_token
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=config
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
