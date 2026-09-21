"""
Request entity for GetMongodbSlowQueryTemplateResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_dbsc.models.mongo_db_slow_log_template import MongoDBSlowLogTemplate


class GetMongodbSlowQueryTemplateResponse(BceResponse):
    """
    GetMongodbSlowQueryTemplateResponse
    """

    def __init__(self, items=None, total_count=None):
        """
        Initialize GetMongodbSlowQueryTemplateResponse response.

        :param items: 全量日志列表
        :type items: List[MongoDBSlowLogTemplate] (optional)

        :param total_count: 日志总数
        :type total_count: int (optional)
        """
        super().__init__()
        self.items = items
        self.total_count = total_count

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
        if self.items is not None:
            result['items'] = [i.to_dict() for i in self.items]
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetMongodbSlowQueryTemplateResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('items') is not None:
            self.items = [MongoDBSlowLogTemplate().from_dict(i) for i in m.get('items')]
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self
