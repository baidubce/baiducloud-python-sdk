import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_rapidfs.api.rapidfs_client import RapidfsClient
from baiducloud_python_sdk_rapidfs import models as rapidfs_models


class RapidfsClientTest(unittest.TestCase):
    """RapidfsClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
        self.client = RapidfsClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_add_cache_nodes(self):
        self.client.add_cache_nodes(rapidfs_models.AddCacheNodesRequest())

    def test_cancel_cache_rule_job(self):
        self.client.cancel_cache_rule_job(rapidfs_models.CancelCacheRuleJobRequest())

    def test_cancel_meta_sync_job(self):
        self.client.cancel_meta_sync_job(rapidfs_models.CancelMetaSyncJobRequest())

    def test_check_before_add_cache_nodes(self):
        self.client.check_before_add_cache_nodes(rapidfs_models.CheckBeforeAddCacheNodesRequest())

    def test_check_before_create_instance(self):
        self.client.check_before_create_instance(rapidfs_models.CheckBeforeCreateInstanceRequest())

    def test_create_and_assign_tag(self):
        self.client.create_and_assign_tag(rapidfs_models.CreateAndAssignTagRequest())

    def test_create_auth_group(self):
        self.client.create_auth_group(rapidfs_models.CreateAuthGroupRequest())

    def test_create_cache_rule(self):
        self.client.create_cache_rule(rapidfs_models.CreateCacheRuleRequest())

    def test_create_instance(self):
        self.client.create_instance(rapidfs_models.CreateInstanceRequest())

    def test_create_meta_sync_rule(self):
        self.client.create_meta_sync_rule(rapidfs_models.CreateMetaSyncRuleRequest())

    def test_delete_auth_group(self):
        self.client.delete_auth_group(rapidfs_models.DeleteAuthGroupRequest())

    def test_delete_cache_rule(self):
        self.client.delete_cache_rule(rapidfs_models.DeleteCacheRuleRequest())

    def test_delete_instance(self):
        self.client.delete_instance(rapidfs_models.DeleteInstanceRequest())

    def test_delete_meta_sync_rule(self):
        self.client.delete_meta_sync_rule(rapidfs_models.DeleteMetaSyncRuleRequest())

    def test_describe_aihc_resource_pools(self):
        self.client.describe_aihc_resource_pools(rapidfs_models.DescribeAihcResourcePoolsRequest())

    def test_describe_allocatable_data_src_quota(self):
        self.client.describe_allocatable_data_src_quota(rapidfs_models.DescribeAllocatableDataSrcQuotaRequest())

    def test_describe_auth_group(self):
        self.client.describe_auth_group(rapidfs_models.DescribeAuthGroupRequest())

    def test_describe_auth_groups(self):
        self.client.describe_auth_groups(rapidfs_models.DescribeAuthGroupsRequest())

    def test_describe_cache_deploy_group(self):
        self.client.describe_cache_deploy_group(rapidfs_models.DescribeCacheDeployGroupRequest())

    def test_describe_cache_deploy_groups(self):
        self.client.describe_cache_deploy_groups(rapidfs_models.DescribeCacheDeployGroupsRequest())

    def test_describe_cache_node(self):
        self.client.describe_cache_node(rapidfs_models.DescribeCacheNodeRequest())

    def test_describe_cache_node_bcc_candidates(self):
        self.client.describe_cache_node_bcc_candidates(rapidfs_models.DescribeCacheNodeBccCandidatesRequest())

    def test_describe_cache_node_quota(self):
        self.client.describe_cache_node_quota(rapidfs_models.DescribeCacheNodeQuotaRequest())

    def test_describe_cache_nodes(self):
        self.client.describe_cache_nodes(rapidfs_models.DescribeCacheNodesRequest())

    def test_describe_cache_rule(self):
        self.client.describe_cache_rule(rapidfs_models.DescribeCacheRuleRequest())

    def test_describe_cache_rule_jobs(self):
        self.client.describe_cache_rule_jobs(rapidfs_models.DescribeCacheRuleJobsRequest())

    def test_describe_cache_rules(self):
        self.client.describe_cache_rules(rapidfs_models.DescribeCacheRulesRequest())

    def test_describe_cce_clusters(self):
        self.client.describe_cce_clusters(rapidfs_models.DescribeCceClustersRequest())

    def test_describe_data_src(self):
        self.client.describe_data_src(rapidfs_models.DescribeDataSrcRequest())

    def test_describe_data_srcs(self):
        self.client.describe_data_srcs(rapidfs_models.DescribeDataSrcsRequest())

    def test_describe_instance(self):
        self.client.describe_instance(rapidfs_models.DescribeInstanceRequest())

    def test_describe_instances(self):
        self.client.describe_instances(rapidfs_models.DescribeInstancesRequest())

    def test_describe_meta_sync_jobs(self):
        self.client.describe_meta_sync_jobs(rapidfs_models.DescribeMetaSyncJobsRequest())

    def test_describe_meta_sync_rule(self):
        self.client.describe_meta_sync_rule(rapidfs_models.DescribeMetaSyncRuleRequest())

    def test_describe_meta_sync_rules(self):
        self.client.describe_meta_sync_rules(rapidfs_models.DescribeMetaSyncRulesRequest())

    def test_describe_order(self):
        self.client.describe_order(rapidfs_models.DescribeOrderRequest())

    def test_describe_price(self):
        self.client.describe_price(rapidfs_models.DescribePriceRequest())

    def test_describe_specs(self):
        self.client.describe_specs(rapidfs_models.DescribeSpecsRequest())

    def test_describe_token(self):
        self.client.describe_token(rapidfs_models.DescribeTokenRequest())

    def test_describe_zones(self):
        self.client.describe_zones()

    def test_disable_meta_sync_rule(self):
        self.client.disable_meta_sync_rule(rapidfs_models.DisableMetaSyncRuleRequest())

    def test_enable_meta_sync_rule(self):
        self.client.enable_meta_sync_rule(rapidfs_models.EnableMetaSyncRuleRequest())

    def test_execute_cache_rule_job(self):
        self.client.execute_cache_rule_job(rapidfs_models.ExecuteCacheRuleJobRequest())

    def test_execute_meta_sync_job(self):
        self.client.execute_meta_sync_job(rapidfs_models.ExecuteMetaSyncJobRequest())

    def test_import_data_src(self):
        self.client.import_data_src(rapidfs_models.ImportDataSrcRequest())

    def test_modify_auth_group(self):
        self.client.modify_auth_group(rapidfs_models.ModifyAuthGroupRequest())

    def test_modify_data_src(self):
        self.client.modify_data_src(rapidfs_models.ModifyDataSrcRequest())

    def test_modify_meta_sync_rule(self):
        self.client.modify_meta_sync_rule(rapidfs_models.ModifyMetaSyncRuleRequest())

    def test_modify_token(self):
        self.client.modify_token(rapidfs_models.ModifyTokenRequest())

    def test_remove_cache_nodes(self):
        self.client.remove_cache_nodes(rapidfs_models.RemoveCacheNodesRequest())

    def test_remove_data_src(self):
        self.client.remove_data_src(rapidfs_models.RemoveDataSrcRequest())

    def test_resize_instance(self):
        self.client.resize_instance(rapidfs_models.ResizeInstanceRequest())

    def test_restart_cache_nodes(self):
        self.client.restart_cache_nodes(rapidfs_models.RestartCacheNodesRequest())

    def test_start_cache_nodes(self):
        self.client.start_cache_nodes(rapidfs_models.StartCacheNodesRequest())

    def test_stop_cache_nodes(self):
        self.client.stop_cache_nodes(rapidfs_models.StopCacheNodesRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(RapidfsClientTest("test_add_cache_nodes"))
    suite.addTest(RapidfsClientTest("test_cancel_cache_rule_job"))
    suite.addTest(RapidfsClientTest("test_cancel_meta_sync_job"))
    suite.addTest(RapidfsClientTest("test_check_before_add_cache_nodes"))
    suite.addTest(RapidfsClientTest("test_check_before_create_instance"))
    suite.addTest(RapidfsClientTest("test_create_and_assign_tag"))
    suite.addTest(RapidfsClientTest("test_create_auth_group"))
    suite.addTest(RapidfsClientTest("test_create_cache_rule"))
    suite.addTest(RapidfsClientTest("test_create_instance"))
    suite.addTest(RapidfsClientTest("test_create_meta_sync_rule"))
    suite.addTest(RapidfsClientTest("test_delete_auth_group"))
    suite.addTest(RapidfsClientTest("test_delete_cache_rule"))
    suite.addTest(RapidfsClientTest("test_delete_instance"))
    suite.addTest(RapidfsClientTest("test_delete_meta_sync_rule"))
    suite.addTest(RapidfsClientTest("test_describe_aihc_resource_pools"))
    suite.addTest(RapidfsClientTest("test_describe_allocatable_data_src_quota"))
    suite.addTest(RapidfsClientTest("test_describe_auth_group"))
    suite.addTest(RapidfsClientTest("test_describe_auth_groups"))
    suite.addTest(RapidfsClientTest("test_describe_cache_deploy_group"))
    suite.addTest(RapidfsClientTest("test_describe_cache_deploy_groups"))
    suite.addTest(RapidfsClientTest("test_describe_cache_node"))
    suite.addTest(RapidfsClientTest("test_describe_cache_node_bcc_candidates"))
    suite.addTest(RapidfsClientTest("test_describe_cache_node_quota"))
    suite.addTest(RapidfsClientTest("test_describe_cache_nodes"))
    suite.addTest(RapidfsClientTest("test_describe_cache_rule"))
    suite.addTest(RapidfsClientTest("test_describe_cache_rule_jobs"))
    suite.addTest(RapidfsClientTest("test_describe_cache_rules"))
    suite.addTest(RapidfsClientTest("test_describe_cce_clusters"))
    suite.addTest(RapidfsClientTest("test_describe_data_src"))
    suite.addTest(RapidfsClientTest("test_describe_data_srcs"))
    suite.addTest(RapidfsClientTest("test_describe_instance"))
    suite.addTest(RapidfsClientTest("test_describe_instances"))
    suite.addTest(RapidfsClientTest("test_describe_meta_sync_jobs"))
    suite.addTest(RapidfsClientTest("test_describe_meta_sync_rule"))
    suite.addTest(RapidfsClientTest("test_describe_meta_sync_rules"))
    suite.addTest(RapidfsClientTest("test_describe_order"))
    suite.addTest(RapidfsClientTest("test_describe_price"))
    suite.addTest(RapidfsClientTest("test_describe_specs"))
    suite.addTest(RapidfsClientTest("test_describe_token"))
    suite.addTest(RapidfsClientTest("test_describe_zones"))
    suite.addTest(RapidfsClientTest("test_disable_meta_sync_rule"))
    suite.addTest(RapidfsClientTest("test_enable_meta_sync_rule"))
    suite.addTest(RapidfsClientTest("test_execute_cache_rule_job"))
    suite.addTest(RapidfsClientTest("test_execute_meta_sync_job"))
    suite.addTest(RapidfsClientTest("test_import_data_src"))
    suite.addTest(RapidfsClientTest("test_modify_auth_group"))
    suite.addTest(RapidfsClientTest("test_modify_data_src"))
    suite.addTest(RapidfsClientTest("test_modify_meta_sync_rule"))
    suite.addTest(RapidfsClientTest("test_modify_token"))
    suite.addTest(RapidfsClientTest("test_remove_cache_nodes"))
    suite.addTest(RapidfsClientTest("test_remove_data_src"))
    suite.addTest(RapidfsClientTest("test_resize_instance"))
    suite.addTest(RapidfsClientTest("test_restart_cache_nodes"))
    suite.addTest(RapidfsClientTest("test_start_cache_nodes"))
    suite.addTest(RapidfsClientTest("test_stop_cache_nodes"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
