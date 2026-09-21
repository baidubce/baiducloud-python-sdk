"""
Request entity for GetMysqlKillSessionHistoryResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_dbsc.models.session_kill_history import SessionKillHistory


class GetMysqlKillSessionHistoryResponse(BceResponse):
    """
    GetMysqlKillSessionHistoryResponse
    """

    def __init__(self, total_count=None, items=None):
        """
        Initialize GetMysqlKillSessionHistoryResponse response.

        :param total_count: 查杀历史会话总数
        :type total_count: int (optional)

        :param items: 查杀历史会话详情
        :type items: List[SessionKillHistory] (optional)
        """
        super().__init__()
        self.total_count = total_count
        self.items = items

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
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.items is not None:
            result['items'] = [i.to_dict() for i in self.items]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetMysqlKillSessionHistoryResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('items') is not None:
            self.items = [SessionKillHistory().from_dict(i) for i in m.get('items')]
        return self
