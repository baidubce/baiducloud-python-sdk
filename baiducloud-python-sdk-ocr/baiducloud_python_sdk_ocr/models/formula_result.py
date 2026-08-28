"""
FormulaResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.doc_analysis_office_point import DocAnalysisOfficePoint


class FormulaResult(AbstractModel):
    """
    FormulaResult
    """

    def __init__(self, form_location=None, form_words=None):
        """
        Initialize FormulaResult instance.

        :param form_location: 公式的位置信息，矩形框坐标数组
        :type form_location: List[DocAnalysisOfficePoint] (optional)

        :param form_words: 公式的内容信息，以Latex格式返回
        :type form_words: str (optional)
        """
        super().__init__()
        self.form_location = form_location
        self.form_words = form_words

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
        if self.form_location is not None:
            result['form_location'] = [i.to_dict() for i in self.form_location]
        if self.form_words is not None:
            result['form_words'] = self.form_words
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FormulaResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('form_location') is not None:
            self.form_location = [DocAnalysisOfficePoint().from_dict(i) for i in m.get('form_location')]
        if m.get('form_words') is not None:
            self.form_words = m.get('form_words')
        return self
