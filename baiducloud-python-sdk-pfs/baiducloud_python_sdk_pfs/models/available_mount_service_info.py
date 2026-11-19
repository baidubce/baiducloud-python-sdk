"""
AvailableMountServiceInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_pfs.models.mount_target_bind_info_item import MountTargetBindInfoItem


class AvailableMountServiceInfo(AbstractModel):
    """
    AvailableMountServiceInfo
    """

    def __init__(
        self,
        mount_target_id=None,
        name=None,
        state=None,
        subnet_id=None,
        version_number=None,
        vpc_id=None,
        zone_name=None,
        mount_target_bind_list=None,
    ):
        """
        Initialize AvailableMountServiceInfo instance.

        :param mount_target_id: 挂载服务 ID
        :type mount_target_id: str (optional)

        :param name: 挂载服务名称
        :type name: str (optional)

        :param state: 挂载服务状态
        :type state: int (optional)

        :param subnet_id: 挂载服务所在子网 ID
        :type subnet_id: str (optional)

        :param version_number: 挂载服务版本号
        :type version_number: str (optional)

        :param vpc_id: 挂载服务所在 VPC ID
        :type vpc_id: str (optional)

        :param zone_name: 挂载服务所在可用区
        :type zone_name: str (optional)

        :param mount_target_bind_list: 挂载服务已有的绑定关系列表
        :type mount_target_bind_list: List[MountTargetBindInfoItem] (optional)
        """
        super().__init__()
        self.mount_target_id = mount_target_id
        self.name = name
        self.state = state
        self.subnet_id = subnet_id
        self.version_number = version_number
        self.vpc_id = vpc_id
        self.zone_name = zone_name
        self.mount_target_bind_list = mount_target_bind_list

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
        if self.mount_target_id is not None:
            result['mountTargetId'] = self.mount_target_id
        if self.name is not None:
            result['name'] = self.name
        if self.state is not None:
            result['state'] = self.state
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.version_number is not None:
            result['versionNumber'] = self.version_number
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.mount_target_bind_list is not None:
            result['mountTargetBindList'] = [i.to_dict() for i in self.mount_target_bind_list]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AvailableMountServiceInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('mountTargetId') is not None:
            self.mount_target_id = m.get('mountTargetId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('versionNumber') is not None:
            self.version_number = m.get('versionNumber')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('mountTargetBindList') is not None:
            self.mount_target_bind_list = [
                MountTargetBindInfoItem().from_dict(i) for i in m.get('mountTargetBindList')
            ]
        return self
