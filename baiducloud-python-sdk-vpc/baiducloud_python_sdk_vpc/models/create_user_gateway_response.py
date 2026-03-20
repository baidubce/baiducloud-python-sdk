"""
Request entity for CreateUserGatewayResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateUserGatewayResponse(BceResponse):
    """
    CreateUserGatewayResponse
    """

    def __init__(self, cgw_id=None):
        """
        Initialize CreateUserGatewayResponse response.

        :param cgw_id: 用户网关id
        :type cgw_id: str (optional)
        """
        super().__init__()
        self.cgw_id = cgw_id

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
        if self.cgw_id is not None:
            result['cgwId'] = self.cgw_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateUserGatewayResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cgwId') is not None:
            self.cgw_id = m.get('cgwId')
        return self
