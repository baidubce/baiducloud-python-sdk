"""
Request entity for ValidateAlarmPolicySQLRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bls.models.log_store import LogStore


class ValidateAlarmPolicySQLRequest(AbstractModel):
    """
    Request entity for ValidateAlarmPolicySQLRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, log_stores, query):
        """
        Initialize ValidateAlarmPolicySQLRequest request entity.

        :param log_stores: 监控对象列表
        :type log_stores: List[LogStore] (required)

        :param query: 执行语句
        :type query: str (required)
        """
        super().__init__()
        self.log_stores = log_stores
        self.query = query

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
        if self.log_stores is not None:
            result['logStores'] = [i.to_dict() for i in self.log_stores]
        if self.query is not None:
            result['query'] = self.query
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ValidateAlarmPolicySQLRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('logStores') is not None:
            self.log_stores = [LogStore().from_dict(i) for i in m.get('logStores')]
        if m.get('query') is not None:
            self.query = m.get('query')
        return self
