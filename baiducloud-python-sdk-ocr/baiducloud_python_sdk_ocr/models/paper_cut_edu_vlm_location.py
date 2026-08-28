"""
PaperCutEduVlmLocation information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class PaperCutEduVlmLocation(AbstractModel):
    """
    PaperCutEduVlmLocation
    """

    def __init__(self, qus_location=None, pic_location=None, ans_location=None):
        """
        Initialize PaperCutEduVlmLocation instance.

        :param qus_location: 单道题位置信息，按照[x,y,w,h]方式返回，其中x,y为左上顶点坐标
        :type qus_location: List[float] (optional)

        :param pic_location: 图片的位置信息，按照[x,y,w,h]方式返回，其中x,y为左上顶点坐标
        :type pic_location: List[float] (optional)

        :param ans_location: 单道题内的手写内容位置信息，当only_split=false时不返回
        :type ans_location: List[float] (optional)
        """
        super().__init__()
        self.qus_location = qus_location
        self.pic_location = pic_location
        self.ans_location = ans_location

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
        if self.qus_location is not None:
            result['qus_location'] = self.qus_location
        if self.pic_location is not None:
            result['pic_location'] = self.pic_location
        if self.ans_location is not None:
            result['ans_location'] = self.ans_location
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PaperCutEduVlmLocation

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('qus_location') is not None:
            self.qus_location = m.get('qus_location')
        if m.get('pic_location') is not None:
            self.pic_location = m.get('pic_location')
        if m.get('ans_location') is not None:
            self.ans_location = m.get('ans_location')
        return self
