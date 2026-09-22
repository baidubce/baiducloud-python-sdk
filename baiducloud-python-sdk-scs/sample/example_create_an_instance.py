"""
Example for scs create_an_instance method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_scs.api.scs_client import ScsClient
from baiducloud_python_sdk_scs import models as scs_models

if __name__ == '__main__':
    try:
        endpoint = ""

        # ==== AK/SK 鉴权 ====
        access_key_id = "Your Ak"
        secret_access_key = "Your Sk"
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )

        client = ScsClient(bce_client_config)

        reservation = scs_models.Reservation(reservation_length=0, reservation_time_unit="")
        billing = scs_models.Billing(payment_timing="", reservation=reservation)
        request = scs_models.CreateAnInstanceRequest(
            billing=billing,
            instance_name="",
            node_type="",
            port=0,
            engine_version="",
            purchase_count=0,
            proxy_num=0,
            cluster_type="",
            client_token="",
            engine=0,
            store_type=0,
            enable_read_only=0,
            shard_num=0,
            disk_flavor=0,
            disk_type="",
            vpc_id="",
            replication_info=[],
            auto_renew_time_unit="",
            auto_renew_time=0,
            bgw_group_id="",
            client_auth="",
            tags=[],
            conf_tpl="",
            resource_group_id="",
            auto_backup_config="",
            deploy_id_list=[],
        )
        res = client.create_an_instance(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
