"""
Request entity for LogListResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_scs.models.shard_log import ShardLog


class LogListResponse(BceResponse):
    """
    LogListResponse
    """

    def __init__(self, log_list=None):
        """
        Initialize LogListResponse response.

        :param log_list: 日志列表
        :type log_list: List[ShardLog] (optional)
        """
        super().__init__()
        self.log_list = log_list

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
        if self.log_list is not None:
            result['logList'] = [i.to_dict() for i in self.log_list]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: LogListResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('logList') is not None:
            self.log_list = [ShardLog().from_dict(i) for i in m.get('logList')]
        return self
