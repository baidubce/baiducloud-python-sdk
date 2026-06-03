"""
Request entity for GetInstanceSyncDetailResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_ccr.models.replication_sync_trigger import ReplicationSyncTrigger


class GetInstanceSyncDetailResponse(BceResponse):
    """
    GetInstanceSyncDetailResponse
    """

    def __init__(
        self,
        creation_time=None,
        description=None,
        dest_instance_id=None,
        dest_project_name=None,
        dest_region=None,
        id=None,
        name=None,
        override=None,
        src_project_name=None,
        src_region=None,
        src_repository_name=None,
        src_tag_name=None,
        sync_type=None,
        trigger=None,
        update_time=None,
    ):
        """
        Initialize GetInstanceSyncDetailResponse response.

        :param creation_time: 同步规则创建时间
        :type creation_time: str (optional)

        :param description: 同步规则备注
        :type description: str (optional)

        :param dest_instance_id: 同步目标实例ID
        :type dest_instance_id: str (optional)

        :param dest_project_name: 同步目标命名空间
        :type dest_project_name: str (optional)

        :param dest_region: 同步目标实例所在地域
        :type dest_region: str (optional)

        :param id: 同步规则ID
        :type id: int (optional)

        :param name: 同步规则名称
        :type name: str (optional)

        :param override: 是否覆盖目标实例已有的同名镜像
        :type override: bool (optional)

        :param src_project_name: 源实例命名空间
        :type src_project_name: str (optional)

        :param src_region: 源实例所在地域
        :type src_region: str (optional)

        :param src_repository_name: 源仓库名称
        :type src_repository_name: str (optional)

        :param src_tag_name: 源镜像版本
        :type src_tag_name: str (optional)

        :param sync_type: 同步类型
        :type sync_type: str (optional)

        :param trigger: trigger field
        :type trigger: ReplicationSyncTrigger (optional)

        :param update_time: 同步规则更新时间
        :type update_time: str (optional)
        """
        super().__init__()
        self.creation_time = creation_time
        self.description = description
        self.dest_instance_id = dest_instance_id
        self.dest_project_name = dest_project_name
        self.dest_region = dest_region
        self.id = id
        self.name = name
        self.override = override
        self.src_project_name = src_project_name
        self.src_region = src_region
        self.src_repository_name = src_repository_name
        self.src_tag_name = src_tag_name
        self.sync_type = sync_type
        self.trigger = trigger
        self.update_time = update_time

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
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.description is not None:
            result['description'] = self.description
        if self.dest_instance_id is not None:
            result['destInstanceId'] = self.dest_instance_id
        if self.dest_project_name is not None:
            result['destProjectName'] = self.dest_project_name
        if self.dest_region is not None:
            result['destRegion'] = self.dest_region
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.override is not None:
            result['override'] = self.override
        if self.src_project_name is not None:
            result['srcProjectName'] = self.src_project_name
        if self.src_region is not None:
            result['srcRegion'] = self.src_region
        if self.src_repository_name is not None:
            result['srcRepositoryName'] = self.src_repository_name
        if self.src_tag_name is not None:
            result['srcTagName'] = self.src_tag_name
        if self.sync_type is not None:
            result['syncType'] = self.sync_type
        if self.trigger is not None:
            result['trigger'] = self.trigger.to_dict()
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetInstanceSyncDetailResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('destInstanceId') is not None:
            self.dest_instance_id = m.get('destInstanceId')
        if m.get('destProjectName') is not None:
            self.dest_project_name = m.get('destProjectName')
        if m.get('destRegion') is not None:
            self.dest_region = m.get('destRegion')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('override') is not None:
            self.override = m.get('override')
        if m.get('srcProjectName') is not None:
            self.src_project_name = m.get('srcProjectName')
        if m.get('srcRegion') is not None:
            self.src_region = m.get('srcRegion')
        if m.get('srcRepositoryName') is not None:
            self.src_repository_name = m.get('srcRepositoryName')
        if m.get('srcTagName') is not None:
            self.src_tag_name = m.get('srcTagName')
        if m.get('syncType') is not None:
            self.sync_type = m.get('syncType')
        if m.get('trigger') is not None:
            self.trigger = ReplicationSyncTrigger().from_dict(m.get('trigger'))
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self
