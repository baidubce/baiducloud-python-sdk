import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_iam.api.iam_client import IamClient
from baiducloud_python_sdk_iam import models as iam_models


class IamClientTest(unittest.TestCase):
    """IamClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''

        # ==== AK/SK 鉴权 ====
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)

        self.client = IamClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_add_user_to_group(self):
        self.client.add_user_to_group(iam_models.AddUserToGroupRequest())

    def test_associate_group_permissions(self):
        self.client.associate_group_permissions(iam_models.AssociateGroupPermissionsRequest())

    def test_associate_role_permissions(self):
        self.client.associate_role_permissions(iam_models.AssociateRolePermissionsRequest())

    def test_associate_user_permissions(self):
        self.client.associate_user_permissions(iam_models.AssociateUserPermissionsRequest())

    def test_change_sub_user_password(self):
        self.client.change_sub_user_password(iam_models.ChangeSubUserPasswordRequest())

    def test_create_access_key(self):
        self.client.create_access_key(iam_models.CreateAccessKeyRequest())

    def test_create_apikey_permanently_valid(self):
        self.client.create_apikey_permanently_valid(iam_models.CreateApikeyPermanentlyValidRequest())

    def test_create_group(self):
        self.client.create_group(iam_models.CreateGroupRequest())

    def test_create_role(self):
        self.client.create_role(iam_models.CreateRoleRequest())

    def test_create_strategy(self):
        self.client.create_strategy(iam_models.CreateStrategyRequest())

    def test_create_user(self):
        self.client.create_user(iam_models.CreateUserRequest())

    def test_decoding_apikey_permanently_valid(self):
        self.client.decoding_apikey_permanently_valid(iam_models.DecodingApikeyPermanentlyValidRequest())

    def test_delete_access_key(self):
        self.client.delete_access_key(iam_models.DeleteAccessKeyRequest())

    def test_delete_apikey_permanently_valid(self):
        self.client.delete_apikey_permanently_valid(iam_models.DeleteApikeyPermanentlyValidRequest())

    def test_delete_group(self):
        self.client.delete_group(iam_models.DeleteGroupRequest())

    def test_delete_login_profile(self):
        self.client.delete_login_profile(iam_models.DeleteLoginProfileRequest())

    def test_delete_role(self):
        self.client.delete_role(iam_models.DeleteRoleRequest())

    def test_delete_strategy(self):
        self.client.delete_strategy(iam_models.DeleteStrategyRequest())

    def test_delete_sub_user_idp(self):
        self.client.delete_sub_user_idp()

    def test_delete_user(self):
        self.client.delete_user(iam_models.DeleteUserRequest())

    def test_disable_access_key(self):
        self.client.disable_access_key(iam_models.DisableAccessKeyRequest())

    def test_enable_access_key(self):
        self.client.enable_access_key(iam_models.EnableAccessKeyRequest())

    def test_get_login_profile(self):
        self.client.get_login_profile(iam_models.GetLoginProfileRequest())

    def test_get_session_api_key(self):
        self.client.get_session_api_key(iam_models.GetSessionApiKeyRequest())

    def test_get_user(self):
        self.client.get_user(iam_models.GetUserRequest())

    def test_list_access_key(self):
        self.client.list_access_key(iam_models.ListAccessKeyRequest())

    def test_list_all_subjects_granted_permissions(self):
        self.client.list_all_subjects_granted_permissions(iam_models.ListAllSubjectsGrantedPermissionsRequest())

    def test_list_groups(self):
        self.client.list_groups()

    def test_list_roles(self):
        self.client.list_roles()

    def test_list_strategies(self):
        self.client.list_strategies(iam_models.ListStrategiesRequest())

    def test_list_the_permissions_of_roles(self):
        self.client.list_the_permissions_of_roles(iam_models.ListThePermissionsOfRolesRequest())

    def test_list_the_permissions_of_the_group(self):
        self.client.list_the_permissions_of_the_group(iam_models.ListThePermissionsOfTheGroupRequest())

    def test_list_the_subjects_granted_permissions(self):
        self.client.list_the_subjects_granted_permissions(iam_models.ListTheSubjectsGrantedPermissionsRequest())

    def test_list_the_user_s_permissions(self):
        self.client.list_the_user_s_permissions(iam_models.ListTheUserSPermissionsRequest())

    def test_list_user(self):
        self.client.list_user()

    def test_list_user_groups(self):
        self.client.list_user_groups(iam_models.ListUserGroupsRequest())

    def test_list_users_within_the_group(self):
        self.client.list_users_within_the_group(iam_models.ListUsersWithinTheGroupRequest())

    def test_modify_sub_user_operation_protection(self):
        self.client.modify_sub_user_operation_protection(iam_models.ModifySubUserOperationProtectionRequest())

    def test_obtain_a_list_of_permanently_valid_apikeys(self):
        self.client.obtain_a_list_of_permanently_valid_apikeys(
            iam_models.ObtainAListOfPermanentlyValidApikeysRequest()
        )

    def test_query_apikey_details_permanently_valid(self):
        self.client.query_apikey_details_permanently_valid(iam_models.QueryApikeyDetailsPermanentlyValidRequest())

    def test_query_group(self):
        self.client.query_group(iam_models.QueryGroupRequest())

    def test_query_role(self):
        self.client.query_role(iam_models.QueryRoleRequest())

    def test_query_strategy(self):
        self.client.query_strategy(iam_models.QueryStrategyRequest())

    def test_query_sub_user_idp(self):
        self.client.query_sub_user_idp()

    def test_query_summary_of_main_account(self):
        self.client.query_summary_of_main_account()

    def test_query_the_last_usage_time_of_accesskey(self):
        self.client.query_the_last_usage_time_of_accesskey(iam_models.QueryTheLastUsageTimeOfAccesskeyRequest())

    def test_remove_group_permissions(self):
        self.client.remove_group_permissions(iam_models.RemoveGroupPermissionsRequest())

    def test_remove_role_permissions(self):
        self.client.remove_role_permissions(iam_models.RemoveRolePermissionsRequest())

    def test_remove_user_from_the_group(self):
        self.client.remove_user_from_the_group(iam_models.RemoveUserFromTheGroupRequest())

    def test_remove_user_permissions(self):
        self.client.remove_user_permissions(iam_models.RemoveUserPermissionsRequest())

    def test_unbind_sub_user_virtual_mfa(self):
        self.client.unbind_sub_user_virtual_mfa(iam_models.UnbindSubUserVirtualMfaRequest())

    def test_update_apikey_permanently_valid(self):
        self.client.update_apikey_permanently_valid(iam_models.UpdateApikeyPermanentlyValidRequest())

    def test_update_group(self):
        self.client.update_group(iam_models.UpdateGroupRequest())

    def test_update_login_profile(self):
        self.client.update_login_profile(iam_models.UpdateLoginProfileRequest())

    def test_update_role(self):
        self.client.update_role(iam_models.UpdateRoleRequest())

    def test_update_strategy(self):
        self.client.update_strategy(iam_models.UpdateStrategyRequest())

    def test_update_sub_user_idp(self):
        self.client.update_sub_user_idp(iam_models.UpdateSubUserIdpRequest())

    def test_update_sub_user_idp_status(self):
        self.client.update_sub_user_idp_status(iam_models.UpdateSubUserIdpStatusRequest())

    def test_update_user(self):
        self.client.update_user(iam_models.UpdateUserRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(IamClientTest("test_add_user_to_group"))
    suite.addTest(IamClientTest("test_associate_group_permissions"))
    suite.addTest(IamClientTest("test_associate_role_permissions"))
    suite.addTest(IamClientTest("test_associate_user_permissions"))
    suite.addTest(IamClientTest("test_change_sub_user_password"))
    suite.addTest(IamClientTest("test_create_access_key"))
    suite.addTest(IamClientTest("test_create_apikey_permanently_valid"))
    suite.addTest(IamClientTest("test_create_group"))
    suite.addTest(IamClientTest("test_create_role"))
    suite.addTest(IamClientTest("test_create_strategy"))
    suite.addTest(IamClientTest("test_create_user"))
    suite.addTest(IamClientTest("test_decoding_apikey_permanently_valid"))
    suite.addTest(IamClientTest("test_delete_access_key"))
    suite.addTest(IamClientTest("test_delete_apikey_permanently_valid"))
    suite.addTest(IamClientTest("test_delete_group"))
    suite.addTest(IamClientTest("test_delete_login_profile"))
    suite.addTest(IamClientTest("test_delete_role"))
    suite.addTest(IamClientTest("test_delete_strategy"))
    suite.addTest(IamClientTest("test_delete_sub_user_idp"))
    suite.addTest(IamClientTest("test_delete_user"))
    suite.addTest(IamClientTest("test_disable_access_key"))
    suite.addTest(IamClientTest("test_enable_access_key"))
    suite.addTest(IamClientTest("test_get_login_profile"))
    suite.addTest(IamClientTest("test_get_session_api_key"))
    suite.addTest(IamClientTest("test_get_user"))
    suite.addTest(IamClientTest("test_list_access_key"))
    suite.addTest(IamClientTest("test_list_all_subjects_granted_permissions"))
    suite.addTest(IamClientTest("test_list_groups"))
    suite.addTest(IamClientTest("test_list_roles"))
    suite.addTest(IamClientTest("test_list_strategies"))
    suite.addTest(IamClientTest("test_list_the_permissions_of_roles"))
    suite.addTest(IamClientTest("test_list_the_permissions_of_the_group"))
    suite.addTest(IamClientTest("test_list_the_subjects_granted_permissions"))
    suite.addTest(IamClientTest("test_list_the_user_s_permissions"))
    suite.addTest(IamClientTest("test_list_user"))
    suite.addTest(IamClientTest("test_list_user_groups"))
    suite.addTest(IamClientTest("test_list_users_within_the_group"))
    suite.addTest(IamClientTest("test_modify_sub_user_operation_protection"))
    suite.addTest(IamClientTest("test_obtain_a_list_of_permanently_valid_apikeys"))
    suite.addTest(IamClientTest("test_query_apikey_details_permanently_valid"))
    suite.addTest(IamClientTest("test_query_group"))
    suite.addTest(IamClientTest("test_query_role"))
    suite.addTest(IamClientTest("test_query_strategy"))
    suite.addTest(IamClientTest("test_query_sub_user_idp"))
    suite.addTest(IamClientTest("test_query_summary_of_main_account"))
    suite.addTest(IamClientTest("test_query_the_last_usage_time_of_accesskey"))
    suite.addTest(IamClientTest("test_remove_group_permissions"))
    suite.addTest(IamClientTest("test_remove_role_permissions"))
    suite.addTest(IamClientTest("test_remove_user_from_the_group"))
    suite.addTest(IamClientTest("test_remove_user_permissions"))
    suite.addTest(IamClientTest("test_unbind_sub_user_virtual_mfa"))
    suite.addTest(IamClientTest("test_update_apikey_permanently_valid"))
    suite.addTest(IamClientTest("test_update_group"))
    suite.addTest(IamClientTest("test_update_login_profile"))
    suite.addTest(IamClientTest("test_update_role"))
    suite.addTest(IamClientTest("test_update_strategy"))
    suite.addTest(IamClientTest("test_update_sub_user_idp"))
    suite.addTest(IamClientTest("test_update_sub_user_idp_status"))
    suite.addTest(IamClientTest("test_update_user"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
