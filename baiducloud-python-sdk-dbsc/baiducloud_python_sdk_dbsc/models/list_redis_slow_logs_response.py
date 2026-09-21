"""
Request entity for ListRedisSlowLogsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_dbsc.models.scs_slow_log_info import SCSSlowLogInfo


class ListRedisSlowLogsResponse(BceResponse):
    """
    ListRedisSlowLogsResponse
    """

    def __init__(
        self,
        app_id=None,
        node_id=None,
        request_id=None,
        start=None,
        end=None,
        total_record_count=None,
        max_record_count_per_page=None,
        page_number=None,
        record_count_in_current_page=None,
        records=None,
    ):
        """
        Initialize ListRedisSlowLogsResponse response.

        :param app_id: 集群ID
        :type app_id: str (optional)

        :param node_id: 节点ID
        :type node_id: str (optional)

        :param request_id: 请求ID
        :type request_id: str (optional)

        :param start: 慢日志起始时间范围节点
        :type start: str (optional)

        :param end: 慢日志结束时间范围节点
        :type end: str (optional)

        :param total_record_count: 慢日志总数
        :type total_record_count: int (optional)

        :param max_record_count_per_page: 每页返回日志的最大数量
        :type max_record_count_per_page: int (optional)

        :param page_number: 当前页码
        :type page_number: int (optional)

        :param record_count_in_current_page: 当前页慢日志数量
        :type record_count_in_current_page: int (optional)

        :param records: 慢日志信息列表
        :type records: List[SCSSlowLogInfo] (optional)
        """
        super().__init__()
        self.app_id = app_id
        self.node_id = node_id
        self.request_id = request_id
        self.start = start
        self.end = end
        self.total_record_count = total_record_count
        self.max_record_count_per_page = max_record_count_per_page
        self.page_number = page_number
        self.record_count_in_current_page = record_count_in_current_page
        self.records = records

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.node_id is not None:
            result['nodeId'] = self.node_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.start is not None:
            result['start'] = self.start
        if self.end is not None:
            result['end'] = self.end
        if self.total_record_count is not None:
            result['totalRecordCount'] = self.total_record_count
        if self.max_record_count_per_page is not None:
            result['maxRecordCountPerPage'] = self.max_record_count_per_page
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.record_count_in_current_page is not None:
            result['recordCountInCurrentPage'] = self.record_count_in_current_page
        if self.records is not None:
            result['records'] = [i.to_dict() for i in self.records]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListRedisSlowLogsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('start') is not None:
            self.start = m.get('start')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('totalRecordCount') is not None:
            self.total_record_count = m.get('totalRecordCount')
        if m.get('maxRecordCountPerPage') is not None:
            self.max_record_count_per_page = m.get('maxRecordCountPerPage')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('recordCountInCurrentPage') is not None:
            self.record_count_in_current_page = m.get('recordCountInCurrentPage')
        if m.get('records') is not None:
            self.records = [SCSSlowLogInfo().from_dict(i) for i in m.get('records')]
        return self
