"""
LexerItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_nlp.models.lexer_loc_detail import LexerLocDetail


class LexerItem(AbstractModel):
    """
    LexerItem
    """

    def __init__(
        self,
        item=None,
        ne=None,
        pos=None,
        byte_offset=None,
        byte_length=None,
        uri=None,
        formal=None,
        basic_words=None,
        loc_details=None,
    ):
        """
        Initialize LexerItem instance.

        :param item: 词汇的字符串
        :type item: str (optional)

        :param ne: 命名实体类型，命名实体识别算法使用。词性标注算法中，此项为空串
        :type ne: str (optional)

        :param pos: 词性，词性标注算法使用。命名实体识别算法中，此项为空串
        :type pos: str (optional)

        :param byte_offset: 在text中的字节级offset
        :type byte_offset: int (optional)

        :param byte_length: 字节级length
        :type byte_length: int (optional)

        :param uri: 链指到知识库的URI，只对命名实体有效。对于非命名实体和链接不到知识库的命名实体，此项为空串
        :type uri: str (optional)

        :param formal: 词汇的标准化表达，主要针对时间、数字单位，没有归一化表达的，此项为空串
        :type formal: str (optional)

        :param basic_words: 基本词成分
        :type basic_words: List[str] (optional)

        :param loc_details: 地址成分，非必需，仅对地址型命名实体有效，没有地址成分的，此项为空数组
        :type loc_details: List[LexerLocDetail] (optional)
        """
        super().__init__()
        self.item = item
        self.ne = ne
        self.pos = pos
        self.byte_offset = byte_offset
        self.byte_length = byte_length
        self.uri = uri
        self.formal = formal
        self.basic_words = basic_words
        self.loc_details = loc_details

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
        if self.item is not None:
            result['item'] = self.item
        if self.ne is not None:
            result['ne'] = self.ne
        if self.pos is not None:
            result['pos'] = self.pos
        if self.byte_offset is not None:
            result['byte_offset'] = self.byte_offset
        if self.byte_length is not None:
            result['byte_length'] = self.byte_length
        if self.uri is not None:
            result['uri'] = self.uri
        if self.formal is not None:
            result['formal'] = self.formal
        if self.basic_words is not None:
            result['basic_words'] = self.basic_words
        if self.loc_details is not None:
            result['loc_details'] = [i.to_dict() for i in self.loc_details]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: LexerItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('item') is not None:
            self.item = m.get('item')
        if m.get('ne') is not None:
            self.ne = m.get('ne')
        if m.get('pos') is not None:
            self.pos = m.get('pos')
        if m.get('byte_offset') is not None:
            self.byte_offset = m.get('byte_offset')
        if m.get('byte_length') is not None:
            self.byte_length = m.get('byte_length')
        if m.get('uri') is not None:
            self.uri = m.get('uri')
        if m.get('formal') is not None:
            self.formal = m.get('formal')
        if m.get('basic_words') is not None:
            self.basic_words = m.get('basic_words')
        if m.get('loc_details') is not None:
            self.loc_details = [LexerLocDetail().from_dict(i) for i in m.get('loc_details')]
        return self
