"""
Request entity for QueryLogRecordRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class QueryLogRecordRequest(AbstractModel):
    """
    Request entity for QueryLogRecordRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        log_store_name,
        query,
        start_date_time,
        end_date_time,
        project=None,
        log_stream_name=None,
        marker=None,
        limit=None,
        sort=None,
        page_no=None,
        page_size=None,
    ):
        """
        Initialize QueryLogRecordRequest request entity.

        :param log_store_name: log_store_name parameter
        :type log_store_name: str (required)

        :param project: project parameter
        :type project: str (optional)

        :param log_stream_name: log_stream_name parameter
        :type log_stream_name: str (optional)

        :param query: query parameter
        :type query: str (required)

        :param start_date_time: start_date_time parameter
        :type start_date_time: datetime (required)

        :param end_date_time: end_date_time parameter
        :type end_date_time: datetime (required)

        :param marker: marker parameter
        :type marker: str (optional)

        :param limit: limit parameter
        :type limit: int (optional)

        :param sort: sort parameter
        :type sort: str (optional)

        :param page_no: page_no parameter
        :type page_no: int (optional)

        :param page_size: page_size parameter
        :type page_size: int (optional)
        """
        super().__init__()
        self.log_store_name = log_store_name
        self.project = project
        self.log_stream_name = log_stream_name
        self.query = query
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.marker = marker
        self.limit = limit
        self.sort = sort
        self.page_no = page_no
        self.page_size = page_size

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
        :rtype: QueryLogRecordRequest

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
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('startDateTime') is not None:
            self.start_date_time = m.get('startDateTime')
        if m.get('endDateTime') is not None:
            self.end_date_time = m.get('endDateTime')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('sort') is not None:
            self.sort = m.get('sort')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
