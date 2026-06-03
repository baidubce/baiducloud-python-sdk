"""
Request entity for GetImageMigrationRuleDetailResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_ccr.models.replication_registry import ReplicationRegistry
from baiducloud_python_sdk_ccr.models.replication_filter import ReplicationFilter
from baiducloud_python_sdk_ccr.models.replication_registry import ReplicationRegistry
from baiducloud_python_sdk_ccr.models.replication_trigger import ReplicationTrigger


class GetImageMigrationRuleDetailResponse(BceResponse):
    """
    GetImageMigrationRuleDetailResponse
    """

    def __init__(
        self,
        creation_time=None,
        deletion=None,
        description=None,
        dest_project_name=None,
        dest_registry=None,
        enabled=None,
        execution_times=None,
        filters=None,
        id=None,
        name=None,
        override=None,
        src_registry=None,
        trigger=None,
        update_time=None,
    ):
        """
        Initialize GetImageMigrationRuleDetailResponse response.

        :param creation_time: 镜像迁移规则创建时间
        :type creation_time: str (optional)

        :param deletion: 级联删除
        :type deletion: bool (optional)

        :param description: 镜像迁移规则描述
        :type description: str (optional)

        :param dest_project_name: 目的命名空间
        :type dest_project_name: str (optional)

        :param dest_registry: dest_registry field
        :type dest_registry: ReplicationRegistry (optional)

        :param enabled: 镜像迁移规则状态
        :type enabled: bool (optional)

        :param execution_times: 镜像迁移规则执行次数
        :type execution_times: int (optional)

        :param filters: 资源筛选
        :type filters: List[ReplicationFilter] (optional)

        :param id: 镜像迁移规则ID
        :type id: int (optional)

        :param name: 镜像迁移规则名称
        :type name: str (optional)

        :param override: 是否覆盖目的仓库上的资源
        :type override: bool (optional)

        :param src_registry: src_registry field
        :type src_registry: ReplicationRegistry (optional)

        :param trigger: trigger field
        :type trigger: ReplicationTrigger (optional)

        :param update_time: 镜像迁移规则更新时间
        :type update_time: str (optional)
        """
        super().__init__()
        self.creation_time = creation_time
        self.deletion = deletion
        self.description = description
        self.dest_project_name = dest_project_name
        self.dest_registry = dest_registry
        self.enabled = enabled
        self.execution_times = execution_times
        self.filters = filters
        self.id = id
        self.name = name
        self.override = override
        self.src_registry = src_registry
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
        if self.deletion is not None:
            result['deletion'] = self.deletion
        if self.description is not None:
            result['description'] = self.description
        if self.dest_project_name is not None:
            result['destProjectName'] = self.dest_project_name
        if self.dest_registry is not None:
            result['destRegistry'] = self.dest_registry.to_dict()
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.execution_times is not None:
            result['executionTimes'] = self.execution_times
        if self.filters is not None:
            result['filters'] = [i.to_dict() for i in self.filters]
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.override is not None:
            result['override'] = self.override
        if self.src_registry is not None:
            result['srcRegistry'] = self.src_registry.to_dict()
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
        :rtype: GetImageMigrationRuleDetailResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('deletion') is not None:
            self.deletion = m.get('deletion')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('destProjectName') is not None:
            self.dest_project_name = m.get('destProjectName')
        if m.get('destRegistry') is not None:
            self.dest_registry = ReplicationRegistry().from_dict(m.get('destRegistry'))
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('executionTimes') is not None:
            self.execution_times = m.get('executionTimes')
        if m.get('filters') is not None:
            self.filters = [ReplicationFilter().from_dict(i) for i in m.get('filters')]
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('override') is not None:
            self.override = m.get('override')
        if m.get('srcRegistry') is not None:
            self.src_registry = ReplicationRegistry().from_dict(m.get('srcRegistry'))
        if m.get('trigger') is not None:
            self.trigger = ReplicationTrigger().from_dict(m.get('trigger'))
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self
