"""
Example for apm apm_describe_alarms method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_apm.api.apm_client import ApmClient
from baiducloud_python_sdk_apm import models as apm_models

if __name__ == '__main__':
    try:
        # 设置Client的Access Key ID和Secret Access Key，获取AKSK详见:https://cloud.baidu.com/doc/Reference/s/9jwvz2egb
        access_key_id = ""
        secret_access_key = ""
        endpoint = ""
        config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )
        client = ApmClient(config)
        request = apm_models.ApmDescribeAlarmsRequest(
            begin_datetime="",
            end_datetime="",
            page_no=0,
            page_size=0,
            policy_name="",
            level="",
            metric_kind="",
            state="",
            order_by="",
            order="",
        )
        res = client.apm_describe_alarms(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
