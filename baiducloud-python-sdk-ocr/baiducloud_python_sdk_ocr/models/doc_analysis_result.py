"""
DocAnalysisResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.doc_analysis_words import DocAnalysisWords

from baiducloud_python_sdk_ocr.models.doc_analysis_char import DocAnalysisChar


class DocAnalysisResult(AbstractModel):
    """
    DocAnalysisResult
    """

    def __init__(self, words_type=None, words=None, chars=None):
        """
        Initialize DocAnalysisResult instance.

        :param words_type: 文字属性（手写、印刷），handwriting手写，print印刷
        :type words_type: str (optional)

        :param words: words attribute
        :type words: DocAnalysisWords (optional)

        :param chars: result_type=small时返回。单字符结果数组
        :type chars: List[DocAnalysisChar] (optional)
        """
        super().__init__()
        self.words_type = words_type
        self.words = words
        self.chars = chars

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
        if self.words_type is not None:
            result['words_type'] = self.words_type
        if self.words is not None:
            result['words'] = self.words.to_dict()
        if self.chars is not None:
            result['chars'] = [i.to_dict() for i in self.chars]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DocAnalysisResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('words_type') is not None:
            self.words_type = m.get('words_type')
        if m.get('words') is not None:
            self.words = DocAnalysisWords().from_dict(m.get('words'))
        if m.get('chars') is not None:
            self.chars = [DocAnalysisChar().from_dict(i) for i in m.get('chars')]
        return self
