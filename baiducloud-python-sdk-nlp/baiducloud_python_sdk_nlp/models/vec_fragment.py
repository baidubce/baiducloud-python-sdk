"""
VecFragment information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class VecFragment(AbstractModel):
    """
    VecFragment
    """

    def __init__(self, ori_frag=None, correct_frag=None, begin_pos=None, end_pos=None):
        """
        Initialize VecFragment instance.

        :param ori_frag: 原片段
        :type ori_frag: str (optional)

        :param correct_frag: 替换片段
        :type correct_frag: str (optional)

        :param begin_pos: 片段起始
        :type begin_pos: int (optional)

        :param end_pos: 片段结尾
        :type end_pos: int (optional)
        """
        super().__init__()
        self.ori_frag = ori_frag
        self.correct_frag = correct_frag
        self.begin_pos = begin_pos
        self.end_pos = end_pos

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
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: VecFragment

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
        return self
