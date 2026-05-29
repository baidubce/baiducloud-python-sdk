"""
ClientInfoModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ClientInfoModel(AbstractModel):
    """
    ClientInfoModel
    """

    def __init__(self, zone=None, vpc_id=None, mount_id=None, client_ip=None):
        """
        Initialize ClientInfoModel instance.

        :param zone: 可用区
        :type zone: str (optional)

        :param vpc_id: VPC ID
        :type vpc_id: str (optional)

        :param mount_id: 挂载点 ID
        :type mount_id: str (optional)

        :param client_ip: 客户端 IP 地址
        :type client_ip: str (optional)
        """
        super().__init__()
        self.zone = zone
        self.vpc_id = vpc_id
        self.mount_id = mount_id
        self.client_ip = client_ip

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
        if self.zone is not None:
            result['zone'] = self.zone
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.mount_id is not None:
            result['mountId'] = self.mount_id
        if self.client_ip is not None:
            result['clientIp'] = self.client_ip
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ClientInfoModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('zone') is not None:
            self.zone = m.get('zone')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('mountId') is not None:
            self.mount_id = m.get('mountId')
        if m.get('clientIp') is not None:
            self.client_ip = m.get('clientIp')
        return self
