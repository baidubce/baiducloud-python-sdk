"""
ShardLog information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_scs.models.log_item import LogItem


class ShardLog(AbstractModel):
    """
    ShardLog
    """

    def __init__(self, shard_show_id=None, total_num=None, log_item=None, shard_id=None):
        """
        Initialize ShardLog instance.

        :param shard_show_id: 分片ID
        :type shard_show_id: str (optional)

        :param total_num: 总数
        :type total_num: int (optional)

        :param log_item: 分片日志列表
        :type log_item: List[LogItem] (optional)

        :param shard_id: 分片数字ID
        :type shard_id: int (optional)
        """
        super().__init__()
        self.shard_show_id = shard_show_id
        self.total_num = total_num
        self.log_item = log_item
        self.shard_id = shard_id

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
        if self.shard_show_id is not None:
            result['shardShowId'] = self.shard_show_id
        if self.total_num is not None:
            result['totalNum'] = self.total_num
        if self.log_item is not None:
            result['logItem'] = [i.to_dict() for i in self.log_item]
        if self.shard_id is not None:
            result['shardId'] = self.shard_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ShardLog

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('shardShowId') is not None:
            self.shard_show_id = m.get('shardShowId')
        if m.get('totalNum') is not None:
            self.total_num = m.get('totalNum')
        if m.get('logItem') is not None:
            self.log_item = [LogItem().from_dict(i) for i in m.get('logItem')]
        if m.get('shardId') is not None:
            self.shard_id = m.get('shardId')
        return self
