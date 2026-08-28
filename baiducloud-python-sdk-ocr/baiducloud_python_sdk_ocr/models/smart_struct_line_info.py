"""
SmartStructLineInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.smart_struct_location import SmartStructLocation


class SmartStructLineInfo(AbstractModel):
    """
    SmartStructLineInfo
    """

    def __init__(
        self,
        object_id=None,
        block_id=None,
        word=None,
        line_class=None,
        line_class_probability=None,
        line__probability=None,
        left=None,
        top=None,
        width=None,
        height=None,
        line_location=None,
    ):
        """
        Initialize SmartStructLineInfo instance.

        :param object_id: 文字行的 id，唯一标识，按从上到下从左到右顺序，依次顺位排列
        :type object_id: int (optional)

        :param block_id: block_id attribute
        :type block_id: int (optional)

        :param word: 文字行的文字结果
        :type word: str (optional)

        :param line_class: line_class attribute
        :type line_class: str (optional)

        :param line_class_probability: line_class 的分类置信度
        :type line_class_probability: float (optional)

        :param line__probability: 文字行的文字结果识别置信度
        :type line__probability: float (optional)

        :param left: 文字行左上角水平坐标
        :type left: float (optional)

        :param top: 文字行左上角垂直坐标
        :type top: float (optional)

        :param width: 文字行宽度
        :type width: float (optional)

        :param height: 文字行高度
        :type height: float (optional)

        :param line_location: line_location attribute
        :type line_location: SmartStructLocation (optional)
        """
        super().__init__()
        self.object_id = object_id
        self.block_id = block_id
        self.word = word
        self.line_class = line_class
        self.line_class_probability = line_class_probability
        self.line__probability = line__probability
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.line_location = line_location

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
        if self.object_id is not None:
            result['object_id'] = self.object_id
        if self.block_id is not None:
            result['block_id'] = self.block_id
        if self.word is not None:
            result['word'] = self.word
        if self.line_class is not None:
            result['line_class'] = self.line_class
        if self.line_class_probability is not None:
            result['line_class_probability'] = self.line_class_probability
        if self.line__probability is not None:
            result['line__probability'] = self.line__probability
        if self.left is not None:
            result['left'] = self.left
        if self.top is not None:
            result['top'] = self.top
        if self.width is not None:
            result['width'] = self.width
        if self.height is not None:
            result['height'] = self.height
        if self.line_location is not None:
            result['line_location'] = self.line_location.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SmartStructLineInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('object_id') is not None:
            self.object_id = m.get('object_id')
        if m.get('block_id') is not None:
            self.block_id = m.get('block_id')
        if m.get('word') is not None:
            self.word = m.get('word')
        if m.get('line_class') is not None:
            self.line_class = m.get('line_class')
        if m.get('line_class_probability') is not None:
            self.line_class_probability = m.get('line_class_probability')
        if m.get('line__probability') is not None:
            self.line__probability = m.get('line__probability')
        if m.get('left') is not None:
            self.left = m.get('left')
        if m.get('top') is not None:
            self.top = m.get('top')
        if m.get('width') is not None:
            self.width = m.get('width')
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('line_location') is not None:
            self.line_location = SmartStructLocation().from_dict(m.get('line_location'))
        return self
