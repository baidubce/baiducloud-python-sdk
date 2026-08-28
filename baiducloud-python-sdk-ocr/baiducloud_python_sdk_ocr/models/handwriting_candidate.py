"""
HandwritingCandidate information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class HandwritingCandidate(AbstractModel):
    """
    HandwritingCandidate
    """

    def __init__(self, word=None, prob=None):
        """
        Initialize HandwritingCandidate instance.

        :param word: 单字符识别结果的候选词文字
        :type word: str (optional)

        :param prob: 单字符识别结果的候选词置信度
        :type prob: str (optional)
        """
        super().__init__()
        self.word = word
        self.prob = prob

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
        if self.word is not None:
            result['word'] = self.word
        if self.prob is not None:
            result['prob'] = self.prob
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HandwritingCandidate

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('word') is not None:
            self.word = m.get('word')
        if m.get('prob') is not None:
            self.prob = m.get('prob')
        return self
