"""
Request entity for ListZonesResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcc.models.zone_model import ZoneModel


class ListZonesResponse(BceResponse):
    """
    ListZonesResponse
    """

    def __init__(self, zones=None):
        """
        Initialize ListZonesResponse response.

        :param zones: 可用区列表信息
        :type zones: List[ZoneModel] (optional)
        """
        super().__init__()
        self.zones = zones

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.zones is not None:
            result['zones'] = [i.to_dict() for i in self.zones]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListZonesResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('zones') is not None:
            self.zones = [ZoneModel().from_dict(i) for i in m.get('zones')]
        return self
