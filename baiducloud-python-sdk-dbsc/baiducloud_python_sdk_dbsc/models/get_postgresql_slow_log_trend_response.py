"""
Request entity for GetPostgresqlSlowLogTrendResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_dbsc.models.slow_trend_data_point import SlowTrendDataPoint


class GetPostgresqlSlowLogTrendResponse(BceResponse):
    """
    GetPostgresqlSlowLogTrendResponse
    """

    def __init__(self, data=None):
        """
        Initialize GetPostgresqlSlowLogTrendResponse response.

        :param data: 趋势数据点列表
        :type data: List[SlowTrendDataPoint] (optional)
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
        :rtype: GetPostgresqlSlowLogTrendResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('data') is not None:
            self.data = [SlowTrendDataPoint().from_dict(i) for i in m.get('data')]
        return self
