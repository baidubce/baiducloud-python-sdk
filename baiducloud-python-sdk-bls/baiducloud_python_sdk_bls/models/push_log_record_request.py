"""
Request entity for PushLogRecordRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bls.models.log_record import LogRecord
from baiducloud_python_sdk_bls.models.log_tag import LogTag


class PushLogRecordRequest(AbstractModel):
    """
    Request entity for PushLogRecordRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, log_store_name, log_records, project=None, log_stream_name=None, type=None, tags=None):
        """
        Initialize PushLogRecordRequest request entity.

        :param log_store_name: log_store_name parameter
        :type log_store_name: str (required)

        :param project: project parameter
        :type project: str (optional)

        :param log_stream_name: log_stream_name parameter
        :type log_stream_name: str (optional)

        :param type: 数据类型，JSON/TEXT，默认为 TEXT
        :type type: str (optional)

        :param log_records: 日志记录
        :type log_records: List[LogRecord] (required)

        :param tags: 日志标签
        :type tags: List[LogTag] (optional)
        """
        super().__init__()
        self.log_store_name = log_store_name
        self.project = project
        self.log_stream_name = log_stream_name
        self.type = type
        self.log_records = log_records
        self.tags = tags

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
        if self.log_stream_name is not None:
            result['logStreamName'] = self.log_stream_name
        if self.type is not None:
            result['type'] = self.type
        if self.log_records is not None:
            result['logRecords'] = [i.to_dict() for i in self.log_records]
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PushLogRecordRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('logStoreName') is not None:
            self.log_store_name = m.get('logStoreName')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('logStreamName') is not None:
            self.log_stream_name = m.get('logStreamName')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('logRecords') is not None:
            self.log_records = [LogRecord().from_dict(i) for i in m.get('logRecords')]
        if m.get('tags') is not None:
            self.tags = [LogTag().from_dict(i) for i in m.get('tags')]
        return self
