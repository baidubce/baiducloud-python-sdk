"""
QusResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.elem_text import ElemText

from baiducloud_python_sdk_ocr.models.qus_location import QusLocation

from baiducloud_python_sdk_ocr.models.qus_element import QusElement


class QusResult(AbstractModel):
    """
    QusResult
    """

    def __init__(self, qus_type=None, qus_probability=None, elem_text=None, qus_location=None, qus_element=None):
        """
        Initialize QusResult instance.

        :param qus_type: 检测到的题目类型
        :type qus_type: str (optional)

        :param qus_probability: 题目置信度
        :type qus_probability: float (optional)

        :param elem_text: elem_text attribute
        :type elem_text: ElemText (optional)

        :param qus_location: qus_location attribute
        :type qus_location: QusLocation (optional)

        :param qus_element: 题目元素信息
        :type qus_element: List[QusElement] (optional)
        """
        super().__init__()
        self.qus_type = qus_type
        self.qus_probability = qus_probability
        self.elem_text = elem_text
        self.qus_location = qus_location
        self.qus_element = qus_element

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
        if self.qus_type is not None:
            result['qus_type'] = self.qus_type
        if self.qus_probability is not None:
            result['qus_probability'] = self.qus_probability
        if self.elem_text is not None:
            result['elem_text'] = self.elem_text.to_dict()
        if self.qus_location is not None:
            result['qus_location'] = self.qus_location.to_dict()
        if self.qus_element is not None:
            result['qus_element'] = [i.to_dict() for i in self.qus_element]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QusResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('qus_type') is not None:
            self.qus_type = m.get('qus_type')
        if m.get('qus_probability') is not None:
            self.qus_probability = m.get('qus_probability')
        if m.get('elem_text') is not None:
            self.elem_text = ElemText().from_dict(m.get('elem_text'))
        if m.get('qus_location') is not None:
            self.qus_location = QusLocation().from_dict(m.get('qus_location'))
        if m.get('qus_element') is not None:
            self.qus_element = [QusElement().from_dict(i) for i in m.get('qus_element')]
        return self
