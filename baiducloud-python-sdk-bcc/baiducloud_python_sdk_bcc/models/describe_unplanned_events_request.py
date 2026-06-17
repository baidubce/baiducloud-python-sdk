"""
Request entity for DescribeUnplannedEventsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescribeUnplannedEventsRequest(AbstractModel):
    """
    Request entity for DescribeUnplannedEventsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        action,
        server_event_status=None,
        server_event_ids=None,
        instance_ids=None,
        product_category=None,
        server_event_type=None,
        server_event_log_time_filter=None,
        period_start_time=None,
        period_end_time=None,
        max_keys=None,
        marker=None,
    ):
        """
        Initialize DescribeUnplannedEventsRequest request entity.

        :param action: action parameter
        :type action: str (required)

        :param server_event_status: server_event_status parameter
        :type server_event_status: str (optional)

        :param server_event_ids: 维修事件的id列表
        :type server_event_ids: List[str] (optional)

        :param instance_ids: 虚机的短id列表
        :type instance_ids: List[str] (optional)

        :param product_category: 故障实例产品类型 （BBC / BCC / HPAS）
        :type product_category: str (optional)

        :param server_event_type: server_event_type parameter
        :type server_event_type: str (optional)

        :param server_event_log_time_filter: server_event_log_time_filter parameter
        :type server_event_log_time_filter: str (optional)

        :param period_start_time: timeFilter类型开始时间, 若为空则只按照periodEndTime限制，符合BCE规范的日期格式
        :type period_start_time: str (optional)

        :param period_end_time: timeFilter类型结束时间, 若为空则只按照periodStartTime限制，符合BCE规范的日期格式
        :type period_end_time: str (optional)

        :param max_keys: 每页包含的最大数量，最大数量通常不超过100，缺省值为10
        :type max_keys: int (optional)

        :param marker: 批量获取列表的查询的起始事件id
        :type marker: str (optional)
        """
        super().__init__()
        self.action = action
        self.server_event_status = server_event_status
        self.server_event_ids = server_event_ids
        self.instance_ids = instance_ids
        self.product_category = product_category
        self.server_event_type = server_event_type
        self.server_event_log_time_filter = server_event_log_time_filter
        self.period_start_time = period_start_time
        self.period_end_time = period_end_time
        self.max_keys = max_keys
        self.marker = marker

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
        if self.server_event_status is not None:
            result['serverEventStatus'] = self.server_event_status
        if self.server_event_ids is not None:
            result['serverEventIds'] = self.server_event_ids
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids
        if self.product_category is not None:
            result['productCategory'] = self.product_category
        if self.server_event_type is not None:
            result['serverEventType'] = self.server_event_type
        if self.server_event_log_time_filter is not None:
            result['serverEventLogTimeFilter'] = self.server_event_log_time_filter
        if self.period_start_time is not None:
            result['periodStartTime'] = self.period_start_time
        if self.period_end_time is not None:
            result['periodEndTime'] = self.period_end_time
        if self.max_keys is not None:
            result['maxKeys'] = self.max_keys
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeUnplannedEventsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('serverEventStatus') is not None:
            self.server_event_status = m.get('serverEventStatus')
        if m.get('serverEventIds') is not None:
            self.server_event_ids = m.get('serverEventIds')
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        if m.get('productCategory') is not None:
            self.product_category = m.get('productCategory')
        if m.get('serverEventType') is not None:
            self.server_event_type = m.get('serverEventType')
        if m.get('serverEventLogTimeFilter') is not None:
            self.server_event_log_time_filter = m.get('serverEventLogTimeFilter')
        if m.get('periodStartTime') is not None:
            self.period_start_time = m.get('periodStartTime')
        if m.get('periodEndTime') is not None:
            self.period_end_time = m.get('periodEndTime')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self
