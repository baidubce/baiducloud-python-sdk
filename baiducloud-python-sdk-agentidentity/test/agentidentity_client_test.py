import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_agentidentity.api.agentidentity_client import AgentidentityClient
from baiducloud_python_sdk_agentidentity import models as agentidentity_models


class AgentidentityClientTest(unittest.TestCase):
    """AgentidentityClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
        self.client = AgentidentityClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_authorize_endpoint(self):
        self.client.authorize_endpoint(agentidentity_models.AuthorizeEndpointRequest())

    def test_batch_acquisition_of_users(self):
        self.client.batch_acquisition_of_users(agentidentity_models.BatchAcquisitionOfUsersRequest())

    def test_batch_get_resource_api_key(self):
        self.client.batch_get_resource_api_key(agentidentity_models.BatchGetResourceApiKeyRequest())

    def test_complete_oauth2session(self):
        self.client.complete_oauth2session(agentidentity_models.CompleteOauth2sessionRequest())

    def test_create_agent(self):
        self.client.create_agent(agentidentity_models.CreateAgentRequest())

    def test_create_credential_provider(self):
        self.client.create_credential_provider(agentidentity_models.CreateCredentialProviderRequest())

    def test_create_idp_configuration(self):
        self.client.create_idp_configuration(agentidentity_models.CreateIdpConfigurationRequest())

    def test_create_oauth2_client(self):
        self.client.create_oauth2_client(agentidentity_models.CreateOauth2ClientRequest())

    def test_create_user(self):
        self.client.create_user(agentidentity_models.CreateUserRequest())

    def test_create_user_pool(self):
        self.client.create_user_pool(agentidentity_models.CreateUserPoolRequest())

    def test_delete_agent(self):
        self.client.delete_agent(agentidentity_models.DeleteAgentRequest())

    def test_delete_credential_provider(self):
        self.client.delete_credential_provider(agentidentity_models.DeleteCredentialProviderRequest())

    def test_delete_idp_configuration(self):
        self.client.delete_idp_configuration(agentidentity_models.DeleteIdpConfigurationRequest())

    def test_delete_oauth2_client(self):
        self.client.delete_oauth2_client(agentidentity_models.DeleteOauth2ClientRequest())

    def test_delete_user(self):
        self.client.delete_user(agentidentity_models.DeleteUserRequest())

    def test_delete_user_pool(self):
        self.client.delete_user_pool(agentidentity_models.DeleteUserPoolRequest())

    def test_disable_idp_configuration(self):
        self.client.disable_idp_configuration(agentidentity_models.DisableIdpConfigurationRequest())

    def test_enable_idp_configuration(self):
        self.client.enable_idp_configuration(agentidentity_models.EnableIdpConfigurationRequest())

    def test_get_agent(self):
        self.client.get_agent(agentidentity_models.GetAgentRequest())

    def test_get_credential_provider(self):
        self.client.get_credential_provider(agentidentity_models.GetCredentialProviderRequest())

    def test_get_idp_configuration(self):
        self.client.get_idp_configuration(agentidentity_models.GetIdpConfigurationRequest())

    def test_get_oauth2_client(self):
        self.client.get_oauth2_client(agentidentity_models.GetOauth2ClientRequest())

    def test_get_resource_apikey(self):
        self.client.get_resource_apikey(agentidentity_models.GetResourceApikeyRequest())

    def test_get_resource_oauth2token(self):
        self.client.get_resource_oauth2token(agentidentity_models.GetResourceOauth2tokenRequest())

    def test_get_user(self):
        self.client.get_user(agentidentity_models.GetUserRequest())

    def test_get_user_pool(self):
        self.client.get_user_pool(agentidentity_models.GetUserPoolRequest())

    def test_get_wat_for_user(self):
        self.client.get_wat_for_user(agentidentity_models.GetWATForUserRequest())

    def test_get_workload_access_token(self):
        self.client.get_workload_access_token(agentidentity_models.GetWorkloadAccessTokenRequest())

    def test_list_agents(self):
        self.client.list_agents(agentidentity_models.ListAgentsRequest())

    def test_list_credential_providers(self):
        self.client.list_credential_providers(agentidentity_models.ListCredentialProvidersRequest())

    def test_list_idp_configurations(self):
        self.client.list_idp_configurations(agentidentity_models.ListIdpConfigurationsRequest())

    def test_list_oauth2_clients(self):
        self.client.list_oauth2_clients(agentidentity_models.ListOauth2ClientsRequest())

    def test_list_user_pools(self):
        self.client.list_user_pools(agentidentity_models.ListUserPoolsRequest())

    def test_list_users(self):
        self.client.list_users(agentidentity_models.ListUsersRequest())

    def test_o_idc_discovery(self):
        self.client.o_idc_discovery(agentidentity_models.OIdcDiscoveryRequest())

    def test_oauth2idp_callback(self):
        self.client.oauth2idp_callback(agentidentity_models.Oauth2idpCallbackRequest())

    def test_reset_password(self):
        self.client.reset_password(agentidentity_models.ResetPasswordRequest())

    def test_token_endpoint(self):
        self.client.token_endpoint(agentidentity_models.TokenEndpointRequest())

    def test_update_agent(self):
        self.client.update_agent(agentidentity_models.UpdateAgentRequest())

    def test_update_credential_provider(self):
        self.client.update_credential_provider(agentidentity_models.UpdateCredentialProviderRequest())

    def test_update_idp_configuration(self):
        self.client.update_idp_configuration(agentidentity_models.UpdateIdpConfigurationRequest())

    def test_update_oauth2_client(self):
        self.client.update_oauth2_client(agentidentity_models.UpdateOauth2ClientRequest())

    def test_update_user(self):
        self.client.update_user(agentidentity_models.UpdateUserRequest())

    def test_update_user_pool(self):
        self.client.update_user_pool(agentidentity_models.UpdateUserPoolRequest())

    def test_userinfo_endpoint(self):
        self.client.userinfo_endpoint(agentidentity_models.UserinfoEndpointRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(AgentidentityClientTest("test_authorize_endpoint"))
    suite.addTest(AgentidentityClientTest("test_batch_acquisition_of_users"))
    suite.addTest(AgentidentityClientTest("test_batch_get_resource_api_key"))
    suite.addTest(AgentidentityClientTest("test_complete_oauth2session"))
    suite.addTest(AgentidentityClientTest("test_create_agent"))
    suite.addTest(AgentidentityClientTest("test_create_credential_provider"))
    suite.addTest(AgentidentityClientTest("test_create_idp_configuration"))
    suite.addTest(AgentidentityClientTest("test_create_oauth2_client"))
    suite.addTest(AgentidentityClientTest("test_create_user"))
    suite.addTest(AgentidentityClientTest("test_create_user_pool"))
    suite.addTest(AgentidentityClientTest("test_delete_agent"))
    suite.addTest(AgentidentityClientTest("test_delete_credential_provider"))
    suite.addTest(AgentidentityClientTest("test_delete_idp_configuration"))
    suite.addTest(AgentidentityClientTest("test_delete_oauth2_client"))
    suite.addTest(AgentidentityClientTest("test_delete_user"))
    suite.addTest(AgentidentityClientTest("test_delete_user_pool"))
    suite.addTest(AgentidentityClientTest("test_disable_idp_configuration"))
    suite.addTest(AgentidentityClientTest("test_enable_idp_configuration"))
    suite.addTest(AgentidentityClientTest("test_get_agent"))
    suite.addTest(AgentidentityClientTest("test_get_credential_provider"))
    suite.addTest(AgentidentityClientTest("test_get_idp_configuration"))
    suite.addTest(AgentidentityClientTest("test_get_oauth2_client"))
    suite.addTest(AgentidentityClientTest("test_get_resource_apikey"))
    suite.addTest(AgentidentityClientTest("test_get_resource_oauth2token"))
    suite.addTest(AgentidentityClientTest("test_get_user"))
    suite.addTest(AgentidentityClientTest("test_get_user_pool"))
    suite.addTest(AgentidentityClientTest("test_get_wat_for_user"))
    suite.addTest(AgentidentityClientTest("test_get_workload_access_token"))
    suite.addTest(AgentidentityClientTest("test_list_agents"))
    suite.addTest(AgentidentityClientTest("test_list_credential_providers"))
    suite.addTest(AgentidentityClientTest("test_list_idp_configurations"))
    suite.addTest(AgentidentityClientTest("test_list_oauth2_clients"))
    suite.addTest(AgentidentityClientTest("test_list_user_pools"))
    suite.addTest(AgentidentityClientTest("test_list_users"))
    suite.addTest(AgentidentityClientTest("test_o_idc_discovery"))
    suite.addTest(AgentidentityClientTest("test_oauth2idp_callback"))
    suite.addTest(AgentidentityClientTest("test_reset_password"))
    suite.addTest(AgentidentityClientTest("test_token_endpoint"))
    suite.addTest(AgentidentityClientTest("test_update_agent"))
    suite.addTest(AgentidentityClientTest("test_update_credential_provider"))
    suite.addTest(AgentidentityClientTest("test_update_idp_configuration"))
    suite.addTest(AgentidentityClientTest("test_update_oauth2_client"))
    suite.addTest(AgentidentityClientTest("test_update_user"))
    suite.addTest(AgentidentityClientTest("test_update_user_pool"))
    suite.addTest(AgentidentityClientTest("test_userinfo_endpoint"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
