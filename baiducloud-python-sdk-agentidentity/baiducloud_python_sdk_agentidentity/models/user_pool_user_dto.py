"""
UserPoolUserDTO information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UserPoolUserDTO(AbstractModel):
    """
    UserPoolUserDTO
    """

    def __init__(
        self,
        id=None,
        username=None,
        display_name=None,
        description=None,
        source=None,
        has_password=None,
        created_at=None,
    ):
        """
        Initialize UserPoolUserDTO instance.

        :param id: 用户 ID
        :type id: str (optional)

        :param username: 用户名
        :type username: str (optional)

        :param display_name: 显示名称
        :type display_name: str (optional)

        :param description: 描述
        :type description: str (optional)

        :param source: 来源：MANUAL / AUTO
        :type source: str (optional)

        :param has_password: 是否已设置密码
        :type has_password: bool (optional)

        :param created_at: 创建时间
        :type created_at: datetime (optional)
        """
        super().__init__()
        self.id = id
        self.username = username
        self.display_name = display_name
        self.description = description
        self.source = source
        self.has_password = has_password
        self.created_at = created_at

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
        if self.username is not None:
            result['username'] = self.username
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.description is not None:
            result['description'] = self.description
        if self.source is not None:
            result['source'] = self.source
        if self.has_password is not None:
            result['hasPassword'] = self.has_password
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UserPoolUserDTO

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('username') is not None:
            self.username = m.get('username')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('hasPassword') is not None:
            self.has_password = m.get('hasPassword')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        return self
