import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_aigw.api.aigw_client import AigwClient
from baiducloud_python_sdk_aigw import models as aigw_models


class AigwClientTest(unittest.TestCase):
    """AigwClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''

        # ==== AK/SK 鉴权 ====
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)

        self.client = AigwClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_create_route(self):
        self.client.create_route(aigw_models.CreateRouteRequest())

    def test_delete_route(self):
        self.client.delete_route(aigw_models.DeleteRouteRequest())

    def test_query_routing_details(self):
        self.client.query_routing_details(aigw_models.QueryRoutingDetailsRequest())

    def test_query_routing_list(self):
        self.client.query_routing_list(aigw_models.QueryRoutingListRequest())

    def test_update_route(self):
        self.client.update_route(aigw_models.UpdateRouteRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(AigwClientTest("test_create_route"))
    suite.addTest(AigwClientTest("test_delete_route"))
    suite.addTest(AigwClientTest("test_query_routing_details"))
    suite.addTest(AigwClientTest("test_query_routing_list"))
    suite.addTest(AigwClientTest("test_update_route"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
