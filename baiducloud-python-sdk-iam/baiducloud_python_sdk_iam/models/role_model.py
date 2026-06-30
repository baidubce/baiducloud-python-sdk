"""
RoleModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RoleModel(AbstractModel):
    """
    RoleModel
    """

    def __init__(self, id=None, name=None, create_time=None, description=None, assume_role_policy_document=None):
        """
        Initialize RoleModel instance.

        :param id: 角色id
        :type id: str (optional)

        :param name: 角色名称
        :type name: str (optional)

        :param create_time: 创建时间
        :type create_time: datetime (optional)

        :param description: 角色描述
        :type description: str (optional)

        :param assume_role_policy_document: 指定允许扮演此角色的实体
        :type assume_role_policy_document: str (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.create_time = create_time
        self.description = description
        self.assume_role_policy_document = assume_role_policy_document

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
        if self.description is not None:
            result['description'] = self.description
        if self.assume_role_policy_document is not None:
            result['assumeRolePolicyDocument'] = self.assume_role_policy_document
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RoleModel

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
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('assumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('assumeRolePolicyDocument')
        return self
