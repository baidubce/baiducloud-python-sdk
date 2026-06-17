"""
Request entity for DescribeLogStoreViewResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bls.models.log_store import LogStore


class DescribeLogStoreViewResponse(BceResponse):
    """
    DescribeLogStoreViewResponse
    """

    def __init__(self, project=None, name=None, logstores=None, created_timestamp=None, updated_timestamp=None):
        """
        Initialize DescribeLogStoreViewResponse response.

        :param project: 日志组名称
        :type project: str (optional)

        :param name: 日志视图名称
        :type name: str (optional)

        :param logstores: 所关联的日志集列表
        :type logstores: List[LogStore] (optional)

        :param created_timestamp: 日志视图创建的日期时间
        :type created_timestamp: datetime (optional)

        :param updated_timestamp: 最后修改的日期时间
        :type updated_timestamp: datetime (optional)
        """
        super().__init__()
        self.project = project
        self.name = name
        self.logstores = logstores
        self.created_timestamp = created_timestamp
        self.updated_timestamp = updated_timestamp

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
        if self.project is not None:
            result['project'] = self.project
        if self.name is not None:
            result['name'] = self.name
        if self.logstores is not None:
            result['logstores'] = [i.to_dict() for i in self.logstores]
        if self.created_timestamp is not None:
            result['createdTimestamp'] = self.created_timestamp
        if self.updated_timestamp is not None:
            result['updatedTimestamp'] = self.updated_timestamp
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeLogStoreViewResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('logstores') is not None:
            self.logstores = [LogStore().from_dict(i) for i in m.get('logstores')]
        if m.get('createdTimestamp') is not None:
            self.created_timestamp = m.get('createdTimestamp')
        if m.get('updatedTimestamp') is not None:
            self.updated_timestamp = m.get('updatedTimestamp')
        return self
