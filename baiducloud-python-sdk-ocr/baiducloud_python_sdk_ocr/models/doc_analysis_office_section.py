"""
DocAnalysisOfficeSection information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.attri_location import AttriLocation

from baiducloud_python_sdk_ocr.models.doc_analysis_office_sec_idx import DocAnalysisOfficeSecIdx


class DocAnalysisOfficeSection(AbstractModel):
    """
    DocAnalysisOfficeSection
    """

    def __init__(self, attribute=None, sections_prob=None, attri_location=None, sec_idx=None):
        """
        Initialize DocAnalysisOfficeSection instance.

        :param attribute: 版面分析的属性标签结果，section、header、footer、number、footnote
        :type attribute: str (optional)

        :param sections_prob: 当前版面检测框的概率大小
        :type sections_prob: float (optional)

        :param attri_location: attri_location attribute
        :type attri_location: AttriLocation (optional)

        :param sec_idx: sec_idx attribute
        :type sec_idx: DocAnalysisOfficeSecIdx (optional)
        """
        super().__init__()
        self.attribute = attribute
        self.sections_prob = sections_prob
        self.attri_location = attri_location
        self.sec_idx = sec_idx

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
        if self.attribute is not None:
            result['attribute'] = self.attribute
        if self.sections_prob is not None:
            result['sections_prob'] = self.sections_prob
        if self.attri_location is not None:
            result['attri_location'] = self.attri_location.to_dict()
        if self.sec_idx is not None:
            result['sec_idx'] = self.sec_idx.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DocAnalysisOfficeSection

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')
        if m.get('sections_prob') is not None:
            self.sections_prob = m.get('sections_prob')
        if m.get('attri_location') is not None:
            self.attri_location = AttriLocation().from_dict(m.get('attri_location'))
        if m.get('sec_idx') is not None:
            self.sec_idx = DocAnalysisOfficeSecIdx().from_dict(m.get('sec_idx'))
        return self
