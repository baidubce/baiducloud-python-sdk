"""
Example for vdb get_price_using_post method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_vdb.api.vdb_client import VdbClient
from baiducloud_python_sdk_vdb import models as vdb_models

if __name__ == '__main__':
    try:
        endpoint = ""

        # ==== AK/SK 鉴权 ====
        access_key_id = "Your Ak"
        secret_access_key = "Your Sk"
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )

        client = VdbClient(bce_client_config)
        instance_param = vdb_models.InstanceParam(
            availability_zone="",
            az_infos=[],
            clone_data_app_backup_id="",
            clone_data_app_id="",
            components=[],
            data_node_num=0,
            disk_flavor=0,
            disk_type="",
            enable_embedding=False,
            enable_encryption=False,
            engine_version="",
            vdb_from="",
            instance_name="",
            instance_num=0,
            instance_type="",
            master_node_spec="",
            master_num=0,
            node_spec="",
            node_type="",
            order_id="",
            password="",
            port=0,
            proxy_node_spec="",
            proxy_num=0,
            req_source="",
            subnet_id="",
            switch_entrance="",
            vpc_id="",
        )
        request = vdb_models.GetPriceUsingPOSTRequest(
            engine_type="",
            auto_renew=False,
            auto_renew_time=0,
            auto_renew_time_unit="",
            components=[],
            duration=0,
            env="",
            instance_param=instance_param,
            product_type="",
            time_unit="",
        )
        res = client.get_price_using_post(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
