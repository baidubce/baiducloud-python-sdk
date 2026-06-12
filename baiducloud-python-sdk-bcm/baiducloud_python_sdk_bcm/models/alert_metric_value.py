"""
AlertMetricValue information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AlertMetricValue(AbstractModel):
    """
    AlertMetricValue
    """

    def __init__(self, name=None, label=None, value=None, unit=None):
        """
        Initialize AlertMetricValue instance.

        :param name: 指标名称
        :type name: str (optional)

        :param label: 指标显示名，根据locale自动切换中英文
        :type label: str (optional)

        :param value: 指标值
        :type value: float (optional)

        :param unit: 指标单位
        :type unit: str (optional)
        """
        super().__init__()
        self.name = name
        self.label = label
        self.value = value
        self.unit = unit

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
        if self.name is not None:
            result['name'] = self.name
        if self.label is not None:
            result['label'] = self.label
        if self.value is not None:
            result['value'] = self.value
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AlertMetricValue

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self
