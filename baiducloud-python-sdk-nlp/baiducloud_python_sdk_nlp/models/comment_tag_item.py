"""
CommentTagItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CommentTagItem(AbstractModel):
    """
    CommentTagItem
    """

    def __init__(self, prop=None, adj=None, sentiment=None, begin_pos=None, end_pos=None, abstract=None):
        """
        Initialize CommentTagItem instance.

        :param prop: 匹配上的属性词
        :type prop: str (optional)

        :param adj: 匹配上的描述词
        :type adj: str (optional)

        :param sentiment: 该情感搭配的极性（0表示消极，1表示中性，2表示积极）
        :type sentiment: int (optional)

        :param begin_pos: 该情感搭配在句子中的开始位置
        :type begin_pos: int (optional)

        :param end_pos: 该情感搭配在句子中的结束位置
        :type end_pos: int (optional)

        :param abstract: 对应于该情感搭配的短句摘要
        :type abstract: str (optional)
        """
        super().__init__()
        self.prop = prop
        self.adj = adj
        self.sentiment = sentiment
        self.begin_pos = begin_pos
        self.end_pos = end_pos
        self.abstract = abstract

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
        if self.prop is not None:
            result['prop'] = self.prop
        if self.adj is not None:
            result['adj'] = self.adj
        if self.sentiment is not None:
            result['sentiment'] = self.sentiment
        if self.begin_pos is not None:
            result['begin_pos'] = self.begin_pos
        if self.end_pos is not None:
            result['end_pos'] = self.end_pos
        if self.abstract is not None:
            result['abstract'] = self.abstract
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CommentTagItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('prop') is not None:
            self.prop = m.get('prop')
        if m.get('adj') is not None:
            self.adj = m.get('adj')
        if m.get('sentiment') is not None:
            self.sentiment = m.get('sentiment')
        if m.get('begin_pos') is not None:
            self.begin_pos = m.get('begin_pos')
        if m.get('end_pos') is not None:
            self.end_pos = m.get('end_pos')
        if m.get('abstract') is not None:
            self.abstract = m.get('abstract')
        return self
