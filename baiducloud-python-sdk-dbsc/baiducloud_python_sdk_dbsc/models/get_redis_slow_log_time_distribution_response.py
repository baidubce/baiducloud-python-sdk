"""
Request entity for GetRedisSlowLogTimeDistributionResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_dbsc.models.scs_slowlog_stats_duartion import SCSSlowlogStatsDuartion


class GetRedisSlowLogTimeDistributionResponse(BceResponse):
    """
    GetRedisSlowLogTimeDistributionResponse
    """

    def __init__(self, stats=None):
        """
        Initialize GetRedisSlowLogTimeDistributionResponse response.

        :param stats: 返回统计区间信息
        :type stats: List[SCSSlowlogStatsDuartion] (optional)
        """
        super().__init__()
        self.stats = stats

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
        if self.stats is not None:
            result['stats'] = [i.to_dict() for i in self.stats]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetRedisSlowLogTimeDistributionResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('stats') is not None:
            self.stats = [SCSSlowlogStatsDuartion().from_dict(i) for i in m.get('stats')]
        return self
