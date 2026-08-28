"""
AccurateChar information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.accurate_location import AccurateLocation


class AccurateChar(AbstractModel):
    """
    AccurateChar
    """

    def __init__(self, char=None, char_prob=None, location=None):
        """
        Initialize AccurateChar instance.

        :param char: 单字符识别结果，当 recognize_granularity=small 时返回该字段
        :type char: str (optional)

        :param char_prob: char_prob attribute
        :type char_prob: int (optional)

        :param location: location attribute
        :type location: AccurateLocation (optional)
        """
        super().__init__()
        self.char = char
        self.char_prob = char_prob
        self.location = location

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
        if self.char is not None:
            result['char'] = self.char
        if self.char_prob is not None:
            result['char_prob'] = self.char_prob
        if self.location is not None:
            result['location'] = self.location.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AccurateChar

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('char') is not None:
            self.char = m.get('char')
        if m.get('char_prob') is not None:
            self.char_prob = m.get('char_prob')
        if m.get('location') is not None:
            self.location = AccurateLocation().from_dict(m.get('location'))
        return self
