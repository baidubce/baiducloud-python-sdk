"""
Example for bcm describe_dimension_values method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_bcm.api.bcm_client import BcmClient
from baiducloud_python_sdk_bcm import models as bcm_models

if __name__ == '__main__':
    try:
        endpoint = ""

        # ==== AK/SK 鉴权 ====
        access_key_id = "Your Ak"
        secret_access_key = "Your Sk"
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )

        client = BcmClient(bce_client_config)
        request = bcm_models.DescribeDimensionValuesRequest(
            action="",
            scope="",
            begin_datetime="",
            end_datetime="",
            metric_name="",
            dimension_key="",
            filters=[],
            resource_type="",
            region="",
        )
        res = client.describe_dimension_values(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
