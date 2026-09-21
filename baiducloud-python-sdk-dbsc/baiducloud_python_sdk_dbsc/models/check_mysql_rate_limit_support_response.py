"""
Request entity for CheckMysqlRateLimitSupportResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CheckMysqlRateLimitSupportResponse(BceResponse):
    """
    CheckMysqlRateLimitSupportResponse
    """

    def __init__(self, allowed=None):
        """
        Initialize CheckMysqlRateLimitSupportResponse response.

        :param allowed: 是否支持SQL限流
        :type allowed: bool (optional)
        """
        super().__init__()
        self.allowed = allowed

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
        if self.allowed is not None:
            result['allowed'] = self.allowed
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CheckMysqlRateLimitSupportResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('allowed') is not None:
            self.allowed = m.get('allowed')
        return self
