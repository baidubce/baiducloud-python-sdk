"""
VpcPrivateIpAddress information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class VpcPrivateIpAddress(AbstractModel):
    """
    VpcPrivateIpAddress
    """

    def __init__(self, cidr=None, private_ip_address=None, private_ip_address_type=None, created_time=None):
        """
        Initialize VpcPrivateIpAddress instance.

        :param cidr: 所属子网CIDR
        :type cidr: str (optional)

        :param private_ip_address: VPC内网IP
        :type private_ip_address: str (optional)

        :param private_ip_address_type: VPC内网IP的类型
        :type private_ip_address_type: str (optional)

        :param created_time: 创建时间
        :type created_time: str (optional)
        """
        super().__init__()
        self.cidr = cidr
        self.private_ip_address = private_ip_address
        self.private_ip_address_type = private_ip_address_type
        self.created_time = created_time

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
        if self.cidr is not None:
            result['cidr'] = self.cidr
        if self.private_ip_address is not None:
            result['privateIpAddress'] = self.private_ip_address
        if self.private_ip_address_type is not None:
            result['privateIpAddressType'] = self.private_ip_address_type
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: VpcPrivateIpAddress

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cidr') is not None:
            self.cidr = m.get('cidr')
        if m.get('privateIpAddress') is not None:
            self.private_ip_address = m.get('privateIpAddress')
        if m.get('privateIpAddressType') is not None:
            self.private_ip_address_type = m.get('privateIpAddressType')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        return self
