import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_bcc.api.bcc_client import BccClient
from baiducloud_python_sdk_bcc import models as bcc_models


class BccClientTest(unittest.TestCase):
    """BccClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
        self.client = BccClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_attach_volume(self):
        self.client.attach_volume(bcc_models.AttachVolumeRequest())

    def test_bind_tag_volume(self):
        self.client.bind_tag_volume(bcc_models.BindTagVolumeRequest())

    def test_create_volume(self):
        self.client.create_volume(bcc_models.CreateVolumeRequest())

    def test_detach_volume(self):
        self.client.detach_volume(bcc_models.DetachVolumeRequest())

    def test_get_cds_price(self):
        self.client.get_cds_price(bcc_models.GetCdsPriceRequest())

    def test_get_disk_quota(self):
        self.client.get_disk_quota(bcc_models.GetDiskQuotaRequest())

    def test_get_volume(self):
        self.client.get_volume(bcc_models.GetVolumeRequest())

    def test_get_volume_resize_progress(self):
        self.client.get_volume_resize_progress(bcc_models.GetVolumeResizeProgressRequest())

    def test_list_volumes(self):
        self.client.list_volumes(bcc_models.ListVolumesRequest())

    def test_modify_cds_attribute(self):
        self.client.modify_cds_attribute(bcc_models.ModifyCdsAttributeRequest())

    def test_modify_volume_charge_type(self):
        self.client.modify_volume_charge_type(bcc_models.ModifyVolumeChargeTypeRequest())

    def test_purchase_reserved_volume(self):
        self.client.purchase_reserved_volume(bcc_models.PurchaseReservedVolumeRequest())

    def test_release_volume(self):
        self.client.release_volume(bcc_models.ReleaseVolumeRequest())

    def test_rename_volume(self):
        self.client.rename_volume(bcc_models.RenameVolumeRequest())

    def test_resize_volume(self):
        self.client.resize_volume(bcc_models.ResizeVolumeRequest())

    def test_rollback_volume(self):
        self.client.rollback_volume(bcc_models.RollbackVolumeRequest())

    def test_unbind_tag_volume(self):
        self.client.unbind_tag_volume(bcc_models.UnbindTagVolumeRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(BccClientTest("test_attach_volume"))
    suite.addTest(BccClientTest("test_bind_tag_volume"))
    suite.addTest(BccClientTest("test_create_volume"))
    suite.addTest(BccClientTest("test_detach_volume"))
    suite.addTest(BccClientTest("test_get_cds_price"))
    suite.addTest(BccClientTest("test_get_disk_quota"))
    suite.addTest(BccClientTest("test_get_volume"))
    suite.addTest(BccClientTest("test_get_volume_resize_progress"))
    suite.addTest(BccClientTest("test_list_volumes"))
    suite.addTest(BccClientTest("test_modify_cds_attribute"))
    suite.addTest(BccClientTest("test_modify_volume_charge_type"))
    suite.addTest(BccClientTest("test_purchase_reserved_volume"))
    suite.addTest(BccClientTest("test_release_volume"))
    suite.addTest(BccClientTest("test_rename_volume"))
    suite.addTest(BccClientTest("test_resize_volume"))
    suite.addTest(BccClientTest("test_rollback_volume"))
    suite.addTest(BccClientTest("test_unbind_tag_volume"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
