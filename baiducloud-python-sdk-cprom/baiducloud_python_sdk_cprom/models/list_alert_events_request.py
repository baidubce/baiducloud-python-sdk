"""
Request entity for ListAlertEventsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListAlertEventsRequest(AbstractModel):
    """
    Request entity for ListAlertEventsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        start_time=None,
        end_time=None,
        page_no=None,
        page_size=None,
        monitor_instance_id=None,
        alerting_rule_id=None,
        alerting_rule_name=None,
        notify_rule_id=None,
        notify_rule_name=None,
        severity=None,
        status=None,
        expr=None,
        order_by=None,
        order=None,
        alarm_tags=None,
    ):
        """
        Initialize ListAlertEventsRequest request entity.

        :param start_time: start_time parameter
        :type start_time: int (optional)

        :param end_time: end_time parameter
        :type end_time: int (optional)

        :param page_no: page_no parameter
        :type page_no: int (optional)

        :param page_size: page_size parameter
        :type page_size: int (optional)

        :param monitor_instance_id: monitor_instance_id parameter
        :type monitor_instance_id: str (optional)

        :param alerting_rule_id: alerting_rule_id parameter
        :type alerting_rule_id: str (optional)

        :param alerting_rule_name: alerting_rule_name parameter
        :type alerting_rule_name: str (optional)

        :param notify_rule_id: notify_rule_id parameter
        :type notify_rule_id: str (optional)

        :param notify_rule_name: notify_rule_name parameter
        :type notify_rule_name: str (optional)

        :param severity: severity parameter
        :type severity: str (optional)

        :param status: status parameter
        :type status: str (optional)

        :param expr: expr parameter
        :type expr: str (optional)

        :param order_by: order_by parameter
        :type order_by: str (optional)

        :param order: order parameter
        :type order: str (optional)

        :param alarm_tags: alarm_tags parameter
        :type alarm_tags: str (optional)
        """
        super().__init__()
        self.start_time = start_time
        self.end_time = end_time
        self.page_no = page_no
        self.page_size = page_size
        self.monitor_instance_id = monitor_instance_id
        self.alerting_rule_id = alerting_rule_id
        self.alerting_rule_name = alerting_rule_name
        self.notify_rule_id = notify_rule_id
        self.notify_rule_name = notify_rule_name
        self.severity = severity
        self.status = status
        self.expr = expr
        self.order_by = order_by
        self.order = order
        self.alarm_tags = alarm_tags

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
        :rtype: ListAlertEventsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('monitorInstanceId') is not None:
            self.monitor_instance_id = m.get('monitorInstanceId')
        if m.get('alertingRuleId') is not None:
            self.alerting_rule_id = m.get('alertingRuleId')
        if m.get('alertingRuleName') is not None:
            self.alerting_rule_name = m.get('alertingRuleName')
        if m.get('notifyRuleId') is not None:
            self.notify_rule_id = m.get('notifyRuleId')
        if m.get('notifyRuleName') is not None:
            self.notify_rule_name = m.get('notifyRuleName')
        if m.get('severity') is not None:
            self.severity = m.get('severity')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('expr') is not None:
            self.expr = m.get('expr')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('alarmTags') is not None:
            self.alarm_tags = m.get('alarmTags')
        return self
