"""
Request entity for CreateRobotAccountRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_ccr.models.robot_permission import RobotPermission


class CreateRobotAccountRequest(AbstractModel):
    """
    Request entity for CreateRobotAccountRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, name, duration, permissions, secret=None, disable=None, description=None):
        """
        Initialize CreateRobotAccountRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param name: name parameter
        :type name: str (required)

        :param secret: secret parameter
        :type secret: str (optional)

        :param disable: 是否禁用，默认是false
        :type disable: bool (optional)

        :param duration: 账号有效期，单位：天，-1表示永不过期
        :type duration: int (required)

        :param description: 账号描述，长度0~1024个字符
        :type description: str (optional)

        :param permissions: 权限
        :type permissions: List[RobotPermission] (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.name = name
        self.secret = secret
        self.disable = disable
        self.duration = duration
        self.description = description
        self.permissions = permissions

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
        if self.secret is not None:
            result['secret'] = self.secret
        if self.disable is not None:
            result['disable'] = self.disable
        if self.duration is not None:
            result['duration'] = self.duration
        if self.description is not None:
            result['description'] = self.description
        if self.permissions is not None:
            result['permissions'] = [i.to_dict() for i in self.permissions]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateRobotAccountRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('secret') is not None:
            self.secret = m.get('secret')
        if m.get('disable') is not None:
            self.disable = m.get('disable')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('permissions') is not None:
            self.permissions = [RobotPermission().from_dict(i) for i in m.get('permissions')]
        return self
