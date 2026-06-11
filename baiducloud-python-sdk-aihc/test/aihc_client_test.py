import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_aihc.api.aihc_client import AihcClient
from baiducloud_python_sdk_aihc import models as aihc_models


class AihcClientTest(unittest.TestCase):
    """AihcClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
        self.client = AihcClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_create_a_dataset_v2(self):
        self.client.create_a_dataset_v2(aihc_models.CreateADatasetV2Request())

    def test_create_a_model_v2(self):
        self.client.create_a_model_v2(aihc_models.CreateAModelV2Request())

    def test_create_dataset_version_v2(self):
        self.client.create_dataset_version_v2(aihc_models.CreateDatasetVersionV2Request())

    def test_delete_dataset_v2(self):
        self.client.delete_dataset_v2(aihc_models.DeleteDatasetV2Request())

    def test_delete_dataset_version_v2(self):
        self.client.delete_dataset_version_v2(aihc_models.DeleteDatasetVersionV2Request())

    def test_delete_model_v2(self):
        self.client.delete_model_v2(aihc_models.DeleteModelV2Request())

    def test_delete_model_version_v2(self):
        self.client.delete_model_version_v2(aihc_models.DeleteModelVersionV2Request())

    def test_get_a_list_of_model_versions_v2(self):
        self.client.get_a_list_of_model_versions_v2(aihc_models.GetAListOfModelVersionsV2Request())

    def test_get_dataset_details_v2(self):
        self.client.get_dataset_details_v2(aihc_models.GetDatasetDetailsV2Request())

    def test_get_dataset_version_details_v2(self):
        self.client.get_dataset_version_details_v2(aihc_models.GetDatasetVersionDetailsV2Request())

    def test_get_model_details_v2(self):
        self.client.get_model_details_v2(aihc_models.GetModelDetailsV2Request())

    def test_get_model_list_v2(self):
        self.client.get_model_list_v2(aihc_models.GetModelListV2Request())

    def test_get_model_version_details_v2(self):
        self.client.get_model_version_details_v2(aihc_models.GetModelVersionDetailsV2Request())

    def test_modify_dataset_v2(self):
        self.client.modify_dataset_v2(aihc_models.ModifyDatasetV2Request())

    def test_modify_the_model_v2(self):
        self.client.modify_the_model_v2(aihc_models.ModifyTheModelV2Request())

    def test_new_model_version_v2(self):
        self.client.new_model_version_v2(aihc_models.NewModelVersionV2Request())

    def test_retrieve_the_dataset_list_v2(self):
        self.client.retrieve_the_dataset_list_v2(aihc_models.RetrieveTheDatasetListV2Request())

    def test_retrieve_the_dataset_version_list_v2(self):
        self.client.retrieve_the_dataset_version_list_v2(aihc_models.RetrieveTheDatasetVersionListV2Request())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(AihcClientTest("test_create_a_dataset_v2"))
    suite.addTest(AihcClientTest("test_create_a_model_v2"))
    suite.addTest(AihcClientTest("test_create_dataset_version_v2"))
    suite.addTest(AihcClientTest("test_delete_dataset_v2"))
    suite.addTest(AihcClientTest("test_delete_dataset_version_v2"))
    suite.addTest(AihcClientTest("test_delete_model_v2"))
    suite.addTest(AihcClientTest("test_delete_model_version_v2"))
    suite.addTest(AihcClientTest("test_get_a_list_of_model_versions_v2"))
    suite.addTest(AihcClientTest("test_get_dataset_details_v2"))
    suite.addTest(AihcClientTest("test_get_dataset_version_details_v2"))
    suite.addTest(AihcClientTest("test_get_model_details_v2"))
    suite.addTest(AihcClientTest("test_get_model_list_v2"))
    suite.addTest(AihcClientTest("test_get_model_version_details_v2"))
    suite.addTest(AihcClientTest("test_modify_dataset_v2"))
    suite.addTest(AihcClientTest("test_modify_the_model_v2"))
    suite.addTest(AihcClientTest("test_new_model_version_v2"))
    suite.addTest(AihcClientTest("test_retrieve_the_dataset_list_v2"))
    suite.addTest(AihcClientTest("test_retrieve_the_dataset_version_list_v2"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
