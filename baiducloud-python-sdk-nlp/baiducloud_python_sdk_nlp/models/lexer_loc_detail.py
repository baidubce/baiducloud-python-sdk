"""
LexerLocDetail information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class LexerLocDetail(AbstractModel):
    """
    LexerLocDetail
    """

    def __init__(self, type=None, byte_offset=None, byte_length=None):
        """
        Initialize LexerLocDetail instance.

        :param type: 成分类型，如省、市、区、县
        :type type: str (optional)

        :param byte_offset: 在item中的字节级offset
        :type byte_offset: int (optional)

        :param byte_length: 字节级length
        :type byte_length: int (optional)
        """
        super().__init__()
        self.type = type
        self.byte_offset = byte_offset
        self.byte_length = byte_length

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
        if self.type is not None:
            result['type'] = self.type
        if self.byte_offset is not None:
            result['byte_offset'] = self.byte_offset
        if self.byte_length is not None:
            result['byte_length'] = self.byte_length
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: LexerLocDetail

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('byte_offset') is not None:
            self.byte_offset = m.get('byte_offset')
        if m.get('byte_length') is not None:
            self.byte_length = m.get('byte_length')
        return self
