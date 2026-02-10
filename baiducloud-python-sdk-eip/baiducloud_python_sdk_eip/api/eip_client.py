import copy
import logging
import uuid

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.auth import bce_v1_signer
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_eip.models.bandwidth_package_inquiry_response import BandwidthPackageInquiryResponse
from baiducloud_python_sdk_eip.models.create_tbsp_response import CreateTbspResponse
from baiducloud_python_sdk_eip.models.detail_tbsp_response import DetailTbspResponse
from baiducloud_python_sdk_eip.models.eip_inquiry_response import EipInquiryResponse
from baiducloud_python_sdk_eip.models.list_tbsp_response import ListTbspResponse
from baiducloud_python_sdk_eip.models.list_tbsp_area_blocking_response import ListTbspAreaBlockingResponse
from baiducloud_python_sdk_eip.models.list_tbsp_ip_clean_response import ListTbspIpCleanResponse
from baiducloud_python_sdk_eip.models.list_tbsp_ip_whitelist_response import ListTbspIpWhitelistResponse
from baiducloud_python_sdk_eip.models.list_tbsp_protocol_blocking_response import ListTbspProtocolBlockingResponse
from baiducloud_python_sdk_eip.models.shared_bandwidth_inquiry_response import SharedBandwidthInquiryResponse
from baiducloud_python_sdk_eip.models.shared_data_package_inquiry_response import SharedDataPackageInquiryResponse

_logger = logging.getLogger(__name__)


