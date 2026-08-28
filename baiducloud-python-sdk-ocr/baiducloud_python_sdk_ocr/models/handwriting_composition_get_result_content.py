"""
HandwritingCompositionGetResultContent information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.paragraph import Paragraph


class HandwritingCompositionGetResultContent(AbstractModel):
    """
    HandwritingCompositionGetResultContent
    """

    def __init__(self, lines=None, paragraphs=None):
        """
        Initialize HandwritingCompositionGetResultContent instance.

        :param lines: 仅字级和行级粒度返回，行级信息列表
        :type lines: List[List[Line]] (optional)

        :param paragraphs: 段落级逻辑信息列表
        :type paragraphs: List[Paragraph] (optional)
        """
        super().__init__()
        self.lines = lines
        self.paragraphs = paragraphs

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
        if self.lines is not None:
            result['lines'] = self.lines
        if self.paragraphs is not None:
            result['paragraphs'] = [i.to_dict() for i in self.paragraphs]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HandwritingCompositionGetResultContent

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('lines') is not None:
            self.lines = m.get('lines')
        if m.get('paragraphs') is not None:
            self.paragraphs = [Paragraph().from_dict(i) for i in m.get('paragraphs')]
        return self
