"""
Request entity for UpdatePermissionGroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdatePermissionGroupRequest(AbstractModel):
    """
    Request entity for UpdatePermissionGroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, ag_name, description=None):
        """
        Initialize UpdatePermissionGroupRequest request entity.

        :param ag_name: ag_name parameter
        :type ag_name: str (required)

        :param description: 对于更新的权限组的描述，不能超过1024个字节
        :type description: str (optional)
        """
        super().__init__()
        self.ag_name = ag_name
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
        :rtype: UpdatePermissionGroupRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('agName') is not None:
            self.ag_name = m.get('agName')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
