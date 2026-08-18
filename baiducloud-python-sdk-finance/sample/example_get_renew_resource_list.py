"""
Example for finance get_renew_resource_list method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_finance.api.finance_client import FinanceClient
from baiducloud_python_sdk_finance import models as finance_models

if __name__ == '__main__':
    try:
        endpoint = ""

        # ==== AK/SK 鉴权 ====
        access_key_id = "Your Ak"
        secret_access_key = "Your Sk"
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )

        client = FinanceClient(bce_client_config)
        request = finance_models.GetRenewResourceListRequest(
            service_type="",
            query_account_id="",
            region="",
            expired_days=0,
            short_or_instance_ids=[],
            page_no=0,
            page_size=0,
        )
        res = client.get_renew_resource_list(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
