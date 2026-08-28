"""
QusElement information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.elem_location import ElemLocation

from baiducloud_python_sdk_ocr.models.elem_word import ElemWord


class QusElement(AbstractModel):
    """
    QusElement
    """

    def __init__(self, elem_type=None, elem_probability=None, elem_location=None, elem_word=None):
        """
        Initialize QusElement instance.

        :param elem_type: 题目元素类型
        :type elem_type: str (optional)

        :param elem_probability: 题目元素置信度
        :type elem_probability: float (optional)

        :param elem_location: elem_location attribute
        :type elem_location: ElemLocation (optional)

        :param elem_word: 题目元素的文本信息
        :type elem_word: List[ElemWord] (optional)
        """
        super().__init__()
        self.elem_type = elem_type
        self.elem_probability = elem_probability
        self.elem_location = elem_location
        self.elem_word = elem_word

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
        if self.elem_type is not None:
            result['elem_type'] = self.elem_type
        if self.elem_probability is not None:
            result['elem_probability'] = self.elem_probability
        if self.elem_location is not None:
            result['elem_location'] = self.elem_location.to_dict()
        if self.elem_word is not None:
            result['elem_word'] = [i.to_dict() for i in self.elem_word]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QusElement

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('elem_type') is not None:
            self.elem_type = m.get('elem_type')
        if m.get('elem_probability') is not None:
            self.elem_probability = m.get('elem_probability')
        if m.get('elem_location') is not None:
            self.elem_location = ElemLocation().from_dict(m.get('elem_location'))
        if m.get('elem_word') is not None:
            self.elem_word = [ElemWord().from_dict(i) for i in m.get('elem_word')]
        return self
