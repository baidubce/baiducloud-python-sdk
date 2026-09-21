"""
Request entity for GetMysqlSlowLogTrendRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetMysqlSlowLogTrendRequest(AbstractModel):
    """
    Request entity for GetMysqlSlowLogTrendRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, app_id, start, end, period, node_id=None):
        """
        Initialize GetMysqlSlowLogTrendRequest request entity.

        :param app_id: app_id parameter
        :type app_id: str (required)

        :param node_id: node_id parameter
        :type node_id: str (optional)

        :param start: start parameter
        :type start: datetime (required)

        :param end: end parameter
        :type end: datetime (required)

        :param period: period parameter
        :type period: str (required)
        """
        super().__init__()
        self.app_id = app_id
        self.node_id = node_id
        self.start = start
        self.end = end
        self.period = period

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetMysqlSlowLogTrendRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')
        if m.get('start') is not None:
            self.start = m.get('start')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('period') is not None:
            self.period = m.get('period')
        return self
