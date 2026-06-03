"""
Robot information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ccr.models.robot_permission import RobotPermission


class Robot(AbstractModel):
    """
    Robot
    """

    def __init__(
        self,
        id=None,
        name=None,
        description=None,
        level=None,
        disable=None,
        duration=None,
        expires_at=None,
        creation_time=None,
        update_time=None,
        permissions=None,
    ):
        """
        Initialize Robot instance.

        :param id: 机器人账号 ID
        :type id: int (optional)

        :param name: 账号名称
        :type name: str (optional)

        :param description: 描述信息
        :type description: str (optional)

        :param level: 等级，固定为 `system`
        :type level: str (optional)

        :param disable: 是否禁用
        :type disable: bool (optional)

        :param duration: 账号剩余有效期，单位：天，`-1` 表示永不过期
        :type duration: int (optional)

        :param expires_at: 过期时间，Unix 时间戳，`-1` 表示永不过期
        :type expires_at: int (optional)

        :param creation_time: 创建时间
        :type creation_time: str (optional)

        :param update_time: 更新时间
        :type update_time: str (optional)

        :param permissions: 权限列表
        :type permissions: List[RobotPermission] (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.description = description
        self.level = level
        self.disable = disable
        self.duration = duration
        self.expires_at = expires_at
        self.creation_time = creation_time
        self.update_time = update_time
        self.permissions = permissions

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
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.level is not None:
            result['level'] = self.level
        if self.disable is not None:
            result['disable'] = self.disable
        if self.duration is not None:
            result['duration'] = self.duration
        if self.expires_at is not None:
            result['expiresAt'] = self.expires_at
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.permissions is not None:
            result['permissions'] = [i.to_dict() for i in self.permissions]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Robot

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('disable') is not None:
            self.disable = m.get('disable')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('expiresAt') is not None:
            self.expires_at = m.get('expiresAt')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('permissions') is not None:
            self.permissions = [RobotPermission().from_dict(i) for i in m.get('permissions')]
        return self
