"""
Example for cce create_node_group_v2 method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_cce.api.cce_client import CceClient
from baiducloud_python_sdk_cce import models as cce_models

if __name__ == '__main__':
    try:
        endpoint = ""

        # ==== AK/SK 鉴权 ====
        access_key_id = "Your Ak"
        secret_access_key = "Your Sk"
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )

        client = CceClient(bce_client_config)
        instance_template = cce_models.InstanceTemplate(
            machine_type="",
            instance_type="",
            instance_name="",
            vpc_config=None,
            instance_resource=None,
            check_gpu_driver=False,
            image_id="",
            user_data=None,
            instance_os=None,
            scale_down_disabled=False,
            is_open_hostname_domain=False,
            need_eip=False,
            eip_option=None,
            iam_role=None,
            deploy_custom_config=None,
            runtime_type="",
            runtime_version="",
            deploy_set_ids=[],
            labels=None,
            annotations=None,
            tags=[],
            taints=[],
            relation_tag=False,
            instance_pre_charging_option=None,
        )
        cluster_autoscaler_spec = cce_models.ClusterAutoscalerSpec(
            enabled=False, min_replicas=0, max_replicas=0, scaling_group_priority=0
        )
        request = cce_models.CreateNodeGroupV2Request(
            cluster_id="",
            instance_group_name="",
            instance_template=instance_template,
            replicas=0,
            cluster_role="",
            shrink_policy="",
            update_policy="",
            clean_policy="",
            cluster_autoscaler_spec=cluster_autoscaler_spec,
        )
        res = client.create_node_group_v2(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
