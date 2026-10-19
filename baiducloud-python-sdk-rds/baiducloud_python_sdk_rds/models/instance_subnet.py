"""
InstanceSubnet information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class InstanceSubnet(AbstractModel):
    """
    InstanceSubnet
    """

    def __init__(self, name=None, subnet_id=None, az=None, zone_name=None, cidr=None, short_id=None):
        """
        Initialize InstanceSubnet instance.

        :param name: 子网名称。
        :type name: str (optional)

        :param subnet_id: 子网长ID。
        :type subnet_id: str (optional)

        :param az: 可用区。
        :type az: str (optional)

        :param zone_name: 可用区名称。
        :type zone_name: str (optional)

        :param cidr: Ipv4地址及子网掩码。
        :type cidr: str (optional)

        :param short_id: 子网短ID。
        :type short_id: str (optional)
        """
        super().__init__()
        self.name = name
        self.subnet_id = subnet_id
        self.az = az
        self.zone_name = zone_name
        self.cidr = cidr
        self.short_id = short_id

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
        if self.name is not None:
            result['name'] = self.name
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.az is not None:
            result['az'] = self.az
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.cidr is not None:
            result['cidr'] = self.cidr
        if self.short_id is not None:
            result['shortId'] = self.short_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InstanceSubnet

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('az') is not None:
            self.az = m.get('az')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('cidr') is not None:
            self.cidr = m.get('cidr')
        if m.get('shortId') is not None:
            self.short_id = m.get('shortId')
        return self
