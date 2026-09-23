"""
TextCorrectionVecFragment information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TextCorrectionVecFragment(AbstractModel):
    """
    TextCorrectionVecFragment
    """

    def __init__(
        self,
        ori_frag=None,
        correct_frag=None,
        begin_pos=None,
        end_pos=None,
        explain=None,
        explain_long=None,
        explain_structure=None,
        operation=None,
        label=None,
        score=None,
    ):
        """
        Initialize TextCorrectionVecFragment instance.

        :param ori_frag: 原片段
        :type ori_frag: str (optional)

        :param correct_frag: 替换片段
        :type correct_frag: str (optional)

        :param begin_pos: 片段起始
        :type begin_pos: int (optional)

        :param end_pos: 片段结尾
        :type end_pos: int (optional)

        :param explain: 纠错释义
        :type explain: str (optional)

        :param explain_long: 详细的释义信息，说明常用字/词纠错的具体原因
        :type explain_long: str (optional)

        :param explain_structure: 涉政相关的结构化释义信息
        :type explain_structure: str (optional)

        :param operation: 建议操作类型，0:检查，1:交换，2:替换，3:插入，4:删除
        :type operation: int (optional)

        :param label: label attribute
        :type label: str (optional)

        :param score: 模型置信度打分
        :type score: float (optional)
        """
        super().__init__()
        self.ori_frag = ori_frag
        self.correct_frag = correct_frag
        self.begin_pos = begin_pos
        self.end_pos = end_pos
        self.explain = explain
        self.explain_long = explain_long
        self.explain_structure = explain_structure
        self.operation = operation
        self.label = label
        self.score = score

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
        if self.ori_frag is not None:
            result['ori_frag'] = self.ori_frag
        if self.correct_frag is not None:
            result['correct_frag'] = self.correct_frag
        if self.begin_pos is not None:
            result['begin_pos'] = self.begin_pos
        if self.end_pos is not None:
            result['end_pos'] = self.end_pos
        if self.explain is not None:
            result['explain'] = self.explain
        if self.explain_long is not None:
            result['explain_long'] = self.explain_long
        if self.explain_structure is not None:
            result['explain_structure'] = self.explain_structure
        if self.operation is not None:
            result['operation'] = self.operation
        if self.label is not None:
            result['label'] = self.label
        if self.score is not None:
            result['score'] = self.score
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TextCorrectionVecFragment

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ori_frag') is not None:
            self.ori_frag = m.get('ori_frag')
        if m.get('correct_frag') is not None:
            self.correct_frag = m.get('correct_frag')
        if m.get('begin_pos') is not None:
            self.begin_pos = m.get('begin_pos')
        if m.get('end_pos') is not None:
            self.end_pos = m.get('end_pos')
        if m.get('explain') is not None:
            self.explain = m.get('explain')
        if m.get('explain_long') is not None:
            self.explain_long = m.get('explain_long')
        if m.get('explain_structure') is not None:
            self.explain_structure = m.get('explain_structure')
        if m.get('operation') is not None:
            self.operation = m.get('operation')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('score') is not None:
            self.score = m.get('score')
        return self
