"""
SearchResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SearchResult(AbstractModel):
    """
    SearchResult
    """

    def __init__(self, cont_sign=None, score=None, brief=None):
        """
        Initialize SearchResult instance.

        :param cont_sign: 图片签名，可用于删除图片或定位问题
        :type cont_sign: str (optional)

        :param score: 图片相关性，0-1，越接近1越相似
        :type score: float (optional)

        :param brief: 入库时添加的brief信息
        :type brief: str (optional)
        """
        super().__init__()
        self.cont_sign = cont_sign
        self.score = score
        self.brief = brief

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
        if self.cont_sign is not None:
            result['cont_sign'] = self.cont_sign
        if self.score is not None:
            result['score'] = self.score
        if self.brief is not None:
            result['brief'] = self.brief
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SearchResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cont_sign') is not None:
            self.cont_sign = m.get('cont_sign')
        if m.get('score') is not None:
            self.score = m.get('score')
        if m.get('brief') is not None:
            self.brief = m.get('brief')
        return self
