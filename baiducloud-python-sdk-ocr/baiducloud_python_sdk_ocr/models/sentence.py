"""
Sentence information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.handwriting_get_b_box import HandwritingGetBBox

from baiducloud_python_sdk_ocr.models.line_segment import LineSegment


class Sentence(AbstractModel):
    """
    Sentence
    """

    def __init__(self, bbox=None, sentence_id=None, text=None, line_segments=None):
        """
        Initialize Sentence instance.

        :param bbox: 仅字级和行级粒度返回，句子轮廓坐标列表
        :type bbox: List[HandwritingGetBBox] (optional)

        :param sentence_id: 句子唯一标识符
        :type sentence_id: str (optional)

        :param text: 句子文本内容
        :type text: str (optional)

        :param line_segments: 仅字级和行级粒度返回，句行映射片段，描述该句子对应的行及起止位置
        :type line_segments: List[LineSegment] (optional)
        """
        super().__init__()
        self.bbox = bbox
        self.sentence_id = sentence_id
        self.text = text
        self.line_segments = line_segments

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
        if self.sentence_id is not None:
            result['sentenceId'] = self.sentence_id
        if self.text is not None:
            result['text'] = self.text
        if self.line_segments is not None:
            result['lineSegments'] = [i.to_dict() for i in self.line_segments]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Sentence

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('bbox') is not None:
            self.bbox = [HandwritingGetBBox().from_dict(i) for i in m.get('bbox')]
        if m.get('sentenceId') is not None:
            self.sentence_id = m.get('sentenceId')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('lineSegments') is not None:
            self.line_segments = [LineSegment().from_dict(i) for i in m.get('lineSegments')]
        return self
