"""
AlertMetric information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcm.models.alert_metric_value import AlertMetricValue

from baiducloud_python_sdk_bcm.models.alert_metric_rule import AlertMetricRule


class AlertMetric(AbstractModel):
    """
    AlertMetric
    """

    def __init__(self, metric=None, rule=None):
        """
        Initialize AlertMetric instance.

        :param metric: metric attribute
        :type metric: AlertMetricValue (optional)

        :param rule: rule attribute
        :type rule: AlertMetricRule (optional)
        """
        super().__init__()
        self.metric = metric
        self.rule = rule

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
        if self.metric is not None:
            result['metric'] = self.metric.to_dict()
        if self.rule is not None:
            result['rule'] = self.rule.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AlertMetric

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('metric') is not None:
            self.metric = AlertMetricValue().from_dict(m.get('metric'))
        if m.get('rule') is not None:
            self.rule = AlertMetricRule().from_dict(m.get('rule'))
        return self
