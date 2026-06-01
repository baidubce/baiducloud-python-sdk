"""
Request entity for DescribeTopologyRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescribeTopologyRequest(AbstractModel):
    """
    Request entity for DescribeTopologyRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, action, begin_datetime, end_datetime, service_name=None, env=None):
        """
        Initialize DescribeTopologyRequest request entity.

        :param action: action parameter
        :type action: str (required)

        :param service_name: 应用名。若未设置，表示查询全局拓扑；若设置，表示查询服务上下游拓扑。支持模糊搜索，例如\".*mall.*\"
        :type service_name: str (optional)

        :param env: 按env过滤，若未设置，返回所有环境的拓扑图
        :type env: str (optional)

        :param begin_datetime: 开始时间，UTC时间
        :type begin_datetime: str (required)

        :param end_datetime: 结束时间，UTC时间
        :type end_datetime: str (required)
        """
        super().__init__()
        self.action = action
        self.service_name = service_name
        self.env = env
        self.begin_datetime = begin_datetime
        self.end_datetime = end_datetime

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
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.env is not None:
            result['env'] = self.env
        if self.begin_datetime is not None:
            result['beginDatetime'] = self.begin_datetime
        if self.end_datetime is not None:
            result['endDatetime'] = self.end_datetime
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeTopologyRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('env') is not None:
            self.env = m.get('env')
        if m.get('beginDatetime') is not None:
            self.begin_datetime = m.get('beginDatetime')
        if m.get('endDatetime') is not None:
            self.end_datetime = m.get('endDatetime')
        return self
