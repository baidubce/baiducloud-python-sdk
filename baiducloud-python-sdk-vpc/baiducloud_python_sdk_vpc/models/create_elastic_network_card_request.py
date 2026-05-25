"""
Request entity for CreateElasticNetworkCardRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_vpc.models.private_ip import PrivateIP
from baiducloud_python_sdk_vpc.models.private_ip import PrivateIP


class CreateElasticNetworkCardRequest(AbstractModel):
    """
    Request entity for CreateElasticNetworkCardRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        name,
        subnet_id,
        private_ip_set,
        client_token=None,
        security_group_ids=None,
        enterprise_security_group_ids=None,
        ipv6_private_ip_set=None,
        description=None,
        network_interface_traffic_mode=None,
    ):
        """
        Initialize CreateElasticNetworkCardRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: 弹性网卡的名称
        :type name: str (required)

        :param subnet_id: 弹性网卡所属的子网ID
        :type subnet_id: str (required)

        :param security_group_ids: 指定绑定的普通安全组集合
        :type security_group_ids: List[str] (optional)

        :param enterprise_security_group_ids: 指定绑定的企业安全组集合
        :type enterprise_security_group_ids: List[str] (optional)

        :param private_ip_set: 指定的内网IPv4 IP信息
        :type private_ip_set: List[PrivateIP] (required)

        :param ipv6_private_ip_set: 指定的内网IPv6 IP信息
        :type ipv6_private_ip_set: List[PrivateIP] (optional)

        :param description: 弹性网卡描述
        :type description: str (optional)

        :param network_interface_traffic_mode: 区分创建弹性RDMA网卡（ERI）和普通弹性网卡（ENI）
        :type network_interface_traffic_mode: str (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.name = name
        self.subnet_id = subnet_id
        self.security_group_ids = security_group_ids
        self.enterprise_security_group_ids = enterprise_security_group_ids
        self.private_ip_set = private_ip_set
        self.ipv6_private_ip_set = ipv6_private_ip_set
        self.description = description
        self.network_interface_traffic_mode = network_interface_traffic_mode

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
        if self.name is not None:
            result['name'] = self.name
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.security_group_ids is not None:
            result['securityGroupIds'] = self.security_group_ids
        if self.enterprise_security_group_ids is not None:
            result['enterpriseSecurityGroupIds'] = self.enterprise_security_group_ids
        if self.private_ip_set is not None:
            result['privateIpSet'] = [i.to_dict() for i in self.private_ip_set]
        if self.ipv6_private_ip_set is not None:
            result['ipv6PrivateIpSet'] = [i.to_dict() for i in self.ipv6_private_ip_set]
        if self.description is not None:
            result['description'] = self.description
        if self.network_interface_traffic_mode is not None:
            result['networkInterfaceTrafficMode'] = self.network_interface_traffic_mode
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateElasticNetworkCardRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('securityGroupIds') is not None:
            self.security_group_ids = m.get('securityGroupIds')
        if m.get('enterpriseSecurityGroupIds') is not None:
            self.enterprise_security_group_ids = m.get('enterpriseSecurityGroupIds')
        if m.get('privateIpSet') is not None:
            self.private_ip_set = [PrivateIP().from_dict(i) for i in m.get('privateIpSet')]
        if m.get('ipv6PrivateIpSet') is not None:
            self.ipv6_private_ip_set = [PrivateIP().from_dict(i) for i in m.get('ipv6PrivateIpSet')]
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('networkInterfaceTrafficMode') is not None:
            self.network_interface_traffic_mode = m.get('networkInterfaceTrafficMode')
        return self
