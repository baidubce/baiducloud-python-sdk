import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_bls.api.bls_client import BlsClient
from baiducloud_python_sdk_bls import models as bls_models


class BlsClientTest(unittest.TestCase):
    """BlsClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
        self.client = BlsClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_create_project(self):
        self.client.create_project(bls_models.CreateProjectRequest())

    def test_delete_project(self):
        self.client.delete_project(bls_models.DeleteProjectRequest())

    def test_describe_project(self):
        self.client.describe_project(bls_models.DescribeProjectRequest())

    def test_list_project(self):
        self.client.list_project(bls_models.ListProjectRequest())

    def test_pull_log_record(self):
        self.client.pull_log_record(bls_models.PullLogRecordRequest())

    def test_push_log_record(self):
        self.client.push_log_record(bls_models.PushLogRecordRequest())

    def test_query_log_histogram(self):
        self.client.query_log_histogram(bls_models.QueryLogHistogramRequest())

    def test_query_log_record(self):
        self.client.query_log_record(bls_models.QueryLogRecordRequest())

    def test_update_project(self):
        self.client.update_project(bls_models.UpdateProjectRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(BlsClientTest("test_create_project"))
    suite.addTest(BlsClientTest("test_delete_project"))
    suite.addTest(BlsClientTest("test_describe_project"))
    suite.addTest(BlsClientTest("test_list_project"))
    suite.addTest(BlsClientTest("test_pull_log_record"))
    suite.addTest(BlsClientTest("test_push_log_record"))
    suite.addTest(BlsClientTest("test_query_log_histogram"))
    suite.addTest(BlsClientTest("test_query_log_record"))
    suite.addTest(BlsClientTest("test_update_project"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
