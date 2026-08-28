"""
DocAnalysisChar information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.chars_location import CharsLocation


class DocAnalysisChar(AbstractModel):
    """
    DocAnalysisChar
    """

    def __init__(self, char=None, chars_location=None):
        """
        Initialize DocAnalysisChar instance.

        :param char: 每个单字的内容
        :type char: str (optional)

        :param chars_location: chars_location attribute
        :type chars_location: CharsLocation (optional)
        """
        super().__init__()
        self.char = char
        self.chars_location = chars_location

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
        if self.chars_location is not None:
            result['chars_location'] = self.chars_location.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DocAnalysisChar

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('char') is not None:
            self.char = m.get('char')
        if m.get('chars_location') is not None:
            self.chars_location = CharsLocation().from_dict(m.get('chars_location'))
        return self
