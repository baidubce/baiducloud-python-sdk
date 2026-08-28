"""
ElemWord information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.word_location import WordLocation


class ElemWord(AbstractModel):
    """
    ElemWord
    """

    def __init__(self, word_location=None, word_type=None, word=None):
        """
        Initialize ElemWord instance.

        :param word_location: word_location attribute
        :type word_location: WordLocation (optional)

        :param word_type: 按行返回文字属性信息
        :type word_type: str (optional)

        :param word: 按行返回文字信息
        :type word: str (optional)
        """
        super().__init__()
        self.word_location = word_location
        self.word_type = word_type
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
        if self.word_location is not None:
            result['word_location'] = self.word_location.to_dict()
        if self.word_type is not None:
            result['word_type'] = self.word_type
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
        :rtype: ElemWord

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('word_location') is not None:
            self.word_location = WordLocation().from_dict(m.get('word_location'))
        if m.get('word_type') is not None:
            self.word_type = m.get('word_type')
        if m.get('word') is not None:
            self.word = m.get('word')
        return self
