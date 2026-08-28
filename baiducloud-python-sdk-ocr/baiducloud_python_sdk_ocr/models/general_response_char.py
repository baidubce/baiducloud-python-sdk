"""
GeneralResponseChar information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.general_location import GeneralLocation


class GeneralResponseChar(AbstractModel):
    """
    GeneralResponseChar
    """

    def __init__(self, char=None, location=None):
        """
        Initialize GeneralResponseChar instance.

        :param char: 单字符识别结果
        :type char: str (optional)

        :param location: location attribute
        :type location: GeneralLocation (optional)
        """
        super().__init__()
        self.char = char
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
        :rtype: GeneralResponseChar

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('char') is not None:
            self.char = m.get('char')
        if m.get('location') is not None:
            self.location = GeneralLocation().from_dict(m.get('location'))
        return self
