"""
ElemText information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ElemText(AbstractModel):
    """
    ElemText
    """

    def __init__(self, stem_text=None, subqus_text=None, answer_text=None, option_text=None, interpretation_text=None):
        """
        Initialize ElemText instance.

        :param stem_text: 题干文本信息
        :type stem_text: str (optional)

        :param subqus_text: 子题文本信息
        :type subqus_text: str (optional)

        :param answer_text: 答案文本信息
        :type answer_text: str (optional)

        :param option_text: 选项文本信息，仅在题目类型为选择题时输出
        :type option_text: str (optional)

        :param interpretation_text: 参考答案文本信息
        :type interpretation_text: str (optional)
        """
        super().__init__()
        self.stem_text = stem_text
        self.subqus_text = subqus_text
        self.answer_text = answer_text
        self.option_text = option_text
        self.interpretation_text = interpretation_text

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
        if self.stem_text is not None:
            result['stem_text'] = self.stem_text
        if self.subqus_text is not None:
            result['subqus_text'] = self.subqus_text
        if self.answer_text is not None:
            result['answer_text'] = self.answer_text
        if self.option_text is not None:
            result['option_text'] = self.option_text
        if self.interpretation_text is not None:
            result['interpretation_text'] = self.interpretation_text
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ElemText

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('stem_text') is not None:
            self.stem_text = m.get('stem_text')
        if m.get('subqus_text') is not None:
            self.subqus_text = m.get('subqus_text')
        if m.get('answer_text') is not None:
            self.answer_text = m.get('answer_text')
        if m.get('option_text') is not None:
            self.option_text = m.get('option_text')
        if m.get('interpretation_text') is not None:
            self.interpretation_text = m.get('interpretation_text')
        return self
