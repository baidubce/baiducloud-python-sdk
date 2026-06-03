"""
Request entity for CreateAuthGroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_rapidfs.models.auth_info import AuthInfo


class CreateAuthGroupRequest(AbstractModel):
    """
    Request entity for CreateAuthGroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, auth_group_name, instance_id, client_token=None, description=None, auth_infos=None):
        """
        Initialize CreateAuthGroupRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param auth_group_name: 权限组名
        :type auth_group_name: str (required)

        :param instance_id: 所属 rapidFS 实例ID
        :type instance_id: str (required)

        :param description: 权限组实例描述信息
        :type description: str (optional)

        :param auth_infos: auth_infos parameter
        :type auth_infos: List[AuthInfo] (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.auth_group_name = auth_group_name
        self.instance_id = instance_id
        self.description = description
        self.auth_infos = auth_infos

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
        if self.auth_group_name is not None:
            result['authGroupName'] = self.auth_group_name
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.description is not None:
            result['description'] = self.description
        if self.auth_infos is not None:
            result['authInfos'] = [i.to_dict() for i in self.auth_infos]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateAuthGroupRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('authGroupName') is not None:
            self.auth_group_name = m.get('authGroupName')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('authInfos') is not None:
            self.auth_infos = [AuthInfo().from_dict(i) for i in m.get('authInfos')]
        return self
