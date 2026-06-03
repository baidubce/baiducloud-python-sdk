"""
ReplicationSyncPolicyResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ccr.models.replication_sync_trigger import ReplicationSyncTrigger


class ReplicationSyncPolicyResult(AbstractModel):
    """
    ReplicationSyncPolicyResult
    """

    def __init__(
        self,
        id=None,
        name=None,
        description=None,
        sync_type=None,
        src_project_name=None,
        src_repository_name=None,
        src_tag_name=None,
        src_region=None,
        creation_time=None,
        update_time=None,
        dest_instance_id=None,
        dest_project_name=None,
        dest_region=None,
        trigger=None,
        override=None,
    ):
        """
        Initialize ReplicationSyncPolicyResult instance.

        :param id: 同步规则 ID
        :type id: int (optional)

        :param name: 同步规则名称
        :type name: str (optional)

        :param description: 同步规则备注
        :type description: str (optional)

        :param sync_type: 同步类型
        :type sync_type: str (optional)

        :param src_project_name: 源实例命名空间
        :type src_project_name: str (optional)

        :param src_repository_name: 源仓库名称
        :type src_repository_name: str (optional)

        :param src_tag_name: 源镜像版本
        :type src_tag_name: str (optional)

        :param src_region: 源实例所在地域
        :type src_region: str (optional)

        :param creation_time: 同步规则创建时间
        :type creation_time: str (optional)

        :param update_time: 同步规则更新时间
        :type update_time: str (optional)

        :param dest_instance_id: 同步目标实例 ID
        :type dest_instance_id: str (optional)

        :param dest_project_name: 同步目标命名空间
        :type dest_project_name: str (optional)

        :param dest_region: 同步目标实例所在地域
        :type dest_region: str (optional)

        :param trigger: trigger attribute
        :type trigger: ReplicationSyncTrigger (optional)

        :param override: 是否覆盖目标实例已有的同名镜像
        :type override: bool (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.description = description
        self.sync_type = sync_type
        self.src_project_name = src_project_name
        self.src_repository_name = src_repository_name
        self.src_tag_name = src_tag_name
        self.src_region = src_region
        self.creation_time = creation_time
        self.update_time = update_time
        self.dest_instance_id = dest_instance_id
        self.dest_project_name = dest_project_name
        self.dest_region = dest_region
        self.trigger = trigger
        self.override = override

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
        if self.sync_type is not None:
            result['syncType'] = self.sync_type
        if self.src_project_name is not None:
            result['srcProjectName'] = self.src_project_name
        if self.src_repository_name is not None:
            result['srcRepositoryName'] = self.src_repository_name
        if self.src_tag_name is not None:
            result['srcTagName'] = self.src_tag_name
        if self.src_region is not None:
            result['srcRegion'] = self.src_region
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.dest_instance_id is not None:
            result['destInstanceId'] = self.dest_instance_id
        if self.dest_project_name is not None:
            result['destProjectName'] = self.dest_project_name
        if self.dest_region is not None:
            result['destRegion'] = self.dest_region
        if self.trigger is not None:
            result['trigger'] = self.trigger.to_dict()
        if self.override is not None:
            result['override'] = self.override
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ReplicationSyncPolicyResult

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
        if m.get('syncType') is not None:
            self.sync_type = m.get('syncType')
        if m.get('srcProjectName') is not None:
            self.src_project_name = m.get('srcProjectName')
        if m.get('srcRepositoryName') is not None:
            self.src_repository_name = m.get('srcRepositoryName')
        if m.get('srcTagName') is not None:
            self.src_tag_name = m.get('srcTagName')
        if m.get('srcRegion') is not None:
            self.src_region = m.get('srcRegion')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('destInstanceId') is not None:
            self.dest_instance_id = m.get('destInstanceId')
        if m.get('destProjectName') is not None:
            self.dest_project_name = m.get('destProjectName')
        if m.get('destRegion') is not None:
            self.dest_region = m.get('destRegion')
        if m.get('trigger') is not None:
            self.trigger = ReplicationSyncTrigger().from_dict(m.get('trigger'))
        if m.get('override') is not None:
            self.override = m.get('override')
        return self
