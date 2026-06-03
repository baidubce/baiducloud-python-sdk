"""
Request entity for CreateTemporaryPasswordResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateTemporaryPasswordResponse(BceResponse):
    """
    CreateTemporaryPasswordResponse
    """

    def __init__(self, password=None):
        """
        Initialize CreateTemporaryPasswordResponse response.

        :param password: 临时密码
        :type password: str (optional)
        """
        super().__init__()
        self.password = password

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
        if self.password is not None:
            result['password'] = self.password
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateTemporaryPasswordResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('password') is not None:
            self.password = m.get('password')
        return self
