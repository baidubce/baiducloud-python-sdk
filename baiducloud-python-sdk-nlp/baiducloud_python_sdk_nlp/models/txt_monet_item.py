"""
TxtMonetItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TxtMonetItem(AbstractModel):
    """
    TxtMonetItem
    """

    def __init__(self, text=None, prob=None, start_offset=None, end_offset=None):
        """
        Initialize TxtMonetItem instance.

        :param text: 每个query的返回结果
        :type text: str (optional)

        :param prob: 返回结果的起始位置概率和结束位置概率的乘积
        :type prob: float (optional)

        :param start_offset: 返回结果的起始位置
        :type start_offset: int (optional)

        :param end_offset: 返回结果的结束位置
        :type end_offset: int (optional)
        """
        super().__init__()
        self.text = text
        self.prob = prob
        self.start_offset = start_offset
        self.end_offset = end_offset

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
        if self.text is not None:
            result['text'] = self.text
        if self.prob is not None:
            result['prob'] = self.prob
        if self.start_offset is not None:
            result['start_offset'] = self.start_offset
        if self.end_offset is not None:
            result['end_offset'] = self.end_offset
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TxtMonetItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('prob') is not None:
            self.prob = m.get('prob')
        if m.get('start_offset') is not None:
            self.start_offset = m.get('start_offset')
        if m.get('end_offset') is not None:
            self.end_offset = m.get('end_offset')
        return self
