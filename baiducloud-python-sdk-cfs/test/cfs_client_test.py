import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_cfs.api.cfs_client import CfsClient
from baiducloud_python_sdk_cfs import models as cfs_models


class CfsClientTest(unittest.TestCase):
    """CfsClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
        self.client = CfsClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_batch_creation_of_permission_group_rules(self):
        self.client.batch_creation_of_permission_group_rules(cfs_models.BatchCreationOfPermissionGroupRulesRequest())

    def test_create_file_system(self):
        self.client.create_file_system(cfs_models.CreateFileSystemRequest())

    def test_create_mounting_target(self):
        self.client.create_mounting_target(cfs_models.CreateMountingTargetRequest())

    def test_create_permission_group(self):
        self.client.create_permission_group(cfs_models.CreatePermissionGroupRequest())

    def test_create_permission_group_rules(self):
        self.client.create_permission_group_rules(cfs_models.CreatePermissionGroupRulesRequest())

    def test_delete_permission_group(self):
        self.client.delete_permission_group(cfs_models.DeletePermissionGroupRequest())

    def test_delete_permission_group_rule(self):
        self.client.delete_permission_group_rule(cfs_models.DeletePermissionGroupRuleRequest())

    def test_drop_file_system(self):
        self.client.drop_file_system(cfs_models.DropFileSystemRequest())

    def test_drop_mount_target(self):
        self.client.drop_mount_target(cfs_models.DropMountTargetRequest())

    def test_modify_the_mount_target_permission_group(self):
        self.client.modify_the_mount_target_permission_group(cfs_models.ModifyTheMountTargetPermissionGroupRequest())

    def test_query_file_system(self):
        self.client.query_file_system(cfs_models.QueryFileSystemRequest())

    def test_query_mounted_client(self):
        self.client.query_mounted_client(cfs_models.QueryMountedClientRequest())

    def test_query_mounting_target(self):
        self.client.query_mounting_target(cfs_models.QueryMountingTargetRequest())

    def test_query_permission_group(self):
        self.client.query_permission_group(cfs_models.QueryPermissionGroupRequest())

    def test_query_permission_group_rules(self):
        self.client.query_permission_group_rules(cfs_models.QueryPermissionGroupRulesRequest())

    def test_update_file_system(self):
        self.client.update_file_system(cfs_models.UpdateFileSystemRequest())

    def test_update_file_system_labels(self):
        self.client.update_file_system_labels(cfs_models.UpdateFileSystemLabelsRequest())

    def test_update_permission_group(self):
        self.client.update_permission_group(cfs_models.UpdatePermissionGroupRequest())

    def test_update_permission_group_rules(self):
        self.client.update_permission_group_rules(cfs_models.UpdatePermissionGroupRulesRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CfsClientTest("test_batch_creation_of_permission_group_rules"))
    suite.addTest(CfsClientTest("test_create_file_system"))
    suite.addTest(CfsClientTest("test_create_mounting_target"))
    suite.addTest(CfsClientTest("test_create_permission_group"))
    suite.addTest(CfsClientTest("test_create_permission_group_rules"))
    suite.addTest(CfsClientTest("test_delete_permission_group"))
    suite.addTest(CfsClientTest("test_delete_permission_group_rule"))
    suite.addTest(CfsClientTest("test_drop_file_system"))
    suite.addTest(CfsClientTest("test_drop_mount_target"))
    suite.addTest(CfsClientTest("test_modify_the_mount_target_permission_group"))
    suite.addTest(CfsClientTest("test_query_file_system"))
    suite.addTest(CfsClientTest("test_query_mounted_client"))
    suite.addTest(CfsClientTest("test_query_mounting_target"))
    suite.addTest(CfsClientTest("test_query_permission_group"))
    suite.addTest(CfsClientTest("test_query_permission_group_rules"))
    suite.addTest(CfsClientTest("test_update_file_system"))
    suite.addTest(CfsClientTest("test_update_file_system_labels"))
    suite.addTest(CfsClientTest("test_update_permission_group"))
    suite.addTest(CfsClientTest("test_update_permission_group_rules"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
