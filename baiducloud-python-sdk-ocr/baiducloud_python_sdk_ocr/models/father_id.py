"""
FatherID information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class FatherID(AbstractModel):
    """
    FatherID
    """

    def __init__(self, words=None):
        """
        Initialize FatherID instance.

        :param words: 父亲身份证号
        :type words: str (optional)
        """
        super().__init__()
        self.words = words

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
        if self.words is not None:
            result['words'] = self.words
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FatherID

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('words') is not None:
            self.words = m.get('words')
        return self
