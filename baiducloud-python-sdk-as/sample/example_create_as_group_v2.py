"""
Example for as create_as_group_v2 method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_as.api.as_client import AsClient
from baiducloud_python_sdk_as import models as as_models

if __name__ == '__main__':
    try:
        # 设置Client的Access Key ID和Secret Access Key，获取AKSK详见:https://cloud.baidu.com/doc/Reference/s/9jwvz2egb
        access_key_id = ""
        secret_access_key = ""
        endpoint = ""
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )
        client = AsClient(bce_client_config)
        config = as_models.GroupConfig(min_node_num=0, max_node_num=0, cooldown_in_sec=0, expect_num=0, init_num=0)
        eip = as_models.EipInfo(if_bind_eip=False, bandwidth_in_mbps=0, eip_product_type="", purchase_type="")

        increase = as_models.EipGroupIncrease(enabled=False, strategy="")

        decrease = as_models.EipGroupDecrease(enabled=False)

        bandwidth = as_models.EipGroupBandwidth(max=0, min=0, standard=0)
        eip_config = as_models.EipConfig(
            eip_group_bind_strategy="",
            eip_group_unbind_strategy="",
            eip_group_id_list=[],
            increase=increase,
            decrease=decrease,
            bandwidth=bandwidth,
        )

        reservation = as_models.Reservation(reservation_length_in_month=0)
        billing = as_models.BillingInfo(payment_timing="", reservation=reservation)
        health_check = as_models.HealthCheckConfig(health_check_interval=0, grace_time=0)
        assign_tag_info = as_models.AssignTagInfo(resource_id="", relation_tag=False, tags=[])
        cmd_config = as_models.CmdConfig(
            has_decrease_cmd=False,
            dec_cmd_strategy="",
            dec_cmd_data="",
            dec_cmd_timeout=0,
            dec_cmd_manual=False,
            has_increase_cmd=False,
            inc_cmd_strategy="",
            inc_cmd_data="",
            inc_cmd_timeout=0,
            inc_cmd_manual=False,
        )
        bcc_name_config = as_models.BccNameConfig(
            bcc_name="", bcc_hostname="", auto_seq_suffix=False, open_hostname_domain=False
        )
        request = as_models.CreateAsGroupV2Request(
            group_name="",
            zone_info=[],
            config=config,
            nodes=[],
            assign_tag_info=assign_tag_info,
            cmd_config=cmd_config,
            keypair_id="",
            keypair_name="",
            keep_image_login=0,
            blb=[],
            blb_unbind_wait_time=0,
            eip=eip,
            eip_config=eip_config,
            billing=billing,
            rds=[],
            scs=[],
            health_check=health_check,
            expansion_strategy="",
            shrinkage_strategy="",
            bcc_name_config=bcc_name_config,
        )
        res = client.create_as_group_v2(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
