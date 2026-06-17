"""
Shard information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Shard(AbstractModel):
    """
    Shard
    """

    def __init__(self, total=None, successful=None, skipped=None, failed=None):
        """
        Initialize Shard instance.

        :param total: 总共查询的分片数，目前固定为1
        :type total: int (optional)

        :param successful: 成功的分片数
        :type successful: int (optional)

        :param skipped: 跳过的分片数
        :type skipped: int (optional)

        :param failed: 失败的分片数
        :type failed: int (optional)
        """
        super().__init__()
        self.total = total
        self.successful = successful
        self.skipped = skipped
        self.failed = failed

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
        if self.total is not None:
            result['total'] = self.total
        if self.successful is not None:
            result['successful'] = self.successful
        if self.skipped is not None:
            result['skipped'] = self.skipped
        if self.failed is not None:
            result['failed'] = self.failed
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Shard

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('successful') is not None:
            self.successful = m.get('successful')
        if m.get('skipped') is not None:
            self.skipped = m.get('skipped')
        if m.get('failed') is not None:
            self.failed = m.get('failed')
        return self
