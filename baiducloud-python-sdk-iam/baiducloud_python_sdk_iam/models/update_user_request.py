"""
Request entity for UpdateUserRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateUserRequest(AbstractModel):
    """
    Request entity for UpdateUserRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, user_name, name=None, description=None, enabled=None):
        """
        Initialize UpdateUserRequest request entity.

        :param user_name: user_name parameter
        :type user_name: str (required)

        :param name: 更新后的用户名
        :type name: str (optional)

        :param description: 用户的描述
        :type description: str (optional)

        :param enabled: 用户状态
        :type enabled: bool (optional)
        """
        super().__init__()
        self.user_name = user_name
        self.name = name
        self.description = description
        self.enabled = enabled

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.enabled is not None:
            result['enabled'] = self.enabled
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateUserRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        return self
