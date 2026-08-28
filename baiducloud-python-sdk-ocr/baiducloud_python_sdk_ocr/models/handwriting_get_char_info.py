"""
HandwritingGetCharInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.handwriting_get_b_box import HandwritingGetBBox


class HandwritingGetCharInfo(AbstractModel):
    """
    HandwritingGetCharInfo
    """

    def __init__(self, is_punctuation=None, bbox=None, char=None, index=None):
        """
        Initialize HandwritingGetCharInfo instance.

        :param is_punctuation: 该字符是否为标点符号
        :type is_punctuation: str (optional)

        :param bbox: bbox attribute
        :type bbox: HandwritingGetBBox (optional)

        :param char: 单个字符
        :type char: str (optional)

        :param index: 字符索引
        :type index: str (optional)
        """
        super().__init__()
        self.is_punctuation = is_punctuation
        self.bbox = bbox
        self.char = char
        self.index = index

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
        if self.is_punctuation is not None:
            result['isPunctuation'] = self.is_punctuation
        if self.bbox is not None:
            result['bbox'] = self.bbox.to_dict()
        if self.char is not None:
            result['char'] = self.char
        if self.index is not None:
            result['index'] = self.index
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HandwritingGetCharInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('isPunctuation') is not None:
            self.is_punctuation = m.get('isPunctuation')
        if m.get('bbox') is not None:
            self.bbox = HandwritingGetBBox().from_dict(m.get('bbox'))
        if m.get('char') is not None:
            self.char = m.get('char')
        if m.get('index') is not None:
            self.index = m.get('index')
        return self
