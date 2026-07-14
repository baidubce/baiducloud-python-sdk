"""
EipGroupBandwidth information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class EipGroupBandwidth(AbstractModel):
    """
    EipGroupBandwidth
    """

    def __init__(self, max=None, min=None, standard=None):
        """
        Initialize EipGroupBandwidth instance.

        :param max: 最大限制
        :type max: int (optional)

        :param min: 最小限制
        :type min: int (optional)

        :param standard: 标准值
        :type standard: int (optional)
        """
        super().__init__()
        self.max = max
        self.min = min
        self.standard = standard

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
        if self.max is not None:
            result['max'] = self.max
        if self.min is not None:
            result['min'] = self.min
        if self.standard is not None:
            result['standard'] = self.standard
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EipGroupBandwidth

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('max') is not None:
            self.max = m.get('max')
        if m.get('min') is not None:
            self.min = m.get('min')
        if m.get('standard') is not None:
            self.standard = m.get('standard')
        return self
