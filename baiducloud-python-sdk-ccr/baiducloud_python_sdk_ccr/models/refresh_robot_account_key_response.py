"""
Request entity for RefreshRobotAccountKeyResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class RefreshRobotAccountKeyResponse(BceResponse):
    """
    RefreshRobotAccountKeyResponse
    """

    def __init__(self, secret=None):
        """
        Initialize RefreshRobotAccountKeyResponse response.

        :param secret: 账号密码
        :type secret: str (optional)
        """
        super().__init__()
        self.secret = secret

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
        if self.secret is not None:
            result['secret'] = self.secret
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RefreshRobotAccountKeyResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('secret') is not None:
            self.secret = m.get('secret')
        return self
