"""
Request entity for UpdateFastQueryRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateFastQueryRequest(AbstractModel):
    """
    Request entity for UpdateFastQueryRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, name, fast_query_name, query, log_store_name, description=None, project=None, log_stream_name=None
    ):
        """
        Initialize UpdateFastQueryRequest request entity.

        :param name: name parameter
        :type name: str (required)

        :param fast_query_name: 快速查询名称
        :type fast_query_name: str (required)

        :param query: 快速查询语句
        :type query: str (required)

        :param description: 信息描述
        :type description: str (optional)

        :param project: 日志组名称，默认default
        :type project: str (optional)

        :param log_store_name: 日志集名称
        :type log_store_name: str (required)

        :param log_stream_name: 日志流名称
        :type log_stream_name: str (optional)
        """
        super().__init__()
        self.name = name
        self.fast_query_name = fast_query_name
        self.query = query
        self.description = description
        self.project = project
        self.log_store_name = log_store_name
        self.log_stream_name = log_stream_name

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
        if self.fast_query_name is not None:
            result['fastQueryName'] = self.fast_query_name
        if self.query is not None:
            result['query'] = self.query
        if self.description is not None:
            result['description'] = self.description
        if self.project is not None:
            result['project'] = self.project
        if self.log_store_name is not None:
            result['logStoreName'] = self.log_store_name
        if self.log_stream_name is not None:
            result['logStreamName'] = self.log_stream_name
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateFastQueryRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('fastQueryName') is not None:
            self.fast_query_name = m.get('fastQueryName')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('logStoreName') is not None:
            self.log_store_name = m.get('logStoreName')
        if m.get('logStreamName') is not None:
            self.log_stream_name = m.get('logStreamName')
        return self
