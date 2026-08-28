"""
AccurateProbability information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AccurateProbability(AbstractModel):
    """
    AccurateProbability
    """

    def __init__(self, average=None, variance=None, min=None):
        """
        Initialize AccurateProbability instance.

        :param average: 行置信度平均值
        :type average: float (optional)

        :param variance: 行置信度方差
        :type variance: float (optional)

        :param min: 行置信度最小值
        :type min: float (optional)
        """
        super().__init__()
        self.average = average
        self.variance = variance
        self.min = min

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
        if self.average is not None:
            result['average'] = self.average
        if self.variance is not None:
            result['variance'] = self.variance
        if self.min is not None:
            result['min'] = self.min
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AccurateProbability

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('average') is not None:
            self.average = m.get('average')
        if m.get('variance') is not None:
            self.variance = m.get('variance')
        if m.get('min') is not None:
            self.min = m.get('min')
        return self
