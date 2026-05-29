"""
SearchStatistic information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bls.models.bucket import Bucket


class SearchStatistic(AbstractModel):
    """
    SearchStatistic
    """

    def __init__(self, interval=None, start_time=None, end_time=None, histogram=None):
        """
        Initialize SearchStatistic instance.

        :param interval: 直方图统计单个区间大小，统计区间的毫秒数
        :type interval: int (optional)

        :param start_time: 直方图统计的开始时间，是请求中的startDateTime
        :type start_time: str (optional)

        :param end_time: 直方图统计的结束时间，是请求中的endDateTime
        :type end_time: str (optional)

        :param histogram: 直方图统计区间的数据条数，直方图按区间大小，顺序分割排列，各个时间区间的日志数量
        :type histogram: List[Bucket] (optional)
        """
        super().__init__()
        self.interval = interval
        self.start_time = start_time
        self.end_time = end_time
        self.histogram = histogram

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.interval is not None:
            result['interval'] = self.interval
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.histogram is not None:
            result['histogram'] = [i.to_dict() for i in self.histogram]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SearchStatistic

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('interval') is not None:
            self.interval = m.get('interval')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('histogram') is not None:
            self.histogram = [Bucket().from_dict(i) for i in m.get('histogram')]
        return self
