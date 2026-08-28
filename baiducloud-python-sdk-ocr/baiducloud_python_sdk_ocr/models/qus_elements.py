"""
QusElements information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class QusElements(AbstractModel):
    """
    QusElements
    """

    def __init__(self, question_words=None, choices=None, qus_type=None, answer_words=None):
        """
        Initialize QusElements instance.

        :param question_words: 题目文本信息，当scene_type=paper时输出
        :type question_words: str (optional)

        :param choices: 选项文本信息，当qus_type为选择题时有值
        :type choices: List[str] (optional)

        :param qus_type: 题目类型，当scene_type=paper时输出
        :type qus_type: str (optional)

        :param answer_words: 手写作答信息
        :type answer_words: List[str] (optional)
        """
        super().__init__()
        self.question_words = question_words
        self.choices = choices
        self.qus_type = qus_type
        self.answer_words = answer_words

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
        if self.question_words is not None:
            result['question_words'] = self.question_words
        if self.choices is not None:
            result['choices'] = self.choices
        if self.qus_type is not None:
            result['qus_type'] = self.qus_type
        if self.answer_words is not None:
            result['answer_words'] = self.answer_words
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QusElements

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('question_words') is not None:
            self.question_words = m.get('question_words')
        if m.get('choices') is not None:
            self.choices = m.get('choices')
        if m.get('qus_type') is not None:
            self.qus_type = m.get('qus_type')
        if m.get('answer_words') is not None:
            self.answer_words = m.get('answer_words')
        return self
