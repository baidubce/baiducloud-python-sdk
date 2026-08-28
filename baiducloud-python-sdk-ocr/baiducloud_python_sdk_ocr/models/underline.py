"""
Underline information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.points import Points


class Underline(AbstractModel):
    """
    Underline
    """

    def __init__(self, points=None, prob=None):
        """
        Initialize Underline instance.

        :param points: points attribute
        :type points: Points (optional)

        :param prob: 下划线置信度，取值范围在[0，1]之间
        :type prob: float (optional)
        """
        super().__init__()
        self.points = points
        self.prob = prob

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
        if self.points is not None:
            result['points'] = self.points.to_dict()
        if self.prob is not None:
            result['prob'] = self.prob
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Underline

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('points') is not None:
            self.points = Points().from_dict(m.get('points'))
        if m.get('prob') is not None:
            self.prob = m.get('prob')
        return self
