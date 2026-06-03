"""
AuthGroupInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_rapidfs.models.auth_info import AuthInfo


class AuthGroupInfo(AbstractModel):
    """
    AuthGroupInfo
    """

    def __init__(
        self,
        auth_group_id=None,
        auth_group_name=None,
        instance_id=None,
        status=None,
        description=None,
        auth_infos=None,
    ):
        """
        Initialize AuthGroupInfo instance.

        :param auth_group_id: 权限组ID
        :type auth_group_id: str (optional)

        :param auth_group_name: 权限组名称
        :type auth_group_name: str (optional)

        :param instance_id: 所属 rapidFS 实例唯一ID
        :type instance_id: str (optional)

        :param status: 权限组状态，见 AuthGroupStatus
        :type status: str (optional)

        :param description: 描述
        :type description: str (optional)

        :param auth_infos: 权限组中的权限列表
        :type auth_infos: List[AuthInfo] (optional)
        """
        super().__init__()
        self.auth_group_id = auth_group_id
        self.auth_group_name = auth_group_name
        self.instance_id = instance_id
        self.status = status
        self.description = description
        self.auth_infos = auth_infos

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
        if self.auth_group_id is not None:
            result['authGroupId'] = self.auth_group_id
        if self.auth_group_name is not None:
            result['authGroupName'] = self.auth_group_name
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.status is not None:
            result['status'] = self.status
        if self.description is not None:
            result['description'] = self.description
        if self.auth_infos is not None:
            result['authInfos'] = [i.to_dict() for i in self.auth_infos]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AuthGroupInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('authGroupId') is not None:
            self.auth_group_id = m.get('authGroupId')
        if m.get('authGroupName') is not None:
            self.auth_group_name = m.get('authGroupName')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('authInfos') is not None:
            self.auth_infos = [AuthInfo().from_dict(i) for i in m.get('authInfos')]
        return self
