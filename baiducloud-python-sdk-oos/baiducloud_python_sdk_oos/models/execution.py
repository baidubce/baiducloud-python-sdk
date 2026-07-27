"""
Execution information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_oos.models.template import Template

from baiducloud_python_sdk_oos.models.execution_task_summary import ExecutionTaskSummary

from baiducloud_python_sdk_oos.models.tag import Tag

from baiducloud_python_sdk_oos.models.event_execution import EventExecution

from baiducloud_python_sdk_oos.models.cron_execution import CronExecution


class Execution(AbstractModel):
    """
    Execution
    """

    def __init__(
        self,
        id=None,
        description=None,
        template=None,
        template_deleted=None,
        parallelism=None,
        manually=None,
        created_timestamp=None,
        updated_timestamp=None,
        finished_timestamp=None,
        state=None,
        properties=None,
        tasks=None,
        tags=None,
        trigger=None,
        reason=None,
        error_code=None,
        event_execution=None,
        cron_execution=None,
        locale=None,
    ):
        """
        Initialize Execution instance.

        :param id: 执行 ID，全局唯一，由服务端自动生成
        :type id: str (optional)

        :param description: 执行描述
        :type description: str (optional)

        :param template: template attribute
        :type template: Template (optional)

        :param template_deleted: 模板是否已被删除
        :type template_deleted: bool (optional)

        :param parallelism: 并发度
        :type parallelism: int (optional)

        :param manually: 是否手动触发
        :type manually: bool (optional)

        :param created_timestamp: 执行开始时间，Unix 时间戳，单位：毫秒；仅用于查询详情或列表接口的字段返回
        :type created_timestamp: int (optional)

        :param updated_timestamp: 执行更新时间，Unix 时间戳，单位：毫秒；仅用于查询详情或列表接口的字段返回
        :type updated_timestamp: int (optional)

        :param finished_timestamp: 执行结束时间，Unix 时间戳，单位：毫秒，未结束填 0；仅用于查询详情或列表接口的字段返回
        :type finished_timestamp: int (optional)

        :param state: state attribute
        :type state: str (optional)

        :param properties: 全局参数取值集合
        :type properties: Dict[str, object] (optional)

        :param tasks: 执行中的任务列表；执行列表接口响应固定为空数组，仅用于查询详情接口的字段返回
        :type tasks: List[ExecutionTaskSummary] (optional)

        :param tags: 执行绑定标签列表
        :type tags: List[Tag] (optional)

        :param trigger: 触发执行的方式
        :type trigger: str (optional)

        :param reason: 原因（失败/取消等）
        :type reason: str (optional)

        :param error_code: 错误码
        :type error_code: str (optional)

        :param event_execution: event_execution attribute
        :type event_execution: EventExecution (optional)

        :param cron_execution: cron_execution attribute
        :type cron_execution: CronExecution (optional)

        :param locale: 语言
        :type locale: str (optional)
        """
        super().__init__()
        self.id = id
        self.description = description
        self.template = template
        self.template_deleted = template_deleted
        self.parallelism = parallelism
        self.manually = manually
        self.created_timestamp = created_timestamp
        self.updated_timestamp = updated_timestamp
        self.finished_timestamp = finished_timestamp
        self.state = state
        self.properties = properties
        self.tasks = tasks
        self.tags = tags
        self.trigger = trigger
        self.reason = reason
        self.error_code = error_code
        self.event_execution = event_execution
        self.cron_execution = cron_execution
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
        if self.id is not None:
            result['id'] = self.id
        if self.description is not None:
            result['description'] = self.description
        if self.template is not None:
            result['template'] = self.template.to_dict()
        if self.template_deleted is not None:
            result['templateDeleted'] = self.template_deleted
        if self.parallelism is not None:
            result['parallelism'] = self.parallelism
        if self.manually is not None:
            result['manually'] = self.manually
        if self.created_timestamp is not None:
            result['createdTimestamp'] = self.created_timestamp
        if self.updated_timestamp is not None:
            result['updatedTimestamp'] = self.updated_timestamp
        if self.finished_timestamp is not None:
            result['finishedTimestamp'] = self.finished_timestamp
        if self.state is not None:
            result['state'] = self.state
        if self.properties is not None:
            result['properties'] = self.properties
        if self.tasks is not None:
            result['tasks'] = [i.to_dict() for i in self.tasks]
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.trigger is not None:
            result['trigger'] = self.trigger
        if self.reason is not None:
            result['reason'] = self.reason
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.event_execution is not None:
            result['eventExecution'] = self.event_execution.to_dict()
        if self.cron_execution is not None:
            result['cronExecution'] = self.cron_execution.to_dict()
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
        :rtype: Execution

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('template') is not None:
            self.template = Template().from_dict(m.get('template'))
        if m.get('templateDeleted') is not None:
            self.template_deleted = m.get('templateDeleted')
        if m.get('parallelism') is not None:
            self.parallelism = m.get('parallelism')
        if m.get('manually') is not None:
            self.manually = m.get('manually')
        if m.get('createdTimestamp') is not None:
            self.created_timestamp = m.get('createdTimestamp')
        if m.get('updatedTimestamp') is not None:
            self.updated_timestamp = m.get('updatedTimestamp')
        if m.get('finishedTimestamp') is not None:
            self.finished_timestamp = m.get('finishedTimestamp')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('tasks') is not None:
            self.tasks = [ExecutionTaskSummary().from_dict(i) for i in m.get('tasks')]
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        if m.get('trigger') is not None:
            self.trigger = m.get('trigger')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('eventExecution') is not None:
            self.event_execution = EventExecution().from_dict(m.get('eventExecution'))
        if m.get('cronExecution') is not None:
            self.cron_execution = CronExecution().from_dict(m.get('cronExecution'))
        if m.get('locale') is not None:
            self.locale = m.get('locale')
        return self
