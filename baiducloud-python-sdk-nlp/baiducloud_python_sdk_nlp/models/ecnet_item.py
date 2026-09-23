"""
EcnetItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_nlp.models.vec_fragment import VecFragment


class EcnetItem(AbstractModel):
    """
    EcnetItem
    """

    def __init__(self, correct_query=None, score=None, vec_fragment=None):
        """
        Initialize EcnetItem instance.

        :param correct_query: 纠错后的文本
        :type correct_query: str (optional)

        :param score: 模型置信度打分。若score返回为数字7，表示输入不合法，比如输入过长或过短，该情况没有纠错结果
        :type score: float (optional)

        :param vec_fragment: 替换候选片段信息
        :type vec_fragment: List[VecFragment] (optional)
        """
        super().__init__()
        self.correct_query = correct_query
        self.score = score
        self.vec_fragment = vec_fragment

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
        if self.correct_query is not None:
            result['correct_query'] = self.correct_query
        if self.score is not None:
            result['score'] = self.score
        if self.vec_fragment is not None:
            result['vec_fragment'] = [i.to_dict() for i in self.vec_fragment]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EcnetItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('correct_query') is not None:
            self.correct_query = m.get('correct_query')
        if m.get('score') is not None:
            self.score = m.get('score')
        if m.get('vec_fragment') is not None:
            self.vec_fragment = [VecFragment().from_dict(i) for i in m.get('vec_fragment')]
        return self
