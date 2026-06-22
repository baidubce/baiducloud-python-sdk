"""
Request entity for DescribeFastQueryResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class DescribeFastQueryResponse(BceResponse):
    """
    DescribeFastQueryResponse
    """

    def __init__(
        self,
        creation_date_time=None,
        last_modified_time=None,
        fast_query_name=None,
        description=None,
        query=None,
        project=None,
        log_store_name=None,
        log_stream_name=None,
        log_store_type=None,
    ):
        """
        Initialize DescribeFastQueryResponse response.

        :param creation_date_time: 日志集创建的日期时间
        :type creation_date_time: datetime (optional)

        :param last_modified_time: 最后修改的日期时间
        :type last_modified_time: datetime (optional)

        :param fast_query_name: 快速查询名称
        :type fast_query_name: str (optional)

        :param description: 描述信息
        :type description: str (optional)

        :param query: 快速查找语句
        :type query: str (optional)

        :param project: 日志组名称
        :type project: str (optional)

        :param log_store_name: 日志集名称
        :type log_store_name: str (optional)

        :param log_stream_name: 日志流名称
        :type log_stream_name: str (optional)

        :param log_store_type: 日志集类型，LOGSTORE或者LOGSTORE_VIEW
        :type log_store_type: str (optional)
        """
        super().__init__()
        self.creation_date_time = creation_date_time
        self.last_modified_time = last_modified_time
        self.fast_query_name = fast_query_name
        self.description = description
        self.query = query
        self.project = project
        self.log_store_name = log_store_name
        self.log_stream_name = log_stream_name
        self.log_store_type = log_store_type

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.fast_query_name is not None:
            result['fastQueryName'] = self.fast_query_name
        if self.description is not None:
            result['description'] = self.description
        if self.query is not None:
            result['query'] = self.query
        if self.project is not None:
            result['project'] = self.project
        if self.log_store_name is not None:
            result['logStoreName'] = self.log_store_name
        if self.log_stream_name is not None:
            result['logStreamName'] = self.log_stream_name
        if self.log_store_type is not None:
            result['logStoreType'] = self.log_store_type
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeFastQueryResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('fastQueryName') is not None:
            self.fast_query_name = m.get('fastQueryName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('logStoreName') is not None:
            self.log_store_name = m.get('logStoreName')
        if m.get('logStreamName') is not None:
            self.log_stream_name = m.get('logStreamName')
        if m.get('logStoreType') is not None:
            self.log_store_type = m.get('logStoreType')
        return self