class EipClient(BceBaseClient):

    VERSION_V1 = b'/v1'

    CONSTANT_TBSP = b'tbsp'

    CONSTANT_AREA_BLOCKING = b'areaBlocking'

    CONSTANT_EIP = b'eip'

    CONSTANT_PRICE = b'price'

    CONSTANT_PROTOCOL_BLOCKING = b'protocolBlocking'

    CONSTANT_EIPBP = b'eipbp'

    CONSTANT_IP_PROTECT_LEVEL = b'ipProtectLevel'

    CONSTANT_IP_CLEAN = b'ipClean'

    CONSTANT_IP_WHITELIST = b'ipWhitelist'

    CONSTANT_EIPTP = b'eiptp'

    CONSTANT_EIPGROUP = b'eipgroup'

    def __init__(self, config=None):
        bce_base_client.BceBaseClient.__init__(self, config)

    def add_tbsp_area_blocking(self, request, config=None):
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id, EipClient.CONSTANT_AREA_BLOCKING)
        params = {
            'clientToken' : request.client_token,
        }
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), params=params, config=config)

    def add_tbsp_ip_whitelist(self, request, config=None):
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id, EipClient.CONSTANT_IP_WHITELIST)
        params = {
            'clientToken' : request.client_token,
        }
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), params=params, config=config)

    def add_tbsp_protocol_blocking(self, request, config=None):
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id, EipClient.CONSTANT_PROTOCOL_BLOCKING)
        params = {
            'clientToken' : request.client_token,
        }
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), params=params, config=config)

    def bandwidth_package_inquiry(self, request, config=None):
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIPBP, EipClient.CONSTANT_PRICE)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=config, model=BandwidthPackageInquiryResponse)

    def bind_tbsp_protection_object(self, request, config=None):
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id)
        params = {
            'bind' : None,
            'clientToken' : request.client_token,
        }
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), params=params, config=config)

    def create_tbsp(self, request, config=None):
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP)
        params = {
            'clientToken' : request.client_token,
        }
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), params=params, config=config, model=CreateTbspResponse)

    def detail_tbsp(self, request, config=None):
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id)
        return self._send_request(http_methods.GET, path=path
                                , config=config, model=DetailTbspResponse)

    def disable_tbsp_ip_clean(self, request, config=None):
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id, EipClient.CONSTANT_IP_CLEAN)
        params = {
            'turnOffClean' : None,
            'clientToken' : request.client_token,
        }
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), params=params, config=config)

    def eip_inquiry(self, request, config=None):
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIP, EipClient.CONSTANT_PRICE)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=config, model=EipInquiryResponse)

    def enable_tbsp_ip_clean(self, request, config=None):
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id, EipClient.CONSTANT_IP_CLEAN)
        params = {
            'turnOnClean' : None,
            'clientToken' : request.client_token,
            'ip' : request.ip,
        }
        return self._send_request(http_methods.PUT, path=path
                                , params=params, config=config)

    def list_tbsp(self, request, config=None):
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP)
        params = {
            'id' : request.id,
            'name' : request.name,
            'status' : request.status,
            'marker' : request.marker,
            'maxKeys' : request.max_keys,
        }
        return self._send_request(http_methods.GET, path=path
                                , params=params, config=config, model=ListTbspResponse)

    def list_tbsp_area_blocking(self, request, config=None):
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id, EipClient.CONSTANT_AREA_BLOCKING)
        params = {
            'ip' : request.ip,
        }
        return self._send_request(http_methods.GET, path=path
                                , params=params, config=config, model=ListTbspAreaBlockingResponse)

    def list_tbsp_ip_clean(self, request, config=None):
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id, EipClient.CONSTANT_IP_CLEAN)
        params = {
            'ip' : request.ip,
            'marker' : request.marker,
            'maxKeys' : request.max_keys,
        }
        return self._send_request(http_methods.GET, path=path
                                , params=params, config=config, model=ListTbspIpCleanResponse)

    def list_tbsp_ip_whitelist(self, request, config=None):
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id, EipClient.CONSTANT_IP_WHITELIST)
        params = {
            'ip' : request.ip,
            'ipCidr' : request.ip_cidr,
            'marker' : request.marker,
            'maxKeys' : request.max_keys,
        }
        return self._send_request(http_methods.GET, path=path
                                , params=params, config=config, model=ListTbspIpWhitelistResponse)

    def list_tbsp_protocol_blocking(self, request, config=None):
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id, EipClient.CONSTANT_PROTOCOL_BLOCKING)
        params = {
            'ip' : request.ip,
        }
        return self._send_request(http_methods.GET, path=path
                                , params=params, config=config, model=ListTbspProtocolBlockingResponse)

    def modify_tbsp_ip_clean_threshold(self, request, config=None):
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id, EipClient.CONSTANT_IP_CLEAN)
        params = {
            'modifyThreshold' : None,
            'clientToken' : request.client_token,
        }
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), params=params, config=config)

    def modify_tbsp_ip_protect_level(self, request, config=None):
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id, EipClient.CONSTANT_IP_PROTECT_LEVEL)
        params = {
            'clientToken' : request.client_token,
        }
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), params=params, config=config)

    def remove_tbsp_area_blocking(self, request, config=None):
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id, EipClient.CONSTANT_AREA_BLOCKING)
        params = {
            'ip' : request.ip,
            'blockType' : request.block_type,
            'clientToken' : request.client_token,
        }
        return self._send_request(http_methods.DELETE, path=path
                                , params=params, config=config)

    def remove_tbsp_ip_whitelist(self, request, config=None):
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id, EipClient.CONSTANT_IP_WHITELIST)
        params = {
            'clientToken' : request.client_token,
            'ip' : request.ip,
            'whitelistId' : request.whitelist_id,
        }
        return self._send_request(http_methods.DELETE, path=path
                                , params=params, config=config)

    def remove_tbsp_protocol_blocking(self, request, config=None):
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id, EipClient.CONSTANT_PROTOCOL_BLOCKING)
        params = {
            'ip' : request.ip,
            'clientToken' : request.client_token,
        }
        return self._send_request(http_methods.DELETE, path=path
                                , params=params, config=config)

    def renew_tbsp(self, request, config=None):
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id)
        params = {
            'purchaseReserved' : None,
            'clientToken' : request.client_token,
        }
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), params=params, config=config)

    def resize_tbsp(self, request, config=None):
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id)
        params = {
            'resize' : None,
            'clientToken' : request.client_token,
        }
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), params=params, config=config)

    def shared_bandwidth_inquiry(self, request, config=None):
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIPGROUP, EipClient.CONSTANT_PRICE)
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), config=config, model=SharedBandwidthInquiryResponse)

    def shared_data_package_inquiry(self, request, config=None):
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_EIPTP, EipClient.CONSTANT_PRICE)
        params = {
            'clientToken' : request.client_token,
        }
        return self._send_request(http_methods.POST, path=path
                                , body=request.to_json_string(), params=params, config=config, model=SharedDataPackageInquiryResponse)

    def unbind_tbsp_protection_object(self, request, config=None):
        path = utils.append_uri(EipClient.VERSION_V1, EipClient.CONSTANT_TBSP, request.id)
        params = {
            'unbind' : None,
            'clientToken' : request.client_token,
        }
        return self._send_request(http_methods.PUT, path=path
                                , body=request.to_json_string(), params=params, config=config)



    @staticmethod
    def _generate_default_client_token():
        """
        default client token by uuid1
        """
        return uuid.uuid1()

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

    def _send_request(self, http_method, path,
                      body=None, headers=None, params=None,
                      config=None, body_parser=None, model=None):
        config = self._merge_config(config)
        if body_parser is None:
            body_parser = handler.parse_json
        if headers is None:
            headers = {b'Accept': b'*/*', b'Content-Type':
                b'application/json;charset=utf-8'}
        return bce_http_client.send_request(
            config, bce_v1_signer.sign, [handler.parse_error, body_parser],
            http_method, path, body, headers, params, model=model)
