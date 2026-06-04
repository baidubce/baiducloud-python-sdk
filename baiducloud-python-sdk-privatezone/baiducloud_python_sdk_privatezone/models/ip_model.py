"""
IpModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class IpModel(AbstractModel):
    """
    IpModel
    """

    def __init__(self, subnet_id=None, ip_address=None):
        """
        Initialize IpModel instance.

        :param subnet_id: 子网 ID
        :type subnet_id: str (optional)

        :param ip_address: 子网掩码参数范围内的 IP 地址（留空则系统自动分配）
        :type ip_address: str (optional)
        """
        super().__init__()
        self.subnet_id = subnet_id
        self.ip_address = ip_address

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
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.ip_address is not None:
            result['ipAddress'] = self.ip_address
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: IpModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('ipAddress') is not None:
            self.ip_address = m.get('ipAddress')
        return self
