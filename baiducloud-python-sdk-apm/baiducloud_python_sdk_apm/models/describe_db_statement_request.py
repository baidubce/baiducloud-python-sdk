"""
Request entity for DescribeDbStatementRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_apm.models.statement_query import StatementQuery


class DescribeDbStatementRequest(AbstractModel):
    """
    Request entity for DescribeDbStatementRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, begin_datetime, end_datetime, service, statements):
        """
        Initialize DescribeDbStatementRequest request entity.

        :param begin_datetime: 开始时间，UTC时间
        :type begin_datetime: str (required)

        :param end_datetime: 结束时间，UTC时间
        :type end_datetime: str (required)

        :param service: 数据库所属服务名称
        :type service: str (required)

        :param statements: 按数据库语句ID批量查询，每项包含id(语句ID，必填)
        :type statements: List[StatementQuery] (required)
        """
        super().__init__()
        self.begin_datetime = begin_datetime
        self.end_datetime = end_datetime
        self.service = service
        self.statements = statements

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
        if self.begin_datetime is not None:
            result['beginDatetime'] = self.begin_datetime
        if self.end_datetime is not None:
            result['endDatetime'] = self.end_datetime
        if self.service is not None:
            result['service'] = self.service
        if self.statements is not None:
            result['statements'] = [i.to_dict() for i in self.statements]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeDbStatementRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('beginDatetime') is not None:
            self.begin_datetime = m.get('beginDatetime')
        if m.get('endDatetime') is not None:
            self.end_datetime = m.get('endDatetime')
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('statements') is not None:
            self.statements = [StatementQuery().from_dict(i) for i in m.get('statements')]
        return self
