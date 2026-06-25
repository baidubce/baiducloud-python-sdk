"""
Request entity for CreateAlertResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateAlertResponse(BceResponse):
    """
    CreateAlertResponse
    """

    def __init__(self, alert_id=None):
        """
        Initialize CreateAlertResponse response.

        :param alert_id: 告警规则ID
        :type alert_id: str (optional)
        """
        super().__init__()
        self.alert_id = alert_id

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.alert_id is not None:
            result['alertId'] = self.alert_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateAlertResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('alertId') is not None:
            self.alert_id = m.get('alertId')
        return self
