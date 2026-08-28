"""
Line information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.handwriting_get_b_box import HandwritingGetBBox

from baiducloud_python_sdk_ocr.models.handwriting_get_char_info import HandwritingGetCharInfo


class Line(AbstractModel):
    """
    Line
    """

    def __init__(self, line_id=None, text=None, bbox=None, paragraph_id=None, chars=None):
        """
        Initialize Line instance.

        :param line_id: 行的唯一标识符
        :type line_id: str (optional)

        :param text: 该行的文本内容
        :type text: str (optional)

        :param bbox: bbox attribute
        :type bbox: HandwritingGetBBox (optional)

        :param paragraph_id: 该行所属段落的ID，关联paragraphs
        :type paragraph_id: str (optional)

        :param chars: 仅字级粒度返回，行内单字/字符详细列表
        :type chars: List[HandwritingGetCharInfo] (optional)
        """
        super().__init__()
        self.line_id = line_id
        self.text = text
        self.bbox = bbox
        self.paragraph_id = paragraph_id
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
        if self.line_id is not None:
            result['lineId'] = self.line_id
        if self.text is not None:
            result['text'] = self.text
        if self.bbox is not None:
            result['bbox'] = self.bbox.to_dict()
        if self.paragraph_id is not None:
            result['paragraphId'] = self.paragraph_id
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
        :rtype: Line

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('lineId') is not None:
            self.line_id = m.get('lineId')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('bbox') is not None:
            self.bbox = HandwritingGetBBox().from_dict(m.get('bbox'))
        if m.get('paragraphId') is not None:
            self.paragraph_id = m.get('paragraphId')
        if m.get('chars') is not None:
            self.chars = [HandwritingGetCharInfo().from_dict(i) for i in m.get('chars')]
        return self
