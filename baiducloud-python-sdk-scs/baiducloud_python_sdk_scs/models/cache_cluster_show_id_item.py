"""
CacheClusterShowIdItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CacheClusterShowIdItem(AbstractModel):
    """
    CacheClusterShowIdItem
    """

    def __init__(self, region=None, cache_cluster_show_id=None):
        """
        Initialize CacheClusterShowIdItem instance.

        :param region: 实例所在地域
        :type region: str (optional)

        :param cache_cluster_show_id: 实例ID
        :type cache_cluster_show_id: str (optional)
        """
        super().__init__()
        self.region = region
        self.cache_cluster_show_id = cache_cluster_show_id

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
        if self.region is not None:
            result['region'] = self.region
        if self.cache_cluster_show_id is not None:
            result['cacheClusterShowId'] = self.cache_cluster_show_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CacheClusterShowIdItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('cacheClusterShowId') is not None:
            self.cache_cluster_show_id = m.get('cacheClusterShowId')
        return self
