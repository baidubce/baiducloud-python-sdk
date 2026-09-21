"""
Request entity for GetMongodbSlowLogTrendResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_dbsc.models.slow_log_trend import SlowLogTrend


class GetMongodbSlowLogTrendResponse(BceResponse):
    """
    GetMongodbSlowLogTrendResponse
    """

    def __init__(self, data=None):
        """
        Initialize GetMongodbSlowLogTrendResponse response.

        :param data: 慢日志趋势数据
        :type data: List[SlowLogTrend] (optional)
        """
        super().__init__()
        self.data = data

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
        if self.data is not None:
            result['data'] = [i.to_dict() for i in self.data]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetMongodbSlowLogTrendResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('data') is not None:
            self.data = [SlowLogTrend().from_dict(i) for i in m.get('data')]
        return self
