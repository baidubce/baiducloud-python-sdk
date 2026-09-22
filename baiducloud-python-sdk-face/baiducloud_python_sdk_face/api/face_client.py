"""
Example for face client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_core.util import request_body_utils
from baiducloud_python_sdk_face.models.face_delete_response import FaceDeleteResponse
from baiducloud_python_sdk_face.models.face_detect_response import FaceDetectResponse
from baiducloud_python_sdk_face.models.face_edit_attr_response import FaceEditAttrResponse
from baiducloud_python_sdk_face.models.face_get_list_response import FaceGetListResponse
from baiducloud_python_sdk_face.models.face_landmark_response import FaceLandmarkResponse
from baiducloud_python_sdk_face.models.face_merge_response import FaceMergeResponse
from baiducloud_python_sdk_face.models.face_multi_search_response import FaceMultiSearchResponse
from baiducloud_python_sdk_face.models.face_person_verify_response import FacePersonVerifyResponse
from baiducloud_python_sdk_face.models.face_search_response import FaceSearchResponse
from baiducloud_python_sdk_face.models.face_verify_response import FaceVerifyResponse
from baiducloud_python_sdk_face.models.face_verify_date_response import FaceVerifyDateResponse
from baiducloud_python_sdk_face.models.group_add_response import GroupAddResponse
from baiducloud_python_sdk_face.models.group_delete_response import GroupDeleteResponse
from baiducloud_python_sdk_face.models.group_get_list_response import GroupGetListResponse
from baiducloud_python_sdk_face.models.group_get_users_response import GroupGetUsersResponse
from baiducloud_python_sdk_face.models.id_match_date_response import IdMatchDateResponse
from baiducloud_python_sdk_face.models.id_match_status_response import IdMatchStatusResponse
from baiducloud_python_sdk_face.models.person_id_match_response import PersonIdMatchResponse
from baiducloud_python_sdk_face.models.session_code_response import SessionCodeResponse
from baiducloud_python_sdk_face.models.user_add_response import UserAddResponse
from baiducloud_python_sdk_face.models.user_copy_response import UserCopyResponse
from baiducloud_python_sdk_face.models.user_delete_response import UserDeleteResponse
from baiducloud_python_sdk_face.models.user_get_response import UserGetResponse
from baiducloud_python_sdk_face.models.user_update_response import UserUpdateResponse
from baiducloud_python_sdk_face.models.verify_response import VerifyResponse

_logger = logging.getLogger(__name__)


class FaceClient(BceBaseClient):
    """
    face base sdk client
    """

    CONSTANT_REST = b'rest'

    CONSTANT_2_0 = b'2.0'

    CONSTANT_FACE = b'face'

    CONSTANT_V1 = b'v1'

    CONSTANT_FACELIVENESS = b'faceliveness'

    CONSTANT_SESSIONCODE = b'sessioncode'

    CONSTANT_V3 = b'v3'

    CONSTANT_DETECT = b'detect'

    CONSTANT_FACESET = b'faceset'

    CONSTANT_GROUP = b'group'

    CONSTANT_ADD = b'add'

    CONSTANT_GETLIST = b'getlist'

    CONSTANT_DELETE = b'delete'

    CONSTANT_PERSON = b'person'

    CONSTANT_VERIFY = b'verify'

    CONSTANT_FACEVERIFY = b'faceverify'

    CONSTANT_SEARCH = b'search'

    CONSTANT_LANDMARK = b'landmark'

    CONSTANT_USER = b'user'

    CONSTANT_MULTI_SEARCH = b'multi-search'

    CONSTANT_UPDATE = b'update'

    CONSTANT_GETUSERS = b'getusers'

    CONSTANT_V4 = b'v4'

    CONSTANT_VERIFY_DATE = b'verify_date'

    CONSTANT_IDMATCH_STATUS = b'idmatch_status'

    CONSTANT_GET = b'get'

    CONSTANT_COPY = b'copy'

    CONSTANT_IDMATCH = b'idmatch'

    CONSTANT_IDMATCH_DATE = b'idmatch_date'

    CONSTANT_EDITATTR = b'editattr'

    CONSTANT_MERGE = b'merge'

    def __init__(self, config=None):
        """
        Initialize the face client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def face_delete(self, request, config=None):
        """
        face_delete

        :param request: Request entity containing all parameters
        :type request: FaceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing FaceDeleteResponse data
        :rtype: FaceDeleteResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            FaceClient.CONSTANT_REST,
            FaceClient.CONSTANT_2_0,
            FaceClient.CONSTANT_FACE,
            FaceClient.CONSTANT_V3,
            FaceClient.CONSTANT_FACESET,
            FaceClient.CONSTANT_FACE,
            FaceClient.CONSTANT_DELETE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), config=merged_config, model=FaceDeleteResponse
        )

    def face_detect(self, request, config=None):
        """
        face_detect

        :param request: Request entity containing all parameters
        :type request: FaceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing FaceDetectResponse data
        :rtype: FaceDetectResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            FaceClient.CONSTANT_REST,
            FaceClient.CONSTANT_2_0,
            FaceClient.CONSTANT_FACE,
            FaceClient.CONSTANT_V3,
            FaceClient.CONSTANT_DETECT,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), config=merged_config, model=FaceDetectResponse
        )

    def face_edit_attr(self, request, config=None):
        """
        face_edit_attr

        :param request: Request entity containing all parameters
        :type request: FaceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing FaceEditAttrResponse data
        :rtype: FaceEditAttrResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            FaceClient.CONSTANT_REST,
            FaceClient.CONSTANT_2_0,
            FaceClient.CONSTANT_FACE,
            FaceClient.CONSTANT_V1,
            FaceClient.CONSTANT_EDITATTR,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=FaceEditAttrResponse,
        )

    def face_get_list(self, request, config=None):
        """
        face_get_list

        :param request: Request entity containing all parameters
        :type request: FaceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing FaceGetListResponse data
        :rtype: FaceGetListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            FaceClient.CONSTANT_REST,
            FaceClient.CONSTANT_2_0,
            FaceClient.CONSTANT_FACE,
            FaceClient.CONSTANT_V3,
            FaceClient.CONSTANT_FACESET,
            FaceClient.CONSTANT_FACE,
            FaceClient.CONSTANT_GETLIST,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=FaceGetListResponse,
        )

    def face_landmark(self, request, config=None):
        """
        face_landmark

        :param request: Request entity containing all parameters
        :type request: FaceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing FaceLandmarkResponse data
        :rtype: FaceLandmarkResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            FaceClient.CONSTANT_REST,
            FaceClient.CONSTANT_2_0,
            FaceClient.CONSTANT_FACE,
            FaceClient.CONSTANT_V1,
            FaceClient.CONSTANT_LANDMARK,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=FaceLandmarkResponse,
        )

    def face_merge(self, request, config=None):
        """
        face_merge

        :param request: Request entity containing all parameters
        :type request: FaceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing FaceMergeResponse data
        :rtype: FaceMergeResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            FaceClient.CONSTANT_REST,
            FaceClient.CONSTANT_2_0,
            FaceClient.CONSTANT_FACE,
            FaceClient.CONSTANT_V1,
            FaceClient.CONSTANT_MERGE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), config=merged_config, model=FaceMergeResponse
        )

    def face_multi_search(self, request, config=None):
        """
        face_multi_search

        :param request: Request entity containing all parameters
        :type request: FaceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing FaceMultiSearchResponse data
        :rtype: FaceMultiSearchResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            FaceClient.CONSTANT_REST,
            FaceClient.CONSTANT_2_0,
            FaceClient.CONSTANT_FACE,
            FaceClient.CONSTANT_V3,
            FaceClient.CONSTANT_MULTI_SEARCH,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=FaceMultiSearchResponse,
        )

    def face_person_verify(self, request, config=None):
        """
        face_person_verify

        :param request: Request entity containing all parameters
        :type request: FaceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing FacePersonVerifyResponse data
        :rtype: FacePersonVerifyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            FaceClient.CONSTANT_REST,
            FaceClient.CONSTANT_2_0,
            FaceClient.CONSTANT_FACE,
            FaceClient.CONSTANT_V3,
            FaceClient.CONSTANT_PERSON,
            FaceClient.CONSTANT_VERIFY,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=FacePersonVerifyResponse,
        )

    def face_search(self, request, config=None):
        """
        face_search

        :param request: Request entity containing all parameters
        :type request: FaceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing FaceSearchResponse data
        :rtype: FaceSearchResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            FaceClient.CONSTANT_REST,
            FaceClient.CONSTANT_2_0,
            FaceClient.CONSTANT_FACE,
            FaceClient.CONSTANT_V3,
            FaceClient.CONSTANT_SEARCH,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), config=merged_config, model=FaceSearchResponse
        )

    def face_verify(self, config=None):
        """
        face_verify
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing FaceVerifyResponse data
        :rtype: FaceVerifyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            FaceClient.CONSTANT_REST,
            FaceClient.CONSTANT_2_0,
            FaceClient.CONSTANT_FACE,
            FaceClient.CONSTANT_V3,
            FaceClient.CONSTANT_FACEVERIFY,
        )
        headers = None
        return self._send_request(http_methods.POST, path=path, config=config, model=FaceVerifyResponse)

    def face_verify_date(self, request, config=None):
        """
        face_verify_date

        :param request: Request entity containing all parameters
        :type request: FaceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing FaceVerifyDateResponse data
        :rtype: FaceVerifyDateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            FaceClient.CONSTANT_REST,
            FaceClient.CONSTANT_2_0,
            FaceClient.CONSTANT_FACE,
            FaceClient.CONSTANT_V4,
            FaceClient.CONSTANT_VERIFY_DATE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=FaceVerifyDateResponse,
        )

    def group_add(self, request, config=None):
        """
        group_add

        :param request: Request entity containing all parameters
        :type request: FaceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GroupAddResponse data
        :rtype: GroupAddResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            FaceClient.CONSTANT_REST,
            FaceClient.CONSTANT_2_0,
            FaceClient.CONSTANT_FACE,
            FaceClient.CONSTANT_V3,
            FaceClient.CONSTANT_FACESET,
            FaceClient.CONSTANT_GROUP,
            FaceClient.CONSTANT_ADD,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), config=merged_config, model=GroupAddResponse
        )

    def group_delete(self, request, config=None):
        """
        group_delete

        :param request: Request entity containing all parameters
        :type request: FaceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GroupDeleteResponse data
        :rtype: GroupDeleteResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            FaceClient.CONSTANT_REST,
            FaceClient.CONSTANT_2_0,
            FaceClient.CONSTANT_FACE,
            FaceClient.CONSTANT_V3,
            FaceClient.CONSTANT_FACESET,
            FaceClient.CONSTANT_GROUP,
            FaceClient.CONSTANT_DELETE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=GroupDeleteResponse,
        )

    def group_get_list(self, request, config=None):
        """
        group_get_list

        :param request: Request entity containing all parameters
        :type request: FaceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GroupGetListResponse data
        :rtype: GroupGetListResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            FaceClient.CONSTANT_REST,
            FaceClient.CONSTANT_2_0,
            FaceClient.CONSTANT_FACE,
            FaceClient.CONSTANT_V3,
            FaceClient.CONSTANT_FACESET,
            FaceClient.CONSTANT_GROUP,
            FaceClient.CONSTANT_GETLIST,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=GroupGetListResponse,
        )

    def group_get_users(self, request, config=None):
        """
        group_get_users

        :param request: Request entity containing all parameters
        :type request: FaceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GroupGetUsersResponse data
        :rtype: GroupGetUsersResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            FaceClient.CONSTANT_REST,
            FaceClient.CONSTANT_2_0,
            FaceClient.CONSTANT_FACE,
            FaceClient.CONSTANT_V3,
            FaceClient.CONSTANT_FACESET,
            FaceClient.CONSTANT_GROUP,
            FaceClient.CONSTANT_GETUSERS,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=GroupGetUsersResponse,
        )

    def id_match_date(self, request, config=None):
        """
        id_match_date

        :param request: Request entity containing all parameters
        :type request: FaceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing IdMatchDateResponse data
        :rtype: IdMatchDateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            FaceClient.CONSTANT_REST,
            FaceClient.CONSTANT_2_0,
            FaceClient.CONSTANT_FACE,
            FaceClient.CONSTANT_V4,
            FaceClient.CONSTANT_IDMATCH_DATE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=IdMatchDateResponse,
        )

    def id_match_status(self, request, config=None):
        """
        id_match_status

        :param request: Request entity containing all parameters
        :type request: FaceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing IdMatchStatusResponse data
        :rtype: IdMatchStatusResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            FaceClient.CONSTANT_REST,
            FaceClient.CONSTANT_2_0,
            FaceClient.CONSTANT_FACE,
            FaceClient.CONSTANT_V4,
            FaceClient.CONSTANT_IDMATCH_STATUS,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=IdMatchStatusResponse,
        )

    def person_id_match(self, request, config=None):
        """
        person_id_match

        :param request: Request entity containing all parameters
        :type request: FaceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing PersonIdMatchResponse data
        :rtype: PersonIdMatchResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            FaceClient.CONSTANT_REST,
            FaceClient.CONSTANT_2_0,
            FaceClient.CONSTANT_FACE,
            FaceClient.CONSTANT_V3,
            FaceClient.CONSTANT_PERSON,
            FaceClient.CONSTANT_IDMATCH,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=PersonIdMatchResponse,
        )

    def session_code(self, request, config=None):
        """
        session_code

        :param request: Request entity containing all parameters
        :type request: FaceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing SessionCodeResponse data
        :rtype: SessionCodeResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            FaceClient.CONSTANT_REST,
            FaceClient.CONSTANT_2_0,
            FaceClient.CONSTANT_FACE,
            FaceClient.CONSTANT_V1,
            FaceClient.CONSTANT_FACELIVENESS,
            FaceClient.CONSTANT_SESSIONCODE,
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
            model=SessionCodeResponse,
        )

    def user_add(self, request, config=None):
        """
        user_add

        :param request: Request entity containing all parameters
        :type request: FaceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UserAddResponse data
        :rtype: UserAddResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            FaceClient.CONSTANT_REST,
            FaceClient.CONSTANT_2_0,
            FaceClient.CONSTANT_FACE,
            FaceClient.CONSTANT_V3,
            FaceClient.CONSTANT_FACESET,
            FaceClient.CONSTANT_USER,
            FaceClient.CONSTANT_ADD,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), config=merged_config, model=UserAddResponse
        )

    def user_copy(self, request, config=None):
        """
        user_copy

        :param request: Request entity containing all parameters
        :type request: FaceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UserCopyResponse data
        :rtype: UserCopyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            FaceClient.CONSTANT_REST,
            FaceClient.CONSTANT_2_0,
            FaceClient.CONSTANT_FACE,
            FaceClient.CONSTANT_V3,
            FaceClient.CONSTANT_FACESET,
            FaceClient.CONSTANT_USER,
            FaceClient.CONSTANT_COPY,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), config=merged_config, model=UserCopyResponse
        )

    def user_delete(self, request, config=None):
        """
        user_delete

        :param request: Request entity containing all parameters
        :type request: FaceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UserDeleteResponse data
        :rtype: UserDeleteResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            FaceClient.CONSTANT_REST,
            FaceClient.CONSTANT_2_0,
            FaceClient.CONSTANT_FACE,
            FaceClient.CONSTANT_V3,
            FaceClient.CONSTANT_FACESET,
            FaceClient.CONSTANT_USER,
            FaceClient.CONSTANT_DELETE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), config=merged_config, model=UserDeleteResponse
        )

    def user_get(self, request, config=None):
        """
        user_get

        :param request: Request entity containing all parameters
        :type request: FaceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UserGetResponse data
        :rtype: UserGetResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            FaceClient.CONSTANT_REST,
            FaceClient.CONSTANT_2_0,
            FaceClient.CONSTANT_FACE,
            FaceClient.CONSTANT_V3,
            FaceClient.CONSTANT_FACESET,
            FaceClient.CONSTANT_USER,
            FaceClient.CONSTANT_GET,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), config=merged_config, model=UserGetResponse
        )

    def user_update(self, request, config=None):
        """
        user_update

        :param request: Request entity containing all parameters
        :type request: FaceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UserUpdateResponse data
        :rtype: UserUpdateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            FaceClient.CONSTANT_REST,
            FaceClient.CONSTANT_2_0,
            FaceClient.CONSTANT_FACE,
            FaceClient.CONSTANT_V3,
            FaceClient.CONSTANT_FACESET,
            FaceClient.CONSTANT_USER,
            FaceClient.CONSTANT_UPDATE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), config=merged_config, model=UserUpdateResponse
        )

    def verify(self, request, config=None):
        """
        verify

        :param request: Request entity containing all parameters
        :type request: FaceClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing VerifyResponse data
        :rtype: VerifyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            FaceClient.CONSTANT_REST,
            FaceClient.CONSTANT_2_0,
            FaceClient.CONSTANT_FACE,
            FaceClient.CONSTANT_V1,
            FaceClient.CONSTANT_FACELIVENESS,
            FaceClient.CONSTANT_VERIFY,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=form_body, headers=headers, config=merged_config, model=VerifyResponse
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
