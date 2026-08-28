"""
FacadeWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class FacadeWordsResult(AbstractModel):
    """
    FacadeWordsResult
    """

    def __init__(self, words=None, score=None, brief=None):
        """
        Initialize FacadeWordsResult instance.

        :param words: 识别结果字符串
        :type words: str (optional)

        :param score: words返回为主门脸名称的置信度评分
        :type score: float (optional)

        :param brief: 门脸副标题等周边描述
        :type brief: str (optional)
        """
        super().__init__()
        self.words = words
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
        if self.words is not None:
            result['words'] = self.words
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
        :rtype: FacadeWordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('words') is not None:
            self.words = m.get('words')
        if m.get('score') is not None:
            self.score = m.get('score')
        if m.get('brief') is not None:
            self.brief = m.get('brief')
        return self
