"""
Word information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.words_location import WordsLocation


class Word(AbstractModel):
    """
    Word
    """

    def __init__(self, word=None, words_location=None):
        """
        Initialize Word instance.

        :param word: 每行文字的内容
        :type word: str (optional)

        :param words_location: words_location attribute
        :type words_location: WordsLocation (optional)
        """
        super().__init__()
        self.word = word
        self.words_location = words_location

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
        if self.words_location is not None:
            result['words_location'] = self.words_location.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Word

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('word') is not None:
            self.word = m.get('word')
        if m.get('words_location') is not None:
            self.words_location = WordsLocation().from_dict(m.get('words_location'))
        return self
