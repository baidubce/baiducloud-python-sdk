"""
TextCorrectionItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_nlp.models.text_correction_detail import TextCorrectionDetail


class TextCorrectionItem(AbstractModel):
    """
    TextCorrectionItem
    """

    def __init__(self, text=None, correct_query=None, content_len=None, details=None, error_num=None):
        """
        Initialize TextCorrectionItem instance.

        :param text: 纠错前的文本
        :type text: str (optional)

        :param correct_query: 纠错后的文本
        :type correct_query: str (optional)

        :param content_len: content的长度
        :type content_len: int (optional)

        :param details: 纠错信息列表
        :type details: List[TextCorrectionDetail] (optional)

        :param error_num: 纠错片段数量
        :type error_num: int (optional)
        """
        super().__init__()
        self.text = text
        self.correct_query = correct_query
        self.content_len = content_len
        self.details = details
        self.error_num = error_num

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
        if self.text is not None:
            result['text'] = self.text
        if self.correct_query is not None:
            result['correct_query'] = self.correct_query
        if self.content_len is not None:
            result['content_len'] = self.content_len
        if self.details is not None:
            result['details'] = [i.to_dict() for i in self.details]
        if self.error_num is not None:
            result['error_num'] = self.error_num
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TextCorrectionItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('correct_query') is not None:
            self.correct_query = m.get('correct_query')
        if m.get('content_len') is not None:
            self.content_len = m.get('content_len')
        if m.get('details') is not None:
            self.details = [TextCorrectionDetail().from_dict(i) for i in m.get('details')]
        if m.get('error_num') is not None:
            self.error_num = m.get('error_num')
        return self
