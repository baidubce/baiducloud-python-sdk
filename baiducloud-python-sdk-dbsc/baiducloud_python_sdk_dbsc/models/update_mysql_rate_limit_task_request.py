"""
Request entity for UpdateMysqlRateLimitTaskRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateMysqlRateLimitTaskRequest(AbstractModel):
    """
    Request entity for UpdateMysqlRateLimitTaskRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, filter_id, app_id, filter_limit, filter_type, node_id=None, filter_key=None):
        """
        Initialize UpdateMysqlRateLimitTaskRequest request entity.

        :param filter_id: 限流规则id
        :type filter_id: int (required)

        :param app_id: 集群ID
        :type app_id: str (required)

        :param node_id: 节点ID
        :type node_id: str (optional)

        :param filter_key: filter_key parameter
        :type filter_key: str (optional)

        :param filter_limit: FilterLimit 限流规则的并发数：取值 0-100w 闭区间
        :type filter_limit: int (required)

        :param filter_type: FilterType SQL限流类型，支持SELECT、UPDATE、INSERT、DELETE、REPLACE
        :type filter_type: str (required)
        """
        super().__init__()
        self.filter_id = filter_id
        self.app_id = app_id
        self.node_id = node_id
        self.filter_key = filter_key
        self.filter_limit = filter_limit
        self.filter_type = filter_type

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.filter_id is not None:
            result['filterId'] = self.filter_id
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.node_id is not None:
            result['nodeId'] = self.node_id
        if self.filter_key is not None:
            result['filterKey'] = self.filter_key
        if self.filter_limit is not None:
            result['filterLimit'] = self.filter_limit
        if self.filter_type is not None:
            result['filterType'] = self.filter_type
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateMysqlRateLimitTaskRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('filterId') is not None:
            self.filter_id = m.get('filterId')
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')
        if m.get('filterKey') is not None:
            self.filter_key = m.get('filterKey')
        if m.get('filterLimit') is not None:
            self.filter_limit = m.get('filterLimit')
        if m.get('filterType') is not None:
            self.filter_type = m.get('filterType')
        return self
