"""
TriggerPolicy information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ccr.models.trigger_filter import TriggerFilter

from baiducloud_python_sdk_ccr.models.trigger_target import TriggerTarget


class TriggerPolicy(AbstractModel):
    """
    TriggerPolicy
    """

    def __init__(
        self,
        creation_time=None,
        description=None,
        enabled=None,
        event_types=None,
        filters=None,
        id=None,
        name=None,
        targets=None,
        update_time=None,
    ):
        """
        Initialize TriggerPolicy instance.

        :param creation_time: 触发器创建时间
        :type creation_time: str (optional)

        :param description: 触发器策略备注
        :type description: str (optional)

        :param enabled: 启动状态
        :type enabled: bool (optional)

        :param event_types: event_types attribute
        :type event_types: List[str] (optional)

        :param filters: 触发规则
        :type filters: List[TriggerFilter] (optional)

        :param id: 触发器 ID
        :type id: int (optional)

        :param name: 触发器名称
        :type name: str (optional)

        :param targets: 访问配置
        :type targets: List[TriggerTarget] (optional)

        :param update_time: 触发器更新时间
        :type update_time: str (optional)
        """
        super().__init__()
        self.creation_time = creation_time
        self.description = description
        self.enabled = enabled
        self.event_types = event_types
        self.filters = filters
        self.id = id
        self.name = name
        self.targets = targets
        self.update_time = update_time

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
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.description is not None:
            result['description'] = self.description
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.event_types is not None:
            result['eventTypes'] = self.event_types
        if self.filters is not None:
            result['filters'] = [i.to_dict() for i in self.filters]
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.targets is not None:
            result['targets'] = [i.to_dict() for i in self.targets]
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TriggerPolicy

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('eventTypes') is not None:
            self.event_types = m.get('eventTypes')
        if m.get('filters') is not None:
            self.filters = [TriggerFilter().from_dict(i) for i in m.get('filters')]
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('targets') is not None:
            self.targets = [TriggerTarget().from_dict(i) for i in m.get('targets')]
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self
