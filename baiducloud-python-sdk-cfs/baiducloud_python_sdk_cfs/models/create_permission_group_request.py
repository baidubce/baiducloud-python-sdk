"""
Request entity for CreatePermissionGroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreatePermissionGroupRequest(AbstractModel):
    """
    Request entity for CreatePermissionGroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, access_group_name, description=None):
        """
        Initialize CreatePermissionGroupRequest request entity.

        :param access_group_name: 新创建的权限组的名字，长度1~65个字节，字母开头，可包含字母数字和- _ .字符。
        :type access_group_name: str (required)

        :param description: 对于新创建的权限组的描述，不能超过1024个字节
        :type description: str (optional)
        """
        super().__init__()
        self.access_group_name = access_group_name
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
        if self.access_group_name is not None:
            result['accessGroupName'] = self.access_group_name
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
        :rtype: CreatePermissionGroupRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('accessGroupName') is not None:
            self.access_group_name = m.get('accessGroupName')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
