"""
Request entity for DescribeAuthGroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescribeAuthGroupRequest(AbstractModel):
    """
    Request entity for DescribeAuthGroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, auth_group_id):
        """
        Initialize DescribeAuthGroupRequest request entity.

        :param instance_id: 待查询的 rapidFS 实例唯一 ID
        :type instance_id: str (required)

        :param auth_group_id: 权限组id
        :type auth_group_id: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.auth_group_id = auth_group_id

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.auth_group_id is not None:
            result['authGroupId'] = self.auth_group_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeAuthGroupRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('authGroupId') is not None:
            self.auth_group_id = m.get('authGroupId')
        return self
