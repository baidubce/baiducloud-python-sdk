"""
DocAnalysisWords information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.words_location import WordsLocation

from baiducloud_python_sdk_ocr.models.doc_analysis_poly_location import DocAnalysisPolyLocation

from baiducloud_python_sdk_ocr.models.doc_analysis_line_probability import DocAnalysisLineProbability


class DocAnalysisWords(AbstractModel):
    """
    DocAnalysisWords
    """

    def __init__(self, word=None, words_location=None, poly_location=None, line_probability=None):
        """
        Initialize DocAnalysisWords instance.

        :param word: 整行的识别结果
        :type word: str (optional)

        :param words_location: words_location attribute
        :type words_location: WordsLocation (optional)

        :param poly_location: poly_location attribute
        :type poly_location: DocAnalysisPolyLocation (optional)

        :param line_probability: line_probability attribute
        :type line_probability: DocAnalysisLineProbability (optional)
        """
        super().__init__()
        self.word = word
        self.words_location = words_location
        self.poly_location = poly_location
        self.line_probability = line_probability

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
        if self.words_location is not None:
            result['words_location'] = self.words_location.to_dict()
        if self.poly_location is not None:
            result['poly_location'] = self.poly_location.to_dict()
        if self.line_probability is not None:
            result['line_probability'] = self.line_probability.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DocAnalysisWords

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('word') is not None:
            self.word = m.get('word')
        if m.get('words_location') is not None:
            self.words_location = WordsLocation().from_dict(m.get('words_location'))
        if m.get('poly_location') is not None:
            self.poly_location = DocAnalysisPolyLocation().from_dict(m.get('poly_location'))
        if m.get('line_probability') is not None:
            self.line_probability = DocAnalysisLineProbability().from_dict(m.get('line_probability'))
        return self
