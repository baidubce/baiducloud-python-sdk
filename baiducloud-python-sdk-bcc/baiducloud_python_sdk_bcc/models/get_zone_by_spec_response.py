"""
Request entity for GetZoneBySpecResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class GetZoneBySpecResponse(BceResponse):
    """
    GetZoneBySpecResponse
    """

    def __init__(self, zone_names=None):
        """
        Initialize GetZoneBySpecResponse response.

        :param zone_names: 可用区列表
        :type zone_names: List[str] (optional)
        """
        super().__init__()
        self.zone_names = zone_names

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
        if self.zone_names is not None:
            result['zoneNames'] = self.zone_names
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetZoneBySpecResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('zoneNames') is not None:
            self.zone_names = m.get('zoneNames')
        return self
