"""
SubnetDetail information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SubnetDetail(AbstractModel):
    """
    SubnetDetail
    """

    def __init__(self, cidr=None, physical_zone=None, subnet_id=None, zone_name=None):
        """
        Initialize SubnetDetail instance.

        :param cidr: 子网掩码
        :type cidr: str (optional)

        :param physical_zone: PFS实例所在物理Zone
        :type physical_zone: str (optional)

        :param subnet_id: 子网ID
        :type subnet_id: str (optional)

        :param zone_name: PFS实例所在逻辑Zone
        :type zone_name: str (optional)
        """
        super().__init__()
        self.cidr = cidr
        self.physical_zone = physical_zone
        self.subnet_id = subnet_id
        self.zone_name = zone_name

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
        if self.physical_zone is not None:
            result['physicalZone'] = self.physical_zone
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SubnetDetail

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cidr') is not None:
            self.cidr = m.get('cidr')
        if m.get('physicalZone') is not None:
            self.physical_zone = m.get('physicalZone')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        return self
