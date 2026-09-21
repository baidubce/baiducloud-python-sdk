"""
Request entity for GetMongodbDatabaseSpaceTrendResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_dbsc.models.trend_result_base import TrendResultBase


class GetMongodbDatabaseSpaceTrendResponse(BceResponse):
    """
    GetMongodbDatabaseSpaceTrendResponse
    """

    def __init__(self, result=None):
        """
        Initialize GetMongodbDatabaseSpaceTrendResponse response.

        :param result: result field
        :type result: TrendResultBase (optional)
        """
        super().__init__()
        self.result = result

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
        if self.result is not None:
            result['result'] = self.result.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetMongodbDatabaseSpaceTrendResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('result') is not None:
            self.result = TrendResultBase().from_dict(m.get('result'))
        return self
