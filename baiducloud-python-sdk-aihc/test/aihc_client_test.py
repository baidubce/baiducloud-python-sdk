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

    def test_create_dataset(self):
        self.client.create_dataset(aihc_models.CreateDatasetRequest())

    def test_create_dataset_version(self):
        self.client.create_dataset_version(aihc_models.CreateDatasetVersionRequest())

    def test_create_model(self):
        self.client.create_model(aihc_models.CreateModelRequest())

    def test_create_model_version(self):
        self.client.create_model_version(aihc_models.CreateModelVersionRequest())

    def test_delete_dataset(self):
        self.client.delete_dataset(aihc_models.DeleteDatasetRequest())

    def test_delete_dataset_version(self):
        self.client.delete_dataset_version(aihc_models.DeleteDatasetVersionRequest())

    def test_delete_model(self):
        self.client.delete_model(aihc_models.DeleteModelRequest())

    def test_delete_model_version(self):
        self.client.delete_model_version(aihc_models.DeleteModelVersionRequest())

    def test_describe_dataset(self):
        self.client.describe_dataset(aihc_models.DescribeDatasetRequest())

    def test_describe_dataset_version(self):
        self.client.describe_dataset_version(aihc_models.DescribeDatasetVersionRequest())

    def test_describe_dataset_versions(self):
        self.client.describe_dataset_versions(aihc_models.DescribeDatasetVersionsRequest())

    def test_describe_datasets(self):
        self.client.describe_datasets(aihc_models.DescribeDatasetsRequest())

    def test_describe_model(self):
        self.client.describe_model(aihc_models.DescribeModelRequest())

    def test_describe_model_version(self):
        self.client.describe_model_version(aihc_models.DescribeModelVersionRequest())

    def test_describe_model_versions(self):
        self.client.describe_model_versions(aihc_models.DescribeModelVersionsRequest())

    def test_describe_models(self):
        self.client.describe_models(aihc_models.DescribeModelsRequest())

    def test_modify_dataset(self):
        self.client.modify_dataset(aihc_models.ModifyDatasetRequest())

    def test_modify_model(self):
        self.client.modify_model(aihc_models.ModifyModelRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(AihcClientTest("test_create_dataset"))
    suite.addTest(AihcClientTest("test_create_dataset_version"))
    suite.addTest(AihcClientTest("test_create_model"))
    suite.addTest(AihcClientTest("test_create_model_version"))
    suite.addTest(AihcClientTest("test_delete_dataset"))
    suite.addTest(AihcClientTest("test_delete_dataset_version"))
    suite.addTest(AihcClientTest("test_delete_model"))
    suite.addTest(AihcClientTest("test_delete_model_version"))
    suite.addTest(AihcClientTest("test_describe_dataset"))
    suite.addTest(AihcClientTest("test_describe_dataset_version"))
    suite.addTest(AihcClientTest("test_describe_dataset_versions"))
    suite.addTest(AihcClientTest("test_describe_datasets"))
    suite.addTest(AihcClientTest("test_describe_model"))
    suite.addTest(AihcClientTest("test_describe_model_version"))
    suite.addTest(AihcClientTest("test_describe_model_versions"))
    suite.addTest(AihcClientTest("test_describe_models"))
    suite.addTest(AihcClientTest("test_modify_dataset"))
    suite.addTest(AihcClientTest("test_modify_model"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
