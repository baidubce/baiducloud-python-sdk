"""
Request entity for CreatePrivateZoneRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreatePrivateZoneRequest(AbstractModel):
    """
    Request entity for CreatePrivateZoneRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, zone_name, client_token=None):
        """
        Initialize CreatePrivateZoneRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param zone_name: Zone名称，由两个及其以上的字母或者数字组成，最大长度不能超过240
        :type zone_name: str (required)
        """
        super().__init__()
        self.client_token = client_token
        self.zone_name = zone_name

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
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
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreatePrivateZoneRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        return self
