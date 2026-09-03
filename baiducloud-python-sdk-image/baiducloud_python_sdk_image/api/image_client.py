"""
Example for image client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_core.util import request_body_utils
from baiducloud_python_sdk_image.models.advanced_general_response import AdvancedGeneralResponse
from baiducloud_python_sdk_image.models.ai_retouching_create_task_response import AiRetouchingCreateTaskResponse
from baiducloud_python_sdk_image.models.ai_retouching_query_task_response import AiRetouchingQueryTaskResponse
from baiducloud_python_sdk_image.models.animal_response import AnimalResponse
from baiducloud_python_sdk_image.models.car_response import CarResponse
from baiducloud_python_sdk_image.models.color_enhance_response import ColorEnhanceResponse
from baiducloud_python_sdk_image.models.colourize_response import ColourizeResponse
from baiducloud_python_sdk_image.models.contrast_enhance_response import ContrastEnhanceResponse
from baiducloud_python_sdk_image.models.dehaze_response import DehazeResponse
from baiducloud_python_sdk_image.models.dish_response import DishResponse
from baiducloud_python_sdk_image.models.doc_repair_response import DocRepairResponse
from baiducloud_python_sdk_image.models.image_definition_enhance_response import ImageDefinitionEnhanceResponse
from baiducloud_python_sdk_image.models.image_quality_enhance_response import ImageQualityEnhanceResponse
from baiducloud_python_sdk_image.models.image_understanding_get_result_response import (
    ImageUnderstandingGetResultResponse,
)
from baiducloud_python_sdk_image.models.image_understanding_request_response import ImageUnderstandingRequestResponse
from baiducloud_python_sdk_image.models.ingredient_response import IngredientResponse
from baiducloud_python_sdk_image.models.inpainting_response import InpaintingResponse
from baiducloud_python_sdk_image.models.landmark_response import LandmarkResponse
from baiducloud_python_sdk_image.models.logo_response import LogoResponse
from baiducloud_python_sdk_image.models.logo_add_response import LogoAddResponse
from baiducloud_python_sdk_image.models.logo_delete_response import LogoDeleteResponse
from baiducloud_python_sdk_image.models.materiel_image_add_response import MaterielImageAddResponse
from baiducloud_python_sdk_image.models.materiel_image_delete_response import MaterielImageDeleteResponse
from baiducloud_python_sdk_image.models.materiel_image_search_response import MaterielImageSearchResponse
from baiducloud_python_sdk_image.models.materiel_image_update_response import MaterielImageUpdateResponse
from baiducloud_python_sdk_image.models.multi_object_detect_response import MultiObjectDetectResponse
from baiducloud_python_sdk_image.models.object_detect_response import ObjectDetectResponse
from baiducloud_python_sdk_image.models.picturebook_image_add_response import PicturebookImageAddResponse
from baiducloud_python_sdk_image.models.picturebook_image_delete_response import PicturebookImageDeleteResponse
from baiducloud_python_sdk_image.models.picturebook_image_search_response import PicturebookImageSearchResponse
from baiducloud_python_sdk_image.models.picturebook_image_update_response import PicturebookImageUpdateResponse
from baiducloud_python_sdk_image.models.plant_response import PlantResponse
from baiducloud_python_sdk_image.models.product_image_add_response import ProductImageAddResponse
from baiducloud_python_sdk_image.models.product_image_delete_response import ProductImageDeleteResponse
from baiducloud_python_sdk_image.models.product_image_search_response import ProductImageSearchResponse
from baiducloud_python_sdk_image.models.product_image_update_response import ProductImageUpdateResponse
from baiducloud_python_sdk_image.models.remove_moire_response import RemoveMoireResponse
from baiducloud_python_sdk_image.models.same_image_add_response import SameImageAddResponse
from baiducloud_python_sdk_image.models.same_image_delete_response import SameImageDeleteResponse
from baiducloud_python_sdk_image.models.same_image_search_response import SameImageSearchResponse
from baiducloud_python_sdk_image.models.same_image_update_response import SameImageUpdateResponse
from baiducloud_python_sdk_image.models.segment_response import SegmentResponse
from baiducloud_python_sdk_image.models.selfie_anime_response import SelfieAnimeResponse
from baiducloud_python_sdk_image.models.similar_image_add_response import SimilarImageAddResponse
from baiducloud_python_sdk_image.models.similar_image_delete_response import SimilarImageDeleteResponse
from baiducloud_python_sdk_image.models.similar_image_search_response import SimilarImageSearchResponse
from baiducloud_python_sdk_image.models.similar_image_update_response import SimilarImageUpdateResponse
from baiducloud_python_sdk_image.models.stretch_restore_response import StretchRestoreResponse
from baiducloud_python_sdk_image.models.style_trans_response import StyleTransResponse
from baiducloud_python_sdk_image.models.vehicle_detect_response import VehicleDetectResponse

_logger = logging.getLogger(__name__)


class ImageClient(BceBaseClient):
    """
    image base sdk client
    """

    CONSTANT_REST = b'rest'

    CONSTANT_2_0 = b'2.0'

    CONSTANT_IMAGE_PROCESS = b'image-process'

    CONSTANT_V1 = b'v1'

    CONSTANT_DEHAZE = b'dehaze'

    CONSTANT_IMAGE_CLASSIFY = b'image-classify'

    CONSTANT_REALTIME_SEARCH = b'realtime_search'

    CONSTANT_MATERIEL = b'materiel'

    CONSTANT_UPDATE = b'update'

    CONSTANT_DELETE = b'delete'

    CONSTANT_SAME_HQ = b'same_hq'

    CONSTANT_SEGMENT = b'segment'

    CONSTANT_V2 = b'v2'

    CONSTANT_LOGO = b'logo'

    CONSTANT_ADD = b'add'

    CONSTANT_LANDMARK = b'landmark'

    CONSTANT_IMAGE_UNDERSTANDING = b'image-understanding'

    CONSTANT_REQUEST = b'request'

    CONSTANT_SEARCH = b'search'

    CONSTANT_CONTRAST_ENHANCE = b'contrast_enhance'

    CONSTANT_SIMILAR = b'similar'

    CONSTANT_RETOUCHING = b'retouching'

    CONSTANT_CREATE_TASK = b'create_task'

    CONSTANT_PRODUCT = b'product'

    CONSTANT_IMAGESEARCH = b'imagesearch'

    CONSTANT_PICTUREBOOK = b'picturebook'

    CONSTANT_QUERY_TASK = b'query_task'

    CONSTANT_DISH = b'dish'

    CONSTANT_SELFIE_ANIME = b'selfie_anime'

    CONSTANT_PLANT = b'plant'

    CONSTANT_ANIMAL = b'animal'

    CONSTANT_IMAGE_DEFINITION_ENHANCE = b'image_definition_enhance'

    CONSTANT_COLOR_ENHANCE = b'color_enhance'

    CONSTANT_COLOURIZE = b'colourize'

    CONSTANT_STYLE_TRANS = b'style_trans'

    CONSTANT_INPAINTING = b'inpainting'

    CONSTANT_MULTI_OBJECT_DETECT = b'multi_object_detect'

    CONSTANT_GET_RESULT = b'get-result'

    CONSTANT_CAR = b'car'

    CONSTANT_REMOVE_MOIRE = b'remove_moire'

    CONSTANT_IMAGE_QUALITY_ENHANCE = b'image_quality_enhance'

    CONSTANT_CLASSIFY = b'classify'

    CONSTANT_INGREDIENT = b'ingredient'

    CONSTANT_ADVANCED_GENERAL = b'advanced_general'

    CONSTANT_OBJECT_DETECT = b'object_detect'

    CONSTANT_DOC_REPAIR = b'doc_repair'

    CONSTANT_VEHICLE_DETECT = b'vehicle_detect'

    CONSTANT_STRETCH_RESTORE = b'stretch_restore'

    def __init__(self, config=None):
        """
        Initialize the image client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def advanced_general(self, request, config=None):
        """
        advanced_general

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing AdvancedGeneralResponse data
        :rtype: AdvancedGeneralResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_CLASSIFY,
            ImageClient.CONSTANT_V2,
            ImageClient.CONSTANT_ADVANCED_GENERAL,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=AdvancedGeneralResponse,
        )

    def ai_retouching_create_task(self, request, config=None):
        """
        ai_retouching_create_task

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing AiRetouchingCreateTaskResponse data
        :rtype: AiRetouchingCreateTaskResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_PROCESS,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_RETOUCHING,
            ImageClient.CONSTANT_CREATE_TASK,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=AiRetouchingCreateTaskResponse,
        )

    def ai_retouching_query_task(self, request, config=None):
        """
        ai_retouching_query_task

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing AiRetouchingQueryTaskResponse data
        :rtype: AiRetouchingQueryTaskResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_PROCESS,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_RETOUCHING,
            ImageClient.CONSTANT_QUERY_TASK,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=AiRetouchingQueryTaskResponse,
        )

    def animal(self, request, config=None):
        """
        animal

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing AnimalResponse data
        :rtype: AnimalResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_CLASSIFY,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_ANIMAL,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=form_body, headers=headers, config=merged_config, model=AnimalResponse
        )

    def car(self, request, config=None):
        """
        car

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CarResponse data
        :rtype: CarResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_CLASSIFY,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_CAR,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=form_body, headers=headers, config=merged_config, model=CarResponse
        )

    def color_enhance(self, request, config=None):
        """
        color_enhance

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ColorEnhanceResponse data
        :rtype: ColorEnhanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_PROCESS,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_COLOR_ENHANCE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=ColorEnhanceResponse,
        )

    def colourize(self, request, config=None):
        """
        colourize

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ColourizeResponse data
        :rtype: ColourizeResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_PROCESS,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_COLOURIZE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=ColourizeResponse,
        )

    def contrast_enhance(self, request, config=None):
        """
        contrast_enhance

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ContrastEnhanceResponse data
        :rtype: ContrastEnhanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_PROCESS,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_CONTRAST_ENHANCE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=ContrastEnhanceResponse,
        )

    def dehaze(self, request, config=None):
        """
        dehaze

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DehazeResponse data
        :rtype: DehazeResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_PROCESS,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_DEHAZE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=form_body, headers=headers, config=merged_config, model=DehazeResponse
        )

    def dish(self, request, config=None):
        """
        dish

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DishResponse data
        :rtype: DishResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_CLASSIFY,
            ImageClient.CONSTANT_V2,
            ImageClient.CONSTANT_DISH,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=form_body, headers=headers, config=merged_config, model=DishResponse
        )

    def doc_repair(self, request, config=None):
        """
        doc_repair

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DocRepairResponse data
        :rtype: DocRepairResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_PROCESS,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_DOC_REPAIR,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=DocRepairResponse,
        )

    def image_definition_enhance(self, request, config=None):
        """
        image_definition_enhance

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ImageDefinitionEnhanceResponse data
        :rtype: ImageDefinitionEnhanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_PROCESS,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_IMAGE_DEFINITION_ENHANCE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=ImageDefinitionEnhanceResponse,
        )

    def image_quality_enhance(self, request, config=None):
        """
        image_quality_enhance

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ImageQualityEnhanceResponse data
        :rtype: ImageQualityEnhanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_PROCESS,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_IMAGE_QUALITY_ENHANCE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=ImageQualityEnhanceResponse,
        )

    def image_understanding_get_result(self, request, config=None):
        """
        image_understanding_get_result

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ImageUnderstandingGetResultResponse data
        :rtype: ImageUnderstandingGetResultResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_CLASSIFY,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_IMAGE_UNDERSTANDING,
            ImageClient.CONSTANT_GET_RESULT,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=ImageUnderstandingGetResultResponse,
        )

    def image_understanding_request(self, request, config=None):
        """
        image_understanding_request

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ImageUnderstandingRequestResponse data
        :rtype: ImageUnderstandingRequestResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_CLASSIFY,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_IMAGE_UNDERSTANDING,
            ImageClient.CONSTANT_REQUEST,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=ImageUnderstandingRequestResponse,
        )

    def ingredient(self, request, config=None):
        """
        ingredient

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing IngredientResponse data
        :rtype: IngredientResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_CLASSIFY,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_CLASSIFY,
            ImageClient.CONSTANT_INGREDIENT,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=IngredientResponse,
        )

    def inpainting(self, request, config=None):
        """
        inpainting

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing InpaintingResponse data
        :rtype: InpaintingResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_PROCESS,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_INPAINTING,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=InpaintingResponse,
        )

    def landmark(self, request, config=None):
        """
        landmark

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing LandmarkResponse data
        :rtype: LandmarkResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_CLASSIFY,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_LANDMARK,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=form_body, headers=headers, config=merged_config, model=LandmarkResponse
        )

    def logo(self, request, config=None):
        """
        logo

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing LogoResponse data
        :rtype: LogoResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_CLASSIFY,
            ImageClient.CONSTANT_V2,
            ImageClient.CONSTANT_LOGO,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=form_body, headers=headers, config=merged_config, model=LogoResponse
        )

    def logo_add(self, request, config=None):
        """
        logo_add

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing LogoAddResponse data
        :rtype: LogoAddResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_REALTIME_SEARCH,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_LOGO,
            ImageClient.CONSTANT_ADD,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=form_body, headers=headers, config=merged_config, model=LogoAddResponse
        )

    def logo_delete(self, request, config=None):
        """
        logo_delete

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing LogoDeleteResponse data
        :rtype: LogoDeleteResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_REALTIME_SEARCH,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_LOGO,
            ImageClient.CONSTANT_DELETE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=LogoDeleteResponse,
        )

    def materiel_image_add(self, request, config=None):
        """
        materiel_image_add

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing MaterielImageAddResponse data
        :rtype: MaterielImageAddResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_CLASSIFY,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_REALTIME_SEARCH,
            ImageClient.CONSTANT_MATERIEL,
            ImageClient.CONSTANT_ADD,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=MaterielImageAddResponse,
        )

    def materiel_image_delete(self, request, config=None):
        """
        materiel_image_delete

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing MaterielImageDeleteResponse data
        :rtype: MaterielImageDeleteResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_CLASSIFY,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_REALTIME_SEARCH,
            ImageClient.CONSTANT_MATERIEL,
            ImageClient.CONSTANT_DELETE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=MaterielImageDeleteResponse,
        )

    def materiel_image_search(self, request, config=None):
        """
        materiel_image_search

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing MaterielImageSearchResponse data
        :rtype: MaterielImageSearchResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_CLASSIFY,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_REALTIME_SEARCH,
            ImageClient.CONSTANT_MATERIEL,
            ImageClient.CONSTANT_SEARCH,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=MaterielImageSearchResponse,
        )

    def materiel_image_update(self, request, config=None):
        """
        materiel_image_update

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing MaterielImageUpdateResponse data
        :rtype: MaterielImageUpdateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_CLASSIFY,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_REALTIME_SEARCH,
            ImageClient.CONSTANT_MATERIEL,
            ImageClient.CONSTANT_UPDATE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=MaterielImageUpdateResponse,
        )

    def multi_object_detect(self, request, config=None):
        """
        multi_object_detect

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing MultiObjectDetectResponse data
        :rtype: MultiObjectDetectResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_CLASSIFY,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_MULTI_OBJECT_DETECT,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=MultiObjectDetectResponse,
        )

    def object_detect(self, request, config=None):
        """
        object_detect

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ObjectDetectResponse data
        :rtype: ObjectDetectResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_CLASSIFY,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_OBJECT_DETECT,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=ObjectDetectResponse,
        )

    def picturebook_image_add(self, request, config=None):
        """
        picturebook_image_add

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing PicturebookImageAddResponse data
        :rtype: PicturebookImageAddResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGESEARCH,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_REALTIME_SEARCH,
            ImageClient.CONSTANT_PICTUREBOOK,
            ImageClient.CONSTANT_ADD,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=PicturebookImageAddResponse,
        )

    def picturebook_image_delete(self, request, config=None):
        """
        picturebook_image_delete

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing PicturebookImageDeleteResponse data
        :rtype: PicturebookImageDeleteResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGESEARCH,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_REALTIME_SEARCH,
            ImageClient.CONSTANT_PICTUREBOOK,
            ImageClient.CONSTANT_DELETE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=PicturebookImageDeleteResponse,
        )

    def picturebook_image_search(self, request, config=None):
        """
        picturebook_image_search

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing PicturebookImageSearchResponse data
        :rtype: PicturebookImageSearchResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGESEARCH,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_REALTIME_SEARCH,
            ImageClient.CONSTANT_PICTUREBOOK,
            ImageClient.CONSTANT_SEARCH,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=PicturebookImageSearchResponse,
        )

    def picturebook_image_update(self, request, config=None):
        """
        picturebook_image_update

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing PicturebookImageUpdateResponse data
        :rtype: PicturebookImageUpdateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGESEARCH,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_REALTIME_SEARCH,
            ImageClient.CONSTANT_PICTUREBOOK,
            ImageClient.CONSTANT_UPDATE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=PicturebookImageUpdateResponse,
        )

    def plant(self, request, config=None):
        """
        plant

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing PlantResponse data
        :rtype: PlantResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_CLASSIFY,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_PLANT,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=form_body, headers=headers, config=merged_config, model=PlantResponse
        )

    def product_image_add(self, request, config=None):
        """
        product_image_add

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ProductImageAddResponse data
        :rtype: ProductImageAddResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_CLASSIFY,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_REALTIME_SEARCH,
            ImageClient.CONSTANT_PRODUCT,
            ImageClient.CONSTANT_ADD,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=ProductImageAddResponse,
        )

    def product_image_delete(self, request, config=None):
        """
        product_image_delete

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ProductImageDeleteResponse data
        :rtype: ProductImageDeleteResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_CLASSIFY,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_REALTIME_SEARCH,
            ImageClient.CONSTANT_PRODUCT,
            ImageClient.CONSTANT_DELETE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=ProductImageDeleteResponse,
        )

    def product_image_search(self, request, config=None):
        """
        product_image_search

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ProductImageSearchResponse data
        :rtype: ProductImageSearchResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_CLASSIFY,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_REALTIME_SEARCH,
            ImageClient.CONSTANT_PRODUCT,
            ImageClient.CONSTANT_SEARCH,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=ProductImageSearchResponse,
        )

    def product_image_update(self, request, config=None):
        """
        product_image_update

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ProductImageUpdateResponse data
        :rtype: ProductImageUpdateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_CLASSIFY,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_REALTIME_SEARCH,
            ImageClient.CONSTANT_PRODUCT,
            ImageClient.CONSTANT_UPDATE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=ProductImageUpdateResponse,
        )

    def remove_moire(self, request, config=None):
        """
        remove_moire

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing RemoveMoireResponse data
        :rtype: RemoveMoireResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_PROCESS,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_REMOVE_MOIRE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=RemoveMoireResponse,
        )

    def same_image_add(self, request, config=None):
        """
        same_image_add

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing SameImageAddResponse data
        :rtype: SameImageAddResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_REALTIME_SEARCH,
            ImageClient.CONSTANT_SAME_HQ,
            ImageClient.CONSTANT_ADD,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=SameImageAddResponse,
        )

    def same_image_delete(self, request, config=None):
        """
        same_image_delete

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing SameImageDeleteResponse data
        :rtype: SameImageDeleteResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_REALTIME_SEARCH,
            ImageClient.CONSTANT_SAME_HQ,
            ImageClient.CONSTANT_DELETE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=SameImageDeleteResponse,
        )

    def same_image_search(self, request, config=None):
        """
        same_image_search

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing SameImageSearchResponse data
        :rtype: SameImageSearchResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_REALTIME_SEARCH,
            ImageClient.CONSTANT_SAME_HQ,
            ImageClient.CONSTANT_SEARCH,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=SameImageSearchResponse,
        )

    def same_image_update(self, request, config=None):
        """
        same_image_update

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing SameImageUpdateResponse data
        :rtype: SameImageUpdateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_REALTIME_SEARCH,
            ImageClient.CONSTANT_SAME_HQ,
            ImageClient.CONSTANT_UPDATE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=SameImageUpdateResponse,
        )

    def segment(self, request, config=None):
        """
        segment

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing SegmentResponse data
        :rtype: SegmentResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_PROCESS,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_SEGMENT,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=form_body, headers=headers, config=merged_config, model=SegmentResponse
        )

    def selfie_anime(self, request, config=None):
        """
        selfie_anime

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing SelfieAnimeResponse data
        :rtype: SelfieAnimeResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_PROCESS,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_SELFIE_ANIME,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=SelfieAnimeResponse,
        )

    def similar_image_add(self, request, config=None):
        """
        similar_image_add

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing SimilarImageAddResponse data
        :rtype: SimilarImageAddResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_CLASSIFY,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_REALTIME_SEARCH,
            ImageClient.CONSTANT_SIMILAR,
            ImageClient.CONSTANT_ADD,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=SimilarImageAddResponse,
        )

    def similar_image_delete(self, request, config=None):
        """
        similar_image_delete

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing SimilarImageDeleteResponse data
        :rtype: SimilarImageDeleteResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_CLASSIFY,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_REALTIME_SEARCH,
            ImageClient.CONSTANT_SIMILAR,
            ImageClient.CONSTANT_DELETE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=SimilarImageDeleteResponse,
        )

    def similar_image_search(self, request, config=None):
        """
        similar_image_search

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing SimilarImageSearchResponse data
        :rtype: SimilarImageSearchResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_CLASSIFY,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_REALTIME_SEARCH,
            ImageClient.CONSTANT_SIMILAR,
            ImageClient.CONSTANT_SEARCH,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=SimilarImageSearchResponse,
        )

    def similar_image_update(self, request, config=None):
        """
        similar_image_update

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing SimilarImageUpdateResponse data
        :rtype: SimilarImageUpdateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_CLASSIFY,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_REALTIME_SEARCH,
            ImageClient.CONSTANT_SIMILAR,
            ImageClient.CONSTANT_UPDATE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=SimilarImageUpdateResponse,
        )

    def stretch_restore(self, request, config=None):
        """
        stretch_restore

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing StretchRestoreResponse data
        :rtype: StretchRestoreResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_PROCESS,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_STRETCH_RESTORE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=StretchRestoreResponse,
        )

    def style_trans(self, request, config=None):
        """
        style_trans

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing StyleTransResponse data
        :rtype: StyleTransResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_PROCESS,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_STYLE_TRANS,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=StyleTransResponse,
        )

    def vehicle_detect(self, request, config=None):
        """
        vehicle_detect

        :param request: Request entity containing all parameters
        :type request: ImageClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing VehicleDetectResponse data
        :rtype: VehicleDetectResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            ImageClient.CONSTANT_REST,
            ImageClient.CONSTANT_2_0,
            ImageClient.CONSTANT_IMAGE_CLASSIFY,
            ImageClient.CONSTANT_V1,
            ImageClient.CONSTANT_VEHICLE_DETECT,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=VehicleDetectResponse,
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
        sign_fn, params = self._choose_signer(config, params)
        return bce_http_client.send_request(
            config, sign_fn, [handler.parse_error, body_parser], http_method, path, body, headers, params, model=model
        )
