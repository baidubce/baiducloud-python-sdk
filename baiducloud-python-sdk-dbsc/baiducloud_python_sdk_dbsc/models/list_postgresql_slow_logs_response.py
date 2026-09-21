"""
Request entity for ListPostgresqlSlowLogsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_dbsc.models.pg_slow_log_info import PGSlowLogInfo


class ListPostgresqlSlowLogsResponse(BceResponse):
    """
    ListPostgresqlSlowLogsResponse
    """

    def __init__(self, total_count=None, logs=None):
        """
        Initialize ListPostgresqlSlowLogsResponse response.

        :param total_count: 总记录数
        :type total_count: int (optional)

        :param logs: 慢日志信息列表
        :type logs: List[PGSlowLogInfo] (optional)
        """
        super().__init__()
        self.total_count = total_count
        self.logs = logs

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
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.logs is not None:
            result['logs'] = [i.to_dict() for i in self.logs]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListPostgresqlSlowLogsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('logs') is not None:
            self.logs = [PGSlowLogInfo().from_dict(i) for i in m.get('logs')]
        return self
