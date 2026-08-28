"""
DocAnalysisOfficeLayout information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.doc_analysis_office_point import DocAnalysisOfficePoint


class DocAnalysisOfficeLayout(AbstractModel):
    """
    DocAnalysisOfficeLayout
    """

    def __init__(self, layout=None, layout_prob=None, layout_location=None, layout_idx=None):
        """
        Initialize DocAnalysisOfficeLayout instance.

        :param layout: layout attribute
        :type layout: str (optional)

        :param layout_prob: 当前版式检测框的概率大小
        :type layout_prob: float (optional)

        :param layout_location: 文档版面信息标签的位置，四个顶点
        :type layout_location: List[DocAnalysisOfficePoint] (optional)

        :param layout_idx: 文档版面信息中的文本在results结果中的位置
        :type layout_idx: List[int] (optional)
        """
        super().__init__()
        self.layout = layout
        self.layout_prob = layout_prob
        self.layout_location = layout_location
        self.layout_idx = layout_idx

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
        if self.layout is not None:
            result['layout'] = self.layout
        if self.layout_prob is not None:
            result['layout_prob'] = self.layout_prob
        if self.layout_location is not None:
            result['layout_location'] = [i.to_dict() for i in self.layout_location]
        if self.layout_idx is not None:
            result['layout_idx'] = self.layout_idx
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DocAnalysisOfficeLayout

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('layout') is not None:
            self.layout = m.get('layout')
        if m.get('layout_prob') is not None:
            self.layout_prob = m.get('layout_prob')
        if m.get('layout_location') is not None:
            self.layout_location = [DocAnalysisOfficePoint().from_dict(i) for i in m.get('layout_location')]
        if m.get('layout_idx') is not None:
            self.layout_idx = m.get('layout_idx')
        return self
