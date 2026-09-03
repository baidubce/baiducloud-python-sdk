import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.auth.api_key_credentials import ApiKeyCredentials
from baiducloud_python_sdk_core.auth.access_token_credentials import AccessTokenCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_image.api.image_client import ImageClient
from baiducloud_python_sdk_image import models as image_models


class ImageClientTest(unittest.TestCase):
    """ImageClient unit test stubs"""

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

        self.client = ImageClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_advanced_general(self):
        self.client.advanced_general(image_models.AdvancedGeneralRequest())

    def test_ai_retouching_create_task(self):
        self.client.ai_retouching_create_task(image_models.AiRetouchingCreateTaskRequest())

    def test_ai_retouching_query_task(self):
        self.client.ai_retouching_query_task(image_models.AiRetouchingQueryTaskRequest())

    def test_animal(self):
        self.client.animal(image_models.AnimalRequest())

    def test_car(self):
        self.client.car(image_models.CarRequest())

    def test_color_enhance(self):
        self.client.color_enhance(image_models.ColorEnhanceRequest())

    def test_colourize(self):
        self.client.colourize(image_models.ColourizeRequest())

    def test_contrast_enhance(self):
        self.client.contrast_enhance(image_models.ContrastEnhanceRequest())

    def test_dehaze(self):
        self.client.dehaze(image_models.DehazeRequest())

    def test_dish(self):
        self.client.dish(image_models.DishRequest())

    def test_doc_repair(self):
        self.client.doc_repair(image_models.DocRepairRequest())

    def test_image_definition_enhance(self):
        self.client.image_definition_enhance(image_models.ImageDefinitionEnhanceRequest())

    def test_image_quality_enhance(self):
        self.client.image_quality_enhance(image_models.ImageQualityEnhanceRequest())

    def test_image_understanding_get_result(self):
        self.client.image_understanding_get_result(image_models.ImageUnderstandingGetResultRequest())

    def test_image_understanding_request(self):
        self.client.image_understanding_request(image_models.ImageUnderstandingRequestRequest())

    def test_ingredient(self):
        self.client.ingredient(image_models.IngredientRequest())

    def test_inpainting(self):
        self.client.inpainting(image_models.InpaintingRequest())

    def test_landmark(self):
        self.client.landmark(image_models.LandmarkRequest())

    def test_logo(self):
        self.client.logo(image_models.LogoRequest())

    def test_logo_add(self):
        self.client.logo_add(image_models.LogoAddRequest())

    def test_logo_delete(self):
        self.client.logo_delete(image_models.LogoDeleteRequest())

    def test_materiel_image_add(self):
        self.client.materiel_image_add(image_models.MaterielImageAddRequest())

    def test_materiel_image_delete(self):
        self.client.materiel_image_delete(image_models.MaterielImageDeleteRequest())

    def test_materiel_image_search(self):
        self.client.materiel_image_search(image_models.MaterielImageSearchRequest())

    def test_materiel_image_update(self):
        self.client.materiel_image_update(image_models.MaterielImageUpdateRequest())

    def test_multi_object_detect(self):
        self.client.multi_object_detect(image_models.MultiObjectDetectRequest())

    def test_object_detect(self):
        self.client.object_detect(image_models.ObjectDetectRequest())

    def test_picturebook_image_add(self):
        self.client.picturebook_image_add(image_models.PicturebookImageAddRequest())

    def test_picturebook_image_delete(self):
        self.client.picturebook_image_delete(image_models.PicturebookImageDeleteRequest())

    def test_picturebook_image_search(self):
        self.client.picturebook_image_search(image_models.PicturebookImageSearchRequest())

    def test_picturebook_image_update(self):
        self.client.picturebook_image_update(image_models.PicturebookImageUpdateRequest())

    def test_plant(self):
        self.client.plant(image_models.PlantRequest())

    def test_product_image_add(self):
        self.client.product_image_add(image_models.ProductImageAddRequest())

    def test_product_image_delete(self):
        self.client.product_image_delete(image_models.ProductImageDeleteRequest())

    def test_product_image_search(self):
        self.client.product_image_search(image_models.ProductImageSearchRequest())

    def test_product_image_update(self):
        self.client.product_image_update(image_models.ProductImageUpdateRequest())

    def test_remove_moire(self):
        self.client.remove_moire(image_models.RemoveMoireRequest())

    def test_same_image_add(self):
        self.client.same_image_add(image_models.SameImageAddRequest())

    def test_same_image_delete(self):
        self.client.same_image_delete(image_models.SameImageDeleteRequest())

    def test_same_image_search(self):
        self.client.same_image_search(image_models.SameImageSearchRequest())

    def test_same_image_update(self):
        self.client.same_image_update(image_models.SameImageUpdateRequest())

    def test_segment(self):
        self.client.segment(image_models.SegmentRequest())

    def test_selfie_anime(self):
        self.client.selfie_anime(image_models.SelfieAnimeRequest())

    def test_similar_image_add(self):
        self.client.similar_image_add(image_models.SimilarImageAddRequest())

    def test_similar_image_delete(self):
        self.client.similar_image_delete(image_models.SimilarImageDeleteRequest())

    def test_similar_image_search(self):
        self.client.similar_image_search(image_models.SimilarImageSearchRequest())

    def test_similar_image_update(self):
        self.client.similar_image_update(image_models.SimilarImageUpdateRequest())

    def test_stretch_restore(self):
        self.client.stretch_restore(image_models.StretchRestoreRequest())

    def test_style_trans(self):
        self.client.style_trans(image_models.StyleTransRequest())

    def test_vehicle_detect(self):
        self.client.vehicle_detect(image_models.VehicleDetectRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ImageClientTest("test_advanced_general"))
    suite.addTest(ImageClientTest("test_ai_retouching_create_task"))
    suite.addTest(ImageClientTest("test_ai_retouching_query_task"))
    suite.addTest(ImageClientTest("test_animal"))
    suite.addTest(ImageClientTest("test_car"))
    suite.addTest(ImageClientTest("test_color_enhance"))
    suite.addTest(ImageClientTest("test_colourize"))
    suite.addTest(ImageClientTest("test_contrast_enhance"))
    suite.addTest(ImageClientTest("test_dehaze"))
    suite.addTest(ImageClientTest("test_dish"))
    suite.addTest(ImageClientTest("test_doc_repair"))
    suite.addTest(ImageClientTest("test_image_definition_enhance"))
    suite.addTest(ImageClientTest("test_image_quality_enhance"))
    suite.addTest(ImageClientTest("test_image_understanding_get_result"))
    suite.addTest(ImageClientTest("test_image_understanding_request"))
    suite.addTest(ImageClientTest("test_ingredient"))
    suite.addTest(ImageClientTest("test_inpainting"))
    suite.addTest(ImageClientTest("test_landmark"))
    suite.addTest(ImageClientTest("test_logo"))
    suite.addTest(ImageClientTest("test_logo_add"))
    suite.addTest(ImageClientTest("test_logo_delete"))
    suite.addTest(ImageClientTest("test_materiel_image_add"))
    suite.addTest(ImageClientTest("test_materiel_image_delete"))
    suite.addTest(ImageClientTest("test_materiel_image_search"))
    suite.addTest(ImageClientTest("test_materiel_image_update"))
    suite.addTest(ImageClientTest("test_multi_object_detect"))
    suite.addTest(ImageClientTest("test_object_detect"))
    suite.addTest(ImageClientTest("test_picturebook_image_add"))
    suite.addTest(ImageClientTest("test_picturebook_image_delete"))
    suite.addTest(ImageClientTest("test_picturebook_image_search"))
    suite.addTest(ImageClientTest("test_picturebook_image_update"))
    suite.addTest(ImageClientTest("test_plant"))
    suite.addTest(ImageClientTest("test_product_image_add"))
    suite.addTest(ImageClientTest("test_product_image_delete"))
    suite.addTest(ImageClientTest("test_product_image_search"))
    suite.addTest(ImageClientTest("test_product_image_update"))
    suite.addTest(ImageClientTest("test_remove_moire"))
    suite.addTest(ImageClientTest("test_same_image_add"))
    suite.addTest(ImageClientTest("test_same_image_delete"))
    suite.addTest(ImageClientTest("test_same_image_search"))
    suite.addTest(ImageClientTest("test_same_image_update"))
    suite.addTest(ImageClientTest("test_segment"))
    suite.addTest(ImageClientTest("test_selfie_anime"))
    suite.addTest(ImageClientTest("test_similar_image_add"))
    suite.addTest(ImageClientTest("test_similar_image_delete"))
    suite.addTest(ImageClientTest("test_similar_image_search"))
    suite.addTest(ImageClientTest("test_similar_image_update"))
    suite.addTest(ImageClientTest("test_stretch_restore"))
    suite.addTest(ImageClientTest("test_style_trans"))
    suite.addTest(ImageClientTest("test_vehicle_detect"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
