import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_csn.api.csn_client import CsnClient
from baiducloud_python_sdk_csn import models as csn_models


class CsnClientTest(unittest.TestCase):
    """CsnClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
        self.client = CsnClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_add_route_rule(self):
        self.client.add_route_rule(csn_models.AddRouteRuleRequest())

    def test_attach_csn_instance(self):
        self.client.attach_csn_instance(csn_models.AttachCsnInstanceRequest())

    def test_bind_csn_bp(self):
        self.client.bind_csn_bp(csn_models.BindCsnBpRequest())

    def test_create_association_relation(self):
        self.client.create_association_relation(csn_models.CreateAssociationRelationRequest())

    def test_create_csn(self):
        self.client.create_csn(csn_models.CreateCsnRequest())

    def test_create_csn_bp(self):
        self.client.create_csn_bp(csn_models.CreateCsnBpRequest())

    def test_create_region_bandwidth(self):
        self.client.create_region_bandwidth(csn_models.CreateRegionBandwidthRequest())

    def test_create_study_relation(self):
        self.client.create_study_relation(csn_models.CreateStudyRelationRequest())

    def test_delete_association_relation(self):
        self.client.delete_association_relation(csn_models.DeleteAssociationRelationRequest())

    def test_delete_csn(self):
        self.client.delete_csn(csn_models.DeleteCsnRequest())

    def test_delete_csn_bp(self):
        self.client.delete_csn_bp(csn_models.DeleteCsnBpRequest())

    def test_delete_region_bandwidth(self):
        self.client.delete_region_bandwidth(csn_models.DeleteRegionBandwidthRequest())

    def test_delete_route_rule(self):
        self.client.delete_route_rule(csn_models.DeleteRouteRuleRequest())

    def test_delete_study_relation(self):
        self.client.delete_study_relation(csn_models.DeleteStudyRelationRequest())

    def test_detach_csn_instance(self):
        self.client.detach_csn_instance(csn_models.DetachCsnInstanceRequest())

    def test_query_association_relation(self):
        self.client.query_association_relation(csn_models.QueryAssociationRelationRequest())

    def test_query_csn_bp_detail(self):
        self.client.query_csn_bp_detail(csn_models.QueryCsnBpDetailRequest())

    def test_query_csn_bp_list(self):
        self.client.query_csn_bp_list(csn_models.QueryCsnBpListRequest())

    def test_query_csn_bp_price(self):
        self.client.query_csn_bp_price(csn_models.QueryCsnBpPriceRequest())

    def test_query_csn_detail(self):
        self.client.query_csn_detail(csn_models.QueryCsnDetailRequest())

    def test_query_csn_instance(self):
        self.client.query_csn_instance(csn_models.QueryCsnInstanceRequest())

    def test_query_csn_list(self):
        self.client.query_csn_list(csn_models.QueryCsnListRequest())

    def test_query_region_bandwidth(self):
        self.client.query_region_bandwidth(csn_models.QueryRegionBandwidthRequest())

    def test_query_region_bandwidth_by_csn(self):
        self.client.query_region_bandwidth_by_csn(csn_models.QueryRegionBandwidthByCsnRequest())

    def test_query_route_rule(self):
        self.client.query_route_rule(csn_models.QueryRouteRuleRequest())

    def test_query_route_table_list(self):
        self.client.query_route_table_list(csn_models.QueryRouteTableListRequest())

    def test_query_study_relation(self):
        self.client.query_study_relation(csn_models.QueryStudyRelationRequest())

    def test_query_tgw_list(self):
        self.client.query_tgw_list(csn_models.QueryTgwListRequest())

    def test_query_tgw_route(self):
        self.client.query_tgw_route(csn_models.QueryTgwRouteRequest())

    def test_resize_csn_bp(self):
        self.client.resize_csn_bp(csn_models.ResizeCsnBpRequest())

    def test_unbind_csn_bp(self):
        self.client.unbind_csn_bp(csn_models.UnbindCsnBpRequest())

    def test_update_csn(self):
        self.client.update_csn(csn_models.UpdateCsnRequest())

    def test_update_csn_bp(self):
        self.client.update_csn_bp(csn_models.UpdateCsnBpRequest())

    def test_update_region_bandwidth(self):
        self.client.update_region_bandwidth(csn_models.UpdateRegionBandwidthRequest())

    def test_update_tgw(self):
        self.client.update_tgw(csn_models.UpdateTgwRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CsnClientTest("test_add_route_rule"))
    suite.addTest(CsnClientTest("test_attach_csn_instance"))
    suite.addTest(CsnClientTest("test_bind_csn_bp"))
    suite.addTest(CsnClientTest("test_create_association_relation"))
    suite.addTest(CsnClientTest("test_create_csn"))
    suite.addTest(CsnClientTest("test_create_csn_bp"))
    suite.addTest(CsnClientTest("test_create_region_bandwidth"))
    suite.addTest(CsnClientTest("test_create_study_relation"))
    suite.addTest(CsnClientTest("test_delete_association_relation"))
    suite.addTest(CsnClientTest("test_delete_csn"))
    suite.addTest(CsnClientTest("test_delete_csn_bp"))
    suite.addTest(CsnClientTest("test_delete_region_bandwidth"))
    suite.addTest(CsnClientTest("test_delete_route_rule"))
    suite.addTest(CsnClientTest("test_delete_study_relation"))
    suite.addTest(CsnClientTest("test_detach_csn_instance"))
    suite.addTest(CsnClientTest("test_query_association_relation"))
    suite.addTest(CsnClientTest("test_query_csn_bp_detail"))
    suite.addTest(CsnClientTest("test_query_csn_bp_list"))
    suite.addTest(CsnClientTest("test_query_csn_bp_price"))
    suite.addTest(CsnClientTest("test_query_csn_detail"))
    suite.addTest(CsnClientTest("test_query_csn_instance"))
    suite.addTest(CsnClientTest("test_query_csn_list"))
    suite.addTest(CsnClientTest("test_query_region_bandwidth"))
    suite.addTest(CsnClientTest("test_query_region_bandwidth_by_csn"))
    suite.addTest(CsnClientTest("test_query_route_rule"))
    suite.addTest(CsnClientTest("test_query_route_table_list"))
    suite.addTest(CsnClientTest("test_query_study_relation"))
    suite.addTest(CsnClientTest("test_query_tgw_list"))
    suite.addTest(CsnClientTest("test_query_tgw_route"))
    suite.addTest(CsnClientTest("test_resize_csn_bp"))
    suite.addTest(CsnClientTest("test_unbind_csn_bp"))
    suite.addTest(CsnClientTest("test_update_csn"))
    suite.addTest(CsnClientTest("test_update_csn_bp"))
    suite.addTest(CsnClientTest("test_update_region_bandwidth"))
    suite.addTest(CsnClientTest("test_update_tgw"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
