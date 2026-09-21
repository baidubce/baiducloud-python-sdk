"""
Request entity for PasswordUsingGETResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class PasswordUsingGETResponse(BceResponse):
    """
    PasswordUsingGETResponse
    """

    def __init__(self, password=None, username=None):
        """
        Initialize PasswordUsingGETResponse response.

        :param password: password field
        :type password: str (optional)

        :param username: username field
        :type username: str (optional)
        """
        super().__init__()
        self.password = password
        self.username = username

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
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PasswordUsingGETResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self
