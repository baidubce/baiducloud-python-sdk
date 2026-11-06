"""
Request entity for GetPgLogListResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_rds.models.pg_log_response import PgLogResponse


class GetPgLogListResponse(BceResponse):
    """
    GetPgLogListResponse
    """

    def __init__(self, pg_logs=None):
        """
        Initialize GetPgLogListResponse response.

        :param pg_logs: pg 日志列表响应结构。
        :type pg_logs: List[PgLogResponse] (optional)
        """
        super().__init__()
        self.pg_logs = pg_logs

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
        if self.pg_logs is not None:
            result['pgLogs'] = [i.to_dict() for i in self.pg_logs]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetPgLogListResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('pgLogs') is not None:
            self.pg_logs = [PgLogResponse().from_dict(i) for i in m.get('pgLogs')]
        return self
