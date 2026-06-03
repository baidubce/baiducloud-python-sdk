"""
CacheNodeQuotaInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CacheNodeQuotaInfo(AbstractModel):
    """
    CacheNodeQuotaInfo
    """

    def __init__(self, used=None, quota=None):
        """
        Initialize CacheNodeQuotaInfo instance.

        :param used: 已添加的 CacheNode 数量
        :type used: int (optional)

        :param quota: CacheNode 节点数配额上限
        :type quota: int (optional)
        """
        super().__init__()
        self.used = used
        self.quota = quota

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
        if self.used is not None:
            result['used'] = self.used
        if self.quota is not None:
            result['quota'] = self.quota
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CacheNodeQuotaInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('used') is not None:
            self.used = m.get('used')
        if m.get('quota') is not None:
            self.quota = m.get('quota')
        return self
