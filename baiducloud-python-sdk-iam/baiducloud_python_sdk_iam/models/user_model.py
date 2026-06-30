"""
UserModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UserModel(AbstractModel):
    """
    UserModel
    """

    def __init__(
        self,
        id=None,
        name=None,
        create_time=None,
        join_time=None,
        last_login_time=None,
        description=None,
        enabled=None,
    ):
        """
        Initialize UserModel instance.

        :param id: 用户id
        :type id: str (optional)

        :param name: 用户名称
        :type name: str (optional)

        :param create_time: 创建时间
        :type create_time: datetime (optional)

        :param join_time: 加入用户组时间
        :type join_time: datetime (optional)

        :param last_login_time: 最后登录时间
        :type last_login_time: datetime (optional)

        :param description: 用户描述
        :type description: str (optional)

        :param enabled: 用户启用状态
        :type enabled: bool (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.create_time = create_time
        self.join_time = join_time
        self.last_login_time = last_login_time
        self.description = description
        self.enabled = enabled

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.join_time is not None:
            result['joinTime'] = self.join_time
        if self.last_login_time is not None:
            result['lastLoginTime'] = self.last_login_time
        if self.description is not None:
            result['description'] = self.description
        if self.enabled is not None:
            result['enabled'] = self.enabled
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UserModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('joinTime') is not None:
            self.join_time = m.get('joinTime')
        if m.get('lastLoginTime') is not None:
            self.last_login_time = m.get('lastLoginTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        return self
