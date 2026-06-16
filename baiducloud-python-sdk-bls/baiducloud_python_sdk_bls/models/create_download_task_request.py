"""
Request entity for CreateDownloadTaskRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateDownloadTaskRequest(AbstractModel):
    """
    Request entity for CreateDownloadTaskRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        log_store_name,
        query_start_time,
        query_end_time,
        name=None,
        project=None,
        log_stream_name=None,
        query=None,
        format=None,
        limit=None,
        order=None,
        file_dir=None,
    ):
        """
        Initialize CreateDownloadTaskRequest request entity.

        :param name: 下载任务名称
        :type name: str (optional)

        :param project: 日志组名称，默认default
        :type project: str (optional)

        :param log_store_name: 日志集名称
        :type log_store_name: str (required)

        :param log_stream_name: 日志流名称，默认在全部日志流中下载数据
        :type log_stream_name: str (optional)

        :param query: 检索语句，默认下载全部数据
        :type query: str (optional)

        :param query_start_time: 日志开始时间，UTC时间，格式ISO8601，例如：2020-01-10T13:23:34Z
        :type query_start_time: str (required)

        :param query_end_time: 日志结束时间，UTC时间，格式ISO8601，例如：2020-01-10T13:23:34Z
        :type query_end_time: str (required)

        :param format: 下载文件的格式，默认json，支持 json,csv
        :type format: str (optional)

        :param limit: 下载日志的行数，默认1000000，最大1000000
        :type limit: int (optional)

        :param order: 排序方式，默认desc，按照时间倒序排序，支持desc和asc
        :type order: str (optional)

        :param file_dir: file_dir parameter
        :type file_dir: str (optional)
        """
        super().__init__()
        self.name = name
        self.project = project
        self.log_store_name = log_store_name
        self.log_stream_name = log_stream_name
        self.query = query
        self.query_start_time = query_start_time
        self.query_end_time = query_end_time
        self.format = format
        self.limit = limit
        self.order = order
        self.file_dir = file_dir

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
        if self.name is not None:
            result['name'] = self.name
        if self.project is not None:
            result['project'] = self.project
        if self.log_store_name is not None:
            result['logStoreName'] = self.log_store_name
        if self.log_stream_name is not None:
            result['logStreamName'] = self.log_stream_name
        if self.query is not None:
            result['query'] = self.query
        if self.query_start_time is not None:
            result['queryStartTime'] = self.query_start_time
        if self.query_end_time is not None:
            result['queryEndTime'] = self.query_end_time
        if self.format is not None:
            result['format'] = self.format
        if self.limit is not None:
            result['limit'] = self.limit
        if self.order is not None:
            result['order'] = self.order
        if self.file_dir is not None:
            result['fileDir'] = self.file_dir
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateDownloadTaskRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('logStoreName') is not None:
            self.log_store_name = m.get('logStoreName')
        if m.get('logStreamName') is not None:
            self.log_stream_name = m.get('logStreamName')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('queryStartTime') is not None:
            self.query_start_time = m.get('queryStartTime')
        if m.get('queryEndTime') is not None:
            self.query_end_time = m.get('queryEndTime')
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('fileDir') is not None:
            self.file_dir = m.get('fileDir')
        return self
