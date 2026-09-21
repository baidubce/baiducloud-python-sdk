"""
MySQLSessionSummary information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MySQLSessionSummary(AbstractModel):
    """
    MySQLSessionSummary
    """

    def __init__(
        self,
        active_average_execute_time=None,
        active_max_execute_time=None,
        active_total_count=None,
        active_total_execute_time=None,
        average_execute_time=None,
        max_execute_time=None,
        total_count=None,
        total_execute_time=None,
    ):
        """
        Initialize MySQLSessionSummary instance.

        :param active_average_execute_time: 活跃会话平均执行时间
        :type active_average_execute_time: float (optional)

        :param active_max_execute_time: 活跃会话最长执行时间
        :type active_max_execute_time: float (optional)

        :param active_total_count: 活跃会话总数
        :type active_total_count: int (optional)

        :param active_total_execute_time: 活跃会话总执行时间
        :type active_total_execute_time: float (optional)

        :param average_execute_time: 会话平均执行时间
        :type average_execute_time: float (optional)

        :param max_execute_time: 会话最长执行时间
        :type max_execute_time: float (optional)

        :param total_count: 会话总数
        :type total_count: int (optional)

        :param total_execute_time: 会话总执行时间
        :type total_execute_time: float (optional)
        """
        super().__init__()
        self.active_average_execute_time = active_average_execute_time
        self.active_max_execute_time = active_max_execute_time
        self.active_total_count = active_total_count
        self.active_total_execute_time = active_total_execute_time
        self.average_execute_time = average_execute_time
        self.max_execute_time = max_execute_time
        self.total_count = total_count
        self.total_execute_time = total_execute_time

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
        if self.active_average_execute_time is not None:
            result['activeAverageExecuteTime'] = self.active_average_execute_time
        if self.active_max_execute_time is not None:
            result['activeMaxExecuteTime'] = self.active_max_execute_time
        if self.active_total_count is not None:
            result['activeTotalCount'] = self.active_total_count
        if self.active_total_execute_time is not None:
            result['activeTotalExecuteTime'] = self.active_total_execute_time
        if self.average_execute_time is not None:
            result['averageExecuteTime'] = self.average_execute_time
        if self.max_execute_time is not None:
            result['maxExecuteTime'] = self.max_execute_time
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.total_execute_time is not None:
            result['totalExecuteTime'] = self.total_execute_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MySQLSessionSummary

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('activeAverageExecuteTime') is not None:
            self.active_average_execute_time = m.get('activeAverageExecuteTime')
        if m.get('activeMaxExecuteTime') is not None:
            self.active_max_execute_time = m.get('activeMaxExecuteTime')
        if m.get('activeTotalCount') is not None:
            self.active_total_count = m.get('activeTotalCount')
        if m.get('activeTotalExecuteTime') is not None:
            self.active_total_execute_time = m.get('activeTotalExecuteTime')
        if m.get('averageExecuteTime') is not None:
            self.average_execute_time = m.get('averageExecuteTime')
        if m.get('maxExecuteTime') is not None:
            self.max_execute_time = m.get('maxExecuteTime')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('totalExecuteTime') is not None:
            self.total_execute_time = m.get('totalExecuteTime')
        return self
