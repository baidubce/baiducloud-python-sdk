"""
Request entity for AnimalRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AnimalRequest(AbstractModel):
    """
    Request entity for AnimalRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, image=None, url=None, top_num=None, baike_num=None):
        """
        Initialize AnimalRequest request entity.

        :param image: image parameter
        :type image: str (optional)

        :param url: url parameter
        :type url: str (optional)

        :param top_num: 返回预测得分top结果数，默认为6
        :type top_num: int (optional)

        :param baike_num: baike_num parameter
        :type baike_num: int (optional)
        """
        super().__init__()
        self.image = image
        self.url = url
        self.top_num = top_num
        self.baike_num = baike_num

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
        if self.top_num is not None:
            result['top_num'] = self.top_num
        if self.baike_num is not None:
            result['baike_num'] = self.baike_num
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AnimalRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('top_num') is not None:
            self.top_num = m.get('top_num')
        if m.get('baike_num') is not None:
            self.baike_num = m.get('baike_num')
        return self
