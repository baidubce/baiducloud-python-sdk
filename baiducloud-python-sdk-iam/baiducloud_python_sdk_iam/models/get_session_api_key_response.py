"""
Request entity for GetSessionApiKeyResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class GetSessionApiKeyResponse(BceResponse):
    """
    GetSessionApiKeyResponse
    """

    def __init__(self, user_id=None, token=None, create_time=None, expire_time=None):
        """
        Initialize GetSessionApiKeyResponse response.

        :param user_id: API Key归属user
        :type user_id: str (optional)

        :param token: API Key本身
        :type token: str (optional)

        :param create_time: 创建时间
        :type create_time: str (optional)

        :param expire_time: 过期时间
        :type expire_time: str (optional)
        """
        super().__init__()
        self.user_id = user_id
        self.token = token
        self.create_time = create_time
        self.expire_time = expire_time

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
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.token is not None:
            result['token'] = self.token
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetSessionApiKeyResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('token') is not None:
            self.token = m.get('token')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        return self
