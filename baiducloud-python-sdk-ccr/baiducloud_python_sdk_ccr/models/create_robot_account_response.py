"""
Request entity for CreateRobotAccountResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateRobotAccountResponse(BceResponse):
    """
    CreateRobotAccountResponse
    """

    def __init__(self, id=None, name=None, secret=None, creation_time=None, expires_at=None):
        """
        Initialize CreateRobotAccountResponse response.

        :param id: 机器人账号ID
        :type id: int (optional)

        :param name: 账号名称
        :type name: str (optional)

        :param secret: 账号密码
        :type secret: str (optional)

        :param creation_time: 创建时间
        :type creation_time: str (optional)

        :param expires_at: 过期时间 Unix 时间戳，-1表示永不过期
        :type expires_at: int (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.secret = secret
        self.creation_time = creation_time
        self.expires_at = expires_at

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
        if self.name is not None:
            result['name'] = self.name
        if self.secret is not None:
            result['secret'] = self.secret
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.expires_at is not None:
            result['expiresAt'] = self.expires_at
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateRobotAccountResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('secret') is not None:
            self.secret = m.get('secret')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('expiresAt') is not None:
            self.expires_at = m.get('expiresAt')
        return self
