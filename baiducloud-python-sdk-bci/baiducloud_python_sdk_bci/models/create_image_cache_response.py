"""
Request entity for CreateImageCacheResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateImageCacheResponse(BceResponse):
    """
    CreateImageCacheResponse
    """

    def __init__(self, image_cache_id=None):
        """
        Initialize CreateImageCacheResponse response.

        :param image_cache_id: 镜像缓存ID
        :type image_cache_id: str (optional)
        """
        super().__init__()
        self.image_cache_id = image_cache_id

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
        if self.image_cache_id is not None:
            result['imageCacheId'] = self.image_cache_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateImageCacheResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('imageCacheId') is not None:
            self.image_cache_id = m.get('imageCacheId')
        return self
