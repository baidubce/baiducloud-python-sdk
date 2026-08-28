"""
AccurateBasicWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.accurate_basic_probability import AccurateBasicProbability


class AccurateBasicWordsResult(AbstractModel):
    """
    AccurateBasicWordsResult
    """

    def __init__(self, words=None, probability=None):
        """
        Initialize AccurateBasicWordsResult instance.

        :param words: 识别结果字符串
        :type words: str (optional)

        :param probability: probability attribute
        :type probability: AccurateBasicProbability (optional)
        """
        super().__init__()
        self.words = words
        self.probability = probability

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
        if self.probability is not None:
            result['probability'] = self.probability.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AccurateBasicWordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('words') is not None:
            self.words = m.get('words')
        if m.get('probability') is not None:
            self.probability = AccurateBasicProbability().from_dict(m.get('probability'))
        return self
