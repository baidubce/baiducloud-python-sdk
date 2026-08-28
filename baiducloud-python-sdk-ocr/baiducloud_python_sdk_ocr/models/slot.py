"""
Slot information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.area import Area


class Slot(AbstractModel):
    """
    Slot
    """

    def __init__(self, slot_id=None, seqence=None, handwriting_area=None, correct_result=None, reason=None):
        """
        Initialize Slot instance.

        :param slot_id: 作答区ID
        :type slot_id: str (optional)

        :param seqence: 作答区序号，1：作答区1；2：作答区2；依此类推
        :type seqence: int (optional)

        :param handwriting_area: handwriting_area attribute
        :type handwriting_area: Area (optional)

        :param correct_result: 作答区批改结果，0：未批，1：正确，2：错误，3：未作答
        :type correct_result: int (optional)

        :param reason: 批改原因 / 错因描述，空表示无额外说明（当前口算题无错因分析内容）
        :type reason: str (optional)
        """
        super().__init__()
        self.slot_id = slot_id
        self.seqence = seqence
        self.handwriting_area = handwriting_area
        self.correct_result = correct_result
        self.reason = reason

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
        if self.slot_id is not None:
            result['slotId'] = self.slot_id
        if self.seqence is not None:
            result['seqence'] = self.seqence
        if self.handwriting_area is not None:
            result['handwritingArea'] = self.handwriting_area.to_dict()
        if self.correct_result is not None:
            result['correctResult'] = self.correct_result
        if self.reason is not None:
            result['reason'] = self.reason
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Slot

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('slotId') is not None:
            self.slot_id = m.get('slotId')
        if m.get('seqence') is not None:
            self.seqence = m.get('seqence')
        if m.get('handwritingArea') is not None:
            self.handwriting_area = Area().from_dict(m.get('handwritingArea'))
        if m.get('correctResult') is not None:
            self.correct_result = m.get('correctResult')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        return self
