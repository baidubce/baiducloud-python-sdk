import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_blb.api.blb_client import BlbClient
from baiducloud_python_sdk_blb import models as blb_models


class BlbClientTest(unittest.TestCase):
    """BlbClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
        self.client = BlbClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_add_app_blb_server_group_rs(self):
        self.client.add_app_blb_server_group_rs(blb_models.AddAppBlbServerGroupRsRequest())

    def test_add_blb_server(self):
        self.client.add_blb_server(blb_models.AddBlbServerRequest())

    def test_add_service_auth(self):
        self.client.add_service_auth(blb_models.AddServiceAuthRequest())

    def test_billing_change_cancel_to_post_blb(self):
        self.client.billing_change_cancel_to_post_blb(blb_models.BillingChangeCancelToPostBlbRequest())

    def test_billing_change_post_to_pre_blb(self):
        self.client.billing_change_post_to_pre_blb(blb_models.BillingChangePostToPreBlbRequest())

    def test_billing_change_pre_to_post_blb(self):
        self.client.billing_change_pre_to_post_blb(blb_models.BillingChangePreToPostBlbRequest())

    def test_bind_blb_enterprise_security_group(self):
        self.client.bind_blb_enterprise_security_group(blb_models.BindBlbEnterpriseSecurityGroupRequest())

    def test_bind_blb_security_group(self):
        self.client.bind_blb_security_group(blb_models.BindBlbSecurityGroupRequest())

    def test_bind_instance_to_service(self):
        self.client.bind_instance_to_service(blb_models.BindInstanceToServiceRequest())

    def test_blb_inquiry(self):
        self.client.blb_inquiry(blb_models.BlbInquiryRequest())

    def test_create_app_blb(self):
        self.client.create_app_blb(blb_models.CreateAppBlbRequest())

    def test_create_app_blb_http_listener(self):
        self.client.create_app_blb_http_listener(blb_models.CreateAppBlbHttpListenerRequest())

    def test_create_app_blb_https_listener(self):
        self.client.create_app_blb_https_listener(blb_models.CreateAppBlbHttpsListenerRequest())

    def test_create_app_blb_ip_group(self):
        self.client.create_app_blb_ip_group(blb_models.CreateAppBlbIpGroupRequest())

    def test_create_app_blb_ip_group_member(self):
        self.client.create_app_blb_ip_group_member(blb_models.CreateAppBlbIpGroupMemberRequest())

    def test_create_app_blb_ip_group_protocol(self):
        self.client.create_app_blb_ip_group_protocol(blb_models.CreateAppBlbIpGroupProtocolRequest())

    def test_create_app_blb_policy(self):
        self.client.create_app_blb_policy(blb_models.CreateAppBlbPolicyRequest())

    def test_create_app_blb_server_group(self):
        self.client.create_app_blb_server_group(blb_models.CreateAppBlbServerGroupRequest())

    def test_create_app_blb_server_group_port(self):
        self.client.create_app_blb_server_group_port(blb_models.CreateAppBlbServerGroupPortRequest())

    def test_create_app_blb_ssl_listener(self):
        self.client.create_app_blb_ssl_listener(blb_models.CreateAppBlbSslListenerRequest())

    def test_create_app_blb_tcp_listener(self):
        self.client.create_app_blb_tcp_listener(blb_models.CreateAppBlbTcpListenerRequest())

    def test_create_app_blb_udp_listener(self):
        self.client.create_app_blb_udp_listener(blb_models.CreateAppBlbUdpListenerRequest())

    def test_create_blb(self):
        self.client.create_blb(blb_models.CreateBlbRequest())

    def test_create_blb_http_listener(self):
        self.client.create_blb_http_listener(blb_models.CreateBlbHttpListenerRequest())

    def test_create_blb_https_listener(self):
        self.client.create_blb_https_listener(blb_models.CreateBlbHttpsListenerRequest())

    def test_create_blb_ssl_listener(self):
        self.client.create_blb_ssl_listener(blb_models.CreateBlbSslListenerRequest())

    def test_create_blb_tcp_listener(self):
        self.client.create_blb_tcp_listener(blb_models.CreateBlbTcpListenerRequest())

    def test_create_blb_udp_listener(self):
        self.client.create_blb_udp_listener(blb_models.CreateBlbUdpListenerRequest())

    def test_create_lbdc(self):
        self.client.create_lbdc(blb_models.CreateLbdcRequest())

    def test_create_service(self):
        self.client.create_service(blb_models.CreateServiceRequest())

    def test_delete_app_blb_ip_group(self):
        self.client.delete_app_blb_ip_group(blb_models.DeleteAppBlbIpGroupRequest())

    def test_delete_app_blb_ip_group_member(self):
        self.client.delete_app_blb_ip_group_member(blb_models.DeleteAppBlbIpGroupMemberRequest())

    def test_delete_app_blb_ip_group_protocol(self):
        self.client.delete_app_blb_ip_group_protocol(blb_models.DeleteAppBlbIpGroupProtocolRequest())

    def test_delete_app_blb_listener(self):
        self.client.delete_app_blb_listener(blb_models.DeleteAppBlbListenerRequest())

    def test_delete_app_blb_policy(self):
        self.client.delete_app_blb_policy(blb_models.DeleteAppBlbPolicyRequest())

    def test_delete_app_blb_server_group(self):
        self.client.delete_app_blb_server_group(blb_models.DeleteAppBlbServerGroupRequest())

    def test_delete_app_blb_server_group_port(self):
        self.client.delete_app_blb_server_group_port(blb_models.DeleteAppBlbServerGroupPortRequest())

    def test_delete_app_blb_server_group_rs(self):
        self.client.delete_app_blb_server_group_rs(blb_models.DeleteAppBlbServerGroupRsRequest())

    def test_delete_blb_listener(self):
        self.client.delete_blb_listener(blb_models.DeleteBlbListenerRequest())

    def test_delete_blb_server(self):
        self.client.delete_blb_server(blb_models.DeleteBlbServerRequest())

    def test_delete_service(self):
        self.client.delete_service(blb_models.DeleteServiceRequest())

    def test_delete_service_auth(self):
        self.client.delete_service_auth(blb_models.DeleteServiceAuthRequest())

    def test_describe_app_blb(self):
        self.client.describe_app_blb(blb_models.DescribeAppBlbRequest())

    def test_describe_app_blb_http_listener(self):
        self.client.describe_app_blb_http_listener(blb_models.DescribeAppBlbHttpListenerRequest())

    def test_describe_app_blb_https_listener(self):
        self.client.describe_app_blb_https_listener(blb_models.DescribeAppBlbHttpsListenerRequest())

    def test_describe_app_blb_ip_group(self):
        self.client.describe_app_blb_ip_group(blb_models.DescribeAppBlbIpGroupRequest())

    def test_describe_app_blb_ip_group_member(self):
        self.client.describe_app_blb_ip_group_member(blb_models.DescribeAppBlbIpGroupMemberRequest())

    def test_describe_app_blb_listener(self):
        self.client.describe_app_blb_listener(blb_models.DescribeAppBlbListenerRequest())

    def test_describe_app_blb_policy(self):
        self.client.describe_app_blb_policy(blb_models.DescribeAppBlbPolicyRequest())

    def test_describe_app_blb_server_group(self):
        self.client.describe_app_blb_server_group(blb_models.DescribeAppBlbServerGroupRequest())

    def test_describe_app_blb_server_group_mount_rs(self):
        self.client.describe_app_blb_server_group_mount_rs(blb_models.DescribeAppBlbServerGroupMountRsRequest())

    def test_describe_app_blb_server_group_rs(self):
        self.client.describe_app_blb_server_group_rs(blb_models.DescribeAppBlbServerGroupRsRequest())

    def test_describe_app_blb_server_group_unmount_rs(self):
        self.client.describe_app_blb_server_group_unmount_rs(blb_models.DescribeAppBlbServerGroupUnmountRsRequest())

    def test_describe_app_blb_ssl_listener(self):
        self.client.describe_app_blb_ssl_listener(blb_models.DescribeAppBlbSslListenerRequest())

    def test_describe_app_blb_tcp_listener(self):
        self.client.describe_app_blb_tcp_listener(blb_models.DescribeAppBlbTcpListenerRequest())

    def test_describe_app_blb_udp_listener(self):
        self.client.describe_app_blb_udp_listener(blb_models.DescribeAppBlbUdpListenerRequest())

    def test_describe_app_blbs(self):
        self.client.describe_app_blbs(blb_models.DescribeAppBlbsRequest())

    def test_describe_blb(self):
        self.client.describe_blb(blb_models.DescribeBlbRequest())

    def test_describe_blb_enterprise_security_groups(self):
        self.client.describe_blb_enterprise_security_groups(blb_models.DescribeBlbEnterpriseSecurityGroupsRequest())

    def test_describe_blb_http_listener(self):
        self.client.describe_blb_http_listener(blb_models.DescribeBlbHttpListenerRequest())

    def test_describe_blb_https_listener(self):
        self.client.describe_blb_https_listener(blb_models.DescribeBlbHttpsListenerRequest())

    def test_describe_blb_listener(self):
        self.client.describe_blb_listener(blb_models.DescribeBlbListenerRequest())

    def test_describe_blb_security_groups(self):
        self.client.describe_blb_security_groups(blb_models.DescribeBlbSecurityGroupsRequest())

    def test_describe_blb_server_health(self):
        self.client.describe_blb_server_health(blb_models.DescribeBlbServerHealthRequest())

    def test_describe_blb_servers(self):
        self.client.describe_blb_servers(blb_models.DescribeBlbServersRequest())

    def test_describe_blb_ssl_listener(self):
        self.client.describe_blb_ssl_listener(blb_models.DescribeBlbSslListenerRequest())

    def test_describe_blb_tcp_listener(self):
        self.client.describe_blb_tcp_listener(blb_models.DescribeBlbTcpListenerRequest())

    def test_describe_blb_udp_listener(self):
        self.client.describe_blb_udp_listener(blb_models.DescribeBlbUdpListenerRequest())

    def test_describe_blbs(self):
        self.client.describe_blbs(blb_models.DescribeBlbsRequest())

    def test_describe_lbdc(self):
        self.client.describe_lbdc(blb_models.DescribeLbdcRequest())

    def test_describe_lbdc_blb(self):
        self.client.describe_lbdc_blb(blb_models.DescribeLbdcBlbRequest())

    def test_describe_lbdcs(self):
        self.client.describe_lbdcs(blb_models.DescribeLbdcsRequest())

    def test_describe_service(self):
        self.client.describe_service(blb_models.DescribeServiceRequest())

    def test_describe_services(self):
        self.client.describe_services(blb_models.DescribeServicesRequest())

    def test_refund_blb(self):
        self.client.refund_blb(blb_models.RefundBlbRequest())

    def test_release_app_blb(self):
        self.client.release_app_blb(blb_models.ReleaseAppBlbRequest())

    def test_release_blb(self):
        self.client.release_blb(blb_models.ReleaseBlbRequest())

    def test_renew_lbdc(self):
        self.client.renew_lbdc(blb_models.RenewLbdcRequest())

    def test_resize_blb(self):
        self.client.resize_blb(blb_models.ResizeBlbRequest())

    def test_unbind_blb_enterprise_security_group(self):
        self.client.unbind_blb_enterprise_security_group(blb_models.UnbindBlbEnterpriseSecurityGroupRequest())

    def test_unbind_blb_security_group(self):
        self.client.unbind_blb_security_group(blb_models.UnbindBlbSecurityGroupRequest())

    def test_unbind_instance_from_service(self):
        self.client.unbind_instance_from_service(blb_models.UnbindInstanceFromServiceRequest())

    def test_update_app_blb(self):
        self.client.update_app_blb(blb_models.UpdateAppBlbRequest())

    def test_update_app_blb_http_listener(self):
        self.client.update_app_blb_http_listener(blb_models.UpdateAppBlbHttpListenerRequest())

    def test_update_app_blb_https_listener(self):
        self.client.update_app_blb_https_listener(blb_models.UpdateAppBlbHttpsListenerRequest())

    def test_update_app_blb_ip_group(self):
        self.client.update_app_blb_ip_group(blb_models.UpdateAppBlbIpGroupRequest())

    def test_update_app_blb_ip_group_member(self):
        self.client.update_app_blb_ip_group_member(blb_models.UpdateAppBlbIpGroupMemberRequest())

    def test_update_app_blb_ip_group_protocol(self):
        self.client.update_app_blb_ip_group_protocol(blb_models.UpdateAppBlbIpGroupProtocolRequest())

    def test_update_app_blb_policy(self):
        self.client.update_app_blb_policy(blb_models.UpdateAppBlbPolicyRequest())

    def test_update_app_blb_server_group(self):
        self.client.update_app_blb_server_group(blb_models.UpdateAppBlbServerGroupRequest())

    def test_update_app_blb_server_group_port(self):
        self.client.update_app_blb_server_group_port(blb_models.UpdateAppBlbServerGroupPortRequest())

    def test_update_app_blb_server_group_rs(self):
        self.client.update_app_blb_server_group_rs(blb_models.UpdateAppBlbServerGroupRsRequest())

    def test_update_app_blb_ssl_listener(self):
        self.client.update_app_blb_ssl_listener(blb_models.UpdateAppBlbSslListenerRequest())

    def test_update_app_blb_tcp_listener(self):
        self.client.update_app_blb_tcp_listener(blb_models.UpdateAppBlbTcpListenerRequest())

    def test_update_app_blb_udp_listener(self):
        self.client.update_app_blb_udp_listener(blb_models.UpdateAppBlbUdpListenerRequest())

    def test_update_blb(self):
        self.client.update_blb(blb_models.UpdateBlbRequest())

    def test_update_blb_acl(self):
        self.client.update_blb_acl(blb_models.UpdateBlbAclRequest())

    def test_update_blb_http_listener(self):
        self.client.update_blb_http_listener(blb_models.UpdateBlbHttpListenerRequest())

    def test_update_blb_https_listener(self):
        self.client.update_blb_https_listener(blb_models.UpdateBlbHttpsListenerRequest())

    def test_update_blb_modify_protection(self):
        self.client.update_blb_modify_protection(blb_models.UpdateBlbModifyProtectionRequest())

    def test_update_blb_server(self):
        self.client.update_blb_server(blb_models.UpdateBlbServerRequest())

    def test_update_blb_ssl_listener(self):
        self.client.update_blb_ssl_listener(blb_models.UpdateBlbSslListenerRequest())

    def test_update_blb_tcp_listener(self):
        self.client.update_blb_tcp_listener(blb_models.UpdateBlbTcpListenerRequest())

    def test_update_blb_udp_listener(self):
        self.client.update_blb_udp_listener(blb_models.UpdateBlbUdpListenerRequest())

    def test_update_lbdc(self):
        self.client.update_lbdc(blb_models.UpdateLbdcRequest())

    def test_update_service(self):
        self.client.update_service(blb_models.UpdateServiceRequest())

    def test_update_service_auth(self):
        self.client.update_service_auth(blb_models.UpdateServiceAuthRequest())

    def test_upgrade_lbdc(self):
        self.client.upgrade_lbdc(blb_models.UpgradeLbdcRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(BlbClientTest("test_add_app_blb_server_group_rs"))
    suite.addTest(BlbClientTest("test_add_blb_server"))
    suite.addTest(BlbClientTest("test_add_service_auth"))
    suite.addTest(BlbClientTest("test_billing_change_cancel_to_post_blb"))
    suite.addTest(BlbClientTest("test_billing_change_post_to_pre_blb"))
    suite.addTest(BlbClientTest("test_billing_change_pre_to_post_blb"))
    suite.addTest(BlbClientTest("test_bind_blb_enterprise_security_group"))
    suite.addTest(BlbClientTest("test_bind_blb_security_group"))
    suite.addTest(BlbClientTest("test_bind_instance_to_service"))
    suite.addTest(BlbClientTest("test_blb_inquiry"))
    suite.addTest(BlbClientTest("test_create_app_blb"))
    suite.addTest(BlbClientTest("test_create_app_blb_http_listener"))
    suite.addTest(BlbClientTest("test_create_app_blb_https_listener"))
    suite.addTest(BlbClientTest("test_create_app_blb_ip_group"))
    suite.addTest(BlbClientTest("test_create_app_blb_ip_group_member"))
    suite.addTest(BlbClientTest("test_create_app_blb_ip_group_protocol"))
    suite.addTest(BlbClientTest("test_create_app_blb_policy"))
    suite.addTest(BlbClientTest("test_create_app_blb_server_group"))
    suite.addTest(BlbClientTest("test_create_app_blb_server_group_port"))
    suite.addTest(BlbClientTest("test_create_app_blb_ssl_listener"))
    suite.addTest(BlbClientTest("test_create_app_blb_tcp_listener"))
    suite.addTest(BlbClientTest("test_create_app_blb_udp_listener"))
    suite.addTest(BlbClientTest("test_create_blb"))
    suite.addTest(BlbClientTest("test_create_blb_http_listener"))
    suite.addTest(BlbClientTest("test_create_blb_https_listener"))
    suite.addTest(BlbClientTest("test_create_blb_ssl_listener"))
    suite.addTest(BlbClientTest("test_create_blb_tcp_listener"))
    suite.addTest(BlbClientTest("test_create_blb_udp_listener"))
    suite.addTest(BlbClientTest("test_create_lbdc"))
    suite.addTest(BlbClientTest("test_create_service"))
    suite.addTest(BlbClientTest("test_delete_app_blb_ip_group"))
    suite.addTest(BlbClientTest("test_delete_app_blb_ip_group_member"))
    suite.addTest(BlbClientTest("test_delete_app_blb_ip_group_protocol"))
    suite.addTest(BlbClientTest("test_delete_app_blb_listener"))
    suite.addTest(BlbClientTest("test_delete_app_blb_policy"))
    suite.addTest(BlbClientTest("test_delete_app_blb_server_group"))
    suite.addTest(BlbClientTest("test_delete_app_blb_server_group_port"))
    suite.addTest(BlbClientTest("test_delete_app_blb_server_group_rs"))
    suite.addTest(BlbClientTest("test_delete_blb_listener"))
    suite.addTest(BlbClientTest("test_delete_blb_server"))
    suite.addTest(BlbClientTest("test_delete_service"))
    suite.addTest(BlbClientTest("test_delete_service_auth"))
    suite.addTest(BlbClientTest("test_describe_app_blb"))
    suite.addTest(BlbClientTest("test_describe_app_blb_http_listener"))
    suite.addTest(BlbClientTest("test_describe_app_blb_https_listener"))
    suite.addTest(BlbClientTest("test_describe_app_blb_ip_group"))
    suite.addTest(BlbClientTest("test_describe_app_blb_ip_group_member"))
    suite.addTest(BlbClientTest("test_describe_app_blb_listener"))
    suite.addTest(BlbClientTest("test_describe_app_blb_policy"))
    suite.addTest(BlbClientTest("test_describe_app_blb_server_group"))
    suite.addTest(BlbClientTest("test_describe_app_blb_server_group_mount_rs"))
    suite.addTest(BlbClientTest("test_describe_app_blb_server_group_rs"))
    suite.addTest(BlbClientTest("test_describe_app_blb_server_group_unmount_rs"))
    suite.addTest(BlbClientTest("test_describe_app_blb_ssl_listener"))
    suite.addTest(BlbClientTest("test_describe_app_blb_tcp_listener"))
    suite.addTest(BlbClientTest("test_describe_app_blb_udp_listener"))
    suite.addTest(BlbClientTest("test_describe_app_blbs"))
    suite.addTest(BlbClientTest("test_describe_blb"))
    suite.addTest(BlbClientTest("test_describe_blb_enterprise_security_groups"))
    suite.addTest(BlbClientTest("test_describe_blb_http_listener"))
    suite.addTest(BlbClientTest("test_describe_blb_https_listener"))
    suite.addTest(BlbClientTest("test_describe_blb_listener"))
    suite.addTest(BlbClientTest("test_describe_blb_security_groups"))
    suite.addTest(BlbClientTest("test_describe_blb_server_health"))
    suite.addTest(BlbClientTest("test_describe_blb_servers"))
    suite.addTest(BlbClientTest("test_describe_blb_ssl_listener"))
    suite.addTest(BlbClientTest("test_describe_blb_tcp_listener"))
    suite.addTest(BlbClientTest("test_describe_blb_udp_listener"))
    suite.addTest(BlbClientTest("test_describe_blbs"))
    suite.addTest(BlbClientTest("test_describe_lbdc"))
    suite.addTest(BlbClientTest("test_describe_lbdc_blb"))
    suite.addTest(BlbClientTest("test_describe_lbdcs"))
    suite.addTest(BlbClientTest("test_describe_service"))
    suite.addTest(BlbClientTest("test_describe_services"))
    suite.addTest(BlbClientTest("test_refund_blb"))
    suite.addTest(BlbClientTest("test_release_app_blb"))
    suite.addTest(BlbClientTest("test_release_blb"))
    suite.addTest(BlbClientTest("test_renew_lbdc"))
    suite.addTest(BlbClientTest("test_resize_blb"))
    suite.addTest(BlbClientTest("test_unbind_blb_enterprise_security_group"))
    suite.addTest(BlbClientTest("test_unbind_blb_security_group"))
    suite.addTest(BlbClientTest("test_unbind_instance_from_service"))
    suite.addTest(BlbClientTest("test_update_app_blb"))
    suite.addTest(BlbClientTest("test_update_app_blb_http_listener"))
    suite.addTest(BlbClientTest("test_update_app_blb_https_listener"))
    suite.addTest(BlbClientTest("test_update_app_blb_ip_group"))
    suite.addTest(BlbClientTest("test_update_app_blb_ip_group_member"))
    suite.addTest(BlbClientTest("test_update_app_blb_ip_group_protocol"))
    suite.addTest(BlbClientTest("test_update_app_blb_policy"))
    suite.addTest(BlbClientTest("test_update_app_blb_server_group"))
    suite.addTest(BlbClientTest("test_update_app_blb_server_group_port"))
    suite.addTest(BlbClientTest("test_update_app_blb_server_group_rs"))
    suite.addTest(BlbClientTest("test_update_app_blb_ssl_listener"))
    suite.addTest(BlbClientTest("test_update_app_blb_tcp_listener"))
    suite.addTest(BlbClientTest("test_update_app_blb_udp_listener"))
    suite.addTest(BlbClientTest("test_update_blb"))
    suite.addTest(BlbClientTest("test_update_blb_acl"))
    suite.addTest(BlbClientTest("test_update_blb_http_listener"))
    suite.addTest(BlbClientTest("test_update_blb_https_listener"))
    suite.addTest(BlbClientTest("test_update_blb_modify_protection"))
    suite.addTest(BlbClientTest("test_update_blb_server"))
    suite.addTest(BlbClientTest("test_update_blb_ssl_listener"))
    suite.addTest(BlbClientTest("test_update_blb_tcp_listener"))
    suite.addTest(BlbClientTest("test_update_blb_udp_listener"))
    suite.addTest(BlbClientTest("test_update_lbdc"))
    suite.addTest(BlbClientTest("test_update_service"))
    suite.addTest(BlbClientTest("test_update_service_auth"))
    suite.addTest(BlbClientTest("test_upgrade_lbdc"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
