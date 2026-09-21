"""
GetMongodbSlowLogTimeDistributionResponse information
"""

from baiducloud_python_sdk_core.bce_response import BceResponse

from baiducloud_python_sdk_dbsc.models.my_sql_slow_log_stats_by_duration import MySQLSlowLogStatsByDuration


class GetMongodbSlowLogTimeDistributionResponse(BceResponse):
    """
    GetMongodbSlowLogTimeDistributionResponse
    """

    def __init__(self, stats=None):
        """
        Initialize GetMongodbSlowLogTimeDistributionResponse instance.

        :param stats: 执行时间区间分布数据
        :type stats: List[MySQLSlowLogStatsByDuration] (optional)
        """
        super().__init__()
        self.stats = stats

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        Includes metadata from the parent BceResponse class.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.stats is not None:
            result['stats'] = [i.to_dict() for i in self.stats]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetMongodbSlowLogTimeDistributionResponse

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('stats') is not None:
            self.stats = [MySQLSlowLogStatsByDuration().from_dict(i) for i in m.get('stats')]
        return self
