"""
KeywordItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class KeywordItem(AbstractModel):
    """
    KeywordItem
    """

    def __init__(self, tag=None, score=None):
        """
        Initialize KeywordItem instance.

        :param tag: 内容标签
        :type tag: str (optional)

        :param score: 权重值，取值范围[0,1]
        :type score: float (optional)
        """
        super().__init__()
        self.tag = tag
        self.score = score

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
        if self.tag is not None:
            result['tag'] = self.tag
        if self.score is not None:
            result['score'] = self.score
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: KeywordItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('score') is not None:
            self.score = m.get('score')
        return self
