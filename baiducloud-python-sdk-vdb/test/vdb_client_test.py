import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_vdb.api.vdb_client import VdbClient
from baiducloud_python_sdk_vdb import models as vdb_models


class VdbClientTest(unittest.TestCase):
    """VdbClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''

        # ==== AK/SK 鉴权 ====
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)

        self.client = VdbClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_account_list_using_get(self):
        self.client.account_list_using_get(vdb_models.AccountListUsingGetRequest())

    def test_bind_eip_using_post(self):
        self.client.bind_eip_using_post(vdb_models.BindEipUsingPOSTRequest())

    def test_create_instance_using_post(self):
        self.client.create_instance_using_post(vdb_models.CreateInstanceUsingPostRequest())

    def test_delete_instance_using_delete(self):
        self.client.delete_instance_using_delete(vdb_models.DeleteInstanceUsingDeleteRequest())

    def test_delete_record_using_delete(self):
        self.client.delete_record_using_delete(vdb_models.DeleteRecordUsingDeleteRequest())

    def test_delete_recycler_instance(self):
        self.client.delete_recycler_instance(vdb_models.DeleteRecyclerInstanceRequest())

    def test_describe_instance_configs(self):
        self.client.describe_instance_configs(vdb_models.DescribeInstanceConfigsRequest())

    def test_get_config_using_get(self):
        self.client.get_config_using_get(vdb_models.GetConfigUsingGetRequest())

    def test_get_free_instance_quota(self):
        self.client.get_free_instance_quota()

    def test_get_instance_list_using_get(self):
        self.client.get_instance_list_using_get(vdb_models.GetInstanceListUsingGetRequest())

    def test_get_node_spec_list_using_get(self):
        self.client.get_node_spec_list_using_get(vdb_models.GetNodeSpecListUsingGetRequest())

    def test_get_price_using_post(self):
        self.client.get_price_using_post(vdb_models.GetPriceUsingPostRequest())

    def test_get_quota_using_get(self):
        self.client.get_quota_using_get(vdb_models.GetQuotaUsingGetRequest())

    def test_get_tls_certificate_using_get(self):
        self.client.get_tls_certificate_using_get(vdb_models.GetTlsCertificateUsingGetRequest())

    def test_get_tls_info_using_get(self):
        self.client.get_tls_info_using_get(vdb_models.GetTlsInfoUsingGetRequest())

    def test_getinstancelistusingget1(self):
        self.client.getinstancelistusingget1(vdb_models.Getinstancelistusingget1Request())

    def test_instance_detail_using_get(self):
        self.client.instance_detail_using_get(vdb_models.InstanceDetailUsingGetRequest())

    def test_list_records_using_get(self):
        self.client.list_records_using_get(vdb_models.ListRecordsUsingGetRequest())

    def test_manual_backup_using_post(self):
        self.client.manual_backup_using_post(vdb_models.ManualBackupUsingPOSTRequest())

    def test_modify_instance_config(self):
        self.client.modify_instance_config(vdb_models.ModifyInstanceConfigRequest())

    def test_modify_password_using_post(self):
        self.client.modify_password_using_post(vdb_models.ModifyPasswordUsingPOSTRequest())

    def test_modify_public_access(self):
        self.client.modify_public_access(vdb_models.ModifyPublicAccessRequest())

    def test_modify_tls_using_put(self):
        self.client.modify_tls_using_put(vdb_models.ModifyTLSUsingPUTRequest())

    def test_password_using_get(self):
        self.client.password_using_get(vdb_models.PasswordUsingGetRequest())

    def test_recover_instance_using_post(self):
        self.client.recover_instance_using_post(vdb_models.RecoverInstanceUsingPostRequest())

    def test_recover_using_post(self):
        self.client.recover_using_post(vdb_models.RecoverUsingPOSTRequest())

    def test_resize_instance_using_post(self):
        self.client.resize_instance_using_post(vdb_models.ResizeInstanceUsingPOSTRequest())

    def test_set_comment_using_post(self):
        self.client.set_comment_using_post(vdb_models.SetCommentUsingPOSTRequest())

    def test_set_config_using_post(self):
        self.client.set_config_using_post(vdb_models.SetConfigUsingPOSTRequest())

    def test_unbind_eip_using_post(self):
        self.client.unbind_eip_using_post(vdb_models.UnbindEipUsingPostRequest())

    def test_update_instance_domain(self):
        self.client.update_instance_domain(vdb_models.UpdateInstanceDomainRequest())

    def test_update_instance_name(self):
        self.client.update_instance_name(vdb_models.UpdateInstanceNameRequest())

    def test_zone_list_using_get(self):
        self.client.zone_list_using_get(vdb_models.ZoneListUsingGetRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(VdbClientTest("test_account_list_using_get"))
    suite.addTest(VdbClientTest("test_bind_eip_using_post"))
    suite.addTest(VdbClientTest("test_create_instance_using_post"))
    suite.addTest(VdbClientTest("test_delete_instance_using_delete"))
    suite.addTest(VdbClientTest("test_delete_record_using_delete"))
    suite.addTest(VdbClientTest("test_delete_recycler_instance"))
    suite.addTest(VdbClientTest("test_describe_instance_configs"))
    suite.addTest(VdbClientTest("test_get_config_using_get"))
    suite.addTest(VdbClientTest("test_get_free_instance_quota"))
    suite.addTest(VdbClientTest("test_get_instance_list_using_get"))
    suite.addTest(VdbClientTest("test_get_node_spec_list_using_get"))
    suite.addTest(VdbClientTest("test_get_price_using_post"))
    suite.addTest(VdbClientTest("test_get_quota_using_get"))
    suite.addTest(VdbClientTest("test_get_tls_certificate_using_get"))
    suite.addTest(VdbClientTest("test_get_tls_info_using_get"))
    suite.addTest(VdbClientTest("test_getinstancelistusingget1"))
    suite.addTest(VdbClientTest("test_instance_detail_using_get"))
    suite.addTest(VdbClientTest("test_list_records_using_get"))
    suite.addTest(VdbClientTest("test_manual_backup_using_post"))
    suite.addTest(VdbClientTest("test_modify_instance_config"))
    suite.addTest(VdbClientTest("test_modify_password_using_post"))
    suite.addTest(VdbClientTest("test_modify_public_access"))
    suite.addTest(VdbClientTest("test_modify_tls_using_put"))
    suite.addTest(VdbClientTest("test_password_using_get"))
    suite.addTest(VdbClientTest("test_recover_instance_using_post"))
    suite.addTest(VdbClientTest("test_recover_using_post"))
    suite.addTest(VdbClientTest("test_resize_instance_using_post"))
    suite.addTest(VdbClientTest("test_set_comment_using_post"))
    suite.addTest(VdbClientTest("test_set_config_using_post"))
    suite.addTest(VdbClientTest("test_unbind_eip_using_post"))
    suite.addTest(VdbClientTest("test_update_instance_domain"))
    suite.addTest(VdbClientTest("test_update_instance_name"))
    suite.addTest(VdbClientTest("test_zone_list_using_get"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
