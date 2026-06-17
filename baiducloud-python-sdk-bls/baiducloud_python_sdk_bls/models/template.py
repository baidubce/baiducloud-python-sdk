"""
Template information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bls.models.index import Index


class Template(AbstractModel):
    """
    Template
    """

    def __init__(
        self,
        retention=None,
        shard_count=None,
        disable_shard_auto_split=None,
        max_shard_count=None,
        enable_hot_retention=None,
        hot_retention=None,
        index=None,
        name=None,
        project_patterns=None,
        logstore_patterns=None,
        priority=None,
        created_timestamp=None,
        updated_timestamp=None,
    ):
        """
        Initialize Template instance.

        :param retention: 保存时长，单位：天
        :type retention: int (optional)

        :param shard_count: 初始shard个数
        :type shard_count: int (optional)

        :param disable_shard_auto_split: 是否关闭shard自动分裂
        :type disable_shard_auto_split: bool (optional)

        :param max_shard_count: 最大分裂数量，取值范围:[1, 50]
        :type max_shard_count: int (optional)

        :param enable_hot_retention: 是否开启冷热自动分层
        :type enable_hot_retention: bool (optional)

        :param hot_retention: 热存时长，单位：天
        :type hot_retention: int (optional)

        :param index: index attribute
        :type index: Index (optional)

        :param name: 模板名称，同user下唯一
        :type name: str (optional)

        :param project_patterns: 日志组匹配模式，支持*通配符
        :type project_patterns: List[str] (optional)

        :param logstore_patterns: 日志集匹配模式，支持*通配符
        :type logstore_patterns: List[str] (optional)

        :param priority: 日志集模板优先级，值越大，优先级越高，同user下唯一
        :type priority: int (optional)

        :param created_timestamp: 创建时间，UTC时间，格式：2025-04-20T10:01:12Z
        :type created_timestamp: str (optional)

        :param updated_timestamp: 更新时间，UTC时间，格式：2025-04-20T10:01:12Z
        :type updated_timestamp: str (optional)
        """
        super().__init__()
        self.retention = retention
        self.shard_count = shard_count
        self.disable_shard_auto_split = disable_shard_auto_split
        self.max_shard_count = max_shard_count
        self.enable_hot_retention = enable_hot_retention
        self.hot_retention = hot_retention
        self.index = index
        self.name = name
        self.project_patterns = project_patterns
        self.logstore_patterns = logstore_patterns
        self.priority = priority
        self.created_timestamp = created_timestamp
        self.updated_timestamp = updated_timestamp

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
        if self.retention is not None:
            result['retention'] = self.retention
        if self.shard_count is not None:
            result['shardCount'] = self.shard_count
        if self.disable_shard_auto_split is not None:
            result['disableShardAutoSplit'] = self.disable_shard_auto_split
        if self.max_shard_count is not None:
            result['maxShardCount'] = self.max_shard_count
        if self.enable_hot_retention is not None:
            result['enableHotRetention'] = self.enable_hot_retention
        if self.hot_retention is not None:
            result['hotRetention'] = self.hot_retention
        if self.index is not None:
            result['index'] = self.index.to_dict()
        if self.name is not None:
            result['name'] = self.name
        if self.project_patterns is not None:
            result['projectPatterns'] = self.project_patterns
        if self.logstore_patterns is not None:
            result['logstorePatterns'] = self.logstore_patterns
        if self.priority is not None:
            result['priority'] = self.priority
        if self.created_timestamp is not None:
            result['createdTimestamp'] = self.created_timestamp
        if self.updated_timestamp is not None:
            result['updatedTimestamp'] = self.updated_timestamp
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Template

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('retention') is not None:
            self.retention = m.get('retention')
        if m.get('shardCount') is not None:
            self.shard_count = m.get('shardCount')
        if m.get('disableShardAutoSplit') is not None:
            self.disable_shard_auto_split = m.get('disableShardAutoSplit')
        if m.get('maxShardCount') is not None:
            self.max_shard_count = m.get('maxShardCount')
        if m.get('enableHotRetention') is not None:
            self.enable_hot_retention = m.get('enableHotRetention')
        if m.get('hotRetention') is not None:
            self.hot_retention = m.get('hotRetention')
        if m.get('index') is not None:
            self.index = Index().from_dict(m.get('index'))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('projectPatterns') is not None:
            self.project_patterns = m.get('projectPatterns')
        if m.get('logstorePatterns') is not None:
            self.logstore_patterns = m.get('logstorePatterns')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('createdTimestamp') is not None:
            self.created_timestamp = m.get('createdTimestamp')
        if m.get('updatedTimestamp') is not None:
            self.updated_timestamp = m.get('updatedTimestamp')
        return self
