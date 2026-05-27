"""
Example for blb create_app_blb_server_group_port method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_blb.api.blb_client import BlbClient
from baiducloud_python_sdk_blb import models as blb_models

if __name__ == '__main__':
    try:
        # 设置Client的Access Key ID和Secret Access Key，获取AKSK详见:https://cloud.baidu.com/doc/Reference/s/9jwvz2egb
        access_key_id = ""
        secret_access_key = ""
        endpoint = ""
        config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )
        client = BlbClient(config)
        request = blb_models.CreateAppBlbServerGroupPortRequest(
            blb_id="",
            sg_id="",
            port=0,
            type="",
            client_token="",
            enable_health_check=False,
            health_check="",
            health_check_port=0,
            health_check_url_path="",
            health_check_timeout_in_second=0,
            health_check_interval_in_second=0,
            health_check_down_retry=0,
            health_check_up_retry=0,
            health_check_normal_status="",
            health_check_host="",
            udp_health_check_string="",
        )
        res = client.create_app_blb_server_group_port(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
