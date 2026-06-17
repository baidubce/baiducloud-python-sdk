"""
ZoneModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ZoneModel(AbstractModel):
    """
    ZoneModel
    """

    def __init__(self, zone_name=None):
        """
        Initialize ZoneModel instance.

        :param zone_name: 可用区名称
        :type zone_name: str (optional)
        """
        super().__init__()
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
        :rtype: ZoneModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        return self
