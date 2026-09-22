"""
Subnet information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Subnet(AbstractModel):
    """
    Subnet
    """

    def __init__(self, name=None, subnet_id=None, zone_name=None, cidr=None, vpc_id=None):
        """
        Initialize Subnet instance.

        :param name: 子网名
        :type name: str (optional)

        :param subnet_id: 子网Id
        :type subnet_id: str (optional)

        :param zone_name: 子网所在可用区
        :type zone_name: str (optional)

        :param cidr: 子网cidr
        :type cidr: str (optional)

        :param vpc_id: 所属vpc的id
        :type vpc_id: str (optional)
        """
        super().__init__()
        self.name = name
        self.subnet_id = subnet_id
        self.zone_name = zone_name
        self.cidr = cidr
        self.vpc_id = vpc_id

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
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.cidr is not None:
            result['cidr'] = self.cidr
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Subnet

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('cidr') is not None:
            self.cidr = m.get('cidr')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self
