"""
Privatelinks information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Privatelinks(AbstractModel):
    """
    Privatelinks
    """

    def __init__(self, vpc_id=None, subnet_id=None, service_net_id=None, ip_address=None, status=None):
        """
        Initialize Privatelinks instance.

        :param vpc_id: 私有网络 ID
        :type vpc_id: str (optional)

        :param subnet_id: 私有网络子网 ID
        :type subnet_id: str (optional)

        :param service_net_id: 服务网卡 ID
        :type service_net_id: str (optional)

        :param ip_address: 内网解析 IP 地址
        :type ip_address: str (optional)

        :param status: 私有网络状态
        :type status: str (optional)
        """
        super().__init__()
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.service_net_id = service_net_id
        self.ip_address = ip_address
        self.status = status

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.vpc_id is not None:
            result['vpcID'] = self.vpc_id
        if self.subnet_id is not None:
            result['subnetID'] = self.subnet_id
        if self.service_net_id is not None:
            result['serviceNetID'] = self.service_net_id
        if self.ip_address is not None:
            result['ipAddress'] = self.ip_address
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Privatelinks

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('vpcID') is not None:
            self.vpc_id = m.get('vpcID')
        if m.get('subnetID') is not None:
            self.subnet_id = m.get('subnetID')
        if m.get('serviceNetID') is not None:
            self.service_net_id = m.get('serviceNetID')
        if m.get('ipAddress') is not None:
            self.ip_address = m.get('ipAddress')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self
