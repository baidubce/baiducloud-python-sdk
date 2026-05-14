"""
Request entity for CreateSnicResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateSnicResponse(BceResponse):
    """
    CreateSnicResponse
    """

    def __init__(self, id=None, ip_address=None):
        """
        Initialize CreateSnicResponse response.

        :param id: 服务网卡的id
        :type id: str (optional)

        :param ip_address: ip地址
        :type ip_address: str (optional)
        """
        super().__init__()
        self.id = id
        self.ip_address = ip_address

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
        if self.id is not None:
            result['id'] = self.id
        if self.ip_address is not None:
            result['ipAddress'] = self.ip_address
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateSnicResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('ipAddress') is not None:
            self.ip_address = m.get('ipAddress')
        return self
