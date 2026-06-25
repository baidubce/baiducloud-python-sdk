"""
Request entity for DeleteAlertRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteAlertRequest(AbstractModel):
    """
    Request entity for DeleteAlertRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, alerting_rule_id, instance_id):
        """
        Initialize DeleteAlertRequest request entity.

        :param alerting_rule_id: alerting_rule_id parameter
        :type alerting_rule_id: str (required)

        :param instance_id: instance_id parameter
        :type instance_id: str (required)
        """
        super().__init__()
        self.alerting_rule_id = alerting_rule_id
        self.instance_id = instance_id

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteAlertRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('alertingRuleId') is not None:
            self.alerting_rule_id = m.get('alertingRuleId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self
