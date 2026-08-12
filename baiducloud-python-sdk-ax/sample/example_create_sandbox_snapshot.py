"""
Example for ax create_sandbox_snapshot method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.auth.api_key_credentials import ApiKeyCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_ax.api.ax_client import AxClient
from baiducloud_python_sdk_ax import models as ax_models

if __name__ == '__main__':
    try:
        endpoint = ""

        # ==== AK/SK 鉴权 ====
        # access_key_id = "Your Ak"
        # secret_access_key = "Your Sk"
        # bce_client_config = BceClientConfiguration(credentials=BceCredentials(access_key_id, secret_access_key),
        # endpoint=endpoint)

        # ==== API Key 鉴权 ====
        api_key = "Your ApiKey"
        bce_client_config = BceClientConfiguration(credentials=ApiKeyCredentials(api_key), endpoint=endpoint)

        client = AxClient(bce_client_config)
        request = ax_models.CreateSandboxSnapshotRequest(sandbox_id="", name="")
        res = client.create_sandbox_snapshot(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
