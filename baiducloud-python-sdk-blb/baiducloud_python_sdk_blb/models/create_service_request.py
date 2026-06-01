"""
Request entity for CreateServiceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_blb.models.auth import Auth


class CreateServiceRequest(AbstractModel):
    """
    Request entity for CreateServiceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, service_name, instance_id, client_token=None, description=None, auth_list=None):
        """
        Initialize CreateServiceRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: 服务发布点的名称，大小写字母、数字以及-_/.特殊字符，必须以字母开头，长度1-65
        :type name: str (required)

        :param description: 服务发布点的描述，最大支持200字符
        :type description: str (optional)

        :param service_name: 对应服务名称,大小写字母、数字长度1-65
        :type service_name: str (required)

        :param instance_id: 绑定实例id，当前只支持绑定blb
        :type instance_id: str (required)

        :param auth_list: 用户授权列表，默认拒绝所有
        :type auth_list: List[Auth] (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.name = name
        self.description = description
        self.service_name = service_name
        self.instance_id = instance_id
        self.auth_list = auth_list

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
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.auth_list is not None:
            result['authList'] = [i.to_dict() for i in self.auth_list]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateServiceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('authList') is not None:
            self.auth_list = [Auth().from_dict(i) for i in m.get('authList')]
        return self
