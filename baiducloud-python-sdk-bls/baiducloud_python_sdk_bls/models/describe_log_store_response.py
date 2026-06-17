"""
Request entity for DescribeLogStoreResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bls.models.index import Index


class DescribeLogStoreResponse(BceResponse):
    """
    DescribeLogStoreResponse
    """

    def __init__(
        self,
        success=None,
        code=None,
        creation_date_time=None,
        last_modified_time=None,
        project=None,
        log_store_name=None,
        retention=None,
        short_id=None,
        shard_count=None,
        max_shard_count=None,
        disable_shard_auto_split=None,
        index_enabled=None,
        hot_retention=None,
        index=None,
    ):
        """
        Initialize DescribeLogStoreResponse response.

        :param success: 请求是否成功
        :type success: bool (optional)

        :param code: 请求码，成功为OK，错误为具体的错误码
        :type code: str (optional)

        :param creation_date_time: 日志集创建的日期时间
        :type creation_date_time: datetime (optional)

        :param last_modified_time: 最后修改的日期时间
        :type last_modified_time: datetime (optional)

        :param project: 日志组名称
        :type project: str (optional)

        :param log_store_name: 日志集名称
        :type log_store_name: str (optional)

        :param retention: 存储时长
        :type retention: int (optional)

        :param short_id: 日志短id
        :type short_id: str (optional)

        :param shard_count: 分片数量
        :type shard_count: int (optional)

        :param max_shard_count: 最大分片数量
        :type max_shard_count: int (optional)

        :param disable_shard_auto_split: 是否禁止自动分裂
        :type disable_shard_auto_split: bool (optional)

        :param index_enabled: 是否开启索引
        :type index_enabled: bool (optional)

        :param hot_retention: 热存时长
        :type hot_retention: int (optional)

        :param index: index field
        :type index: Index (optional)
        """
        super().__init__()
        self.success = success
        self.code = code
        self.creation_date_time = creation_date_time
        self.last_modified_time = last_modified_time
        self.project = project
        self.log_store_name = log_store_name
        self.retention = retention
        self.short_id = short_id
        self.shard_count = shard_count
        self.max_shard_count = max_shard_count
        self.disable_shard_auto_split = disable_shard_auto_split
        self.index_enabled = index_enabled
        self.hot_retention = hot_retention
        self.index = index

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
        if self.success is not None:
            result['success'] = self.success
        if self.code is not None:
            result['code'] = self.code
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.project is not None:
            result['project'] = self.project
        if self.log_store_name is not None:
            result['logStoreName'] = self.log_store_name
        if self.retention is not None:
            result['retention'] = self.retention
        if self.short_id is not None:
            result['shortID'] = self.short_id
        if self.shard_count is not None:
            result['shardCount'] = self.shard_count
        if self.max_shard_count is not None:
            result['maxShardCount'] = self.max_shard_count
        if self.disable_shard_auto_split is not None:
            result['disableShardAutoSplit'] = self.disable_shard_auto_split
        if self.index_enabled is not None:
            result['indexEnabled'] = self.index_enabled
        if self.hot_retention is not None:
            result['hotRetention'] = self.hot_retention
        if self.index is not None:
            result['index'] = self.index.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeLogStoreResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('logStoreName') is not None:
            self.log_store_name = m.get('logStoreName')
        if m.get('retention') is not None:
            self.retention = m.get('retention')
        if m.get('shortID') is not None:
            self.short_id = m.get('shortID')
        if m.get('shardCount') is not None:
            self.shard_count = m.get('shardCount')
        if m.get('maxShardCount') is not None:
            self.max_shard_count = m.get('maxShardCount')
        if m.get('disableShardAutoSplit') is not None:
            self.disable_shard_auto_split = m.get('disableShardAutoSplit')
        if m.get('indexEnabled') is not None:
            self.index_enabled = m.get('indexEnabled')
        if m.get('hotRetention') is not None:
            self.hot_retention = m.get('hotRetention')
        if m.get('index') is not None:
            self.index = Index().from_dict(m.get('index'))
        return self
