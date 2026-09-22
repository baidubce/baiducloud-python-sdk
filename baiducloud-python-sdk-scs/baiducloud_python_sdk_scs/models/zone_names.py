"""
ZoneNames information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ZoneNames(AbstractModel):
    """
    ZoneNames
    """

    def __init__(self, zone_names=None):
        """
        Initialize ZoneNames instance.

        :param zone_names: 可用区列表
        :type zone_names: List[str] (optional)
        """
        super().__init__()
        self.zone_names = zone_names

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
        if self.zone_names is not None:
            result['zoneNames'] = self.zone_names
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ZoneNames

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('zoneNames') is not None:
            self.zone_names = m.get('zoneNames')
        return self
