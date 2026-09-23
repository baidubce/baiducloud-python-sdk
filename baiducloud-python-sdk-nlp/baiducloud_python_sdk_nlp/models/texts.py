"""
Texts information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Texts(AbstractModel):
    """
    Texts
    """

    def __init__(self, text_1=None, text_2=None):
        """
        Initialize Texts instance.

        :param text_1: 输入的第一段文本
        :type text_1: str (optional)

        :param text_2: 输入的第二段文本
        :type text_2: str (optional)
        """
        super().__init__()
        self.text_1 = text_1
        self.text_2 = text_2

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
        if self.text_1 is not None:
            result['text_1'] = self.text_1
        if self.text_2 is not None:
            result['text_2'] = self.text_2
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Texts

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('text_1') is not None:
            self.text_1 = m.get('text_1')
        if m.get('text_2') is not None:
            self.text_2 = m.get('text_2')
        return self
