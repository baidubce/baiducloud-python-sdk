"""
Example for bcm update_alarm_masking method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_bcm.api.bcm_client import BcmClient
from baiducloud_python_sdk_bcm import models as bcm_models

if __name__ == '__main__':
    try:
        # 设置Client的Access Key ID和Secret Access Key，获取AKSK详见:https://cloud.baidu.com/doc/Reference/s/9jwvz2egb
        access_key_id = ""
        secret_access_key = ""
        endpoint = ""
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )
        client = BcmClient(bce_client_config)
        request = bcm_models.UpdateAlarmMaskingRequest(
            id="",
            state="",
            name="",
            scope="",
            resource_type="",
            instances=[],
            region="",
            policy_id="",
            metric_names=[],
            period_type="",
            begin_time="",
            end_time="",
            tz="",
            daily_begin_timestamp=0,
            daily_end_timestamp=0,
        )
        res = client.update_alarm_masking(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
