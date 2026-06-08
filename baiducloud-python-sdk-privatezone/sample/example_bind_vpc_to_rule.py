"""
Example for privatezone bind_vpc_to_rule method.
"""

import uuid

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_privatezone.api.privatezone_client import PrivatezoneClient
from baiducloud_python_sdk_privatezone import models as privatezone_models

if __name__ == '__main__':
    try:
        # 设置Client的Access Key ID和Secret Access Key，获取AKSK详见:https://cloud.baidu.com/doc/Reference/s/9jwvz2egb
        access_key_id = ""
        secret_access_key = ""
        endpoint = ""
        config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )
        vpc_region = privatezone_models.VpcRegion(
            region="",
            vpc_ids=[""]
        )
        client = PrivatezoneClient(config)
        # 传入 client_token 让服务端按幂等语义去重，避免并发绑定时返回 RuleBindingException
        request = privatezone_models.BindVpcToRuleRequest(
            rule_id="",
            vpc_regions=[vpc_region],
            client_token=str(uuid.uuid4()),
        )
        try:
            res = client.bind_vpc_to_rule(request)
            print(res.to_json_string())
        except exception.BceHttpClientError as e:
            # RuleBindingException 表示该 rule 上已有绑定任务在进行；服务端会异步完成绑定，
            # 此处视为非致命错误，记录后继续后续流程。
            if getattr(e, 'code', None) == "RuleBindingException":
                print("bind already in progress, request_id=%s" % e.request_id)
            else:
                raise
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
