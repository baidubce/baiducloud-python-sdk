"""
Request entity for TxtKeywordsExtractionRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TxtKeywordsExtractionRequest(AbstractModel):
    """
    Request entity for TxtKeywordsExtractionRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, text, charset=None, num=None):
        """
        Initialize TxtKeywordsExtractionRequest request entity.

        :param charset: charset parameter
        :type charset: str (optional)

        :param text: 原文本内容，最大65535字符，建议在文本中同一词语的出现次数少于500次
        :type text: List[str] (required)

        :param num: num parameter
        :type num: int (optional)
        """
        super().__init__()
        self.charset = charset
        self.text = text
        self.num = num

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.text is not None:
            result['text'] = self.text
        if self.num is not None:
            result['num'] = self.num
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TxtKeywordsExtractionRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('charset') is not None:
            self.charset = m.get('charset')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('num') is not None:
            self.num = m.get('num')
        return self
