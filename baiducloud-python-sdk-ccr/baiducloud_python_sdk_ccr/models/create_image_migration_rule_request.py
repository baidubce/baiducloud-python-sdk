"""
Request entity for CreateImageMigrationRuleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_ccr.models.replication_filter_request import ReplicationFilterRequest
from baiducloud_python_sdk_ccr.models.replication_registry_request import ReplicationRegistryRequest
from baiducloud_python_sdk_ccr.models.replication_trigger_request import ReplicationTriggerRequest


class CreateImageMigrationRuleRequest(AbstractModel):
    """
    Request entity for CreateImageMigrationRuleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, instance_id, dest_project_name, filters, name, override, src_registry, trigger, description=None
    ):
        """
        Initialize CreateImageMigrationRuleRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param description: 镜像迁移规则描述
        :type description: str (optional)

        :param dest_project_name: 目的命名空间
        :type dest_project_name: str (required)

        :param filters: 资源筛选
        :type filters: List[ReplicationFilterRequest] (required)

        :param name: 镜像迁移规则名称
        :type name: str (required)

        :param override: 是否覆盖目的仓库上的资源
        :type override: bool (required)

        :param src_registry: src_registry parameter
        :type src_registry: ReplicationRegistryRequest (required)

        :param trigger: trigger parameter
        :type trigger: ReplicationTriggerRequest (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.description = description
        self.dest_project_name = dest_project_name
        self.filters = filters
        self.name = name
        self.override = override
        self.src_registry = src_registry
        self.trigger = trigger

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
        if self.description is not None:
            result['description'] = self.description
        if self.dest_project_name is not None:
            result['destProjectName'] = self.dest_project_name
        if self.filters is not None:
            result['filters'] = [i.to_dict() for i in self.filters]
        if self.name is not None:
            result['name'] = self.name
        if self.override is not None:
            result['override'] = self.override
        if self.src_registry is not None:
            result['srcRegistry'] = self.src_registry.to_dict()
        if self.trigger is not None:
            result['trigger'] = self.trigger.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateImageMigrationRuleRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('destProjectName') is not None:
            self.dest_project_name = m.get('destProjectName')
        if m.get('filters') is not None:
            self.filters = [ReplicationFilterRequest().from_dict(i) for i in m.get('filters')]
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('override') is not None:
            self.override = m.get('override')
        if m.get('srcRegistry') is not None:
            self.src_registry = ReplicationRegistryRequest().from_dict(m.get('srcRegistry'))
        if m.get('trigger') is not None:
            self.trigger = ReplicationTriggerRequest().from_dict(m.get('trigger'))
        return self
