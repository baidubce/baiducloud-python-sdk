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

    def test_async_search(self):
        self.client.async_search(bls_models.AsyncSearchRequest())

    def test_batch_get_log_store(self):
        self.client.batch_get_log_store(bls_models.BatchGetLogStoreRequest())

    def test_bulk_delete_log_shipper(self):
        self.client.bulk_delete_log_shipper(bls_models.BulkDeleteLogShipperRequest())

    def test_bulk_set_log_shipper_status(self):
        self.client.bulk_set_log_shipper_status(bls_models.BulkSetLogShipperStatusRequest())

    def test_create_alarm_policy(self):
        self.client.create_alarm_policy(bls_models.CreateAlarmPolicyRequest())

    def test_create_download_task(self):
        self.client.create_download_task(bls_models.CreateDownloadTaskRequest())

    def test_create_fast_query(self):
        self.client.create_fast_query(bls_models.CreateFastQueryRequest())

    def test_create_index(self):
        self.client.create_index(bls_models.CreateIndexRequest())

    def test_create_log_shipper(self):
        self.client.create_log_shipper(bls_models.CreateLogShipperRequest())

    def test_create_log_store(self):
        self.client.create_log_store(bls_models.CreateLogStoreRequest())

    def test_create_log_store_template(self):
        self.client.create_log_store_template(bls_models.CreateLogStoreTemplateRequest())

    def test_create_log_store_view(self):
        self.client.create_log_store_view(bls_models.CreateLogStoreViewRequest())

    def test_create_project(self):
        self.client.create_project(bls_models.CreateProjectRequest())

    def test_create_task(self):
        self.client.create_task(bls_models.CreateTaskRequest())

    def test_delete_alarm_policy(self):
        self.client.delete_alarm_policy(bls_models.DeleteAlarmPolicyRequest())

    def test_delete_download_task(self):
        self.client.delete_download_task(bls_models.DeleteDownloadTaskRequest())

    def test_delete_fast_query(self):
        self.client.delete_fast_query(bls_models.DeleteFastQueryRequest())

    def test_delete_index(self):
        self.client.delete_index(bls_models.DeleteIndexRequest())

    def test_delete_log_store(self):
        self.client.delete_log_store(bls_models.DeleteLogStoreRequest())

    def test_delete_log_store_templates(self):
        self.client.delete_log_store_templates(bls_models.DeleteLogStoreTemplatesRequest())

    def test_delete_log_store_view(self):
        self.client.delete_log_store_view(bls_models.DeleteLogStoreViewRequest())

    def test_delete_project(self):
        self.client.delete_project(bls_models.DeleteProjectRequest())

    def test_delete_single_log_shipper(self):
        self.client.delete_single_log_shipper(bls_models.DeleteSingleLogShipperRequest())

    def test_describe_alarm_policy(self):
        self.client.describe_alarm_policy(bls_models.DescribeAlarmPolicyRequest())

    def test_describe_alarm_record(self):
        self.client.describe_alarm_record(bls_models.DescribeAlarmRecordRequest())

    def test_describe_download_task(self):
        self.client.describe_download_task(bls_models.DescribeDownloadTaskRequest())

    def test_describe_fast_query(self):
        self.client.describe_fast_query(bls_models.DescribeFastQueryRequest())

    def test_describe_index(self):
        self.client.describe_index(bls_models.DescribeIndexRequest())

    def test_describe_log_store(self):
        self.client.describe_log_store(bls_models.DescribeLogStoreRequest())

    def test_describe_log_store_template(self):
        self.client.describe_log_store_template(bls_models.DescribeLogStoreTemplateRequest())

    def test_describe_log_store_templates(self):
        self.client.describe_log_store_templates(bls_models.DescribeLogStoreTemplatesRequest())

    def test_describe_log_store_view(self):
        self.client.describe_log_store_view(bls_models.DescribeLogStoreViewRequest())

    def test_describe_project(self):
        self.client.describe_project(bls_models.DescribeProjectRequest())

    def test_disable_alarm_policy(self):
        self.client.disable_alarm_policy(bls_models.DisableAlarmPolicyRequest())

    def test_enable_alarm_policy(self):
        self.client.enable_alarm_policy(bls_models.EnableAlarmPolicyRequest())

    def test_field_caps(self):
        self.client.field_caps(bls_models.FieldCapsRequest())

    def test_get_download_task_link(self):
        self.client.get_download_task_link(bls_models.GetDownloadTaskLinkRequest())

    def test_get_log_shipper(self):
        self.client.get_log_shipper(bls_models.GetLogShipperRequest())

    def test_list_alarm_execution_stats(self):
        self.client.list_alarm_execution_stats(bls_models.ListAlarmExecutionStatsRequest())

    def test_list_alarm_executions(self):
        self.client.list_alarm_executions(bls_models.ListAlarmExecutionsRequest())

    def test_list_alarm_policy(self):
        self.client.list_alarm_policy(bls_models.ListAlarmPolicyRequest())

    def test_list_alarm_record(self):
        self.client.list_alarm_record(bls_models.ListAlarmRecordRequest())

    def test_list_download_task(self):
        self.client.list_download_task(bls_models.ListDownloadTaskRequest())

    def test_list_fast_query(self):
        self.client.list_fast_query(bls_models.ListFastQueryRequest())

    def test_list_log_shipper(self):
        self.client.list_log_shipper(bls_models.ListLogShipperRequest())

    def test_list_log_shipper_record(self):
        self.client.list_log_shipper_record(bls_models.ListLogShipperRecordRequest())

    def test_list_log_store(self):
        self.client.list_log_store(bls_models.ListLogStoreRequest())

    def test_list_log_store_view(self):
        self.client.list_log_store_view(bls_models.ListLogStoreViewRequest())

    def test_list_log_stream(self):
        self.client.list_log_stream(bls_models.ListLogStreamRequest())

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

    def test_resolve_index(self):
        self.client.resolve_index(bls_models.ResolveIndexRequest())

    def test_set_single_log_shipper_status(self):
        self.client.set_single_log_shipper_status(bls_models.SetSingleLogShipperStatusRequest())

    def test_terms_enum(self):
        self.client.terms_enum(bls_models.TermsEnumRequest())

    def test_update_alarm_policy(self):
        self.client.update_alarm_policy(bls_models.UpdateAlarmPolicyRequest())

    def test_update_fast_query(self):
        self.client.update_fast_query(bls_models.UpdateFastQueryRequest())

    def test_update_index(self):
        self.client.update_index(bls_models.UpdateIndexRequest())

    def test_update_log_shipper(self):
        self.client.update_log_shipper(bls_models.UpdateLogShipperRequest())

    def test_update_log_store(self):
        self.client.update_log_store(bls_models.UpdateLogStoreRequest())

    def test_update_log_store_template(self):
        self.client.update_log_store_template(bls_models.UpdateLogStoreTemplateRequest())

    def test_update_log_store_view(self):
        self.client.update_log_store_view(bls_models.UpdateLogStoreViewRequest())

    def test_update_project(self):
        self.client.update_project(bls_models.UpdateProjectRequest())

    def test_update_task(self):
        self.client.update_task(bls_models.UpdateTaskRequest())

    def test_validate_alarm_condition(self):
        self.client.validate_alarm_condition(bls_models.ValidateAlarmConditionRequest())

    def test_validate_alarm_policy_sql(self):
        self.client.validate_alarm_policy_sql(bls_models.ValidateAlarmPolicySQLRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(BlsClientTest("test_async_search"))
    suite.addTest(BlsClientTest("test_batch_get_log_store"))
    suite.addTest(BlsClientTest("test_bulk_delete_log_shipper"))
    suite.addTest(BlsClientTest("test_bulk_set_log_shipper_status"))
    suite.addTest(BlsClientTest("test_create_alarm_policy"))
    suite.addTest(BlsClientTest("test_create_download_task"))
    suite.addTest(BlsClientTest("test_create_fast_query"))
    suite.addTest(BlsClientTest("test_create_index"))
    suite.addTest(BlsClientTest("test_create_log_shipper"))
    suite.addTest(BlsClientTest("test_create_log_store"))
    suite.addTest(BlsClientTest("test_create_log_store_template"))
    suite.addTest(BlsClientTest("test_create_log_store_view"))
    suite.addTest(BlsClientTest("test_create_project"))
    suite.addTest(BlsClientTest("test_create_task"))
    suite.addTest(BlsClientTest("test_delete_alarm_policy"))
    suite.addTest(BlsClientTest("test_delete_download_task"))
    suite.addTest(BlsClientTest("test_delete_fast_query"))
    suite.addTest(BlsClientTest("test_delete_index"))
    suite.addTest(BlsClientTest("test_delete_log_store"))
    suite.addTest(BlsClientTest("test_delete_log_store_templates"))
    suite.addTest(BlsClientTest("test_delete_log_store_view"))
    suite.addTest(BlsClientTest("test_delete_project"))
    suite.addTest(BlsClientTest("test_delete_single_log_shipper"))
    suite.addTest(BlsClientTest("test_describe_alarm_policy"))
    suite.addTest(BlsClientTest("test_describe_alarm_record"))
    suite.addTest(BlsClientTest("test_describe_download_task"))
    suite.addTest(BlsClientTest("test_describe_fast_query"))
    suite.addTest(BlsClientTest("test_describe_index"))
    suite.addTest(BlsClientTest("test_describe_log_store"))
    suite.addTest(BlsClientTest("test_describe_log_store_template"))
    suite.addTest(BlsClientTest("test_describe_log_store_templates"))
    suite.addTest(BlsClientTest("test_describe_log_store_view"))
    suite.addTest(BlsClientTest("test_describe_project"))
    suite.addTest(BlsClientTest("test_disable_alarm_policy"))
    suite.addTest(BlsClientTest("test_enable_alarm_policy"))
    suite.addTest(BlsClientTest("test_field_caps"))
    suite.addTest(BlsClientTest("test_get_download_task_link"))
    suite.addTest(BlsClientTest("test_get_log_shipper"))
    suite.addTest(BlsClientTest("test_list_alarm_execution_stats"))
    suite.addTest(BlsClientTest("test_list_alarm_executions"))
    suite.addTest(BlsClientTest("test_list_alarm_policy"))
    suite.addTest(BlsClientTest("test_list_alarm_record"))
    suite.addTest(BlsClientTest("test_list_download_task"))
    suite.addTest(BlsClientTest("test_list_fast_query"))
    suite.addTest(BlsClientTest("test_list_log_shipper"))
    suite.addTest(BlsClientTest("test_list_log_shipper_record"))
    suite.addTest(BlsClientTest("test_list_log_store"))
    suite.addTest(BlsClientTest("test_list_log_store_view"))
    suite.addTest(BlsClientTest("test_list_log_stream"))
    suite.addTest(BlsClientTest("test_list_project"))
    suite.addTest(BlsClientTest("test_pull_log_record"))
    suite.addTest(BlsClientTest("test_push_log_record"))
    suite.addTest(BlsClientTest("test_query_log_histogram"))
    suite.addTest(BlsClientTest("test_query_log_record"))
    suite.addTest(BlsClientTest("test_resolve_index"))
    suite.addTest(BlsClientTest("test_set_single_log_shipper_status"))
    suite.addTest(BlsClientTest("test_terms_enum"))
    suite.addTest(BlsClientTest("test_update_alarm_policy"))
    suite.addTest(BlsClientTest("test_update_fast_query"))
    suite.addTest(BlsClientTest("test_update_index"))
    suite.addTest(BlsClientTest("test_update_log_shipper"))
    suite.addTest(BlsClientTest("test_update_log_store"))
    suite.addTest(BlsClientTest("test_update_log_store_template"))
    suite.addTest(BlsClientTest("test_update_log_store_view"))
    suite.addTest(BlsClientTest("test_update_project"))
    suite.addTest(BlsClientTest("test_update_task"))
    suite.addTest(BlsClientTest("test_validate_alarm_condition"))
    suite.addTest(BlsClientTest("test_validate_alarm_policy_sql"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
