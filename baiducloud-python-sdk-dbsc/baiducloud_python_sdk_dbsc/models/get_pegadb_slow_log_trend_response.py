"""
GetPegadbSlowLogTrendResponse information
"""

from baiducloud_python_sdk_core.bce_response import BceResponse

from baiducloud_python_sdk_dbsc.models.scs_slowlog_trend import SCSSlowlogTrend


class GetPegadbSlowLogTrendResponse(BceResponse):
    """
    GetPegadbSlowLogTrendResponse
    """

    def __init__(self, data=None):
        """
        Initialize GetPegadbSlowLogTrendResponse instance.

        :param data: 慢日志趋势数据
        :type data: List[SCSSlowlogTrend] (optional)
        """
        super().__init__()
        self.data = data

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
        if self.data is not None:
            result['data'] = [i.to_dict() for i in self.data]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetPegadbSlowLogTrendResponse

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('data') is not None:
            self.data = [SCSSlowlogTrend().from_dict(i) for i in m.get('data')]
        return self
