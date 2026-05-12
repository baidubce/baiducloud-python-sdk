"""
Request entity for CreateAPrivateZoneResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateAPrivateZoneResponse(BceResponse):
    """
    CreateAPrivateZoneResponse
    """

    def __init__(self, zone_id=None):
        """
        Initialize CreateAPrivateZoneResponse response.

        :param zone_id: Zone的ID
        :type zone_id: str (optional)
        """
        super().__init__()
        self.zone_id = zone_id

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
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateAPrivateZoneResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self
