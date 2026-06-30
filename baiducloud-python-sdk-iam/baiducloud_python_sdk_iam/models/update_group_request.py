"""
Request entity for UpdateGroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateGroupRequest(AbstractModel):
    """
    Request entity for UpdateGroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, group_name, name=None, description=None):
        """
        Initialize UpdateGroupRequest request entity.

        :param group_name: group_name parameter
        :type group_name: str (required)

        :param name: 更新后的组名
        :type name: str (optional)

        :param description: 组的描述
        :type description: str (optional)
        """
        super().__init__()
        self.group_name = group_name
        self.name = name
        self.description = description

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateGroupRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
