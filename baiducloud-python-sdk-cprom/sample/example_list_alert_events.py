"""
Example for cprom list_alert_events method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_cprom.api.cprom_client import CpromClient
from baiducloud_python_sdk_cprom import models as cprom_models

if __name__ == '__main__':
    try:
        # 设置Client的Access Key ID和Secret Access Key，获取AKSK详见:https://cloud.baidu.com/doc/Reference/s/9jwvz2egb
        access_key_id = ""
        secret_access_key = ""
        endpoint = ""
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )
        client = CpromClient(bce_client_config)
        request = cprom_models.ListAlertEventsRequest(
            start_time=0,
            end_time=0,
            page_no=0,
            page_size=0,
            monitor_instance_id="",
            alerting_rule_id="",
            alerting_rule_name="",
            notify_rule_id="",
            notify_rule_name="",
            severity="",
            status="",
            expr="",
            order_by="",
            order="",
            alarm_tags="",
        )
        res = client.list_alert_events(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
