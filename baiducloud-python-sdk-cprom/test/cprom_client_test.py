import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_cprom.api.cprom_client import CpromClient
from baiducloud_python_sdk_cprom import models as cprom_models


class CpromClientTest(unittest.TestCase):
    """CpromClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
        self.client = CpromClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_bind_cluster(self):
        self.client.bind_cluster(cprom_models.BindClusterRequest())

    def test_claim_alert_event(self):
        self.client.claim_alert_event(cprom_models.ClaimAlertEventRequest())

    def test_create_alert(self):
        self.client.create_alert(cprom_models.CreateAlertRequest())

    def test_create_custom_scrape_task(self):
        self.client.create_custom_scrape_task(cprom_models.CreateCustomScrapeTaskRequest())

    def test_create_instance(self):
        self.client.create_instance(cprom_models.CreateInstanceRequest())

    def test_create_notification_policy(self):
        self.client.create_notification_policy(cprom_models.CreateNotificationPolicyRequest())

    def test_create_podmonitor(self):
        self.client.create_podmonitor(cprom_models.CreatePodmonitorRequest())

    def test_create_service_monitor(self):
        self.client.create_service_monitor(cprom_models.CreateServiceMonitorRequest())

    def test_delete_alert(self):
        self.client.delete_alert(cprom_models.DeleteAlertRequest())

    def test_delete_custom_scrape_task(self):
        self.client.delete_custom_scrape_task(cprom_models.DeleteCustomScrapeTaskRequest())

    def test_delete_instance(self):
        self.client.delete_instance(cprom_models.DeleteInstanceRequest())

    def test_delete_notification_policy(self):
        self.client.delete_notification_policy(cprom_models.DeleteNotificationPolicyRequest())

    def test_delete_podmonitor(self):
        self.client.delete_podmonitor(cprom_models.DeletePodmonitorRequest())

    def test_delete_service_monitor(self):
        self.client.delete_service_monitor(cprom_models.DeleteServiceMonitorRequest())

    def test_generate_instance_token(self):
        self.client.generate_instance_token(cprom_models.GenerateInstanceTokenRequest())

    def test_get_alert_detail(self):
        self.client.get_alert_detail(cprom_models.GetAlertDetailRequest())

    def test_get_alert_event_detail(self):
        self.client.get_alert_event_detail(cprom_models.GetAlertEventDetailRequest())

    def test_get_cluster_bind_status(self):
        self.client.get_cluster_bind_status(cprom_models.GetClusterBindStatusRequest())

    def test_get_notification_policy(self):
        self.client.get_notification_policy(cprom_models.GetNotificationPolicyRequest())

    def test_list_alert_events(self):
        self.client.list_alert_events(cprom_models.ListAlertEventsRequest())

    def test_list_alert_templates(self):
        self.client.list_alert_templates()

    def test_list_alerts(self):
        self.client.list_alerts(cprom_models.ListAlertsRequest())

    def test_list_bindable_cloud_products(self):
        self.client.list_bindable_cloud_products()

    def test_list_instances(self):
        self.client.list_instances(cprom_models.ListInstancesRequest())

    def test_list_notification_policies(self):
        self.client.list_notification_policies(cprom_models.ListNotificationPoliciesRequest())

    def test_list_pod_monitors(self):
        self.client.list_pod_monitors(cprom_models.ListPodMonitorsRequest())

    def test_list_related_cloud_products(self):
        self.client.list_related_cloud_products(cprom_models.ListRelatedCloudProductsRequest())

    def test_list_service_monitors(self):
        self.client.list_service_monitors(cprom_models.ListServiceMonitorsRequest())

    def test_remote_read(self):
        self.client.remote_read(cprom_models.RemoteReadRequest())

    def test_remote_write(self):
        self.client.remote_write(cprom_models.RemoteWriteRequest())

    def test_toggle_pod_monitor_service(self):
        self.client.toggle_pod_monitor_service(cprom_models.TogglePodMonitorServiceRequest())

    def test_toggle_service_monitor_service(self):
        self.client.toggle_service_monitor_service(cprom_models.ToggleServiceMonitorServiceRequest())

    def test_update_alert(self):
        self.client.update_alert(cprom_models.UpdateAlertRequest())

    def test_update_notification_policy(self):
        self.client.update_notification_policy(cprom_models.UpdateNotificationPolicyRequest())

    def test_update_pod_monitor(self):
        self.client.update_pod_monitor(cprom_models.UpdatePodMonitorRequest())

    def test_update_related_cloud_products(self):
        self.client.update_related_cloud_products(cprom_models.UpdateRelatedCloudProductsRequest())

    def test_update_service_monitor(self):
        self.client.update_service_monitor(cprom_models.UpdateServiceMonitorRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CpromClientTest("test_bind_cluster"))
    suite.addTest(CpromClientTest("test_claim_alert_event"))
    suite.addTest(CpromClientTest("test_create_alert"))
    suite.addTest(CpromClientTest("test_create_custom_scrape_task"))
    suite.addTest(CpromClientTest("test_create_instance"))
    suite.addTest(CpromClientTest("test_create_notification_policy"))
    suite.addTest(CpromClientTest("test_create_podmonitor"))
    suite.addTest(CpromClientTest("test_create_service_monitor"))
    suite.addTest(CpromClientTest("test_delete_alert"))
    suite.addTest(CpromClientTest("test_delete_custom_scrape_task"))
    suite.addTest(CpromClientTest("test_delete_instance"))
    suite.addTest(CpromClientTest("test_delete_notification_policy"))
    suite.addTest(CpromClientTest("test_delete_podmonitor"))
    suite.addTest(CpromClientTest("test_delete_service_monitor"))
    suite.addTest(CpromClientTest("test_generate_instance_token"))
    suite.addTest(CpromClientTest("test_get_alert_detail"))
    suite.addTest(CpromClientTest("test_get_alert_event_detail"))
    suite.addTest(CpromClientTest("test_get_cluster_bind_status"))
    suite.addTest(CpromClientTest("test_get_notification_policy"))
    suite.addTest(CpromClientTest("test_list_alert_events"))
    suite.addTest(CpromClientTest("test_list_alert_templates"))
    suite.addTest(CpromClientTest("test_list_alerts"))
    suite.addTest(CpromClientTest("test_list_bindable_cloud_products"))
    suite.addTest(CpromClientTest("test_list_instances"))
    suite.addTest(CpromClientTest("test_list_notification_policies"))
    suite.addTest(CpromClientTest("test_list_pod_monitors"))
    suite.addTest(CpromClientTest("test_list_related_cloud_products"))
    suite.addTest(CpromClientTest("test_list_service_monitors"))
    suite.addTest(CpromClientTest("test_remote_read"))
    suite.addTest(CpromClientTest("test_remote_write"))
    suite.addTest(CpromClientTest("test_toggle_pod_monitor_service"))
    suite.addTest(CpromClientTest("test_toggle_service_monitor_service"))
    suite.addTest(CpromClientTest("test_update_alert"))
    suite.addTest(CpromClientTest("test_update_notification_policy"))
    suite.addTest(CpromClientTest("test_update_pod_monitor"))
    suite.addTest(CpromClientTest("test_update_related_cloud_products"))
    suite.addTest(CpromClientTest("test_update_service_monitor"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
