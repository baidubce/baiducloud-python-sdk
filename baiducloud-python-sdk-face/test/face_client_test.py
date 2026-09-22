import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.auth.api_key_credentials import ApiKeyCredentials
from baiducloud_python_sdk_core.auth.access_token_credentials import AccessTokenCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_face.api.face_client import FaceClient
from baiducloud_python_sdk_face import models as face_models


class FaceClientTest(unittest.TestCase):
    """FaceClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        API_KEY = ''
        SECRET_KEY = ''

        # ==== AK/SK 鉴权 ====
        # config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)

        # ==== AccessToken 鉴权（API Key / Secret Key 换取 AccessToken）====
        # config = BceClientConfiguration(credentials=AccessTokenCredentials(API_KEY, SECRET_KEY), endpoint=HOST)

        # ==== API Key 鉴权 ====
        config = BceClientConfiguration(credentials=ApiKeyCredentials(API_KEY), endpoint=HOST)

        self.client = FaceClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_face_delete(self):
        self.client.face_delete(face_models.FaceDeleteRequest())

    def test_face_detect(self):
        self.client.face_detect(face_models.FaceDetectRequest())

    def test_face_edit_attr(self):
        self.client.face_edit_attr(face_models.FaceEditAttrRequest())

    def test_face_get_list(self):
        self.client.face_get_list(face_models.FaceGetListRequest())

    def test_face_landmark(self):
        self.client.face_landmark(face_models.FaceLandmarkRequest())

    def test_face_merge(self):
        self.client.face_merge(face_models.FaceMergeRequest())

    def test_face_multi_search(self):
        self.client.face_multi_search(face_models.FaceMultiSearchRequest())

    def test_face_person_verify(self):
        self.client.face_person_verify(face_models.FacePersonVerifyRequest())

    def test_face_search(self):
        self.client.face_search(face_models.FaceSearchRequest())

    def test_face_verify(self):
        self.client.face_verify()

    def test_face_verify_date(self):
        self.client.face_verify_date(face_models.FaceVerifyDateRequest())

    def test_group_add(self):
        self.client.group_add(face_models.GroupAddRequest())

    def test_group_delete(self):
        self.client.group_delete(face_models.GroupDeleteRequest())

    def test_group_get_list(self):
        self.client.group_get_list(face_models.GroupGetListRequest())

    def test_group_get_users(self):
        self.client.group_get_users(face_models.GroupGetUsersRequest())

    def test_id_match_date(self):
        self.client.id_match_date(face_models.IdMatchDateRequest())

    def test_id_match_status(self):
        self.client.id_match_status(face_models.IdMatchStatusRequest())

    def test_person_id_match(self):
        self.client.person_id_match(face_models.PersonIdMatchRequest())

    def test_session_code(self):
        self.client.session_code(face_models.SessionCodeRequest())

    def test_user_add(self):
        self.client.user_add(face_models.UserAddRequest())

    def test_user_copy(self):
        self.client.user_copy(face_models.UserCopyRequest())

    def test_user_delete(self):
        self.client.user_delete(face_models.UserDeleteRequest())

    def test_user_get(self):
        self.client.user_get(face_models.UserGetRequest())

    def test_user_update(self):
        self.client.user_update(face_models.UserUpdateRequest())

    def test_verify(self):
        self.client.verify(face_models.VerifyRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(FaceClientTest("test_face_delete"))
    suite.addTest(FaceClientTest("test_face_detect"))
    suite.addTest(FaceClientTest("test_face_edit_attr"))
    suite.addTest(FaceClientTest("test_face_get_list"))
    suite.addTest(FaceClientTest("test_face_landmark"))
    suite.addTest(FaceClientTest("test_face_merge"))
    suite.addTest(FaceClientTest("test_face_multi_search"))
    suite.addTest(FaceClientTest("test_face_person_verify"))
    suite.addTest(FaceClientTest("test_face_search"))
    suite.addTest(FaceClientTest("test_face_verify"))
    suite.addTest(FaceClientTest("test_face_verify_date"))
    suite.addTest(FaceClientTest("test_group_add"))
    suite.addTest(FaceClientTest("test_group_delete"))
    suite.addTest(FaceClientTest("test_group_get_list"))
    suite.addTest(FaceClientTest("test_group_get_users"))
    suite.addTest(FaceClientTest("test_id_match_date"))
    suite.addTest(FaceClientTest("test_id_match_status"))
    suite.addTest(FaceClientTest("test_person_id_match"))
    suite.addTest(FaceClientTest("test_session_code"))
    suite.addTest(FaceClientTest("test_user_add"))
    suite.addTest(FaceClientTest("test_user_copy"))
    suite.addTest(FaceClientTest("test_user_delete"))
    suite.addTest(FaceClientTest("test_user_get"))
    suite.addTest(FaceClientTest("test_user_update"))
    suite.addTest(FaceClientTest("test_verify"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
