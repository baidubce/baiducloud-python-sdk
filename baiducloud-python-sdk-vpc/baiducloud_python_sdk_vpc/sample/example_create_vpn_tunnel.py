"""
This module demonstrates how to create a VPN tunnel using Baidu Cloud Python SDK.
It includes setting up credentials, configuring the client, and making the API call.
"""
from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_vpc.api.vpc_client import VpcClient
from baiducloud_python_sdk_vpc.models.ipsec_config import IpsecConfig
from baiducloud_python_sdk_vpc.models.create_vpn_tunnel_request import CreateVpnTunnelRequest
from baiducloud_python_sdk_vpc.models.ike_config import IkeConfig

if __name__ == '__main__':
    try:
        # 设置Client的Access Key ID和Secret Access Key，获取AKSK详见:https://cloud.baidu.com/doc/Reference/s/9jwvz2egb
        access_key_id = ""
        secret_access_key = ""
        endpoint = ""
        config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), 
            endpoint=endpoint
        )
        client = VpcClient(config)
        ike_config = IkeConfig(
            ike_version="", 
            ike_mode="", 
            ike_enc_alg="", 
            ike_auth_alg="", 
            ike_pfs="", 
            ike_life_time=""
        )
        ipsec_config = IpsecConfig(
            ipsec_enc_alg="", 
            ipsec_auth_alg="", 
            ipsec_pfs="", 
            ipsec_lifetime=""
        )
        request = CreateVpnTunnelRequest(
            vpn_id="", 
            secret_key="", 
            local_subnets=[], 
            cgw_id="", 
            remote_subnets=[], 
            vpn_conn_name="", 
            ike_config=ike_config, 
            ipsec_config=ipsec_config, 
            client_token="", 
            description=""
        )
        res = client.create_vpn_tunnel(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)