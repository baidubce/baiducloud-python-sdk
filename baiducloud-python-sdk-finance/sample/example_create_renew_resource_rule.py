"""
Example for finance create_renew_resource_rule method.
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
        request = finance_models.CreateRenewResourceRuleRequest(
            service_type="", region="", instance_id="", renew_time_unit="", renew_time="", account_id=""
        )
        res = client.create_renew_resource_rule(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
