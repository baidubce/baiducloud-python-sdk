"""
DocAnalysisOfficeChar information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.doc_anaysis_office_location import DocAnaysisOfficeLocation


class DocAnalysisOfficeChar(AbstractModel):
    """
    DocAnalysisOfficeChar
    """

    def __init__(self, char=None, char_prob=None, chars_location=None):
        """
        Initialize DocAnalysisOfficeChar instance.

        :param char: 每个单字的内容
        :type char: str (optional)

        :param char_prob: 单字符置信度，result_type=small 且 char_probability=true 时返回
        :type char_prob: float (optional)

        :param chars_location: chars_location attribute
        :type chars_location: DocAnaysisOfficeLocation (optional)
        """
        super().__init__()
        self.char = char
        self.char_prob = char_prob
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
        if self.char_prob is not None:
            result['char_prob'] = self.char_prob
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
        :rtype: DocAnalysisOfficeChar

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('char') is not None:
            self.char = m.get('char')
        if m.get('char_prob') is not None:
            self.char_prob = m.get('char_prob')
        if m.get('chars_location') is not None:
            self.chars_location = DocAnaysisOfficeLocation().from_dict(m.get('chars_location'))
        return self
