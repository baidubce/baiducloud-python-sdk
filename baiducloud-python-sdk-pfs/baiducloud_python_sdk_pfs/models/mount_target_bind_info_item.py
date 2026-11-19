"""
MountTargetBindInfoItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MountTargetBindInfoItem(AbstractModel):
    """
    MountTargetBindInfoItem
    """

    def __init__(
        self,
        mount_target_bind_id=None,
        mount_target_id=None,
        mount_target_name=None,
        instance_id=None,
        instance_name=None,
        region=None,
        zone=None,
        local_mount_path=None,
        bind_time=None,
        state=None,
        is_primary_instance=None,
    ):
        """
        Initialize MountTargetBindInfoItem instance.

        :param mount_target_bind_id: 绑定关系 ID
        :type mount_target_bind_id: str (optional)

        :param mount_target_id: 挂载服务 ID
        :type mount_target_id: str (optional)

        :param mount_target_name: 挂载服务名称
        :type mount_target_name: str (optional)

        :param instance_id: 绑定的实例 ID
        :type instance_id: str (optional)

        :param instance_name: 绑定的实例名称
        :type instance_name: str (optional)

        :param region: 地域
        :type region: str (optional)

        :param zone: 可用区
        :type zone: str (optional)

        :param local_mount_path: 挂载路径
        :type local_mount_path: str (optional)

        :param bind_time: 绑定时间
        :type bind_time: str (optional)

        :param state: 绑定状态
        :type state: int (optional)

        :param is_primary_instance: 是否为主实例
        :type is_primary_instance: bool (optional)
        """
        super().__init__()
        self.mount_target_bind_id = mount_target_bind_id
        self.mount_target_id = mount_target_id
        self.mount_target_name = mount_target_name
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.region = region
        self.zone = zone
        self.local_mount_path = local_mount_path
        self.bind_time = bind_time
        self.state = state
        self.is_primary_instance = is_primary_instance

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
        if self.mount_target_bind_id is not None:
            result['mountTargetBindId'] = self.mount_target_bind_id
        if self.mount_target_id is not None:
            result['mountTargetId'] = self.mount_target_id
        if self.mount_target_name is not None:
            result['mountTargetName'] = self.mount_target_name
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.region is not None:
            result['region'] = self.region
        if self.zone is not None:
            result['zone'] = self.zone
        if self.local_mount_path is not None:
            result['localMountPath'] = self.local_mount_path
        if self.bind_time is not None:
            result['bindTime'] = self.bind_time
        if self.state is not None:
            result['state'] = self.state
        if self.is_primary_instance is not None:
            result['isPrimaryInstance'] = self.is_primary_instance
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MountTargetBindInfoItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('mountTargetBindId') is not None:
            self.mount_target_bind_id = m.get('mountTargetBindId')
        if m.get('mountTargetId') is not None:
            self.mount_target_id = m.get('mountTargetId')
        if m.get('mountTargetName') is not None:
            self.mount_target_name = m.get('mountTargetName')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('zone') is not None:
            self.zone = m.get('zone')
        if m.get('localMountPath') is not None:
            self.local_mount_path = m.get('localMountPath')
        if m.get('bindTime') is not None:
            self.bind_time = m.get('bindTime')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('isPrimaryInstance') is not None:
            self.is_primary_instance = m.get('isPrimaryInstance')
        return self
