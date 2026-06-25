"""
Example for cprom update_pod_monitor method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_cprom.api.cprom_client import CpromClient
from baiducloud_python_sdk_cprom import models as cprom_models

if __name__ == '__main__':
    try:
        # 设置Client的Access Key ID和Secret Access Key，获取AKSK详见:https://cloud.baidu.com/doc/Reference/s/9jwvz2egb
        access_key_id = ""
        secret_access_key = ""
        endpoint = ""
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )
        client = CpromClient(bce_client_config)

        metadata = cprom_models.ObjectMeta(name="", namespace="")

        namespace_selector = cprom_models.NamespaceSelector(match_names=[])
        selector = cprom_models.LabelSelector(match_labels=None)
        spec = cprom_models.PodMonitorSpec(
            namespace_selector=namespace_selector, pod_metrics_endpoints=[], selector=selector
        )
        pod_monitor = cprom_models.PodMonitor(api_version="", kind="", metadata=metadata, spec=spec)
        request = cprom_models.UpdatePodMonitorRequest(
            pod_monitor_name="", instance_id="", agent_id="", enable="", pod_monitor=pod_monitor
        )
        res = client.update_pod_monitor(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
