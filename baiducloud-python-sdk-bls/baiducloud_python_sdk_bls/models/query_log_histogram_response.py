"""
Request entity for QueryLogHistogramResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bls.models.search_info import SearchInfo
from baiducloud_python_sdk_bls.models.search_statistic import SearchStatistic


class QueryLogHistogramResponse(BceResponse):
    """
    QueryLogHistogramResponse
    """

    def __init__(self, search_info=None, search_statistic=None):
        """
        Initialize QueryLogHistogramResponse response.

        :param search_info: search_info field
        :type search_info: SearchInfo (optional)

        :param search_statistic: search_statistic field
        :type search_statistic: SearchStatistic (optional)
        """
        super().__init__()
        self.search_info = search_info
        self.search_statistic = search_statistic

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
        if self.search_info is not None:
            result['searchInfo'] = self.search_info.to_dict()
        if self.search_statistic is not None:
            result['searchStatistic'] = self.search_statistic.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QueryLogHistogramResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('searchInfo') is not None:
            self.search_info = SearchInfo().from_dict(m.get('searchInfo'))
        if m.get('searchStatistic') is not None:
            self.search_statistic = SearchStatistic().from_dict(m.get('searchStatistic'))
        return self
