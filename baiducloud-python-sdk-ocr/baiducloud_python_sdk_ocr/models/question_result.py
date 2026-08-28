"""
QuestionResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.area import Area

from baiducloud_python_sdk_ocr.models.slot import Slot


class QuestionResult(AbstractModel):
    """
    QuestionResult
    """

    def __init__(
        self,
        correct_result=None,
        question_id=None,
        question=None,
        question_area=None,
        is_finish=None,
        seqence=None,
        type=None,
        crop_url=None,
        slot=None,
    ):
        """
        Initialize QuestionResult instance.

        :param correct_result: 批改结果，0：未批；1：正确；2：错误；3：未作答
        :type correct_result: int (optional)

        :param question_id: 题目ID
        :type question_id: str (optional)

        :param question: 题目内容，当前该字段不会返回内容
        :type question: str (optional)

        :param question_area: question_area attribute
        :type question_area: List[Area] (optional)

        :param is_finish: 是否完成批改。true：批改完成；false：批改未完成
        :type is_finish: bool (optional)

        :param seqence: 题目序号，0：题目1；1：题目2；依此类推
        :type seqence: int (optional)

        :param type: type attribute
        :type type: int (optional)

        :param crop_url: 批改后的题目图片url
        :type crop_url: str (optional)

        :param slot: 题目作答区批改结果数组，每个元素对应一个作答区
        :type slot: List[Slot] (optional)
        """
        super().__init__()
        self.correct_result = correct_result
        self.question_id = question_id
        self.question = question
        self.question_area = question_area
        self.is_finish = is_finish
        self.seqence = seqence
        self.type = type
        self.crop_url = crop_url
        self.slot = slot

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
        if self.correct_result is not None:
            result['correctResult'] = self.correct_result
        if self.question_id is not None:
            result['questionId'] = self.question_id
        if self.question is not None:
            result['question'] = self.question
        if self.question_area is not None:
            result['questionArea'] = [i.to_dict() for i in self.question_area]
        if self.is_finish is not None:
            result['isFinish'] = self.is_finish
        if self.seqence is not None:
            result['seqence'] = self.seqence
        if self.type is not None:
            result['type'] = self.type
        if self.crop_url is not None:
            result['cropUrl'] = self.crop_url
        if self.slot is not None:
            result['slot'] = [i.to_dict() for i in self.slot]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QuestionResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('correctResult') is not None:
            self.correct_result = m.get('correctResult')
        if m.get('questionId') is not None:
            self.question_id = m.get('questionId')
        if m.get('question') is not None:
            self.question = m.get('question')
        if m.get('questionArea') is not None:
            self.question_area = [Area().from_dict(i) for i in m.get('questionArea')]
        if m.get('isFinish') is not None:
            self.is_finish = m.get('isFinish')
        if m.get('seqence') is not None:
            self.seqence = m.get('seqence')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('cropUrl') is not None:
            self.crop_url = m.get('cropUrl')
        if m.get('slot') is not None:
            self.slot = [Slot().from_dict(i) for i in m.get('slot')]
        return self
