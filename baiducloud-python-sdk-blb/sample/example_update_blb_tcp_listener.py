"""
Example for blb update_blb_tcp_listener method.
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
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )
        client = BlbClient(bce_client_config)
        request = blb_models.UpdateBlbTcpListenerRequest(
            blb_id="",
            listener_port=0,
            client_token="",
            backend_port=0,
            scheduler="",
            health_check_type="",
            health_check_timeout_in_second=0,
            health_check_interval=0,
            unhealthy_threshold=0,
            healthy_threshold=0,
        )
        res = client.update_blb_tcp_listener(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
