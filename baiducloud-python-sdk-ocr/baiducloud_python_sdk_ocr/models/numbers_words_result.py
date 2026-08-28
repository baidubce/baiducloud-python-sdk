"""
NumbersWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.numbers_location import NumbersLocation

from baiducloud_python_sdk_ocr.models.number_char import NumberChar


class NumbersWordsResult(AbstractModel):
    """
    NumbersWordsResult
    """

    def __init__(self, location=None, words=None, chars=None):
        """
        Initialize NumbersWordsResult instance.

        :param location: location attribute
        :type location: NumbersLocation (optional)

        :param words: 识别结果字符串
        :type words: str (optional)

        :param chars: 单字符结果，当 recognize_granularity=small 时返回该字段
        :type chars: List[NumberChar] (optional)
        """
        super().__init__()
        self.location = location
        self.words = words
        self.chars = chars

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
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: NumbersWordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('location') is not None:
            self.location = NumbersLocation().from_dict(m.get('location'))
        if m.get('words') is not None:
            self.words = m.get('words')
        if m.get('chars') is not None:
            self.chars = [NumberChar().from_dict(i) for i in m.get('chars')]
        return self
