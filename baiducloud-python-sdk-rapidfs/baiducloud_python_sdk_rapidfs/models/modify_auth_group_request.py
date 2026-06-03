"""
Request entity for ModifyAuthGroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_rapidfs.models.auth_info import AuthInfo
from baiducloud_python_sdk_rapidfs.models.auth_info import AuthInfo


class ModifyAuthGroupRequest(AbstractModel):
    """
    Request entity for ModifyAuthGroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        auth_group_id,
        instance_id,
        client_token=None,
        auth_group_name=None,
        description=None,
        auth_infos=None,
        original_auth_infos=None,
    ):
        """
        Initialize ModifyAuthGroupRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param auth_group_id: 权限组id
        :type auth_group_id: str (required)

        :param instance_id: 所属 RapidFS 实例唯一 Id
        :type instance_id: str (required)

        :param auth_group_name: 权限组名称
        :type auth_group_name: str (optional)

        :param description: 描述信息
        :type description: str (optional)

        :param auth_infos: 修改之后的权限规则列表。默认权限组不允许增加或删除权限规则
        :type auth_infos: List[AuthInfo] (optional)

        :param original_auth_infos: original_auth_infos parameter
        :type original_auth_infos: List[AuthInfo] (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.auth_group_id = auth_group_id
        self.instance_id = instance_id
        self.auth_group_name = auth_group_name
        self.description = description
        self.auth_infos = auth_infos
        self.original_auth_infos = original_auth_infos

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
        if self.auth_group_id is not None:
            result['authGroupId'] = self.auth_group_id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.auth_group_name is not None:
            result['authGroupName'] = self.auth_group_name
        if self.description is not None:
            result['description'] = self.description
        if self.auth_infos is not None:
            result['authInfos'] = [i.to_dict() for i in self.auth_infos]
        if self.original_auth_infos is not None:
            result['originalAuthInfos'] = [i.to_dict() for i in self.original_auth_infos]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyAuthGroupRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('authGroupId') is not None:
            self.auth_group_id = m.get('authGroupId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('authGroupName') is not None:
            self.auth_group_name = m.get('authGroupName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('authInfos') is not None:
            self.auth_infos = [AuthInfo().from_dict(i) for i in m.get('authInfos')]
        if m.get('originalAuthInfos') is not None:
            self.original_auth_infos = [AuthInfo().from_dict(i) for i in m.get('originalAuthInfos')]
        return self
