"""
Request entity for ApmDescribeAlarmsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ApmDescribeAlarmsRequest(AbstractModel):
    """
    Request entity for ApmDescribeAlarmsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        begin_datetime,
        end_datetime,
        page_no,
        page_size,
        policy_name=None,
        level=None,
        metric_kind=None,
        state=None,
        order_by=None,
        order=None,
    ):
        """
        Initialize ApmDescribeAlarmsRequest request entity.

        :param begin_datetime: 开始时间，UTC时间
        :type begin_datetime: str (required)

        :param end_datetime: 结束时间，UTC时间
        :type end_datetime: str (required)

        :param policy_name: 按策略名称过滤
        :type policy_name: str (optional)

        :param level: 报警等级过滤，可选值：NOTICE-通知，WARNING-警告，MAJOR-重要，CRITICAL-严重
        :type level: str (optional)

        :param metric_kind: metric_kind parameter
        :type metric_kind: str (optional)

        :param state: 报警状态过滤，可选值：OK-已恢复，ALERT-报警中，NODATA-无数据报警，CLOSED-已关闭
        :type state: str (optional)

        :param order_by: 排序字段，默认值：startTime，可选值：startTime-报警开始时间
        :type order_by: str (optional)

        :param order: 排序方式，默认值：desc，可选值：desc-降序，asc-升序
        :type order: str (optional)

        :param page_no: 第几页，从1开始计数
        :type page_no: int (required)

        :param page_size: 每页展示数量，最大值：100
        :type page_size: int (required)
        """
        super().__init__()
        self.begin_datetime = begin_datetime
        self.end_datetime = end_datetime
        self.policy_name = policy_name
        self.level = level
        self.metric_kind = metric_kind
        self.state = state
        self.order_by = order_by
        self.order = order
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
        if self.begin_datetime is not None:
            result['beginDatetime'] = self.begin_datetime
        if self.end_datetime is not None:
            result['endDatetime'] = self.end_datetime
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.level is not None:
            result['level'] = self.level
        if self.metric_kind is not None:
            result['metricKind'] = self.metric_kind
        if self.state is not None:
            result['state'] = self.state
        if self.order_by is not None:
            result['orderBy'] = self.order_by
        if self.order is not None:
            result['order'] = self.order
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
        :rtype: ApmDescribeAlarmsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('beginDatetime') is not None:
            self.begin_datetime = m.get('beginDatetime')
        if m.get('endDatetime') is not None:
            self.end_datetime = m.get('endDatetime')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('metricKind') is not None:
            self.metric_kind = m.get('metricKind')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
