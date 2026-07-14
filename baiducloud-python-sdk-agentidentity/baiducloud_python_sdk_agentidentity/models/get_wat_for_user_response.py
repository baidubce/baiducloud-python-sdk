"""
GetWATForUserResponse information
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class GetWATForUserResponse(BceResponse):
    """
    GetWATForUserResponse
    """

    def __init__(self, token=None, expire_at=None):
        """
        Initialize GetWATForUserResponse instance.

        :param token: WAT 令牌（格式：wat-v1.<encrypted-payload>）
        :type token: str (optional)

        :param expire_at: 过期时间（ISO 8601）
        :type expire_at: datetime (optional)
        """
        super().__init__()
        self.token = token
        self.expire_at = expire_at

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        Includes metadata from the parent BceResponse class.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.token is not None:
            result['token'] = self.token
        if self.expire_at is not None:
            result['expireAt'] = self.expire_at
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetWATForUserResponse

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('token') is not None:
            self.token = m.get('token')
        if m.get('expireAt') is not None:
            self.expire_at = m.get('expireAt')
        return self
