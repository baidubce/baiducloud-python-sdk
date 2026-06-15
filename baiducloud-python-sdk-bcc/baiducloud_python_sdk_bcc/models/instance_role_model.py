"""
InstanceRoleModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class InstanceRoleModel(AbstractModel):
    """
    InstanceRoleModel
    """

    def __init__(self, role_name=None):
        """
        Initialize InstanceRoleModel instance.

        :param role_name: 角色名称
        :type role_name: str (optional)
        """
        super().__init__()
        self.role_name = role_name

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
        if self.role_name is not None:
            result['roleName'] = self.role_name
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InstanceRoleModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')
        return self
