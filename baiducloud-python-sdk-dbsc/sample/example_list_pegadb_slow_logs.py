"""
Example for dbsc list_pegadb_slow_logs method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_dbsc.api.dbsc_client import DbscClient
from baiducloud_python_sdk_dbsc import models as dbsc_models

if __name__ == '__main__':
    try:
        endpoint = ""

        # ==== AK/SK 鉴权 ====
        access_key_id = "Your Ak"
        secret_access_key = "Your Sk"
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )

        client = DbscClient(bce_client_config)
        request = dbsc_models.ListPegadbSlowLogsRequest(
            app_id="", node_id="", start="", end="", db_engine="", page=0, page_size=0, order_by="", order=""
        )
        res = client.list_pegadb_slow_logs(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
