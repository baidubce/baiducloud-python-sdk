"""
OriginImage information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class OriginImage(AbstractModel):
    """
    OriginImage
    """

    def __init__(self, origin_image_address=None, origin_image_version=None):
        """
        Initialize OriginImage instance.

        :param origin_image_address: 原始镜像地址
        :type origin_image_address: str (optional)

        :param origin_image_version: 原始镜像版本
        :type origin_image_version: str (optional)
        """
        super().__init__()
        self.origin_image_address = origin_image_address
        self.origin_image_version = origin_image_version

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
        if self.origin_image_address is not None:
            result['originImageAddress'] = self.origin_image_address
        if self.origin_image_version is not None:
            result['originImageVersion'] = self.origin_image_version
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: OriginImage

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('originImageAddress') is not None:
            self.origin_image_address = m.get('originImageAddress')
        if m.get('originImageVersion') is not None:
            self.origin_image_version = m.get('originImageVersion')
        return self
