"""
Request entity for SelfieAnimeRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SelfieAnimeRequest(AbstractModel):
    """
    Request entity for SelfieAnimeRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, image=None, url=None, type=None, mask_id=None):
        """
        Initialize SelfieAnimeRequest request entity.

        :param image: image parameter
        :type image: str (optional)

        :param url: url parameter
        :type url: str (optional)

        :param type: anime或者anime_mask。前者生成二次元动漫图，后者生成戴口罩的二次元动漫人像
        :type type: str (optional)

        :param mask_id: mask_id parameter
        :type mask_id: str (optional)
        """
        super().__init__()
        self.image = image
        self.url = url
        self.type = type
        self.mask_id = mask_id

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
        if self.image is not None:
            result['image'] = self.image
        if self.url is not None:
            result['url'] = self.url
        if self.type is not None:
            result['type'] = self.type
        if self.mask_id is not None:
            result['mask_id'] = self.mask_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SelfieAnimeRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('mask_id') is not None:
            self.mask_id = m.get('mask_id')
        return self
