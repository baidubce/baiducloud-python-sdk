"""
Example for as create_rule_v2 method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_as.api.as_client import AsClient
from baiducloud_python_sdk_as import models as as_models

if __name__ == '__main__':
    try:
        # 设置Client的Access Key ID和Secret Access Key，获取AKSK详见:https://cloud.baidu.com/doc/Reference/s/9jwvz2egb
        access_key_id = ""
        secret_access_key = ""
        endpoint = ""
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )
        client = AsClient(bce_client_config)

        monitor_object = as_models.MonitorObject(type="", names=[], resources=[], type_name="")
        as_alarm_rule = as_models.AsAlarmRule(
            id=0,
            scope="",
            monitor_object=monitor_object,
            rules=[],
            alarm_name="",
            alias_name="",
            insufficient_cycle=0,
            policy_enabled=False,
            rule_contents=[],
            rule_contents_en=[],
            source="",
            component_type="",
            alarm_actions=[],
            ok_actions=[],
            insufficient_actions=[],
        )
        request = as_models.CreateRuleV2Request(
            rule_name="",
            group_id="",
            state="",
            type="",
            action_type="",
            action_num=0,
            cooldown_in_sec=0,
            cron_time="",
            period_type="",
            period_value=0,
            period_start_time="",
            period_end_time="",
            as_alarm_rule=as_alarm_rule,
        )
        res = client.create_rule_v2(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
