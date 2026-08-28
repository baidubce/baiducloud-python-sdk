"""
Paragraph information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.handwriting_get_b_box import HandwritingGetBBox

from baiducloud_python_sdk_ocr.models.sentence import Sentence


class Paragraph(AbstractModel):
    """
    Paragraph
    """

    def __init__(self, bbox=None, paragraph_id=None, is_column=None, text=None, sentences=None):
        """
        Initialize Paragraph instance.

        :param bbox: 仅字级和行级粒度返回，段落轮廓坐标列表，可能含多个框
        :type bbox: List[HandwritingGetBBox] (optional)

        :param paragraph_id: 段落唯一标识符（如p1）
        :type paragraph_id: str (optional)

        :param is_column: 仅字级和行级粒度返回，是否分栏。1：分栏，0：不分栏
        :type is_column: int (optional)

        :param text: 段落完整文本
        :type text: str (optional)

        :param sentences: 段落内的句子列表
        :type sentences: List[Sentence] (optional)
        """
        super().__init__()
        self.bbox = bbox
        self.paragraph_id = paragraph_id
        self.is_column = is_column
        self.text = text
        self.sentences = sentences

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
        if self.bbox is not None:
            result['bbox'] = [i.to_dict() for i in self.bbox]
        if self.paragraph_id is not None:
            result['paragraphId'] = self.paragraph_id
        if self.is_column is not None:
            result['isColumn'] = self.is_column
        if self.text is not None:
            result['text'] = self.text
        if self.sentences is not None:
            result['sentences'] = [i.to_dict() for i in self.sentences]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Paragraph

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('bbox') is not None:
            self.bbox = [HandwritingGetBBox().from_dict(i) for i in m.get('bbox')]
        if m.get('paragraphId') is not None:
            self.paragraph_id = m.get('paragraphId')
        if m.get('isColumn') is not None:
            self.is_column = m.get('isColumn')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('sentences') is not None:
            self.sentences = [Sentence().from_dict(i) for i in m.get('sentences')]
        return self
