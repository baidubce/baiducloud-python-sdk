"""
SubnetMap information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SubnetMap(AbstractModel):
    """
    SubnetMap
    """

    def __init__(self, zone_name=None, subnet_id=None):
        """
        Initialize SubnetMap instance.

        :param zone_name: 可用区
        :type zone_name: str (optional)

        :param subnet_id: 子网ID
        :type subnet_id: str (optional)
        """
        super().__init__()
        self.zone_name = zone_name
        self.subnet_id = subnet_id

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
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SubnetMap

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        return self
