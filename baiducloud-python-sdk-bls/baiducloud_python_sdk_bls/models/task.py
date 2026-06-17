"""
Task information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Task(AbstractModel):
    """
    Task
    """

    def __init__(
        self,
        uuid=None,
        name=None,
        project=None,
        log_store_name=None,
        query=None,
        query_start_time=None,
        query_end_time=None,
        format=None,
        limit=None,
        order=None,
        state=None,
        failed_code=None,
        failed_message=None,
        written_rows=None,
        file_dir=None,
        file_name=None,
        exec_start_time=None,
        exec_end_time=None,
        created_time=None,
        updated_time=None,
    ):
        """
        Initialize Task instance.

        :param uuid: 下载任务的唯一ID
        :type uuid: str (optional)

        :param name: 下载任务名称
        :type name: str (optional)

        :param project: 日志组名称
        :type project: str (optional)

        :param log_store_name: 日志集名称
        :type log_store_name: str (optional)

        :param query: 查询语句
        :type query: str (optional)

        :param query_start_time: 日志开始时间
        :type query_start_time: str (optional)

        :param query_end_time: 日志结束时间
        :type query_end_time: str (optional)

        :param format: 下载文件的格式
        :type format: str (optional)

        :param limit: 下载日志行数
        :type limit: int (optional)

        :param order: 排序方式
        :type order: str (optional)

        :param state: state attribute
        :type state: str (optional)

        :param failed_code: 下载任务执行失败码
        :type failed_code: datetime (optional)

        :param failed_message: 下载任务执行失败的具体原因
        :type failed_message: datetime (optional)

        :param written_rows: 写入的日志行数
        :type written_rows: int (optional)

        :param file_dir: 下载文件目录
        :type file_dir: str (optional)

        :param file_name: 下载文件名称
        :type file_name: str (optional)

        :param exec_start_time: 开始执行下载任务时间
        :type exec_start_time: str (optional)

        :param exec_end_time: 下载任务执行结束时间
        :type exec_end_time: str (optional)

        :param created_time: 下载任务创建时间
        :type created_time: str (optional)

        :param updated_time: 下载任务更新时间
        :type updated_time: str (optional)
        """
        super().__init__()
        self.uuid = uuid
        self.name = name
        self.project = project
        self.log_store_name = log_store_name
        self.query = query
        self.query_start_time = query_start_time
        self.query_end_time = query_end_time
        self.format = format
        self.limit = limit
        self.order = order
        self.state = state
        self.failed_code = failed_code
        self.failed_message = failed_message
        self.written_rows = written_rows
        self.file_dir = file_dir
        self.file_name = file_name
        self.exec_start_time = exec_start_time
        self.exec_end_time = exec_end_time
        self.created_time = created_time
        self.updated_time = updated_time

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
        if self.uuid is not None:
            result['uuid'] = self.uuid
        if self.name is not None:
            result['name'] = self.name
        if self.project is not None:
            result['project'] = self.project
        if self.log_store_name is not None:
            result['logStoreName'] = self.log_store_name
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
        if self.state is not None:
            result['state'] = self.state
        if self.failed_code is not None:
            result['failedCode'] = self.failed_code
        if self.failed_message is not None:
            result['failedMessage'] = self.failed_message
        if self.written_rows is not None:
            result['writtenRows'] = self.written_rows
        if self.file_dir is not None:
            result['fileDir'] = self.file_dir
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.exec_start_time is not None:
            result['execStartTime'] = self.exec_start_time
        if self.exec_end_time is not None:
            result['execEndTime'] = self.exec_end_time
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.updated_time is not None:
            result['updatedTime'] = self.updated_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Task

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('logStoreName') is not None:
            self.log_store_name = m.get('logStoreName')
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
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('failedCode') is not None:
            self.failed_code = m.get('failedCode')
        if m.get('failedMessage') is not None:
            self.failed_message = m.get('failedMessage')
        if m.get('writtenRows') is not None:
            self.written_rows = m.get('writtenRows')
        if m.get('fileDir') is not None:
            self.file_dir = m.get('fileDir')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('execStartTime') is not None:
            self.exec_start_time = m.get('execStartTime')
        if m.get('execEndTime') is not None:
            self.exec_end_time = m.get('execEndTime')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('updatedTime') is not None:
            self.updated_time = m.get('updatedTime')
        return self
