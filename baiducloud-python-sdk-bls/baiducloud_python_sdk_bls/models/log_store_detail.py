"""
LogStoreDetail information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bls.models.tag import Tag


class LogStoreDetail(AbstractModel):
    """
    LogStoreDetail
    """

    def __init__(
        self,
        creation_date_time=None,
        disable_shard_auto_split=None,
        enable_archive_retention=None,
        enable_hot_retention=None,
        hot_retention=None,
        index_enabled=None,
        last_modified_time=None,
        log_store_name=None,
        low_frequency_retention=None,
        max_shard_count=None,
        project=None,
        resource_id=None,
        retention=None,
        shard_count=None,
        short_id=None,
        tags=None,
    ):
        """
        Initialize LogStoreDetail instance.

        :param creation_date_time: 创建时间
        :type creation_date_time: str (optional)

        :param disable_shard_auto_split: 是否关闭自动分裂
        :type disable_shard_auto_split: bool (optional)

        :param enable_archive_retention: 是否开启归档存储
        :type enable_archive_retention: bool (optional)

        :param enable_hot_retention: 是否开启热存
        :type enable_hot_retention: bool (optional)

        :param hot_retention: 热存时长，单位天
        :type hot_retention: int (optional)

        :param index_enabled: 是否开启索引
        :type index_enabled: bool (optional)

        :param last_modified_time: 更新时间
        :type last_modified_time: str (optional)

        :param log_store_name: 日志集名称
        :type log_store_name: str (optional)

        :param low_frequency_retention: 低频存储时长，单位天
        :type low_frequency_retention: int (optional)

        :param max_shard_count: 最大分片数量
        :type max_shard_count: int (optional)

        :param project: 日志项目
        :type project: str (optional)

        :param resource_id: 资源id
        :type resource_id: str (optional)

        :param retention: 存储时长，单位天
        :type retention: int (optional)

        :param shard_count: 分片数量
        :type shard_count: int (optional)

        :param short_id: 日志集短id
        :type short_id: str (optional)

        :param tags: 日志集标签
        :type tags: List[Tag] (optional)
        """
        super().__init__()
        self.creation_date_time = creation_date_time
        self.disable_shard_auto_split = disable_shard_auto_split
        self.enable_archive_retention = enable_archive_retention
        self.enable_hot_retention = enable_hot_retention
        self.hot_retention = hot_retention
        self.index_enabled = index_enabled
        self.last_modified_time = last_modified_time
        self.log_store_name = log_store_name
        self.low_frequency_retention = low_frequency_retention
        self.max_shard_count = max_shard_count
        self.project = project
        self.resource_id = resource_id
        self.retention = retention
        self.shard_count = shard_count
        self.short_id = short_id
        self.tags = tags

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
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.disable_shard_auto_split is not None:
            result['disableShardAutoSplit'] = self.disable_shard_auto_split
        if self.enable_archive_retention is not None:
            result['enableArchiveRetention'] = self.enable_archive_retention
        if self.enable_hot_retention is not None:
            result['enableHotRetention'] = self.enable_hot_retention
        if self.hot_retention is not None:
            result['hotRetention'] = self.hot_retention
        if self.index_enabled is not None:
            result['indexEnabled'] = self.index_enabled
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.log_store_name is not None:
            result['logStoreName'] = self.log_store_name
        if self.low_frequency_retention is not None:
            result['lowFrequencyRetention'] = self.low_frequency_retention
        if self.max_shard_count is not None:
            result['maxShardCount'] = self.max_shard_count
        if self.project is not None:
            result['project'] = self.project
        if self.resource_id is not None:
            result['resourceID'] = self.resource_id
        if self.retention is not None:
            result['retention'] = self.retention
        if self.shard_count is not None:
            result['shardCount'] = self.shard_count
        if self.short_id is not None:
            result['shortID'] = self.short_id
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: LogStoreDetail

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('disableShardAutoSplit') is not None:
            self.disable_shard_auto_split = m.get('disableShardAutoSplit')
        if m.get('enableArchiveRetention') is not None:
            self.enable_archive_retention = m.get('enableArchiveRetention')
        if m.get('enableHotRetention') is not None:
            self.enable_hot_retention = m.get('enableHotRetention')
        if m.get('hotRetention') is not None:
            self.hot_retention = m.get('hotRetention')
        if m.get('indexEnabled') is not None:
            self.index_enabled = m.get('indexEnabled')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('logStoreName') is not None:
            self.log_store_name = m.get('logStoreName')
        if m.get('lowFrequencyRetention') is not None:
            self.low_frequency_retention = m.get('lowFrequencyRetention')
        if m.get('maxShardCount') is not None:
            self.max_shard_count = m.get('maxShardCount')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('resourceID') is not None:
            self.resource_id = m.get('resourceID')
        if m.get('retention') is not None:
            self.retention = m.get('retention')
        if m.get('shardCount') is not None:
            self.shard_count = m.get('shardCount')
        if m.get('shortID') is not None:
            self.short_id = m.get('shortID')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        return self
