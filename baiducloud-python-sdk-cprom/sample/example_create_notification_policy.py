"""
Example for cprom create_notification_policy method.
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
        repeat_notify_config = cprom_models.RepeatNotifyConfig(
            enabled=False, interval_hour=0, interval_min=0, max_count=0, strategy=""
        )
        request = cprom_models.CreateNotificationPolicyRequest(
            notify_rule_name="",
            start_time="",
            end_time="",
            channel=[],
            receiver_type="",
            users=[],
            user_groups=[],
            webhook_config_list=[],
            escalate_config_list=[],
            repeat_notify_config=repeat_notify_config,
        )
        res = client.create_notification_policy(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
