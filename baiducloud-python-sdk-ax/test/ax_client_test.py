import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.auth.api_key_credentials import ApiKeyCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_ax.api.ax_client import AxClient
from baiducloud_python_sdk_ax import models as ax_models


class AxClientTest(unittest.TestCase):
    """AxClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        API_KEY = ''

        # ==== AK/SK 鉴权 ====
        # config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)

        # ==== API Key 鉴权 ====
        config = BceClientConfiguration(credentials=ApiKeyCredentials(API_KEY), endpoint=HOST)

        self.client = AxClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_batch_release_sandboxes(self):
        self.client.batch_release_sandboxes(ax_models.BatchReleaseSandboxesRequest())

    def test_connect_sandbox(self):
        self.client.connect_sandbox(ax_models.ConnectSandboxRequest())

    def test_create_sandbox(self):
        self.client.create_sandbox(ax_models.CreateSandboxRequest())

    def test_create_sandbox_snapshot(self):
        self.client.create_sandbox_snapshot(ax_models.CreateSandboxSnapshotRequest())

    def test_delete_sandbox(self):
        self.client.delete_sandbox(ax_models.DeleteSandboxRequest())

    def test_fork_sandbox(self):
        self.client.fork_sandbox(ax_models.ForkSandboxRequest())

    def test_get_sandbox(self):
        self.client.get_sandbox(ax_models.GetSandboxRequest())

    def test_get_sandbox_resources(self):
        self.client.get_sandbox_resources(ax_models.GetSandboxResourcesRequest())

    def test_get_sandbox_snapshot(self):
        self.client.get_sandbox_snapshot(ax_models.GetSandboxSnapshotRequest())

    def test_list_sandbox_snapshots(self):
        self.client.list_sandbox_snapshots(ax_models.ListSandboxSnapshotsRequest())

    def test_list_sandboxes(self):
        self.client.list_sandboxes(ax_models.ListSandboxesRequest())

    def test_list_sandboxes_v2(self):
        self.client.list_sandboxes_v2(ax_models.ListSandboxesV2Request())

    def test_list_sandboxes_v2_by_path(self):
        self.client.list_sandboxes_v2_by_path(ax_models.ListSandboxesV2ByPathRequest())

    def test_pause_sandbox(self):
        self.client.pause_sandbox(ax_models.PauseSandboxRequest())

    def test_query_sandboxes(self):
        self.client.query_sandboxes(ax_models.QuerySandboxesRequest())

    def test_resume_sandbox(self):
        self.client.resume_sandbox(ax_models.ResumeSandboxRequest())

    def test_set_sandbox_timeout(self):
        self.client.set_sandbox_timeout(ax_models.SetSandboxTimeoutRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(AxClientTest("test_batch_release_sandboxes"))
    suite.addTest(AxClientTest("test_connect_sandbox"))
    suite.addTest(AxClientTest("test_create_sandbox"))
    suite.addTest(AxClientTest("test_create_sandbox_snapshot"))
    suite.addTest(AxClientTest("test_delete_sandbox"))
    suite.addTest(AxClientTest("test_fork_sandbox"))
    suite.addTest(AxClientTest("test_get_sandbox"))
    suite.addTest(AxClientTest("test_get_sandbox_resources"))
    suite.addTest(AxClientTest("test_get_sandbox_snapshot"))
    suite.addTest(AxClientTest("test_list_sandbox_snapshots"))
    suite.addTest(AxClientTest("test_list_sandboxes"))
    suite.addTest(AxClientTest("test_list_sandboxes_v2"))
    suite.addTest(AxClientTest("test_list_sandboxes_v2_by_path"))
    suite.addTest(AxClientTest("test_pause_sandbox"))
    suite.addTest(AxClientTest("test_query_sandboxes"))
    suite.addTest(AxClientTest("test_resume_sandbox"))
    suite.addTest(AxClientTest("test_set_sandbox_timeout"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
