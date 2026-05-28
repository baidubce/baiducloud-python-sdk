"""
Example for blb update_blb_http_listener method.
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
        additional_attributes = blb_models.AdditionalAttributesModel(gzip_json="")
        request = blb_models.UpdateBlbHttpListenerRequest(
            blb_id="",
            listener_port=0,
            backend_port=0,
            scheduler="",
            keep_session=False,
            keep_session_type="",
            keep_session_duration=0,
            keep_session_cookie_name="",
            x_forward_for=False,
            x_forwarded_proto=False,
            additional_attributes=additional_attributes,
            health_check_type="",
            health_check_port=0,
            health_check_uri="",
            health_check_timeout_in_second=0,
            health_check_interval=0,
            unhealthy_threshold=0,
            healthy_threshold=0,
            health_check_normal_status="",
            health_check_host="",
            server_timeout=0,
            redirect_port=0,
        )
        res = client.update_blb_http_listener(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
