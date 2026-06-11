"""
Example for bcc client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.auth import bce_v1_signer
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_bcc.models.attach_volume_response import AttachVolumeResponse
from baiducloud_python_sdk_bcc.models.create_image_response import CreateImageResponse
from baiducloud_python_sdk_bcc.models.create_volume_response import CreateVolumeResponse
from baiducloud_python_sdk_bcc.models.get_available_images_by_spec_response import GetAvailableImagesBySpecResponse
from baiducloud_python_sdk_bcc.models.get_cds_price_response import GetCdsPriceResponse
from baiducloud_python_sdk_bcc.models.get_disk_quota_response import GetDiskQuotaResponse
from baiducloud_python_sdk_bcc.models.get_image_response import GetImageResponse
from baiducloud_python_sdk_bcc.models.get_volume_response import GetVolumeResponse
from baiducloud_python_sdk_bcc.models.get_volume_resize_progress_response import GetVolumeResizeProgressResponse
from baiducloud_python_sdk_bcc.models.import_image_response import ImportImageResponse
from baiducloud_python_sdk_bcc.models.list_images_response import ListImagesResponse
from baiducloud_python_sdk_bcc.models.list_os_response import ListOsResponse
from baiducloud_python_sdk_bcc.models.list_shared_user_response import ListSharedUserResponse
from baiducloud_python_sdk_bcc.models.list_volumes_response import ListVolumesResponse
from baiducloud_python_sdk_bcc.models.purchase_reserved_volume_response import PurchaseReservedVolumeResponse
from baiducloud_python_sdk_bcc.models.remote_copy_image_response import RemoteCopyImageResponse
from baiducloud_python_sdk_bcc.models.resize_volume_response import ResizeVolumeResponse

_logger = logging.getLogger(__name__)


class BccClient(BceBaseClient):
    """
    bcc base sdk client
    """

    VERSION_V2 = b'/v2'

    CONSTANT_IMAGE = b'image'

    CONSTANT_TAG = b'tag'

    CONSTANT_VOLUME = b'volume'

    CONSTANT_PROGRESS = b'progress'

    CONSTANT_DISK = b'disk'

    CONSTANT_QUOTA = b'quota'

    CONSTANT_GET_PRICE = b'getPrice'

    CONSTANT_GET_AVAILABLE_IMAGES_BY_SPEC = b'getAvailableImagesBySpec'

    CONSTANT_RENAME = b'rename'

    CONSTANT_IMPORT = b'import'

    CONSTANT_OS = b'os'

    CONSTANT_SHARED_USERS = b'sharedUsers'

    def __init__(self, config=None):
        """
        Initialize the bcc client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def attach_volume(self, request, config=None):
        """
        attach_volume

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing AttachVolumeResponse data
        :rtype: AttachVolumeResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, request.volume_id)
        headers = None
        params = {}
        params['attach'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=AttachVolumeResponse,
        )

    def bind_tag_image(self, request, config=None):
        """
        bind_tag_image

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_IMAGE, request.image_id, BccClient.CONSTANT_TAG
        )
        headers = None
        params = {}
        params['bind'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def bind_tag_volume(self, request, config=None):
        """
        bind_tag_volume

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, request.volume_id, BccClient.CONSTANT_TAG
        )
        headers = None
        params = {}
        params['bind'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def cancel_remote_copy_image(self, request, config=None):
        """
        cancel_remote_copy_image

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_IMAGE, request.image_id)
        headers = None
        params = {}
        params['cancelRemoteCopy'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, params=params, config=merged_config)

    def create_image(self, request, config=None):
        """
        create_image

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateImageResponse data
        :rtype: CreateImageResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_IMAGE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateImageResponse,
        )

    def create_volume(self, request, config=None):
        """
        create_volume

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateVolumeResponse data
        :rtype: CreateVolumeResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateVolumeResponse,
        )

    def delete_image(self, request, config=None):
        """
        delete_image

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_IMAGE, request.image_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def detach_volume(self, request, config=None):
        """
        detach_volume

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, request.volume_id)
        headers = None
        params = {}
        params['detach'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def get_available_images_by_spec(self, request, config=None):
        """
        get_available_images_by_spec

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetAvailableImagesBySpecResponse data
        :rtype: GetAvailableImagesBySpecResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_IMAGE, BccClient.CONSTANT_GET_AVAILABLE_IMAGES_BY_SPEC
        )
        headers = None
        params = {}
        if request.spec is not None:
            params['spec'] = request.spec
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.os_name is not None:
            params['osName'] = request.os_name
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetAvailableImagesBySpecResponse
        )

    def get_cds_price(self, request, config=None):
        """
        get_cds_price

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetCdsPriceResponse data
        :rtype: GetCdsPriceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, BccClient.CONSTANT_GET_PRICE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=GetCdsPriceResponse,
        )

    def get_disk_quota(self, request, config=None):
        """
        get_disk_quota

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetDiskQuotaResponse data
        :rtype: GetDiskQuotaResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, BccClient.CONSTANT_DISK, BccClient.CONSTANT_QUOTA
        )
        headers = None
        params = {}
        if request.zone_name is not None:
            params['zoneName'] = request.zone_name
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetDiskQuotaResponse
        )

    def get_image(self, request, config=None):
        """
        get_image

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetImageResponse data
        :rtype: GetImageResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_IMAGE, request.image_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetImageResponse)

    def get_volume(self, request, config=None):
        """
        get_volume

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetVolumeResponse data
        :rtype: GetVolumeResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, request.volume_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetVolumeResponse)

    def get_volume_resize_progress(self, request, config=None):
        """
        get_volume_resize_progress

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetVolumeResizeProgressResponse data
        :rtype: GetVolumeResizeProgressResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, BccClient.CONSTANT_PROGRESS, request.volume_id
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=GetVolumeResizeProgressResponse
        )

    def import_image(self, request, config=None):
        """
        import_image

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ImportImageResponse data
        :rtype: ImportImageResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_IMAGE, BccClient.CONSTANT_IMPORT)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=ImportImageResponse,
        )

    def list_images(self, request, config=None):
        """
        list_images

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListImagesResponse data
        :rtype: ListImagesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_IMAGE)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.image_type is not None:
            params['imageType'] = request.image_type
        if request.image_name is not None:
            params['imageName'] = request.image_name
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListImagesResponse
        )

    def list_os(self, request, config=None):
        """
        list_os

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListOsResponse data
        :rtype: ListOsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_IMAGE, BccClient.CONSTANT_OS)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), config=merged_config, model=ListOsResponse
        )

    def list_shared_user(self, request, config=None):
        """
        list_shared_user

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListSharedUserResponse data
        :rtype: ListSharedUserResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_IMAGE, request.image_id, BccClient.CONSTANT_SHARED_USERS
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=ListSharedUserResponse)

    def list_volumes(self, request, config=None):
        """
        list_volumes

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListVolumesResponse data
        :rtype: ListVolumesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME)
        headers = None
        params = {}
        if request.marker is not None:
            params['marker'] = request.marker
        if request.max_keys is not None:
            params['maxKeys'] = request.max_keys
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.zone_name is not None:
            params['zoneName'] = request.zone_name
        if request.cluster_id is not None:
            params['clusterId'] = request.cluster_id
        if request.charge_filter is not None:
            params['chargeFilter'] = request.charge_filter
        if request.usage_filter is not None:
            params['usageFilter'] = request.usage_filter
        if request.name is not None:
            params['name'] = request.name
        if request.product_category is not None:
            params['productCategory'] = request.product_category
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListVolumesResponse
        )

    def modify_cds_attribute(self, request, config=None):
        """
        modify_cds_attribute

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, request.volume_id)
        headers = None
        params = {}
        params['modify'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def modify_volume_charge_type(self, request, config=None):
        """
        modify_volume_charge_type

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, request.volume_id)
        headers = None
        params = {}
        params['modifyChargeType'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def purchase_reserved_volume(self, request, config=None):
        """
        purchase_reserved_volume

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing PurchaseReservedVolumeResponse data
        :rtype: PurchaseReservedVolumeResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, request.volume_id)
        headers = None
        params = {}
        params['purchaseReserved'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=PurchaseReservedVolumeResponse,
        )

    def release_volume(self, request, config=None):
        """
        release_volume

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, request.volume_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def remote_copy_image(self, request, config=None):
        """
        remote_copy_image

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing RemoteCopyImageResponse data
        :rtype: RemoteCopyImageResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_IMAGE, request.image_id)
        headers = None
        params = {}
        params['remoteCopy'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=RemoteCopyImageResponse,
        )

    def rename_image(self, request, config=None):
        """
        rename_image

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_IMAGE, BccClient.CONSTANT_RENAME)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def rename_volume(self, request, config=None):
        """
        rename_volume

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, request.volume_id)
        headers = None
        params = {}
        params['rename'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def resize_volume(self, request, config=None):
        """
        resize_volume

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ResizeVolumeResponse data
        :rtype: ResizeVolumeResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, request.volume_id)
        headers = None
        params = {}
        params['resize'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=ResizeVolumeResponse,
        )

    def rollback_volume(self, request, config=None):
        """
        rollback_volume

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, request.volume_id)
        headers = None
        params = {}
        params['rollback'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def share_image(self, request, config=None):
        """
        share_image

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_IMAGE, request.image_id)
        headers = None
        params = {}
        params['share'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def un_share_image(self, request, config=None):
        """
        un_share_image

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(BccClient.VERSION_V2, BccClient.CONSTANT_IMAGE, request.image_id)
        headers = None
        params = {}
        params['unshare'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def unbind_tag_image(self, request, config=None):
        """
        unbind_tag_image

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_IMAGE, request.image_id, BccClient.CONSTANT_TAG
        )
        headers = None
        params = {}
        params['unbind'] = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def unbind_tag_volume(self, request, config=None):
        """
        unbind_tag_volume

        :param request: Request entity containing all parameters
        :type request: BccClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            BccClient.VERSION_V2, BccClient.CONSTANT_VOLUME, request.volume_id, BccClient.CONSTANT_TAG
        )
        headers = None
        params = {}
        params['unbind'] = None
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
