"""
CronExecution information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_oos.models.template import Template

from baiducloud_python_sdk_oos.models.tag import Tag

from baiducloud_python_sdk_oos.models.period import Period


class CronExecution(AbstractModel):
    """
    CronExecution
    """

    def __init__(
        self,
        namespace=None,
        description=None,
        name=None,
        template=None,
        template_deleted=None,
        properties=None,
        tags=None,
        cron=None,
        period=None,
        depend_on_past=None,
        schedule_timeout=None,
        created_timestamp=None,
        updated_timestamp=None,
        next_schedule_timestamp=None,
        begin_timestamp=None,
        end_timestamp=None,
        state=None,
        locale=None,
    ):
        """
        Initialize CronExecution instance.

        :param namespace: 名称空间
        :type namespace: str (optional)

        :param description: 描述
        :type description: str (optional)

        :param name: 定时运维名称
        :type name: str (optional)

        :param template: template attribute
        :type template: Template (optional)

        :param template_deleted: 模板是否已被删除
        :type template_deleted: bool (optional)

        :param properties: 全局参数取值集合
        :type properties: object (optional)

        :param tags: 标签
        :type tags: List[Tag] (optional)

        :param cron: cron 表达式
        :type cron: str (optional)

        :param period: period attribute
        :type period: Period (optional)

        :param depend_on_past: 是否依赖上次执行
        :type depend_on_past: bool (optional)

        :param schedule_timeout: 调度超时（毫秒）
        :type schedule_timeout: int (optional)

        :param created_timestamp: 创建时间，Unix 时间戳，单位：毫秒
        :type created_timestamp: int (optional)

        :param updated_timestamp: 更新时间，Unix 时间戳，单位：毫秒
        :type updated_timestamp: int (optional)

        :param next_schedule_timestamp: 下一次调度时间，Unix 时间戳，单位：毫秒
        :type next_schedule_timestamp: int (optional)

        :param begin_timestamp: 生效开始时间，Unix 时间戳，单位：毫秒
        :type begin_timestamp: int (optional)

        :param end_timestamp: 生效结束时间，Unix 时间戳，单位：毫秒
        :type end_timestamp: int (optional)

        :param state: 状态
        :type state: str (optional)

        :param locale: 语言
        :type locale: str (optional)
        """
        super().__init__()
        self.namespace = namespace
        self.description = description
        self.name = name
        self.template = template
        self.template_deleted = template_deleted
        self.properties = properties
        self.tags = tags
        self.cron = cron
        self.period = period
        self.depend_on_past = depend_on_past
        self.schedule_timeout = schedule_timeout
        self.created_timestamp = created_timestamp
        self.updated_timestamp = updated_timestamp
        self.next_schedule_timestamp = next_schedule_timestamp
        self.begin_timestamp = begin_timestamp
        self.end_timestamp = end_timestamp
        self.state = state
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
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.template is not None:
            result['template'] = self.template.to_dict()
        if self.template_deleted is not None:
            result['templateDeleted'] = self.template_deleted
        if self.properties is not None:
            result['properties'] = self.properties
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.cron is not None:
            result['cron'] = self.cron
        if self.period is not None:
            result['period'] = self.period.to_dict()
        if self.depend_on_past is not None:
            result['dependOnPast'] = self.depend_on_past
        if self.schedule_timeout is not None:
            result['scheduleTimeout'] = self.schedule_timeout
        if self.created_timestamp is not None:
            result['createdTimestamp'] = self.created_timestamp
        if self.updated_timestamp is not None:
            result['updatedTimestamp'] = self.updated_timestamp
        if self.next_schedule_timestamp is not None:
            result['nextScheduleTimestamp'] = self.next_schedule_timestamp
        if self.begin_timestamp is not None:
            result['beginTimestamp'] = self.begin_timestamp
        if self.end_timestamp is not None:
            result['endTimestamp'] = self.end_timestamp
        if self.state is not None:
            result['state'] = self.state
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
        :rtype: CronExecution

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('template') is not None:
            self.template = Template().from_dict(m.get('template'))
        if m.get('templateDeleted') is not None:
            self.template_deleted = m.get('templateDeleted')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        if m.get('cron') is not None:
            self.cron = m.get('cron')
        if m.get('period') is not None:
            self.period = Period().from_dict(m.get('period'))
        if m.get('dependOnPast') is not None:
            self.depend_on_past = m.get('dependOnPast')
        if m.get('scheduleTimeout') is not None:
            self.schedule_timeout = m.get('scheduleTimeout')
        if m.get('createdTimestamp') is not None:
            self.created_timestamp = m.get('createdTimestamp')
        if m.get('updatedTimestamp') is not None:
            self.updated_timestamp = m.get('updatedTimestamp')
        if m.get('nextScheduleTimestamp') is not None:
            self.next_schedule_timestamp = m.get('nextScheduleTimestamp')
        if m.get('beginTimestamp') is not None:
            self.begin_timestamp = m.get('beginTimestamp')
        if m.get('endTimestamp') is not None:
            self.end_timestamp = m.get('endTimestamp')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('locale') is not None:
            self.locale = m.get('locale')
        return self
