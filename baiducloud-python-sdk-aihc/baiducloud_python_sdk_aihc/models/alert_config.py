"""
AlertConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AlertConfig(AbstractModel):
    """
    AlertConfig
    """

    def __init__(self, instance_id=None, alert_items=None, aihc_for=None, notify_rule_id=None):
        """
        Initialize AlertConfig instance.

        :param instance_id: 是
        :type instance_id: str (optional)

        :param alert_items: 是
        :type alert_items: List[str] (optional)

        :param aihc_for: 否
        :type aihc_for: str (optional)

        :param notify_rule_id: 是
        :type notify_rule_id: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.alert_items = alert_items
        self.aihc_for = aihc_for
        self.notify_rule_id = notify_rule_id

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.alert_items is not None:
            result['alertItems'] = self.alert_items
        if self.aihc_for is not None:
            result['for'] = self.aihc_for
        if self.notify_rule_id is not None:
            result['notifyRuleId'] = self.notify_rule_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AlertConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('alertItems') is not None:
            self.alert_items = m.get('alertItems')
        if m.get('for') is not None:
            self.aihc_for = m.get('for')
        if m.get('notifyRuleId') is not None:
            self.notify_rule_id = m.get('notifyRuleId')
        return self
