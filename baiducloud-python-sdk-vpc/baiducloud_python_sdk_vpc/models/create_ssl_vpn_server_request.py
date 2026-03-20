"""
Request entity for CreateSslVpnServerRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateSslVpnServerRequest(AbstractModel):
    """
    Request entity for CreateSslVpnServerRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        vpn_id,
        ssl_vpn_server_name,
        local_subnets,
        remote_subnet,
        client_token=None,
        interface_type=None,
        client_dns=None,
    ):
        """
        Initialize CreateSslVpnServerRequest request entity.

        :param vpn_id: vpn_id parameter
        :type vpn_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param ssl_vpn_server_name: SSL-VPN服务端实例名称，大小写字母、数字以及-_/.特殊字符，必须以字母开头，长度1-65
        :type ssl_vpn_server_name: str (required)

        :param interface_type: SSL-VPN服务端接口类型。取值[tap, tun]，默认为“tap”
        :type interface_type: str (optional)

        :param local_subnets: 本端网络CIDR列表
        :type local_subnets: List[str] (required)

        :param remote_subnet: 客户端网络CIDR
        :type remote_subnet: str (required)

        :param client_dns: 客户端的DNS地址
        :type client_dns: str (optional)
        """
        super().__init__()
        self.vpn_id = vpn_id
        self.client_token = client_token
        self.ssl_vpn_server_name = ssl_vpn_server_name
        self.interface_type = interface_type
        self.local_subnets = local_subnets
        self.remote_subnet = remote_subnet
        self.client_dns = client_dns

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
        if self.ssl_vpn_server_name is not None:
            result['sslVpnServerName'] = self.ssl_vpn_server_name
        if self.interface_type is not None:
            result['interfaceType'] = self.interface_type
        if self.local_subnets is not None:
            result['localSubnets'] = self.local_subnets
        if self.remote_subnet is not None:
            result['remoteSubnet'] = self.remote_subnet
        if self.client_dns is not None:
            result['clientDns'] = self.client_dns
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateSslVpnServerRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('vpnId') is not None:
            self.vpn_id = m.get('vpnId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('sslVpnServerName') is not None:
            self.ssl_vpn_server_name = m.get('sslVpnServerName')
        if m.get('interfaceType') is not None:
            self.interface_type = m.get('interfaceType')
        if m.get('localSubnets') is not None:
            self.local_subnets = m.get('localSubnets')
        if m.get('remoteSubnet') is not None:
            self.remote_subnet = m.get('remoteSubnet')
        if m.get('clientDns') is not None:
            self.client_dns = m.get('clientDns')
        return self
