"""
EventExecution information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_oos.models.template import Template

from baiducloud_python_sdk_oos.models.event import Event

from baiducloud_python_sdk_oos.models.tag import Tag


class EventExecution(AbstractModel):
    """
    EventExecution
    """

    def __init__(
        self,
        namespace=None,
        name=None,
        state=None,
        description=None,
        template=None,
        properties=None,
        event=None,
        silent_cycle_milli=None,
        tags=None,
        template_deleted=None,
        locale=None,
    ):
        """
        Initialize EventExecution instance.

        :param namespace: 名称空间
        :type namespace: str (optional)

        :param name: 事件运维名称
        :type name: str (optional)

        :param state: 状态：RUNNING/STOPPED
        :type state: str (optional)

        :param description: 描述
        :type description: str (optional)

        :param template: template attribute
        :type template: Template (optional)

        :param properties: 全局参数取值集合
        :type properties: Dict[str, object] (optional)

        :param event: event attribute
        :type event: Event (optional)

        :param silent_cycle_milli: 静默周期，单位毫秒
        :type silent_cycle_milli: int (optional)

        :param tags: 标签
        :type tags: List[Tag] (optional)

        :param template_deleted: 模板是否已被删除
        :type template_deleted: bool (optional)

        :param locale: 语言
        :type locale: str (optional)
        """
        super().__init__()
        self.namespace = namespace
        self.name = name
        self.state = state
        self.description = description
        self.template = template
        self.properties = properties
        self.event = event
        self.silent_cycle_milli = silent_cycle_milli
        self.tags = tags
        self.template_deleted = template_deleted
        self.locale = locale

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
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.name is not None:
            result['name'] = self.name
        if self.state is not None:
            result['state'] = self.state
        if self.description is not None:
            result['description'] = self.description
        if self.template is not None:
            result['template'] = self.template.to_dict()
        if self.properties is not None:
            result['properties'] = self.properties
        if self.event is not None:
            result['event'] = self.event.to_dict()
        if self.silent_cycle_milli is not None:
            result['silentCycleMilli'] = self.silent_cycle_milli
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.template_deleted is not None:
            result['templateDeleted'] = self.template_deleted
        if self.locale is not None:
            result['locale'] = self.locale
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EventExecution

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('template') is not None:
            self.template = Template().from_dict(m.get('template'))
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('event') is not None:
            self.event = Event().from_dict(m.get('event'))
        if m.get('silentCycleMilli') is not None:
            self.silent_cycle_milli = m.get('silentCycleMilli')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        if m.get('templateDeleted') is not None:
            self.template_deleted = m.get('templateDeleted')
        if m.get('locale') is not None:
            self.locale = m.get('locale')
        return self
