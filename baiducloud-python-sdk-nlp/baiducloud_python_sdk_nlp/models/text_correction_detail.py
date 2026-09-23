"""
TextCorrectionDetail information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_nlp.models.text_correction_vec_fragment import TextCorrectionVecFragment


class TextCorrectionDetail(AbstractModel):
    """
    TextCorrectionDetail
    """

    def __init__(
        self,
        sentence_id=None,
        sentence=None,
        sentence_fixed=None,
        vec_fragment=None,
        begin_sentence_offset=None,
        end_sentence_offset=None,
        begin_psent_cont_offset=None,
        end_psent_cont_offset=None,
    ):
        """
        Initialize TextCorrectionDetail instance.

        :param sentence_id: 子句id，子句为最细标点符号切割粒度
        :type sentence_id: int (optional)

        :param sentence: 原始子句文本
        :type sentence: str (optional)

        :param sentence_fixed: 纠正后的子句文本
        :type sentence_fixed: str (optional)

        :param vec_fragment: 替换候选片段信息
        :type vec_fragment: List[TextCorrectionVecFragment] (optional)

        :param begin_sentence_offset: 子句在content中的起始位置
        :type begin_sentence_offset: int (optional)

        :param end_sentence_offset: 子句在content中的结尾位置
        :type end_sentence_offset: int (optional)

        :param begin_psent_cont_offset: 子句所属句子在content中的起始位置
        :type begin_psent_cont_offset: int (optional)

        :param end_psent_cont_offset: 子句所属句子在content中的结尾位置
        :type end_psent_cont_offset: int (optional)
        """
        super().__init__()
        self.sentence_id = sentence_id
        self.sentence = sentence
        self.sentence_fixed = sentence_fixed
        self.vec_fragment = vec_fragment
        self.begin_sentence_offset = begin_sentence_offset
        self.end_sentence_offset = end_sentence_offset
        self.begin_psent_cont_offset = begin_psent_cont_offset
        self.end_psent_cont_offset = end_psent_cont_offset

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
        if self.sentence_id is not None:
            result['sentence_id'] = self.sentence_id
        if self.sentence is not None:
            result['sentence'] = self.sentence
        if self.sentence_fixed is not None:
            result['sentence_fixed'] = self.sentence_fixed
        if self.vec_fragment is not None:
            result['vec_fragment'] = [i.to_dict() for i in self.vec_fragment]
        if self.begin_sentence_offset is not None:
            result['begin_sentence_offset'] = self.begin_sentence_offset
        if self.end_sentence_offset is not None:
            result['end_sentence_offset'] = self.end_sentence_offset
        if self.begin_psent_cont_offset is not None:
            result['begin_psent_cont_offset'] = self.begin_psent_cont_offset
        if self.end_psent_cont_offset is not None:
            result['end_psent_cont_offset'] = self.end_psent_cont_offset
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TextCorrectionDetail

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('sentence_id') is not None:
            self.sentence_id = m.get('sentence_id')
        if m.get('sentence') is not None:
            self.sentence = m.get('sentence')
        if m.get('sentence_fixed') is not None:
            self.sentence_fixed = m.get('sentence_fixed')
        if m.get('vec_fragment') is not None:
            self.vec_fragment = [TextCorrectionVecFragment().from_dict(i) for i in m.get('vec_fragment')]
        if m.get('begin_sentence_offset') is not None:
            self.begin_sentence_offset = m.get('begin_sentence_offset')
        if m.get('end_sentence_offset') is not None:
            self.end_sentence_offset = m.get('end_sentence_offset')
        if m.get('begin_psent_cont_offset') is not None:
            self.begin_psent_cont_offset = m.get('begin_psent_cont_offset')
        if m.get('end_psent_cont_offset') is not None:
            self.end_psent_cont_offset = m.get('end_psent_cont_offset')
        return self
