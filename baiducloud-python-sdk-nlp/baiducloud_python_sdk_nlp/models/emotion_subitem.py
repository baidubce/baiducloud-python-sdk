"""
EmotionSubitem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class EmotionSubitem(AbstractModel):
    """
    EmotionSubitem
    """

    def __init__(self, label=None, prob=None):
        """
        Initialize EmotionSubitem instance.

        :param label: label attribute
        :type label: str (optional)

        :param prob: 情绪二级分类标签对应的概率
        :type prob: float (optional)
        """
        super().__init__()
        self.label = label
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
        if self.label is not None:
            result['label'] = self.label
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
        :rtype: EmotionSubitem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('prob') is not None:
            self.prob = m.get('prob')
        return self
