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

    def test_create_ai_gateway(self):
        self.client.create_ai_gateway(aigw_models.CreateAIGatewayRequest())

    def test_create_consumer(self):
        self.client.create_consumer(aigw_models.CreateConsumerRequest())

    def test_create_route(self):
        self.client.create_route(aigw_models.CreateRouteRequest())

    def test_create_service(self):
        self.client.create_service(aigw_models.CreateServiceRequest())

    def test_delete_ai_gateway(self):
        self.client.delete_ai_gateway(aigw_models.DeleteAiGatewayRequest())

    def test_delete_consumer(self):
        self.client.delete_consumer(aigw_models.DeleteConsumerRequest())

    def test_delete_route(self):
        self.client.delete_route(aigw_models.DeleteRouteRequest())

    def test_delete_service(self):
        self.client.delete_service(aigw_models.DeleteServiceRequest())

    def test_get_ai_gateway_detail(self):
        self.client.get_ai_gateway_detail(aigw_models.GetAiGatewayDetailRequest())

    def test_get_consumer(self):
        self.client.get_consumer(aigw_models.GetConsumerRequest())

    def test_get_consumer_list(self):
        self.client.get_consumer_list(aigw_models.GetConsumerListRequest())

    def test_get_service_detail(self):
        self.client.get_service_detail(aigw_models.GetServiceDetailRequest())

    def test_get_service_list(self):
        self.client.get_service_list(aigw_models.GetServiceListRequest())

    def test_list_ai_gateways(self):
        self.client.list_ai_gateways(aigw_models.ListAiGatewaysRequest())

    def test_list_services_by_source(self):
        self.client.list_services_by_source(aigw_models.ListServicesBySourceRequest())

    def test_query_routing_details(self):
        self.client.query_routing_details(aigw_models.QueryRoutingDetailsRequest())

    def test_query_routing_list(self):
        self.client.query_routing_list(aigw_models.QueryRoutingListRequest())

    def test_update_ai_gateway(self):
        self.client.update_ai_gateway(aigw_models.UpdateAIGatewayRequest())

    def test_update_consumer(self):
        self.client.update_consumer(aigw_models.UpdateConsumerRequest())

    def test_update_route(self):
        self.client.update_route(aigw_models.UpdateRouteRequest())

    def test_update_service(self):
        self.client.update_service(aigw_models.UpdateServiceRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(AigwClientTest("test_create_ai_gateway"))
    suite.addTest(AigwClientTest("test_create_consumer"))
    suite.addTest(AigwClientTest("test_create_route"))
    suite.addTest(AigwClientTest("test_create_service"))
    suite.addTest(AigwClientTest("test_delete_ai_gateway"))
    suite.addTest(AigwClientTest("test_delete_consumer"))
    suite.addTest(AigwClientTest("test_delete_route"))
    suite.addTest(AigwClientTest("test_delete_service"))
    suite.addTest(AigwClientTest("test_get_ai_gateway_detail"))
    suite.addTest(AigwClientTest("test_get_consumer"))
    suite.addTest(AigwClientTest("test_get_consumer_list"))
    suite.addTest(AigwClientTest("test_get_service_detail"))
    suite.addTest(AigwClientTest("test_get_service_list"))
    suite.addTest(AigwClientTest("test_list_ai_gateways"))
    suite.addTest(AigwClientTest("test_list_services_by_source"))
    suite.addTest(AigwClientTest("test_query_routing_details"))
    suite.addTest(AigwClientTest("test_query_routing_list"))
    suite.addTest(AigwClientTest("test_update_ai_gateway"))
    suite.addTest(AigwClientTest("test_update_consumer"))
    suite.addTest(AigwClientTest("test_update_route"))
    suite.addTest(AigwClientTest("test_update_service"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
