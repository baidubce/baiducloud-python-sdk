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

    def test_accept_reserved_instance_transfer(self):
        self.client.accept_reserved_instance_transfer(bcc_models.AcceptReservedInstanceTransferRequest())

    def test_add_ipv6(self):
        self.client.add_ipv6(bcc_models.AddIpv6Request())

    def test_attach_asp(self):
        self.client.attach_asp(bcc_models.AttachAspRequest())

    def test_attach_keypair(self):
        self.client.attach_keypair(bcc_models.AttachKeypairRequest())

    def test_attach_volume(self):
        self.client.attach_volume(bcc_models.AttachVolumeRequest())

    def test_authorize_security_group_rule(self):
        self.client.authorize_security_group_rule(bcc_models.AuthorizeSecurityGroupRuleRequest())

    def test_authorize_server_event(self):
        self.client.authorize_server_event(bcc_models.AuthorizeServerEventRequest())

    def test_auto_release_instance(self):
        self.client.auto_release_instance(bcc_models.AutoReleaseInstanceRequest())

    def test_auto_renew_reserved_instance(self):
        self.client.auto_renew_reserved_instance(bcc_models.AutoRenewReservedInstanceRequest())

    def test_auto_renew_volume_cluster(self):
        self.client.auto_renew_volume_cluster(bcc_models.AutoRenewVolumeClusterRequest())

    def test_batch_add_ip(self):
        self.client.batch_add_ip(bcc_models.BatchAddIpRequest())

    def test_batch_change_to_postpaid(self):
        self.client.batch_change_to_postpaid(bcc_models.BatchChangeToPostpaidRequest())

    def test_batch_change_to_prepaid(self):
        self.client.batch_change_to_prepaid(bcc_models.BatchChangeToPrepaidRequest())

    def test_batch_delete_ip(self):
        self.client.batch_delete_ip(bcc_models.BatchDeleteIpRequest())

    def test_batch_refund_resource(self):
        self.client.batch_refund_resource(bcc_models.BatchRefundResourceRequest())

    def test_batch_start_instance(self):
        self.client.batch_start_instance(bcc_models.BatchStartInstanceRequest())

    def test_batch_stop_instance(self):
        self.client.batch_stop_instance(bcc_models.BatchStopInstanceRequest())

    def test_bind_instance_security_group(self):
        self.client.bind_instance_security_group(bcc_models.BindInstanceSecurityGroupRequest())

    def test_bind_instance_to_security_group(self):
        self.client.bind_instance_to_security_group(bcc_models.BindInstanceToSecurityGroupRequest())

    def test_bind_instance_to_tags(self):
        self.client.bind_instance_to_tags(bcc_models.BindInstanceToTagsRequest())

    def test_bind_reserved_instance_to_tags(self):
        self.client.bind_reserved_instance_to_tags(bcc_models.BindReservedInstanceToTagsRequest())

    def test_bind_role(self):
        self.client.bind_role(bcc_models.BindRoleRequest())

    def test_bind_tag_image(self):
        self.client.bind_tag_image(bcc_models.BindTagImageRequest())

    def test_bind_tag_snapchain(self):
        self.client.bind_tag_snapchain(bcc_models.BindTagSnapchainRequest())

    def test_bind_tag_volume(self):
        self.client.bind_tag_volume(bcc_models.BindTagVolumeRequest())

    def test_bind_tag_volume_cluster(self):
        self.client.bind_tag_volume_cluster(bcc_models.BindTagVolumeClusterRequest())

    def test_cancel_auto_renew_reserved_instance(self):
        self.client.cancel_auto_renew_reserved_instance(bcc_models.CancelAutoRenewReservedInstanceRequest())

    def test_cancel_auto_renew_volume_cluster(self):
        self.client.cancel_auto_renew_volume_cluster(bcc_models.CancelAutoRenewVolumeClusterRequest())

    def test_cancel_bid_order(self):
        self.client.cancel_bid_order(bcc_models.CancelBidOrderRequest())

    def test_cancel_remote_copy_image(self):
        self.client.cancel_remote_copy_image(bcc_models.CancelRemoteCopyImageRequest())

    def test_cancel_snapshot_share(self):
        self.client.cancel_snapshot_share(bcc_models.CancelSnapshotShareRequest())

    def test_change_to_prepaid(self):
        self.client.change_to_prepaid(bcc_models.ChangeToPrepaidRequest())

    def test_change_vpc(self):
        self.client.change_vpc(bcc_models.ChangeVpcRequest())

    def test_check_server_event(self):
        self.client.check_server_event(bcc_models.CheckServerEventRequest())

    def test_create_asp(self):
        self.client.create_asp(bcc_models.CreateAspRequest())

    def test_create_authorization_rule(self):
        self.client.create_authorization_rule(bcc_models.CreateAuthorizationRuleRequest())

    def test_create_auto_renew_rule(self):
        self.client.create_auto_renew_rule(bcc_models.CreateAutoRenewRuleRequest())

    def test_create_bid_instance(self):
        self.client.create_bid_instance(bcc_models.CreateBidInstanceRequest())

    def test_create_deploy_set(self):
        self.client.create_deploy_set(bcc_models.CreateDeploySetRequest())

    def test_create_ehc_cluster(self):
        self.client.create_ehc_cluster(bcc_models.CreateEhcClusterRequest())

    def test_create_image(self):
        self.client.create_image(bcc_models.CreateImageRequest())

    def test_create_instance_by_spec(self):
        self.client.create_instance_by_spec(bcc_models.CreateInstanceBySpecRequest())

    def test_create_keypair(self):
        self.client.create_keypair(bcc_models.CreateKeypairRequest())

    def test_create_reserved_instance_transfer(self):
        self.client.create_reserved_instance_transfer(bcc_models.CreateReservedInstanceTransferRequest())

    def test_create_reserved_instances(self):
        self.client.create_reserved_instances(bcc_models.CreateReservedInstancesRequest())

    def test_create_security_group(self):
        self.client.create_security_group(bcc_models.CreateSecurityGroupRequest())

    def test_create_snapshot(self):
        self.client.create_snapshot(bcc_models.CreateSnapshotRequest())

    def test_create_snapshot_share(self):
        self.client.create_snapshot_share(bcc_models.CreateSnapshotShareRequest())

    def test_create_volume(self):
        self.client.create_volume(bcc_models.CreateVolumeRequest())

    def test_create_volume_cluster(self):
        self.client.create_volume_cluster(bcc_models.CreateVolumeClusterRequest())

    def test_del_ipv6(self):
        self.client.del_ipv6(bcc_models.DelIpv6Request())

    def test_delete_asp(self):
        self.client.delete_asp(bcc_models.DeleteAspRequest())

    def test_delete_auto_renew_rule(self):
        self.client.delete_auto_renew_rule(bcc_models.DeleteAutoRenewRuleRequest())

    def test_delete_deploy_set(self):
        self.client.delete_deploy_set(bcc_models.DeleteDeploySetRequest())

    def test_delete_ehc_cluster(self):
        self.client.delete_ehc_cluster(bcc_models.DeleteEhcClusterRequest())

    def test_delete_image(self):
        self.client.delete_image(bcc_models.DeleteImageRequest())

    def test_delete_inst_user_op_authorize_rule(self):
        self.client.delete_inst_user_op_authorize_rule(bcc_models.DeleteInstUserOpAuthorizeRuleRequest())

    def test_delete_instance_deploy_set(self):
        self.client.delete_instance_deploy_set(bcc_models.DeleteInstanceDeploySetRequest())

    def test_delete_keypair(self):
        self.client.delete_keypair(bcc_models.DeleteKeypairRequest())

    def test_delete_prepay_instance(self):
        self.client.delete_prepay_instance(bcc_models.DeletePrepayInstanceRequest())

    def test_delete_recycled_instance(self):
        self.client.delete_recycled_instance(bcc_models.DeleteRecycledInstanceRequest())

    def test_delete_security_group(self):
        self.client.delete_security_group(bcc_models.DeleteSecurityGroupRequest())

    def test_delete_security_group_rule(self):
        self.client.delete_security_group_rule(bcc_models.DeleteSecurityGroupRuleRequest())

    def test_delete_snapshot(self):
        self.client.delete_snapshot(bcc_models.DeleteSnapshotRequest())

    def test_deletes_instance_deploy_set(self):
        self.client.deletes_instance_deploy_set(bcc_models.DeletesInstanceDeploySetRequest())

    def test_describe_authorize_rules(self):
        self.client.describe_authorize_rules(bcc_models.DescribeAuthorizeRulesRequest())

    def test_describe_planned_event_records(self):
        self.client.describe_planned_event_records(bcc_models.DescribePlannedEventRecordsRequest())

    def test_describe_planned_events(self):
        self.client.describe_planned_events(bcc_models.DescribePlannedEventsRequest())

    def test_describe_regions(self):
        self.client.describe_regions(bcc_models.DescribeRegionsRequest())

    def test_describe_unplanned_event_records(self):
        self.client.describe_unplanned_event_records(bcc_models.DescribeUnplannedEventRecordsRequest())

    def test_describe_unplanned_events(self):
        self.client.describe_unplanned_events(bcc_models.DescribeUnplannedEventsRequest())

    def test_detach_asp(self):
        self.client.detach_asp(bcc_models.DetachAspRequest())

    def test_detach_keypair(self):
        self.client.detach_keypair(bcc_models.DetachKeypairRequest())

    def test_detach_volume(self):
        self.client.detach_volume(bcc_models.DetachVolumeRequest())

    def test_ehc_cluster_list(self):
        self.client.ehc_cluster_list(bcc_models.EhcClusterListRequest())

    def test_enter_rescue_mode(self):
        self.client.enter_rescue_mode(bcc_models.EnterRescueModeRequest())

    def test_exit_rescue_mode(self):
        self.client.exit_rescue_mode(bcc_models.ExitRescueModeRequest())

    def test_get_asp(self):
        self.client.get_asp(bcc_models.GetAspRequest())

    def test_get_available_images_by_spec(self):
        self.client.get_available_images_by_spec(bcc_models.GetAvailableImagesBySpecRequest())

    def test_get_bid_instance_price(self):
        self.client.get_bid_instance_price(bcc_models.GetBidInstancePriceRequest())

    def test_get_cds_price(self):
        self.client.get_cds_price(bcc_models.GetCdsPriceRequest())

    def test_get_deploy_set(self):
        self.client.get_deploy_set(bcc_models.GetDeploySetRequest())

    def test_get_disk_quota(self):
        self.client.get_disk_quota(bcc_models.GetDiskQuotaRequest())

    def test_get_image(self):
        self.client.get_image(bcc_models.GetImageRequest())

    def test_get_instance(self):
        self.client.get_instance(bcc_models.GetInstanceRequest())

    def test_get_instance_no_charge_list(self):
        self.client.get_instance_no_charge_list(bcc_models.GetInstanceNoChargeListRequest())

    def test_get_instance_user_data_info(self):
        self.client.get_instance_user_data_info(bcc_models.GetInstanceUserDataInfoRequest())

    def test_get_instance_vnc(self):
        self.client.get_instance_vnc(bcc_models.GetInstanceVncRequest())

    def test_get_price_by_spec(self):
        self.client.get_price_by_spec(bcc_models.GetPriceBySpecRequest())

    def test_get_reserved_instance(self):
        self.client.get_reserved_instance(bcc_models.GetReservedInstanceRequest())

    def test_get_reserved_instance_price(self):
        self.client.get_reserved_instance_price(bcc_models.GetReservedInstancePriceRequest())

    def test_get_role_list(self):
        self.client.get_role_list()

    def test_get_snapshot(self):
        self.client.get_snapshot(bcc_models.GetSnapshotRequest())

    def test_get_task(self):
        self.client.get_task(bcc_models.GetTaskRequest())

    def test_get_volume(self):
        self.client.get_volume(bcc_models.GetVolumeRequest())

    def test_get_volume_cluster(self):
        self.client.get_volume_cluster(bcc_models.GetVolumeClusterRequest())

    def test_get_volume_resize_progress(self):
        self.client.get_volume_resize_progress(bcc_models.GetVolumeResizeProgressRequest())

    def test_get_zone_by_spec(self):
        self.client.get_zone_by_spec(bcc_models.GetZoneBySpecRequest())

    def test_import_image(self):
        self.client.import_image(bcc_models.ImportImageRequest())

    def test_import_keypair(self):
        self.client.import_keypair(bcc_models.ImportKeypairRequest())

    def test_instance_batch_resize_by_spec(self):
        self.client.instance_batch_resize_by_spec(bcc_models.InstanceBatchResizeBySpecRequest())

    def test_instance_deletion_protection(self):
        self.client.instance_deletion_protection(bcc_models.InstanceDeletionProtectionRequest())

    def test_instance_recovery(self):
        self.client.instance_recovery(bcc_models.InstanceRecoveryRequest())

    def test_keypair_detail(self):
        self.client.keypair_detail(bcc_models.KeypairDetailRequest())

    def test_list_asps(self):
        self.client.list_asps(bcc_models.ListAspsRequest())

    def test_list_available_resize_spec(self):
        self.client.list_available_resize_spec(bcc_models.ListAvailableResizeSpecRequest())

    def test_list_bid_flavor(self):
        self.client.list_bid_flavor()

    def test_list_deploy_set(self):
        self.client.list_deploy_set()

    def test_list_flavor_spec(self):
        self.client.list_flavor_spec(bcc_models.ListFlavorSpecRequest())

    def test_list_images(self):
        self.client.list_images(bcc_models.ListImagesRequest())

    def test_list_instance_by_ids(self):
        self.client.list_instance_by_ids(bcc_models.ListInstanceByIdsRequest())

    def test_list_instance_enis(self):
        self.client.list_instance_enis(bcc_models.ListInstanceEnisRequest())

    def test_list_instances(self):
        self.client.list_instances(bcc_models.ListInstancesRequest())

    def test_list_keypair(self):
        self.client.list_keypair(bcc_models.ListKeypairRequest())

    def test_list_os(self):
        self.client.list_os(bcc_models.ListOsRequest())

    def test_list_recycle_instance(self):
        self.client.list_recycle_instance(bcc_models.ListRecycleInstanceRequest())

    def test_list_reserved_instance_transfer_in(self):
        self.client.list_reserved_instance_transfer_in(bcc_models.ListReservedInstanceTransferInRequest())

    def test_list_reserved_instance_transfer_out(self):
        self.client.list_reserved_instance_transfer_out(bcc_models.ListReservedInstanceTransferOutRequest())

    def test_list_security_groups(self):
        self.client.list_security_groups(bcc_models.ListSecurityGroupsRequest())

    def test_list_shared_user(self):
        self.client.list_shared_user(bcc_models.ListSharedUserRequest())

    def test_list_snapchain(self):
        self.client.list_snapchain(bcc_models.ListSnapchainRequest())

    def test_list_snapshot_share(self):
        self.client.list_snapshot_share(bcc_models.ListSnapshotShareRequest())

    def test_list_snapshots(self):
        self.client.list_snapshots(bcc_models.ListSnapshotsRequest())

    def test_list_task(self):
        self.client.list_task(bcc_models.ListTaskRequest())

    def test_list_volume_clusters(self):
        self.client.list_volume_clusters(bcc_models.ListVolumeClustersRequest())

    def test_list_volumes(self):
        self.client.list_volumes(bcc_models.ListVolumesRequest())

    def test_list_zones(self):
        self.client.list_zones()

    def test_modify_cds_attribute(self):
        self.client.modify_cds_attribute(bcc_models.ModifyCdsAttributeRequest())

    def test_modify_ehc_cluster(self):
        self.client.modify_ehc_cluster(bcc_models.ModifyEhcClusterRequest())

    def test_modify_inst_user_op_authorize_rule_attribute(self):
        self.client.modify_inst_user_op_authorize_rule_attribute(
            bcc_models.ModifyInstUserOpAuthorizeRuleAttributeRequest()
        )

    def test_modify_instance_attributes(self):
        self.client.modify_instance_attributes(bcc_models.ModifyInstanceAttributesRequest())

    def test_modify_instance_desc(self):
        self.client.modify_instance_desc(bcc_models.ModifyInstanceDescRequest())

    def test_modify_instance_hostname(self):
        self.client.modify_instance_hostname(bcc_models.ModifyInstanceHostnameRequest())

    def test_modify_instance_password(self):
        self.client.modify_instance_password(bcc_models.ModifyInstancePasswordRequest())

    def test_modify_related_delete_policy(self):
        self.client.modify_related_delete_policy(bcc_models.ModifyRelatedDeletePolicyRequest())

    def test_modify_reserved_instances(self):
        self.client.modify_reserved_instances(bcc_models.ModifyReservedInstancesRequest())

    def test_modify_volume_charge_type(self):
        self.client.modify_volume_charge_type(bcc_models.ModifyVolumeChargeTypeRequest())

    def test_purchase_reserved_instance(self):
        self.client.purchase_reserved_instance(bcc_models.PurchaseReservedInstanceRequest())

    def test_purchase_reserved_volume(self):
        self.client.purchase_reserved_volume(bcc_models.PurchaseReservedVolumeRequest())

    def test_purchase_reserved_volume_cluster(self):
        self.client.purchase_reserved_volume_cluster(bcc_models.PurchaseReservedVolumeClusterRequest())

    def test_reboot_instance(self):
        self.client.reboot_instance(bcc_models.RebootInstanceRequest())

    def test_rebuild_batch_instance(self):
        self.client.rebuild_batch_instance(bcc_models.RebuildBatchInstanceRequest())

    def test_rebuild_instance(self):
        self.client.rebuild_instance(bcc_models.RebuildInstanceRequest())

    def test_refuse_reserved_instance_transfer(self):
        self.client.refuse_reserved_instance_transfer(bcc_models.RefuseReservedInstanceTransferRequest())

    def test_release_instance_by_post(self):
        self.client.release_instance_by_post(bcc_models.ReleaseInstanceByPostRequest())

    def test_release_multiple_instance_by_post(self):
        self.client.release_multiple_instance_by_post(bcc_models.ReleaseMultipleInstanceByPostRequest())

    def test_release_volume(self):
        self.client.release_volume(bcc_models.ReleaseVolumeRequest())

    def test_remote_copy_image(self):
        self.client.remote_copy_image(bcc_models.RemoteCopyImageRequest())

    def test_remote_copy_snapshot(self):
        self.client.remote_copy_snapshot(bcc_models.RemoteCopySnapshotRequest())

    def test_rename_image(self):
        self.client.rename_image(bcc_models.RenameImageRequest())

    def test_rename_keypair(self):
        self.client.rename_keypair(bcc_models.RenameKeypairRequest())

    def test_rename_volume(self):
        self.client.rename_volume(bcc_models.RenameVolumeRequest())

    def test_renew_reserved_instance(self):
        self.client.renew_reserved_instance(bcc_models.RenewReservedInstanceRequest())

    def test_replace_instance_security_group(self):
        self.client.replace_instance_security_group(bcc_models.ReplaceInstanceSecurityGroupRequest())

    def test_resize_instance_by_spec(self):
        self.client.resize_instance_by_spec(bcc_models.ResizeInstanceBySpecRequest())

    def test_resize_volume(self):
        self.client.resize_volume(bcc_models.ResizeVolumeRequest())

    def test_resize_volume_cluster(self):
        self.client.resize_volume_cluster(bcc_models.ResizeVolumeClusterRequest())

    def test_revoke_reserved_instance_transfer(self):
        self.client.revoke_reserved_instance_transfer(bcc_models.RevokeReservedInstanceTransferRequest())

    def test_revoke_security_group_rule(self):
        self.client.revoke_security_group_rule(bcc_models.RevokeSecurityGroupRuleRequest())

    def test_rollback_volume(self):
        self.client.rollback_volume(bcc_models.RollbackVolumeRequest())

    def test_share_image(self):
        self.client.share_image(bcc_models.ShareImageRequest())

    def test_start_instance(self):
        self.client.start_instance(bcc_models.StartInstanceRequest())

    def test_stop_instance(self):
        self.client.stop_instance(bcc_models.StopInstanceRequest())

    def test_un_share_image(self):
        self.client.un_share_image(bcc_models.UnShareImageRequest())

    def test_unbind_instance_from_security_group(self):
        self.client.unbind_instance_from_security_group(bcc_models.UnbindInstanceFromSecurityGroupRequest())

    def test_unbind_instance_from_tags(self):
        self.client.unbind_instance_from_tags(bcc_models.UnbindInstanceFromTagsRequest())

    def test_unbind_instance_security_group(self):
        self.client.unbind_instance_security_group(bcc_models.UnbindInstanceSecurityGroupRequest())

    def test_unbind_reserved_instance_from_tags(self):
        self.client.unbind_reserved_instance_from_tags(bcc_models.UnbindReservedInstanceFromTagsRequest())

    def test_unbind_role(self):
        self.client.unbind_role(bcc_models.UnbindRoleRequest())

    def test_unbind_tag_image(self):
        self.client.unbind_tag_image(bcc_models.UnbindTagImageRequest())

    def test_unbind_tag_snapchain(self):
        self.client.unbind_tag_snapchain(bcc_models.UnbindTagSnapchainRequest())

    def test_unbind_tag_volume(self):
        self.client.unbind_tag_volume(bcc_models.UnbindTagVolumeRequest())

    def test_unbind_tag_volume_cluster(self):
        self.client.unbind_tag_volume_cluster(bcc_models.UnbindTagVolumeClusterRequest())

    def test_update_asp(self):
        self.client.update_asp(bcc_models.UpdateAspRequest())

    def test_update_deploy_set(self):
        self.client.update_deploy_set(bcc_models.UpdateDeploySetRequest())

    def test_update_deploy_set_relation(self):
        self.client.update_deploy_set_relation(bcc_models.UpdateDeploySetRelationRequest())

    def test_update_instance_subnet(self):
        self.client.update_instance_subnet(bcc_models.UpdateInstanceSubnetRequest())

    def test_update_keypair_description(self):
        self.client.update_keypair_description(bcc_models.UpdateKeypairDescriptionRequest())

    def test_update_security_group_rule(self):
        self.client.update_security_group_rule(bcc_models.UpdateSecurityGroupRuleRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(BccClientTest("test_accept_reserved_instance_transfer"))
    suite.addTest(BccClientTest("test_add_ipv6"))
    suite.addTest(BccClientTest("test_attach_asp"))
    suite.addTest(BccClientTest("test_attach_keypair"))
    suite.addTest(BccClientTest("test_attach_volume"))
    suite.addTest(BccClientTest("test_authorize_security_group_rule"))
    suite.addTest(BccClientTest("test_authorize_server_event"))
    suite.addTest(BccClientTest("test_auto_release_instance"))
    suite.addTest(BccClientTest("test_auto_renew_reserved_instance"))
    suite.addTest(BccClientTest("test_auto_renew_volume_cluster"))
    suite.addTest(BccClientTest("test_batch_add_ip"))
    suite.addTest(BccClientTest("test_batch_change_to_postpaid"))
    suite.addTest(BccClientTest("test_batch_change_to_prepaid"))
    suite.addTest(BccClientTest("test_batch_delete_ip"))
    suite.addTest(BccClientTest("test_batch_refund_resource"))
    suite.addTest(BccClientTest("test_batch_start_instance"))
    suite.addTest(BccClientTest("test_batch_stop_instance"))
    suite.addTest(BccClientTest("test_bind_instance_security_group"))
    suite.addTest(BccClientTest("test_bind_instance_to_security_group"))
    suite.addTest(BccClientTest("test_bind_instance_to_tags"))
    suite.addTest(BccClientTest("test_bind_reserved_instance_to_tags"))
    suite.addTest(BccClientTest("test_bind_role"))
    suite.addTest(BccClientTest("test_bind_tag_image"))
    suite.addTest(BccClientTest("test_bind_tag_snapchain"))
    suite.addTest(BccClientTest("test_bind_tag_volume"))
    suite.addTest(BccClientTest("test_bind_tag_volume_cluster"))
    suite.addTest(BccClientTest("test_cancel_auto_renew_reserved_instance"))
    suite.addTest(BccClientTest("test_cancel_auto_renew_volume_cluster"))
    suite.addTest(BccClientTest("test_cancel_bid_order"))
    suite.addTest(BccClientTest("test_cancel_remote_copy_image"))
    suite.addTest(BccClientTest("test_cancel_snapshot_share"))
    suite.addTest(BccClientTest("test_change_to_prepaid"))
    suite.addTest(BccClientTest("test_change_vpc"))
    suite.addTest(BccClientTest("test_check_server_event"))
    suite.addTest(BccClientTest("test_create_asp"))
    suite.addTest(BccClientTest("test_create_authorization_rule"))
    suite.addTest(BccClientTest("test_create_auto_renew_rule"))
    suite.addTest(BccClientTest("test_create_bid_instance"))
    suite.addTest(BccClientTest("test_create_deploy_set"))
    suite.addTest(BccClientTest("test_create_ehc_cluster"))
    suite.addTest(BccClientTest("test_create_image"))
    suite.addTest(BccClientTest("test_create_instance_by_spec"))
    suite.addTest(BccClientTest("test_create_keypair"))
    suite.addTest(BccClientTest("test_create_reserved_instance_transfer"))
    suite.addTest(BccClientTest("test_create_reserved_instances"))
    suite.addTest(BccClientTest("test_create_security_group"))
    suite.addTest(BccClientTest("test_create_snapshot"))
    suite.addTest(BccClientTest("test_create_snapshot_share"))
    suite.addTest(BccClientTest("test_create_volume"))
    suite.addTest(BccClientTest("test_create_volume_cluster"))
    suite.addTest(BccClientTest("test_del_ipv6"))
    suite.addTest(BccClientTest("test_delete_asp"))
    suite.addTest(BccClientTest("test_delete_auto_renew_rule"))
    suite.addTest(BccClientTest("test_delete_deploy_set"))
    suite.addTest(BccClientTest("test_delete_ehc_cluster"))
    suite.addTest(BccClientTest("test_delete_image"))
    suite.addTest(BccClientTest("test_delete_inst_user_op_authorize_rule"))
    suite.addTest(BccClientTest("test_delete_instance_deploy_set"))
    suite.addTest(BccClientTest("test_delete_keypair"))
    suite.addTest(BccClientTest("test_delete_prepay_instance"))
    suite.addTest(BccClientTest("test_delete_recycled_instance"))
    suite.addTest(BccClientTest("test_delete_security_group"))
    suite.addTest(BccClientTest("test_delete_security_group_rule"))
    suite.addTest(BccClientTest("test_delete_snapshot"))
    suite.addTest(BccClientTest("test_deletes_instance_deploy_set"))
    suite.addTest(BccClientTest("test_describe_authorize_rules"))
    suite.addTest(BccClientTest("test_describe_planned_event_records"))
    suite.addTest(BccClientTest("test_describe_planned_events"))
    suite.addTest(BccClientTest("test_describe_regions"))
    suite.addTest(BccClientTest("test_describe_unplanned_event_records"))
    suite.addTest(BccClientTest("test_describe_unplanned_events"))
    suite.addTest(BccClientTest("test_detach_asp"))
    suite.addTest(BccClientTest("test_detach_keypair"))
    suite.addTest(BccClientTest("test_detach_volume"))
    suite.addTest(BccClientTest("test_ehc_cluster_list"))
    suite.addTest(BccClientTest("test_enter_rescue_mode"))
    suite.addTest(BccClientTest("test_exit_rescue_mode"))
    suite.addTest(BccClientTest("test_get_asp"))
    suite.addTest(BccClientTest("test_get_available_images_by_spec"))
    suite.addTest(BccClientTest("test_get_bid_instance_price"))
    suite.addTest(BccClientTest("test_get_cds_price"))
    suite.addTest(BccClientTest("test_get_deploy_set"))
    suite.addTest(BccClientTest("test_get_disk_quota"))
    suite.addTest(BccClientTest("test_get_image"))
    suite.addTest(BccClientTest("test_get_instance"))
    suite.addTest(BccClientTest("test_get_instance_no_charge_list"))
    suite.addTest(BccClientTest("test_get_instance_user_data_info"))
    suite.addTest(BccClientTest("test_get_instance_vnc"))
    suite.addTest(BccClientTest("test_get_price_by_spec"))
    suite.addTest(BccClientTest("test_get_reserved_instance"))
    suite.addTest(BccClientTest("test_get_reserved_instance_price"))
    suite.addTest(BccClientTest("test_get_role_list"))
    suite.addTest(BccClientTest("test_get_snapshot"))
    suite.addTest(BccClientTest("test_get_task"))
    suite.addTest(BccClientTest("test_get_volume"))
    suite.addTest(BccClientTest("test_get_volume_cluster"))
    suite.addTest(BccClientTest("test_get_volume_resize_progress"))
    suite.addTest(BccClientTest("test_get_zone_by_spec"))
    suite.addTest(BccClientTest("test_import_image"))
    suite.addTest(BccClientTest("test_import_keypair"))
    suite.addTest(BccClientTest("test_instance_batch_resize_by_spec"))
    suite.addTest(BccClientTest("test_instance_deletion_protection"))
    suite.addTest(BccClientTest("test_instance_recovery"))
    suite.addTest(BccClientTest("test_keypair_detail"))
    suite.addTest(BccClientTest("test_list_asps"))
    suite.addTest(BccClientTest("test_list_available_resize_spec"))
    suite.addTest(BccClientTest("test_list_bid_flavor"))
    suite.addTest(BccClientTest("test_list_deploy_set"))
    suite.addTest(BccClientTest("test_list_flavor_spec"))
    suite.addTest(BccClientTest("test_list_images"))
    suite.addTest(BccClientTest("test_list_instance_by_ids"))
    suite.addTest(BccClientTest("test_list_instance_enis"))
    suite.addTest(BccClientTest("test_list_instances"))
    suite.addTest(BccClientTest("test_list_keypair"))
    suite.addTest(BccClientTest("test_list_os"))
    suite.addTest(BccClientTest("test_list_recycle_instance"))
    suite.addTest(BccClientTest("test_list_reserved_instance_transfer_in"))
    suite.addTest(BccClientTest("test_list_reserved_instance_transfer_out"))
    suite.addTest(BccClientTest("test_list_security_groups"))
    suite.addTest(BccClientTest("test_list_shared_user"))
    suite.addTest(BccClientTest("test_list_snapchain"))
    suite.addTest(BccClientTest("test_list_snapshot_share"))
    suite.addTest(BccClientTest("test_list_snapshots"))
    suite.addTest(BccClientTest("test_list_task"))
    suite.addTest(BccClientTest("test_list_volume_clusters"))
    suite.addTest(BccClientTest("test_list_volumes"))
    suite.addTest(BccClientTest("test_list_zones"))
    suite.addTest(BccClientTest("test_modify_cds_attribute"))
    suite.addTest(BccClientTest("test_modify_ehc_cluster"))
    suite.addTest(BccClientTest("test_modify_inst_user_op_authorize_rule_attribute"))
    suite.addTest(BccClientTest("test_modify_instance_attributes"))
    suite.addTest(BccClientTest("test_modify_instance_desc"))
    suite.addTest(BccClientTest("test_modify_instance_hostname"))
    suite.addTest(BccClientTest("test_modify_instance_password"))
    suite.addTest(BccClientTest("test_modify_related_delete_policy"))
    suite.addTest(BccClientTest("test_modify_reserved_instances"))
    suite.addTest(BccClientTest("test_modify_volume_charge_type"))
    suite.addTest(BccClientTest("test_purchase_reserved_instance"))
    suite.addTest(BccClientTest("test_purchase_reserved_volume"))
    suite.addTest(BccClientTest("test_purchase_reserved_volume_cluster"))
    suite.addTest(BccClientTest("test_reboot_instance"))
    suite.addTest(BccClientTest("test_rebuild_batch_instance"))
    suite.addTest(BccClientTest("test_rebuild_instance"))
    suite.addTest(BccClientTest("test_refuse_reserved_instance_transfer"))
    suite.addTest(BccClientTest("test_release_instance_by_post"))
    suite.addTest(BccClientTest("test_release_multiple_instance_by_post"))
    suite.addTest(BccClientTest("test_release_volume"))
    suite.addTest(BccClientTest("test_remote_copy_image"))
    suite.addTest(BccClientTest("test_remote_copy_snapshot"))
    suite.addTest(BccClientTest("test_rename_image"))
    suite.addTest(BccClientTest("test_rename_keypair"))
    suite.addTest(BccClientTest("test_rename_volume"))
    suite.addTest(BccClientTest("test_renew_reserved_instance"))
    suite.addTest(BccClientTest("test_replace_instance_security_group"))
    suite.addTest(BccClientTest("test_resize_instance_by_spec"))
    suite.addTest(BccClientTest("test_resize_volume"))
    suite.addTest(BccClientTest("test_resize_volume_cluster"))
    suite.addTest(BccClientTest("test_revoke_reserved_instance_transfer"))
    suite.addTest(BccClientTest("test_revoke_security_group_rule"))
    suite.addTest(BccClientTest("test_rollback_volume"))
    suite.addTest(BccClientTest("test_share_image"))
    suite.addTest(BccClientTest("test_start_instance"))
    suite.addTest(BccClientTest("test_stop_instance"))
    suite.addTest(BccClientTest("test_un_share_image"))
    suite.addTest(BccClientTest("test_unbind_instance_from_security_group"))
    suite.addTest(BccClientTest("test_unbind_instance_from_tags"))
    suite.addTest(BccClientTest("test_unbind_instance_security_group"))
    suite.addTest(BccClientTest("test_unbind_reserved_instance_from_tags"))
    suite.addTest(BccClientTest("test_unbind_role"))
    suite.addTest(BccClientTest("test_unbind_tag_image"))
    suite.addTest(BccClientTest("test_unbind_tag_snapchain"))
    suite.addTest(BccClientTest("test_unbind_tag_volume"))
    suite.addTest(BccClientTest("test_unbind_tag_volume_cluster"))
    suite.addTest(BccClientTest("test_update_asp"))
    suite.addTest(BccClientTest("test_update_deploy_set"))
    suite.addTest(BccClientTest("test_update_deploy_set_relation"))
    suite.addTest(BccClientTest("test_update_instance_subnet"))
    suite.addTest(BccClientTest("test_update_keypair_description"))
    suite.addTest(BccClientTest("test_update_security_group_rule"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
