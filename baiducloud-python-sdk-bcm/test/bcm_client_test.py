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

        # ==== AK/SK 鉴权 ====
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

    def test_create_alarm_template(self):
        self.client.create_alarm_template(bcm_models.CreateAlarmTemplateRequest())

    def test_create_instance_group(self):
        self.client.create_instance_group(bcm_models.CreateInstanceGroupRequest())

    def test_create_notify_template(self):
        self.client.create_notify_template(bcm_models.CreateNotifyTemplateRequest())

    def test_delete_alarm_maskings(self):
        self.client.delete_alarm_maskings(bcm_models.DeleteAlarmMaskingsRequest())

    def test_delete_alarm_policies(self):
        self.client.delete_alarm_policies(bcm_models.DeleteAlarmPoliciesRequest())

    def test_delete_alarm_policy_actions(self):
        self.client.delete_alarm_policy_actions(bcm_models.DeleteAlarmPolicyActionsRequest())

    def test_delete_alarm_templates(self):
        self.client.delete_alarm_templates(bcm_models.DeleteAlarmTemplatesRequest())

    def test_delete_instance_group(self):
        self.client.delete_instance_group(bcm_models.DeleteInstanceGroupRequest())

    def test_delete_instance_group_instances(self):
        self.client.delete_instance_group_instances(bcm_models.DeleteInstanceGroupInstancesRequest())

    def test_delete_notify_template(self):
        self.client.delete_notify_template(bcm_models.DeleteNotifyTemplateRequest())

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

    def test_describe_alarm_template(self):
        self.client.describe_alarm_template(bcm_models.DescribeAlarmTemplateRequest())

    def test_describe_alarm_templates(self):
        self.client.describe_alarm_templates(bcm_models.DescribeAlarmTemplatesRequest())

    def test_describe_alarms(self):
        self.client.describe_alarms(bcm_models.DescribeAlarmsRequest())

    def test_describe_dimension_values(self):
        self.client.describe_dimension_values(bcm_models.DescribeDimensionValuesRequest())

    def test_describe_instance_group(self):
        self.client.describe_instance_group(bcm_models.DescribeInstanceGroupRequest())

    def test_describe_instance_groups(self):
        self.client.describe_instance_groups(bcm_models.DescribeInstanceGroupsRequest())

    def test_describe_metric_catalogs(self):
        self.client.describe_metric_catalogs(bcm_models.DescribeMetricCatalogsRequest())

    def test_describe_metric_data(self):
        self.client.describe_metric_data(bcm_models.DescribeMetricDataRequest())

    def test_describe_metric_data_latest(self):
        self.client.describe_metric_data_latest(bcm_models.DescribeMetricDataLatestRequest())

    def test_describe_metric_data_latest_top(self):
        self.client.describe_metric_data_latest_top(bcm_models.DescribeMetricDataLatestTopRequest())

    def test_describe_notify_template(self):
        self.client.describe_notify_template(bcm_models.DescribeNotifyTemplateRequest())

    def test_describe_notify_templates(self):
        self.client.describe_notify_templates(bcm_models.DescribeNotifyTemplatesRequest())

    def test_describe_receivers(self):
        self.client.describe_receivers(bcm_models.DescribeReceiversRequest())

    def test_describe_resource_catalogs(self):
        self.client.describe_resource_catalogs(bcm_models.DescribeResourceCatalogsRequest())

    def test_describe_system_template_rules(self):
        self.client.describe_system_template_rules(bcm_models.DescribeSystemTemplateRulesRequest())

    def test_export_alarm_templates(self):
        self.client.export_alarm_templates(bcm_models.ExportAlarmTemplatesRequest())

    def test_import_alarm_templates(self):
        self.client.import_alarm_templates(bcm_models.ImportAlarmTemplatesRequest())

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

    def test_update_alarm_template(self):
        self.client.update_alarm_template(bcm_models.UpdateAlarmTemplateRequest())

    def test_update_instance_group(self):
        self.client.update_instance_group(bcm_models.UpdateInstanceGroupRequest())

    def test_update_notify_template(self):
        self.client.update_notify_template(bcm_models.UpdateNotifyTemplateRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(BcmClientTest("test_add_alarm_policy_actions"))
    suite.addTest(BcmClientTest("test_create_alarm_masking"))
    suite.addTest(BcmClientTest("test_create_alarm_policy"))
    suite.addTest(BcmClientTest("test_create_alarm_template"))
    suite.addTest(BcmClientTest("test_create_instance_group"))
    suite.addTest(BcmClientTest("test_create_notify_template"))
    suite.addTest(BcmClientTest("test_delete_alarm_maskings"))
    suite.addTest(BcmClientTest("test_delete_alarm_policies"))
    suite.addTest(BcmClientTest("test_delete_alarm_policy_actions"))
    suite.addTest(BcmClientTest("test_delete_alarm_templates"))
    suite.addTest(BcmClientTest("test_delete_instance_group"))
    suite.addTest(BcmClientTest("test_delete_instance_group_instances"))
    suite.addTest(BcmClientTest("test_delete_notify_template"))
    suite.addTest(BcmClientTest("test_describe_alarm"))
    suite.addTest(BcmClientTest("test_describe_alarm_masking"))
    suite.addTest(BcmClientTest("test_describe_alarm_maskings"))
    suite.addTest(BcmClientTest("test_describe_alarm_policies"))
    suite.addTest(BcmClientTest("test_describe_alarm_policy"))
    suite.addTest(BcmClientTest("test_describe_alarm_template"))
    suite.addTest(BcmClientTest("test_describe_alarm_templates"))
    suite.addTest(BcmClientTest("test_describe_alarms"))
    suite.addTest(BcmClientTest("test_describe_dimension_values"))
    suite.addTest(BcmClientTest("test_describe_instance_group"))
    suite.addTest(BcmClientTest("test_describe_instance_groups"))
    suite.addTest(BcmClientTest("test_describe_metric_catalogs"))
    suite.addTest(BcmClientTest("test_describe_metric_data"))
    suite.addTest(BcmClientTest("test_describe_metric_data_latest"))
    suite.addTest(BcmClientTest("test_describe_metric_data_latest_top"))
    suite.addTest(BcmClientTest("test_describe_notify_template"))
    suite.addTest(BcmClientTest("test_describe_notify_templates"))
    suite.addTest(BcmClientTest("test_describe_receivers"))
    suite.addTest(BcmClientTest("test_describe_resource_catalogs"))
    suite.addTest(BcmClientTest("test_describe_system_template_rules"))
    suite.addTest(BcmClientTest("test_export_alarm_templates"))
    suite.addTest(BcmClientTest("test_import_alarm_templates"))
    suite.addTest(BcmClientTest("test_update_alarm_masking"))
    suite.addTest(BcmClientTest("test_update_alarm_masking_states"))
    suite.addTest(BcmClientTest("test_update_alarm_policy"))
    suite.addTest(BcmClientTest("test_update_alarm_policy_notify_enabled"))
    suite.addTest(BcmClientTest("test_update_alarm_policy_state"))
    suite.addTest(BcmClientTest("test_update_alarm_template"))
    suite.addTest(BcmClientTest("test_update_instance_group"))
    suite.addTest(BcmClientTest("test_update_notify_template"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
