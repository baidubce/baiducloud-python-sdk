"""
Request entity for GetExecutionListV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetExecutionListV2Request(AbstractModel):
    """
    Request entity for GetExecutionListV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        page_no,
        page_size,
        locale=None,
        namespace=None,
        template=None,
        state=None,
        trigger=None,
        cron_execution_name=None,
        event_execution_name=None,
        start_time=None,
        end_time=None,
        sort=None,
        ascending=None,
    ):
        """
        Initialize GetExecutionListV2Request request entity.

        :param locale: locale parameter
        :type locale: str (optional)

        :param namespace: 名称空间，默认 default
        :type namespace: str (optional)

        :param template: 模版过滤条件
        :type template: object (optional)

        :param state: state parameter
        :type state: str (optional)

        :param trigger: 触发方式
        :type trigger: str (optional)

        :param cron_execution_name: 定时运维名称，如设置则只返回指定定时运维触发的执行列表
        :type cron_execution_name: str (optional)

        :param event_execution_name: 报警事件运维名称，如设置则只返回指定报警事件运维触发的执行列表
        :type event_execution_name: str (optional)

        :param start_time: 执行开始时间，单位：毫秒，默认值为7天前毫秒时间戳
        :type start_time: int (optional)

        :param end_time: 执行结束时间，单位：毫秒，默认值为当前毫秒时间戳
        :type end_time: int (optional)

        :param sort: 排序字段，默认为执行开始时间，可选值：startTime，endTime
        :type sort: str (optional)

        :param ascending: 是否升序，默认false
        :type ascending: bool (optional)

        :param page_no: 页数，从 1 开始计数
        :type page_no: int (required)

        :param page_size: 每页展示数量，最大 100
        :type page_size: int (required)
        """
        super().__init__()
        self.locale = locale
        self.namespace = namespace
        self.template = template
        self.state = state
        self.trigger = trigger
        self.cron_execution_name = cron_execution_name
        self.event_execution_name = event_execution_name
        self.start_time = start_time
        self.end_time = end_time
        self.sort = sort
        self.ascending = ascending
        self.page_no = page_no
        self.page_size = page_size

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
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.template is not None:
            result['template'] = self.template
        if self.state is not None:
            result['state'] = self.state
        if self.trigger is not None:
            result['trigger'] = self.trigger
        if self.cron_execution_name is not None:
            result['cronExecutionName'] = self.cron_execution_name
        if self.event_execution_name is not None:
            result['eventExecutionName'] = self.event_execution_name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.sort is not None:
            result['sort'] = self.sort
        if self.ascending is not None:
            result['ascending'] = self.ascending
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetExecutionListV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('locale') is not None:
            self.locale = m.get('locale')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('template') is not None:
            self.template = m.get('template')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('trigger') is not None:
            self.trigger = m.get('trigger')
        if m.get('cronExecutionName') is not None:
            self.cron_execution_name = m.get('cronExecutionName')
        if m.get('eventExecutionName') is not None:
            self.event_execution_name = m.get('eventExecutionName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('sort') is not None:
            self.sort = m.get('sort')
        if m.get('ascending') is not None:
            self.ascending = m.get('ascending')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
