"""
Request entity for CreateTriggerRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_ccr.models.trigger_filter import TriggerFilter
from baiducloud_python_sdk_ccr.models.trigger_target import TriggerTarget


class CreateTriggerRequest(AbstractModel):
    """
    Request entity for CreateTriggerRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, event_types, name, description=None, filters=None, targets=None):
        """
        Initialize CreateTriggerRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param description: 触发器策略备注
        :type description: str (optional)

        :param event_types: event_types parameter
        :type event_types: List[str] (required)

        :param filters: 触发规则
        :type filters: List[TriggerFilter] (optional)

        :param name: 触发器名称
        :type name: str (required)

        :param targets: 访问配置
        :type targets: List[TriggerTarget] (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.description = description
        self.event_types = event_types
        self.filters = filters
        self.name = name
        self.targets = targets

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
        if self.event_types is not None:
            result['eventTypes'] = self.event_types
        if self.filters is not None:
            result['filters'] = [i.to_dict() for i in self.filters]
        if self.name is not None:
            result['name'] = self.name
        if self.targets is not None:
            result['targets'] = [i.to_dict() for i in self.targets]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateTriggerRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('eventTypes') is not None:
            self.event_types = m.get('eventTypes')
        if m.get('filters') is not None:
            self.filters = [TriggerFilter().from_dict(i) for i in m.get('filters')]
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('targets') is not None:
            self.targets = [TriggerTarget().from_dict(i) for i in m.get('targets')]
        return self
