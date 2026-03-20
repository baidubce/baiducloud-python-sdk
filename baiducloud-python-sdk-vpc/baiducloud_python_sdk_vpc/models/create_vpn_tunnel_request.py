"""
Request entity for CreateVpnTunnelRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_vpc.models.ike_config import IkeConfig
from baiducloud_python_sdk_vpc.models.ipsec_config import IpsecConfig


class CreateVpnTunnelRequest(AbstractModel):
    """
    Request entity for CreateVpnTunnelRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        vpn_id,
        secret_key,
        local_subnets,
        cgw_id,
        remote_subnets,
        vpn_conn_name,
        ike_config,
        ipsec_config,
        client_token=None,
        description=None,
    ):
        """
        Initialize CreateVpnTunnelRequest request entity.

        :param vpn_id: vpn_id parameter
        :type vpn_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param secret_key: 共享秘钥，8～17位字符，英文、数字和符号必须同时存在，符号仅限!@#$%^*()_
        :type secret_key: str (required)

        :param local_subnets: 本端网络cidr列表
        :type local_subnets: List[str] (required)

        :param cgw_id: 用户网关ID
        :type cgw_id: str (required)

        :param remote_subnets: 对端网络cidr列表
        :type remote_subnets: List[str] (required)

        :param description: 描述
        :type description: str (optional)

        :param vpn_conn_name: VPN隧道名称，大小写字母、数字以及-_/.特殊字符，必须以字母开头，长度1-65
        :type vpn_conn_name: str (required)

        :param ike_config: ike_config parameter
        :type ike_config: IkeConfig (required)

        :param ipsec_config: ipsec_config parameter
        :type ipsec_config: IpsecConfig (required)
        """
        super().__init__()
        self.vpn_id = vpn_id
        self.client_token = client_token
        self.secret_key = secret_key
        self.local_subnets = local_subnets
        self.cgw_id = cgw_id
        self.remote_subnets = remote_subnets
        self.description = description
        self.vpn_conn_name = vpn_conn_name
        self.ike_config = ike_config
        self.ipsec_config = ipsec_config

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.secret_key is not None:
            result['secretKey'] = self.secret_key
        if self.local_subnets is not None:
            result['localSubnets'] = self.local_subnets
        if self.cgw_id is not None:
            result['cgwId'] = self.cgw_id
        if self.remote_subnets is not None:
            result['remoteSubnets'] = self.remote_subnets
        if self.description is not None:
            result['description'] = self.description
        if self.vpn_conn_name is not None:
            result['vpnConnName'] = self.vpn_conn_name
        if self.ike_config is not None:
            result['ikeConfig'] = self.ike_config.to_dict()
        if self.ipsec_config is not None:
            result['ipsecConfig'] = self.ipsec_config.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateVpnTunnelRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('vpnId') is not None:
            self.vpn_id = m.get('vpnId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('secretKey') is not None:
            self.secret_key = m.get('secretKey')
        if m.get('localSubnets') is not None:
            self.local_subnets = m.get('localSubnets')
        if m.get('cgwId') is not None:
            self.cgw_id = m.get('cgwId')
        if m.get('remoteSubnets') is not None:
            self.remote_subnets = m.get('remoteSubnets')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('vpnConnName') is not None:
            self.vpn_conn_name = m.get('vpnConnName')
        if m.get('ikeConfig') is not None:
            self.ike_config = IkeConfig().from_dict(m.get('ikeConfig'))
        if m.get('ipsecConfig') is not None:
            self.ipsec_config = IpsecConfig().from_dict(m.get('ipsecConfig'))
        return self
