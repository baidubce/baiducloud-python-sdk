"""
CardQuality information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CardQuality(AbstractModel):
    """
    CardQuality
    """

    def __init__(self, is_clear=None, is_clear_probability=None, is_complete=None, is_complete_probability=None):
        """
        Initialize CardQuality instance.

        :param is_clear: 是否清晰
        :type is_clear: int (optional)

        :param is_clear_probability: 清晰度概率
        :type is_clear_probability: float (optional)

        :param is_complete: 是否边框完整
        :type is_complete: int (optional)

        :param is_complete_probability: 完整度概率
        :type is_complete_probability: float (optional)
        """
        super().__init__()
        self.is_clear = is_clear
        self.is_clear_probability = is_clear_probability
        self.is_complete = is_complete
        self.is_complete_probability = is_complete_probability

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
        if self.is_clear is not None:
            result['IsClear'] = self.is_clear
        if self.is_clear_probability is not None:
            result['IsClear_probability'] = self.is_clear_probability
        if self.is_complete is not None:
            result['IsComplete'] = self.is_complete
        if self.is_complete_probability is not None:
            result['IsComplete_probability'] = self.is_complete_probability
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CardQuality

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('IsClear') is not None:
            self.is_clear = m.get('IsClear')
        if m.get('IsClear_probability') is not None:
            self.is_clear_probability = m.get('IsClear_probability')
        if m.get('IsComplete') is not None:
            self.is_complete = m.get('IsComplete')
        if m.get('IsComplete_probability') is not None:
            self.is_complete_probability = m.get('IsComplete_probability')
        return self
