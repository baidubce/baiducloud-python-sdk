"""
DocAnalysisOfficeWords information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.doc_analysis_office_line_probability import DocAnalysisOfficeLineProbability

from baiducloud_python_sdk_ocr.models.doc_analysis_office_point import DocAnalysisOfficePoint

from baiducloud_python_sdk_ocr.models.doc_anaysis_office_location import DocAnaysisOfficeLocation


class DocAnalysisOfficeWords(AbstractModel):
    """
    DocAnalysisOfficeWords
    """

    def __init__(self, word=None, line_probability=None, poly_location=None, words_location=None):
        """
        Initialize DocAnalysisOfficeWords instance.

        :param word: 整行的识别结果
        :type word: str (optional)

        :param line_probability: line_probability attribute
        :type line_probability: DocAnalysisOfficeLineProbability (optional)

        :param poly_location: 每行的四角点坐标，自左上角点顺时针排列，disp_line_poly=true时返回
        :type poly_location: List[DocAnalysisOfficePoint] (optional)

        :param words_location: words_location attribute
        :type words_location: DocAnaysisOfficeLocation (optional)
        """
        super().__init__()
        self.word = word
        self.line_probability = line_probability
        self.poly_location = poly_location
        self.words_location = words_location

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
        if self.word is not None:
            result['word'] = self.word
        if self.line_probability is not None:
            result['line_probability'] = self.line_probability.to_dict()
        if self.poly_location is not None:
            result['poly_location'] = [i.to_dict() for i in self.poly_location]
        if self.words_location is not None:
            result['words_location'] = self.words_location.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DocAnalysisOfficeWords

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('word') is not None:
            self.word = m.get('word')
        if m.get('line_probability') is not None:
            self.line_probability = DocAnalysisOfficeLineProbability().from_dict(m.get('line_probability'))
        if m.get('poly_location') is not None:
            self.poly_location = [DocAnalysisOfficePoint().from_dict(i) for i in m.get('poly_location')]
        if m.get('words_location') is not None:
            self.words_location = DocAnaysisOfficeLocation().from_dict(m.get('words_location'))
        return self
