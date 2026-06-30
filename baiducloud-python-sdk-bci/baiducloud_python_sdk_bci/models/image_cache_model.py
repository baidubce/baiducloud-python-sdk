"""
ImageCacheModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ImageCacheModel(AbstractModel):
    """
    ImageCacheModel
    """

    def __init__(
        self,
        image_cache_id=None,
        origin_images=None,
        status=None,
        progress=None,
        expired_time=None,
        created_time=None,
        lastest_matched_time=None,
    ):
        """
        Initialize ImageCacheModel instance.

        :param image_cache_id: 镜像缓存id，全局唯一
        :type image_cache_id: str (optional)

        :param origin_images: 用户原始镜像地址
        :type origin_images: List[str] (optional)

        :param status: 制作状态：创建成功、创建失败、创建中
        :type status: str (optional)

        :param progress: 制作进度，范围[0,100]
        :type progress: int (optional)

        :param expired_time: 超时回收时间
        :type expired_time: str (optional)

        :param created_time: 创建时间
        :type created_time: str (optional)

        :param lastest_matched_time: 最近一次使用时间
        :type lastest_matched_time: str (optional)
        """
        super().__init__()
        self.image_cache_id = image_cache_id
        self.origin_images = origin_images
        self.status = status
        self.progress = progress
        self.expired_time = expired_time
        self.created_time = created_time
        self.lastest_matched_time = lastest_matched_time

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
        if self.image_cache_id is not None:
            result['imageCacheId'] = self.image_cache_id
        if self.origin_images is not None:
            result['originImages'] = self.origin_images
        if self.status is not None:
            result['status'] = self.status
        if self.progress is not None:
            result['progress'] = self.progress
        if self.expired_time is not None:
            result['expiredTime'] = self.expired_time
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.lastest_matched_time is not None:
            result['lastestMatchedTime'] = self.lastest_matched_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ImageCacheModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('imageCacheId') is not None:
            self.image_cache_id = m.get('imageCacheId')
        if m.get('originImages') is not None:
            self.origin_images = m.get('originImages')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        if m.get('expiredTime') is not None:
            self.expired_time = m.get('expiredTime')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('lastestMatchedTime') is not None:
            self.lastest_matched_time = m.get('lastestMatchedTime')
        return self
