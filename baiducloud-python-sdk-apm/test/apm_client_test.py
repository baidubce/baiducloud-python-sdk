import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_apm.api.apm_client import ApmClient
from baiducloud_python_sdk_apm import models as apm_models


class ApmClientTest(unittest.TestCase):
    """ApmClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
        self.client = ApmClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_apm_create_alarm_policy(self):
        self.client.apm_create_alarm_policy(apm_models.ApmCreateAlarmPolicyRequest())

    def test_apm_delete_alarm_policy(self):
        self.client.apm_delete_alarm_policy(apm_models.ApmDeleteAlarmPolicyRequest())

    def test_apm_describe_alarm(self):
        self.client.apm_describe_alarm(apm_models.ApmDescribeAlarmRequest())

    def test_apm_describe_alarm_policies(self):
        self.client.apm_describe_alarm_policies(apm_models.ApmDescribeAlarmPoliciesRequest())

    def test_apm_describe_alarm_policy(self):
        self.client.apm_describe_alarm_policy(apm_models.ApmDescribeAlarmPolicyRequest())

    def test_apm_describe_alarms(self):
        self.client.apm_describe_alarms(apm_models.ApmDescribeAlarmsRequest())

    def test_apm_update_alarm_policy(self):
        self.client.apm_update_alarm_policy(apm_models.ApmUpdateAlarmPolicyRequest())

    def test_apm_update_alarm_policy_action(self):
        self.client.apm_update_alarm_policy_action(apm_models.ApmUpdateAlarmPolicyActionRequest())

    def test_apm_update_alarm_policy_state(self):
        self.client.apm_update_alarm_policy_state(apm_models.ApmUpdateAlarmPolicyStateRequest())

    def test_bind_service_tag(self):
        self.client.bind_service_tag(apm_models.BindServiceTagRequest())

    def test_delete_services(self):
        self.client.delete_services(apm_models.DeleteServicesRequest())

    def test_describe_db_statement(self):
        self.client.describe_db_statement(apm_models.DescribeDbStatementRequest())

    def test_describe_default_config(self):
        self.client.describe_default_config()

    def test_describe_dimension_values(self):
        self.client.describe_dimension_values(apm_models.DescribeDimensionValuesRequest())

    def test_describe_env(self):
        self.client.describe_env()

    def test_describe_exceptions(self):
        self.client.describe_exceptions(apm_models.DescribeExceptionsRequest())

    def test_describe_llm_dimension_values(self):
        self.client.describe_llm_dimension_values(apm_models.DescribeLLMDimensionValuesRequest())

    def test_describe_llm_metric_data(self):
        self.client.describe_llm_metric_data(apm_models.DescribeLLMMetricDataRequest())

    def test_describe_llm_services(self):
        self.client.describe_llm_services(apm_models.DescribeLLMServicesRequest())

    def test_describe_llm_session(self):
        self.client.describe_llm_session(apm_models.DescribeLLMSessionRequest())

    def test_describe_llm_sessions(self):
        self.client.describe_llm_sessions(apm_models.DescribeLLMSessionsRequest())

    def test_describe_llm_sessions_statistics(self):
        self.client.describe_llm_sessions_statistics(apm_models.DescribeLLMSessionsStatisticsRequest())

    def test_describe_llm_spans(self):
        self.client.describe_llm_spans(apm_models.DescribeLLMSpansRequest())

    def test_describe_llm_trace(self):
        self.client.describe_llm_trace(apm_models.DescribeLLMTraceRequest())

    def test_describe_llm_traces(self):
        self.client.describe_llm_traces(apm_models.DescribeLLMTracesRequest())

    def test_describe_llm_traces_statistics(self):
        self.client.describe_llm_traces_statistics(apm_models.DescribeLLMTracesStatisticsRequest())

    def test_describe_metric_data(self):
        self.client.describe_metric_data(apm_models.DescribeMetricDataRequest())

    def test_describe_retention_limit(self):
        self.client.describe_retention_limit()

    def test_describe_service_config(self):
        self.client.describe_service_config(apm_models.DescribeServiceConfigRequest())

    def test_describe_services_metrics(self):
        self.client.describe_services_metrics(apm_models.DescribeServicesMetricsRequest())

    def test_describe_services_names(self):
        self.client.describe_services_names(apm_models.DescribeServicesNamesRequest())

    def test_describe_span_field_values(self):
        self.client.describe_span_field_values(apm_models.DescribeSpanFieldValuesRequest())

    def test_describe_spans(self):
        self.client.describe_spans(apm_models.DescribeSpansRequest())

    def test_describe_topology(self):
        self.client.describe_topology(apm_models.DescribeTopologyRequest())

    def test_describe_trace(self):
        self.client.describe_trace(apm_models.DescribeTraceRequest())

    def test_describe_trace_metric_data(self):
        self.client.describe_trace_metric_data(apm_models.DescribeTraceMetricDataRequest())

    def test_update_service_config(self):
        self.client.update_service_config(apm_models.UpdateServiceConfigRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ApmClientTest("test_apm_create_alarm_policy"))
    suite.addTest(ApmClientTest("test_apm_delete_alarm_policy"))
    suite.addTest(ApmClientTest("test_apm_describe_alarm"))
    suite.addTest(ApmClientTest("test_apm_describe_alarm_policies"))
    suite.addTest(ApmClientTest("test_apm_describe_alarm_policy"))
    suite.addTest(ApmClientTest("test_apm_describe_alarms"))
    suite.addTest(ApmClientTest("test_apm_update_alarm_policy"))
    suite.addTest(ApmClientTest("test_apm_update_alarm_policy_action"))
    suite.addTest(ApmClientTest("test_apm_update_alarm_policy_state"))
    suite.addTest(ApmClientTest("test_bind_service_tag"))
    suite.addTest(ApmClientTest("test_delete_services"))
    suite.addTest(ApmClientTest("test_describe_db_statement"))
    suite.addTest(ApmClientTest("test_describe_default_config"))
    suite.addTest(ApmClientTest("test_describe_dimension_values"))
    suite.addTest(ApmClientTest("test_describe_env"))
    suite.addTest(ApmClientTest("test_describe_exceptions"))
    suite.addTest(ApmClientTest("test_describe_llm_dimension_values"))
    suite.addTest(ApmClientTest("test_describe_llm_metric_data"))
    suite.addTest(ApmClientTest("test_describe_llm_services"))
    suite.addTest(ApmClientTest("test_describe_llm_session"))
    suite.addTest(ApmClientTest("test_describe_llm_sessions"))
    suite.addTest(ApmClientTest("test_describe_llm_sessions_statistics"))
    suite.addTest(ApmClientTest("test_describe_llm_spans"))
    suite.addTest(ApmClientTest("test_describe_llm_trace"))
    suite.addTest(ApmClientTest("test_describe_llm_traces"))
    suite.addTest(ApmClientTest("test_describe_llm_traces_statistics"))
    suite.addTest(ApmClientTest("test_describe_metric_data"))
    suite.addTest(ApmClientTest("test_describe_retention_limit"))
    suite.addTest(ApmClientTest("test_describe_service_config"))
    suite.addTest(ApmClientTest("test_describe_services_metrics"))
    suite.addTest(ApmClientTest("test_describe_services_names"))
    suite.addTest(ApmClientTest("test_describe_span_field_values"))
    suite.addTest(ApmClientTest("test_describe_spans"))
    suite.addTest(ApmClientTest("test_describe_topology"))
    suite.addTest(ApmClientTest("test_describe_trace"))
    suite.addTest(ApmClientTest("test_describe_trace_metric_data"))
    suite.addTest(ApmClientTest("test_update_service_config"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
