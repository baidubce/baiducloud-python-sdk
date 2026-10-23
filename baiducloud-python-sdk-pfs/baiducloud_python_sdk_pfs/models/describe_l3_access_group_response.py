"""
Request entity for DescribeL3AccessGroupResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_pfs.models.l3_attached_mount_target import L3AttachedMountTarget


class DescribeL3AccessGroupResponse(BceResponse):
    """
    DescribeL3AccessGroupResponse
    """

    def __init__(
        self,
        request_id=None,
        access_group_name=None,
        description=None,
        instance_count=None,
        mount_count=None,
        create_time=None,
        zone_name=None,
        attached_mount_targets=None,
    ):
        """
        Initialize DescribeL3AccessGroupResponse response.

        :param request_id: 唯一请求 ID，每次请求都会返回
        :type request_id: str (optional)

        :param access_group_name: 权限组名称
        :type access_group_name: str (optional)

        :param description: 描述，未设置时该字段不返回
        :type description: str (optional)

        :param instance_count: 关联实例数量
        :type instance_count: int (optional)

        :param mount_count: 关联挂载点数量
        :type mount_count: int (optional)

        :param create_time: 创建时间，ISO-8601 UTC 秒精度，如 2026-09-01T03:12:45Z
        :type create_time: str (optional)

        :param zone_name: 逻辑机房（可用区）
        :type zone_name: str (optional)

        :param attached_mount_targets: attached_mount_targets field
        :type attached_mount_targets: list[L3AttachedMountTarget] (optional)
        """
        super().__init__()
        self.request_id = request_id
        self.access_group_name = access_group_name
        self.description = description
        self.instance_count = instance_count
        self.mount_count = mount_count
        self.create_time = create_time
        self.zone_name = zone_name
        self.attached_mount_targets = attached_mount_targets

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.access_group_name is not None:
            result['accessGroupName'] = self.access_group_name
        if self.description is not None:
            result['description'] = self.description
        if self.instance_count is not None:
            result['instanceCount'] = self.instance_count
        if self.mount_count is not None:
            result['mountCount'] = self.mount_count
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.attached_mount_targets is not None:
            result['attachedMountTargets'] = [item.to_dict() for item in self.attached_mount_targets]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeL3AccessGroupResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('accessGroupName') is not None:
            self.access_group_name = m.get('accessGroupName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('instanceCount') is not None:
            self.instance_count = m.get('instanceCount')
        if m.get('mountCount') is not None:
            self.mount_count = m.get('mountCount')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('attachedMountTargets') is not None:
            self.attached_mount_targets = [
                L3AttachedMountTarget().from_dict(item) for item in m.get('attachedMountTargets')
            ]
        return self
