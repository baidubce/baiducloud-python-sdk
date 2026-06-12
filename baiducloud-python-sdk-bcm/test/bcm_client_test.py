import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_bcm.api.bcm_client import BcmClient
from baiducloud_python_sdk_bcm import models as bcm_models


class BcmClientTest(unittest.TestCase):
    """BcmClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
        self.client = BcmClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_add_alarm_policy_actions(self):
        self.client.add_alarm_policy_actions(bcm_models.AddAlarmPolicyActionsRequest())

    def test_create_alarm_masking(self):
        self.client.create_alarm_masking(bcm_models.CreateAlarmMaskingRequest())

    def test_create_alarm_policy(self):
        self.client.create_alarm_policy(bcm_models.CreateAlarmPolicyRequest())

    def test_delete_alarm_maskings(self):
        self.client.delete_alarm_maskings(bcm_models.DeleteAlarmMaskingsRequest())

    def test_delete_alarm_policies(self):
        self.client.delete_alarm_policies(bcm_models.DeleteAlarmPoliciesRequest())

    def test_delete_alarm_policy_actions(self):
        self.client.delete_alarm_policy_actions(bcm_models.DeleteAlarmPolicyActionsRequest())

    def test_describe_alarm(self):
        self.client.describe_alarm(bcm_models.DescribeAlarmRequest())

    def test_describe_alarm_masking(self):
        self.client.describe_alarm_masking(bcm_models.DescribeAlarmMaskingRequest())

    def test_describe_alarm_maskings(self):
        self.client.describe_alarm_maskings(bcm_models.DescribeAlarmMaskingsRequest())

    def test_describe_alarm_policies(self):
        self.client.describe_alarm_policies(bcm_models.DescribeAlarmPoliciesRequest())

    def test_describe_alarm_policy(self):
        self.client.describe_alarm_policy(bcm_models.DescribeAlarmPolicyRequest())

    def test_describe_alarms(self):
        self.client.describe_alarms(bcm_models.DescribeAlarmsRequest())

    def test_describe_dimension_values(self):
        self.client.describe_dimension_values(bcm_models.DescribeDimensionValuesRequest())

    def test_describe_metric_data(self):
        self.client.describe_metric_data(bcm_models.DescribeMetricDataRequest())

    def test_describe_metric_data_latest(self):
        self.client.describe_metric_data_latest(bcm_models.DescribeMetricDataLatestRequest())

    def test_describe_metric_data_latest_top(self):
        self.client.describe_metric_data_latest_top(bcm_models.DescribeMetricDataLatestTopRequest())

    def test_update_alarm_masking(self):
        self.client.update_alarm_masking(bcm_models.UpdateAlarmMaskingRequest())

    def test_update_alarm_masking_states(self):
        self.client.update_alarm_masking_states(bcm_models.UpdateAlarmMaskingStatesRequest())

    def test_update_alarm_policy(self):
        self.client.update_alarm_policy(bcm_models.UpdateAlarmPolicyRequest())

    def test_update_alarm_policy_notify_enabled(self):
        self.client.update_alarm_policy_notify_enabled(bcm_models.UpdateAlarmPolicyNotifyEnabledRequest())

    def test_update_alarm_policy_state(self):
        self.client.update_alarm_policy_state(bcm_models.UpdateAlarmPolicyStateRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(BcmClientTest("test_add_alarm_policy_actions"))
    suite.addTest(BcmClientTest("test_create_alarm_masking"))
    suite.addTest(BcmClientTest("test_create_alarm_policy"))
    suite.addTest(BcmClientTest("test_delete_alarm_maskings"))
    suite.addTest(BcmClientTest("test_delete_alarm_policies"))
    suite.addTest(BcmClientTest("test_delete_alarm_policy_actions"))
    suite.addTest(BcmClientTest("test_describe_alarm"))
    suite.addTest(BcmClientTest("test_describe_alarm_masking"))
    suite.addTest(BcmClientTest("test_describe_alarm_maskings"))
    suite.addTest(BcmClientTest("test_describe_alarm_policies"))
    suite.addTest(BcmClientTest("test_describe_alarm_policy"))
    suite.addTest(BcmClientTest("test_describe_alarms"))
    suite.addTest(BcmClientTest("test_describe_dimension_values"))
    suite.addTest(BcmClientTest("test_describe_metric_data"))
    suite.addTest(BcmClientTest("test_describe_metric_data_latest"))
    suite.addTest(BcmClientTest("test_describe_metric_data_latest_top"))
    suite.addTest(BcmClientTest("test_update_alarm_masking"))
    suite.addTest(BcmClientTest("test_update_alarm_masking_states"))
    suite.addTest(BcmClientTest("test_update_alarm_policy"))
    suite.addTest(BcmClientTest("test_update_alarm_policy_notify_enabled"))
    suite.addTest(BcmClientTest("test_update_alarm_policy_state"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
