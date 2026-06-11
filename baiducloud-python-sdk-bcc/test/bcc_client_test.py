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

    def test_bind_tag_image(self):
        self.client.bind_tag_image(bcc_models.BindTagImageRequest())

    def test_bind_tag_volume(self):
        self.client.bind_tag_volume(bcc_models.BindTagVolumeRequest())

    def test_cancel_remote_copy_image(self):
        self.client.cancel_remote_copy_image(bcc_models.CancelRemoteCopyImageRequest())

    def test_create_image(self):
        self.client.create_image(bcc_models.CreateImageRequest())

    def test_create_volume(self):
        self.client.create_volume(bcc_models.CreateVolumeRequest())

    def test_delete_image(self):
        self.client.delete_image(bcc_models.DeleteImageRequest())

    def test_detach_volume(self):
        self.client.detach_volume(bcc_models.DetachVolumeRequest())

    def test_get_available_images_by_spec(self):
        self.client.get_available_images_by_spec(bcc_models.GetAvailableImagesBySpecRequest())

    def test_get_cds_price(self):
        self.client.get_cds_price(bcc_models.GetCdsPriceRequest())

    def test_get_disk_quota(self):
        self.client.get_disk_quota(bcc_models.GetDiskQuotaRequest())

    def test_get_image(self):
        self.client.get_image(bcc_models.GetImageRequest())

    def test_get_volume(self):
        self.client.get_volume(bcc_models.GetVolumeRequest())

    def test_get_volume_resize_progress(self):
        self.client.get_volume_resize_progress(bcc_models.GetVolumeResizeProgressRequest())

    def test_import_image(self):
        self.client.import_image(bcc_models.ImportImageRequest())

    def test_list_images(self):
        self.client.list_images(bcc_models.ListImagesRequest())

    def test_list_os(self):
        self.client.list_os(bcc_models.ListOsRequest())

    def test_list_shared_user(self):
        self.client.list_shared_user(bcc_models.ListSharedUserRequest())

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

    def test_remote_copy_image(self):
        self.client.remote_copy_image(bcc_models.RemoteCopyImageRequest())

    def test_rename_image(self):
        self.client.rename_image(bcc_models.RenameImageRequest())

    def test_rename_volume(self):
        self.client.rename_volume(bcc_models.RenameVolumeRequest())

    def test_resize_volume(self):
        self.client.resize_volume(bcc_models.ResizeVolumeRequest())

    def test_rollback_volume(self):
        self.client.rollback_volume(bcc_models.RollbackVolumeRequest())

    def test_share_image(self):
        self.client.share_image(bcc_models.ShareImageRequest())

    def test_un_share_image(self):
        self.client.un_share_image(bcc_models.UnShareImageRequest())

    def test_unbind_tag_image(self):
        self.client.unbind_tag_image(bcc_models.UnbindTagImageRequest())

    def test_unbind_tag_volume(self):
        self.client.unbind_tag_volume(bcc_models.UnbindTagVolumeRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(BccClientTest("test_attach_volume"))
    suite.addTest(BccClientTest("test_bind_tag_image"))
    suite.addTest(BccClientTest("test_bind_tag_volume"))
    suite.addTest(BccClientTest("test_cancel_remote_copy_image"))
    suite.addTest(BccClientTest("test_create_image"))
    suite.addTest(BccClientTest("test_create_volume"))
    suite.addTest(BccClientTest("test_delete_image"))
    suite.addTest(BccClientTest("test_detach_volume"))
    suite.addTest(BccClientTest("test_get_available_images_by_spec"))
    suite.addTest(BccClientTest("test_get_cds_price"))
    suite.addTest(BccClientTest("test_get_disk_quota"))
    suite.addTest(BccClientTest("test_get_image"))
    suite.addTest(BccClientTest("test_get_volume"))
    suite.addTest(BccClientTest("test_get_volume_resize_progress"))
    suite.addTest(BccClientTest("test_import_image"))
    suite.addTest(BccClientTest("test_list_images"))
    suite.addTest(BccClientTest("test_list_os"))
    suite.addTest(BccClientTest("test_list_shared_user"))
    suite.addTest(BccClientTest("test_list_volumes"))
    suite.addTest(BccClientTest("test_modify_cds_attribute"))
    suite.addTest(BccClientTest("test_modify_volume_charge_type"))
    suite.addTest(BccClientTest("test_purchase_reserved_volume"))
    suite.addTest(BccClientTest("test_release_volume"))
    suite.addTest(BccClientTest("test_remote_copy_image"))
    suite.addTest(BccClientTest("test_rename_image"))
    suite.addTest(BccClientTest("test_rename_volume"))
    suite.addTest(BccClientTest("test_resize_volume"))
    suite.addTest(BccClientTest("test_rollback_volume"))
    suite.addTest(BccClientTest("test_share_image"))
    suite.addTest(BccClientTest("test_un_share_image"))
    suite.addTest(BccClientTest("test_unbind_tag_image"))
    suite.addTest(BccClientTest("test_unbind_tag_volume"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
