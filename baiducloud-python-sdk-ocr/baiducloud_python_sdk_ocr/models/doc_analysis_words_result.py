"""
DocAnalysisWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.doc_analysis_location import DocAnalysisLocation

from baiducloud_python_sdk_ocr.models.doc_analysis_char import DocAnalysisChar


class DocAnalysisWordsResult(AbstractModel):
    """
    DocAnalysisWordsResult
    """

    def __init__(self, location=None, words=None, type=None, chars=None):
        """
        Initialize DocAnalysisWordsResult instance.

        :param location: location attribute
        :type location: DocAnalysisLocation (optional)

        :param words: 识别结果中整行的内容
        :type words: str (optional)

        :param type: 整行内容的类型，print：印刷，handwriting：手写
        :type type: str (optional)

        :param chars: 单字符结果数组，公式整体作为一个单字，result_type=small时返回
        :type chars: List[DocAnalysisChar] (optional)
        """
        super().__init__()
        self.location = location
        self.words = words
        self.type = type
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
        if self.location is not None:
            result['location'] = self.location.to_dict()
        if self.words is not None:
            result['words'] = self.words
        if self.type is not None:
            result['type'] = self.type
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
        :rtype: DocAnalysisWordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('location') is not None:
            self.location = DocAnalysisLocation().from_dict(m.get('location'))
        if m.get('words') is not None:
            self.words = m.get('words')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('chars') is not None:
            self.chars = [DocAnalysisChar().from_dict(i) for i in m.get('chars')]
        return self
