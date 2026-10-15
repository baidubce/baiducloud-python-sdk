import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_rds.api.rds_client import RdsClient
from baiducloud_python_sdk_rds import models as rds_models


class RdsClientTest(unittest.TestCase):
    """RdsClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''

        # ==== AK/SK 鉴权 ====
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)

        self.client = RdsClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_create_a_primary_instance(self):
        self.client.create_a_primary_instance(rds_models.CreateAPrimaryInstanceRequest())

    def test_create_a_proxy_instance(self):
        self.client.create_a_proxy_instance(rds_models.CreateAProxyInstanceRequest())

    def test_create_read_only_instance(self):
        self.client.create_read_only_instance(rds_models.CreateReadOnlyInstanceRequest())

    def test_query_task_list(self):
        self.client.query_task_list(rds_models.QueryTaskListRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(RdsClientTest("test_create_a_primary_instance"))
    suite.addTest(RdsClientTest("test_create_a_proxy_instance"))
    suite.addTest(RdsClientTest("test_create_read_only_instance"))
    suite.addTest(RdsClientTest("test_query_task_list"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
