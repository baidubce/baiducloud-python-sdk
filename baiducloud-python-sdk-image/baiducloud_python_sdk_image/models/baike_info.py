"""
BaikeInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BaikeInfo(AbstractModel):
    """
    BaikeInfo
    """

    def __init__(self, baike_url=None, image_url=None, description=None):
        """
        Initialize BaikeInfo instance.

        :param baike_url: 百科页面链接
        :type baike_url: str (optional)

        :param image_url: 百科图片链接
        :type image_url: str (optional)

        :param description: 百科内容描述
        :type description: str (optional)
        """
        super().__init__()
        self.baike_url = baike_url
        self.image_url = image_url
        self.description = description

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
        if self.baike_url is not None:
            result['baike_url'] = self.baike_url
        if self.image_url is not None:
            result['image_url'] = self.image_url
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BaikeInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('baike_url') is not None:
            self.baike_url = m.get('baike_url')
        if m.get('image_url') is not None:
            self.image_url = m.get('image_url')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
