"""
Request entity for ListAlarmRecordRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListAlarmRecordRequest(AbstractModel):
    """
    Request entity for ListAlarmRecordRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        page_no,
        page_size,
        policy_name_pattern=None,
        policy_id_pattern=None,
        log_store_name_pattern=None,
        level=None,
        state=None,
        start_date_time=None,
        end_date_time=None,
        order_by=None,
        order=None,
    ):
        """
        Initialize ListAlarmRecordRequest request entity.

        :param policy_name_pattern: 按策略名称过滤
        :type policy_name_pattern: str (optional)

        :param policy_id_pattern: 按策略ID过滤
        :type policy_id_pattern: str (optional)

        :param log_store_name_pattern: 按日志集过滤
        :type log_store_name_pattern: str (optional)

        :param level: 按报警等级过滤, 取值：INFO, WARN, CRITICAL
        :type level: str (optional)

        :param state: 按报警状态过滤，取值：OK: 已恢复, ALERT: 报警中, CLOSED: 已关闭
        :type state: str (optional)

        :param start_date_time: 查询开始时间，UTC时间，默认值：30天前
        :type start_date_time: str (optional)

        :param end_date_time: 查询结束时间，UTC时间，默认值：当前时间
        :type end_date_time: str (optional)

        :param order_by: 排序字段，startTime: 报警开始时间， endTime: 报警结束时间，默认值：startTime
        :type order_by: str (optional)

        :param order: 排序方式，asc: 升序， desc: 降序，默认值：desc
        :type order: str (optional)

        :param page_no: 第几页，从1开始计数
        :type page_no: int (required)

        :param page_size: 每页展示数量，最大值：100
        :type page_size: int (required)
        """
        super().__init__()
        self.policy_name_pattern = policy_name_pattern
        self.policy_id_pattern = policy_id_pattern
        self.log_store_name_pattern = log_store_name_pattern
        self.level = level
        self.state = state
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
        if self.policy_name_pattern is not None:
            result['policyNamePattern'] = self.policy_name_pattern
        if self.policy_id_pattern is not None:
            result['policyIdPattern'] = self.policy_id_pattern
        if self.log_store_name_pattern is not None:
            result['logStoreNamePattern'] = self.log_store_name_pattern
        if self.level is not None:
            result['level'] = self.level
        if self.state is not None:
            result['state'] = self.state
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
        :rtype: ListAlarmRecordRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('policyNamePattern') is not None:
            self.policy_name_pattern = m.get('policyNamePattern')
        if m.get('policyIdPattern') is not None:
            self.policy_id_pattern = m.get('policyIdPattern')
        if m.get('logStoreNamePattern') is not None:
            self.log_store_name_pattern = m.get('logStoreNamePattern')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('state') is not None:
            self.state = m.get('state')
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
