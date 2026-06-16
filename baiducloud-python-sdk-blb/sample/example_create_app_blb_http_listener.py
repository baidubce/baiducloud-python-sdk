"""
Example for blb create_app_blb_http_listener method.
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
        additional_attributes = blb_models.AdditionalAttributesModel(gzip_json="")
        request = blb_models.CreateAppBlbHttpListenerRequest(
            blb_id="",
            listener_port=0,
            scheduler="",
            client_token="",
            keep_session=False,
            keep_session_type="",
            keep_session_timeout=0,
            keep_session_cookie_name="",
            x_forwarded_for=False,
            x_forwarded_proto=False,
            additional_attributes=additional_attributes,
            server_timeout=0,
            redirect_port=0,
            description="",
        )
        res = client.create_app_blb_http_listener(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
