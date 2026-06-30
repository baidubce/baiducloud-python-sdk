"""
Request entity for BatchDeleteImageCachesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BatchDeleteImageCachesRequest(AbstractModel):
    """
    Request entity for BatchDeleteImageCachesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, image_cache_ids):
        """
        Initialize BatchDeleteImageCachesRequest request entity.

        :param image_cache_ids: 需要被删除的镜像缓存ID列表
        :type image_cache_ids: List[str] (required)
        """
        super().__init__()
        self.image_cache_ids = image_cache_ids

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
        if self.image_cache_ids is not None:
            result['imageCacheIds'] = self.image_cache_ids
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BatchDeleteImageCachesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('imageCacheIds') is not None:
            self.image_cache_ids = m.get('imageCacheIds')
        return self
