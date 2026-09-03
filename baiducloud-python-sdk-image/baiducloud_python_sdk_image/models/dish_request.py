"""
Request entity for DishRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DishRequest(AbstractModel):
    """
    Request entity for DishRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, image=None, url=None, top_num=None, filter_threshold=None, baike_num=None):
        """
        Initialize DishRequest request entity.

        :param image: image parameter
        :type image: str (optional)

        :param url: url parameter
        :type url: str (optional)

        :param top_num: 返回预测得分top n结果，默认5
        :type top_num: int (optional)

        :param filter_threshold: 默认0.95，可以通过该参数调节识别效果，降低非菜识别率。
        :type filter_threshold: float (optional)

        :param baike_num: baike_num parameter
        :type baike_num: int (optional)
        """
        super().__init__()
        self.image = image
        self.url = url
        self.top_num = top_num
        self.filter_threshold = filter_threshold
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
        if self.filter_threshold is not None:
            result['filter_threshold'] = self.filter_threshold
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
        :rtype: DishRequest

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
        if m.get('filter_threshold') is not None:
            self.filter_threshold = m.get('filter_threshold')
        if m.get('baike_num') is not None:
            self.baike_num = m.get('baike_num')
        return self
