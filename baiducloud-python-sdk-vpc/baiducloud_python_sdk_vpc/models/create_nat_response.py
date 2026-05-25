"""
Request entity for CreateNatResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateNatResponse(BceResponse):
    """
    CreateNatResponse
    """

    def __init__(self, nat_id=None):
        """
        Initialize CreateNatResponse response.

        :param nat_id: 创建的NAT的ID
        :type nat_id: str (optional)
        """
        super().__init__()
        self.nat_id = nat_id

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
        if self.nat_id is not None:
            result['natId'] = self.nat_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateNatResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('natId') is not None:
            self.nat_id = m.get('natId')
        return self
