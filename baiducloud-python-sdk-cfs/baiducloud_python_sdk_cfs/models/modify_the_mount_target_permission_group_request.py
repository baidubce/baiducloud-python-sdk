"""
Request entity for ModifyTheMountTargetPermissionGroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModifyTheMountTargetPermissionGroupRequest(AbstractModel):
    """
    Request entity for ModifyTheMountTargetPermissionGroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, fs_id, mount_id, access_group_name):
        """
        Initialize ModifyTheMountTargetPermissionGroupRequest request entity.

        :param fs_id: fs_id parameter
        :type fs_id: str (required)

        :param mount_id: mount_id parameter
        :type mount_id: str (required)

        :param access_group_name: 修改的的权限组的名称，长度1~65个字节，字母开头，可包含字母数字和- _ .字符。
        :type access_group_name: str (required)
        """
        super().__init__()
        self.fs_id = fs_id
        self.mount_id = mount_id
        self.access_group_name = access_group_name

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyTheMountTargetPermissionGroupRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('fsId') is not None:
            self.fs_id = m.get('fsId')
        if m.get('mountID') is not None:
            self.mount_id = m.get('mountID')
        if m.get('accessGroupName') is not None:
            self.access_group_name = m.get('accessGroupName')
        return self
