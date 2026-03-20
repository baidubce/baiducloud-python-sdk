"""
Request entity for CreateTbspResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateTbspResponse(BceResponse):
    """
    CreateTbspResponse
    """

    def __init__(self, id=None):
        """
        Initialize CreateTbspResponse response.

        :param id: DDoS增强防护包id
        :type id: str (optional)
        """
        super().__init__()
        self.id = id

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
            result['metadata'] = self.metadata
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateTbspResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        return self
