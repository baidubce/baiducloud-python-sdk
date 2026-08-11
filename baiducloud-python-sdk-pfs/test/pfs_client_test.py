import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_pfs.api.pfs_client import PfsClient
from baiducloud_python_sdk_pfs import models as pfs_models


class PfsClientTest(unittest.TestCase):
    """PfsClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
        self.client = PfsClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_cancel_l2_bucket_link(self):
        self.client.cancel_l2_bucket_link(pfs_models.CancelL2BucketLinkRequest())

    def test_create_fileset(self):
        self.client.create_fileset(pfs_models.CreateFilesetRequest())

    def test_create_l2_bucket_link(self):
        self.client.create_l2_bucket_link(pfs_models.CreateL2BucketLinkRequest())

    def test_create_l2_policy(self):
        self.client.create_l2_policy(pfs_models.CreateL2PolicyRequest())

    def test_create_l3_mount_target(self):
        self.client.create_l3_mount_target(pfs_models.CreateL3MountTargetRequest())

    def test_create_pfs(self):
        self.client.create_pfs(pfs_models.CreatePfsRequest())

    def test_delete_fileset(self):
        self.client.delete_fileset(pfs_models.DeleteFilesetRequest())

    def test_delete_l2_bucket_link(self):
        self.client.delete_l2_bucket_link(pfs_models.DeleteL2BucketLinkRequest())

    def test_delete_l2_policy(self):
        self.client.delete_l2_policy(pfs_models.DeleteL2PolicyRequest())

    def test_delete_l3_mount_target(self):
        self.client.delete_l3_mount_target(pfs_models.DeleteL3MountTargetRequest())

    def test_delete_pfs(self):
        self.client.delete_pfs(pfs_models.DeletePfsRequest())

    def test_desc_fileset(self):
        self.client.desc_fileset(pfs_models.DescFilesetRequest())

    def test_desc_l2_bucket_link(self):
        self.client.desc_l2_bucket_link(pfs_models.DescL2BucketLinkRequest())

    def test_desc_l2_policy(self):
        self.client.desc_l2_policy(pfs_models.DescL2PolicyRequest())

    def test_desc_pfs(self):
        self.client.desc_pfs(pfs_models.DescPfsRequest())

    def test_describe_l3_mount_target(self):
        self.client.describe_l3_mount_target(pfs_models.DescribeL3MountTargetRequest())

    def test_instance_list_clients(self):
        self.client.instance_list_clients(pfs_models.InstanceListClientsRequest())

    def test_list_fileset(self):
        self.client.list_fileset(pfs_models.ListFilesetRequest())

    def test_list_l2_bucket_link(self):
        self.client.list_l2_bucket_link(pfs_models.ListL2BucketLinkRequest())

    def test_list_l2_policy(self):
        self.client.list_l2_policy(pfs_models.ListL2PolicyRequest())

    def test_list_l3_mount_target(self):
        self.client.list_l3_mount_target(pfs_models.ListL3MountTargetRequest())

    def test_list_pfs(self):
        self.client.list_pfs(pfs_models.ListPfsRequest())

    def test_lst_per_l2_bkt_lnk_exec_log(self):
        self.client.lst_per_l2_bkt_lnk_exec_log(pfs_models.LstPerL2BktLnkExecLogRequest())

    def test_mount_target_list_clients(self):
        self.client.mount_target_list_clients(pfs_models.MountTargetListClientsRequest())

    def test_pause_l2_bucket_link(self):
        self.client.pause_l2_bucket_link(pfs_models.PauseL2BucketLinkRequest())

    def test_qry_l2_pol_exec_detail(self):
        self.client.qry_l2_pol_exec_detail(pfs_models.QryL2PolExecDetailRequest())

    def test_qry_l2_pol_exec_log(self):
        self.client.qry_l2_pol_exec_log(pfs_models.QryL2PolExecLogRequest())

    def test_resume_l2_bucket_link(self):
        self.client.resume_l2_bucket_link(pfs_models.ResumeL2BucketLinkRequest())

    def test_upd_per_l2_bkt_lnk_info(self):
        self.client.upd_per_l2_bkt_lnk_info(pfs_models.UpdPerL2BktLnkInfoRequest())

    def test_update_fileset(self):
        self.client.update_fileset(pfs_models.UpdateFilesetRequest())

    def test_update_l2_policy(self):
        self.client.update_l2_policy(pfs_models.UpdateL2PolicyRequest())

    def test_update_pfs_tag(self):
        self.client.update_pfs_tag(pfs_models.UpdatePFSTagRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(PfsClientTest("test_cancel_l2_bucket_link"))
    suite.addTest(PfsClientTest("test_create_fileset"))
    suite.addTest(PfsClientTest("test_create_l2_bucket_link"))
    suite.addTest(PfsClientTest("test_create_l2_policy"))
    suite.addTest(PfsClientTest("test_create_l3_mount_target"))
    suite.addTest(PfsClientTest("test_create_pfs"))
    suite.addTest(PfsClientTest("test_delete_fileset"))
    suite.addTest(PfsClientTest("test_delete_l2_bucket_link"))
    suite.addTest(PfsClientTest("test_delete_l2_policy"))
    suite.addTest(PfsClientTest("test_delete_l3_mount_target"))
    suite.addTest(PfsClientTest("test_delete_pfs"))
    suite.addTest(PfsClientTest("test_desc_fileset"))
    suite.addTest(PfsClientTest("test_desc_l2_bucket_link"))
    suite.addTest(PfsClientTest("test_desc_l2_policy"))
    suite.addTest(PfsClientTest("test_desc_pfs"))
    suite.addTest(PfsClientTest("test_describe_l3_mount_target"))
    suite.addTest(PfsClientTest("test_instance_list_clients"))
    suite.addTest(PfsClientTest("test_list_fileset"))
    suite.addTest(PfsClientTest("test_list_l2_bucket_link"))
    suite.addTest(PfsClientTest("test_list_l2_policy"))
    suite.addTest(PfsClientTest("test_list_l3_mount_target"))
    suite.addTest(PfsClientTest("test_list_pfs"))
    suite.addTest(PfsClientTest("test_lst_per_l2_bkt_lnk_exec_log"))
    suite.addTest(PfsClientTest("test_mount_target_list_clients"))
    suite.addTest(PfsClientTest("test_pause_l2_bucket_link"))
    suite.addTest(PfsClientTest("test_qry_l2_pol_exec_detail"))
    suite.addTest(PfsClientTest("test_qry_l2_pol_exec_log"))
    suite.addTest(PfsClientTest("test_resume_l2_bucket_link"))
    suite.addTest(PfsClientTest("test_upd_per_l2_bkt_lnk_info"))
    suite.addTest(PfsClientTest("test_update_fileset"))
    suite.addTest(PfsClientTest("test_update_l2_policy"))
    suite.addTest(PfsClientTest("test_update_pfs_tag"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
