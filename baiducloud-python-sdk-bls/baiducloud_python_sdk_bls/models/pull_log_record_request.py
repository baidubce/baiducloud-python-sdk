"""
Request entity for PullLogRecordRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class PullLogRecordRequest(AbstractModel):
    """
    Request entity for PullLogRecordRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, log_store_name, log_stream_name, start_date_time, end_date_time, project=None, limit=None, marker=None
    ):
        """
        Initialize PullLogRecordRequest request entity.

        :param log_store_name: log_store_name parameter
        :type log_store_name: str (required)

        :param project: project parameter
        :type project: str (optional)

        :param log_stream_name: log_stream_name parameter
        :type log_stream_name: str (required)

        :param start_date_time: start_date_time parameter
        :type start_date_time: datetime (required)

        :param end_date_time: end_date_time parameter
        :type end_date_time: datetime (required)

        :param limit: limit parameter
        :type limit: int (optional)

        :param marker: marker parameter
        :type marker: str (optional)
        """
        super().__init__()
        self.log_store_name = log_store_name
        self.project = project
        self.log_stream_name = log_stream_name
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.limit = limit
        self.marker = marker

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
        :rtype: PullLogRecordRequest

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
        if m.get('startDateTime') is not None:
            self.start_date_time = m.get('startDateTime')
        if m.get('endDateTime') is not None:
            self.end_date_time = m.get('endDateTime')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self
