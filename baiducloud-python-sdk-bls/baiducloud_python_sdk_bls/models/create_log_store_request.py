"""
Request entity for CreateLogStoreRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bls.models.tag import Tag
from baiducloud_python_sdk_bls.models.index import Index


class CreateLogStoreRequest(AbstractModel):
    """
    Request entity for CreateLogStoreRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        log_store_name,
        retention,
        project=None,
        tags=None,
        index=None,
        shard_count=None,
        max_shard_count=None,
        disable_shard_auto_split=None,
        index_enabled=None,
        hot_retention=None,
        enable_hot_retention=None,
    ):
        """
        Initialize CreateLogStoreRequest request entity.

        :param project: 日志组名称，默认default
        :type project: str (optional)

        :param log_store_name: 日志集名称
        :type log_store_name: str (required)

        :param retention: 日志集的租期，最大3650天，表示永久保存。单位：天数
        :type retention: int (required)

        :param tags: 待创建的标签列表，具体参数格式参见下述
        :type tags: List[Tag] (optional)

        :param index: index parameter
        :type index: Index (optional)

        :param shard_count: 日志集初始shard数量，默认为1，最大值为50
        :type shard_count: int (optional)

        :param max_shard_count: 最大分片数量
        :type max_shard_count: int (optional)

        :param disable_shard_auto_split: 是否禁止自动分裂
        :type disable_shard_auto_split: bool (optional)

        :param index_enabled: 是否开启索引
        :type index_enabled: bool (optional)

        :param hot_retention: 热存时长
        :type hot_retention: int (optional)

        :param enable_hot_retention: 是否开启热存
        :type enable_hot_retention: bool (optional)
        """
        super().__init__()
        self.project = project
        self.log_store_name = log_store_name
        self.retention = retention
        self.tags = tags
        self.index = index
        self.shard_count = shard_count
        self.max_shard_count = max_shard_count
        self.disable_shard_auto_split = disable_shard_auto_split
        self.index_enabled = index_enabled
        self.hot_retention = hot_retention
        self.enable_hot_retention = enable_hot_retention

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
        if self.project is not None:
            result['project'] = self.project
        if self.log_store_name is not None:
            result['logStoreName'] = self.log_store_name
        if self.retention is not None:
            result['retention'] = self.retention
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.index is not None:
            result['index'] = self.index.to_dict()
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
        if self.enable_hot_retention is not None:
            result['EnableHotRetention'] = self.enable_hot_retention
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateLogStoreRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('logStoreName') is not None:
            self.log_store_name = m.get('logStoreName')
        if m.get('retention') is not None:
            self.retention = m.get('retention')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        if m.get('index') is not None:
            self.index = Index().from_dict(m.get('index'))
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
        if m.get('EnableHotRetention') is not None:
            self.enable_hot_retention = m.get('EnableHotRetention')
        return self
