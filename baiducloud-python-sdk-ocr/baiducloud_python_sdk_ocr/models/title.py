"""
Title information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.handwriting_get_b_box import HandwritingGetBBox

from baiducloud_python_sdk_ocr.models.handwriting_get_char_info import HandwritingGetCharInfo


class Title(AbstractModel):
    """
    Title
    """

    def __init__(self, bbox=None, text=None, chars=None):
        """
        Initialize Title instance.

        :param bbox: 仅字级和行级粒度返回，标题外接矩形坐标
        :type bbox: List[HandwritingGetBBox] (optional)

        :param text: 标题文本内容
        :type text: str (optional)

        :param chars: 仅字级粒度返回，标题字级别详细列表
        :type chars: List[HandwritingGetCharInfo] (optional)
        """
        super().__init__()
        self.bbox = bbox
        self.text = text
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
        if self.bbox is not None:
            result['bbox'] = [i.to_dict() for i in self.bbox]
        if self.text is not None:
            result['text'] = self.text
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
        :rtype: Title

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('bbox') is not None:
            self.bbox = [HandwritingGetBBox().from_dict(i) for i in m.get('bbox')]
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('chars') is not None:
            self.chars = [HandwritingGetCharInfo().from_dict(i) for i in m.get('chars')]
        return self
