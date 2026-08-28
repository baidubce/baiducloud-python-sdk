"""
HandwritingWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.hand_writing_location import HandWritingLocation

from baiducloud_python_sdk_ocr.models.handwriting_char import HandwritingChar

from baiducloud_python_sdk_ocr.models.hand_writing_probability import HandWritingProbability


class HandwritingWordsResult(AbstractModel):
    """
    HandwritingWordsResult
    """

    def __init__(self, location=None, words=None, chars=None, probability=None):
        """
        Initialize HandwritingWordsResult instance.

        :param location: location attribute
        :type location: HandWritingLocation (optional)

        :param words: 识别结果字符串
        :type words: str (optional)

        :param chars: 单字符结果，当 recognize_granularity=small 时返回该字段
        :type chars: List[HandwritingChar] (optional)

        :param probability: probability attribute
        :type probability: HandWritingProbability (optional)
        """
        super().__init__()
        self.location = location
        self.words = words
        self.chars = chars
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
        if self.location is not None:
            result['location'] = self.location.to_dict()
        if self.words is not None:
            result['words'] = self.words
        if self.chars is not None:
            result['chars'] = [i.to_dict() for i in self.chars]
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
        :rtype: HandwritingWordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('location') is not None:
            self.location = HandWritingLocation().from_dict(m.get('location'))
        if m.get('words') is not None:
            self.words = m.get('words')
        if m.get('chars') is not None:
            self.chars = [HandwritingChar().from_dict(i) for i in m.get('chars')]
        if m.get('probability') is not None:
            self.probability = HandWritingProbability().from_dict(m.get('probability'))
        return self
