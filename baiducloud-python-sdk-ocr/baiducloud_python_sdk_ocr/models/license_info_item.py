"""
LicenseInfoItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class LicenseInfoItem(AbstractModel):
    """
    LicenseInfoItem
    """

    def __init__(self, word_name=None, word=None):
        """
        Initialize LicenseInfoItem instance.

        :param word_name: 字段名，如号牌号码、车辆类型、所有人、品牌型号、车辆识别代码、发动机号码、核定载人数、质量、尺寸、检验记录等
        :type word_name: str (optional)

        :param word: word_name字段对应的识别结果
        :type word: str (optional)
        """
        super().__init__()
        self.word_name = word_name
        self.word = word

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
        if self.word_name is not None:
            result['word_name'] = self.word_name
        if self.word is not None:
            result['word'] = self.word
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: LicenseInfoItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('word_name') is not None:
            self.word_name = m.get('word_name')
        if m.get('word') is not None:
            self.word = m.get('word')
        return self
