"""
Request entity for ListAlarmExecutionStatsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListAlarmExecutionStatsRequest(AbstractModel):
    """
    Request entity for ListAlarmExecutionStatsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        page_no,
        page_size,
        policy_id=None,
        policy_name=None,
        log_store_name=None,
        states=None,
        start_date_time=None,
        end_date_time=None,
        order_by=None,
        order=None,
    ):
        """
        Initialize ListAlarmExecutionStatsRequest request entity.

        :param policy_id: 按策略ID过滤
        :type policy_id: str (optional)

        :param policy_name: 按策略名称过滤
        :type policy_name: str (optional)

        :param log_store_name: 按日志集过滤
        :type log_store_name: str (optional)

        :param states: 按报警状态过滤，取值：OK: 已恢复, ALERT: 报警中, CLOSED: 已关闭
        :type states: List[str] (optional)

        :param start_date_time: 查询开始时间，UTC时间，默认值：30天前
        :type start_date_time: str (optional)

        :param end_date_time: 查询结束时间，UTC时间，默认值：当前时间
        :type end_date_time: str (optional)

        :param order_by: order_by parameter
        :type order_by: str (optional)

        :param order: 排序方式，asc: 升序， desc: 降序，默认值：desc
        :type order: str (optional)

        :param page_no: 第几页，从1开始计数
        :type page_no: int (required)

        :param page_size: 每页展示数量，最大值：100
        :type page_size: int (required)
        """
        super().__init__()
        self.policy_id = policy_id
        self.policy_name = policy_name
        self.log_store_name = log_store_name
        self.states = states
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
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
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.log_store_name is not None:
            result['logStoreName'] = self.log_store_name
        if self.states is not None:
            result['states'] = self.states
        if self.start_date_time is not None:
            result['startDateTime'] = self.start_date_time
        if self.end_date_time is not None:
            result['endDateTime'] = self.end_date_time
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
        :rtype: ListAlarmExecutionStatsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('logStoreName') is not None:
            self.log_store_name = m.get('logStoreName')
        if m.get('states') is not None:
            self.states = m.get('states')
        if m.get('startDateTime') is not None:
            self.start_date_time = m.get('startDateTime')
        if m.get('endDateTime') is not None:
            self.end_date_time = m.get('endDateTime')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
