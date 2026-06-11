"""
PermissionEntry information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class PermissionEntry(AbstractModel):
    """
    PermissionEntry
    """

    def __init__(self, id=None, name=None, permission=None):
        """
        Initialize PermissionEntry instance.

        :param id: 是
        :type id: str (optional)

        :param name: 是
        :type name: str (optional)

        :param permission: 是
        :type permission: str (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.permission = permission

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
        if self.permission is not None:
            result['permission'] = self.permission
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PermissionEntry

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('permission') is not None:
            self.permission = m.get('permission')
        return self
