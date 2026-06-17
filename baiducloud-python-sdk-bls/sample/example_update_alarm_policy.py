"""
Example for bls update_alarm_policy method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_bls.api.bls_client import BlsClient
from baiducloud_python_sdk_bls import models as bls_models

if __name__ == '__main__':
    try:
        # 设置Client的Access Key ID和Secret Access Key，获取AKSK详见:https://cloud.baidu.com/doc/Reference/s/9jwvz2egb
        access_key_id = ""
        secret_access_key = ""
        endpoint = ""
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )
        client = BlsClient(bce_client_config)
        schedule = bls_models.Schedule(interval_minute=0, fix_time_minute=0, day_of_week=0)
        request = bls_models.UpdateAlarmPolicyRequest(
            name="",
            targets=[],
            trigger_conditions=[],
            schedule=schedule,
            pending_count=0,
            notices=[],
            objects=[],
            groups=[],
            repeat_interval_minute=0,
            recover_without_notice=False,
            state="",
            notice_state="",
            notice_raw_logs=[],
        )
        res = client.update_alarm_policy(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
