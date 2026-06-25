"""
Request entity for CreateAlertRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateAlertRequest(AbstractModel):
    """
    Request entity for CreateAlertRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        instance_id,
        alert_name,
        expr,
        cprom_for,
        description,
        notify_rule_id,
        enable=None,
        severity=None,
        labels=None,
        annotations=None,
    ):
        """
        Initialize CreateAlertRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param alert_name: 告警名称
        :type alert_name: str (required)

        :param expr: 告警规则，promQL查询语句
        :type expr: str (required)

        :param cprom_for: 告警持续时间
        :type cprom_for: str (required)

        :param description: 告警内容
        :type description: str (required)

        :param notify_rule_id: 通知策略ID
        :type notify_rule_id: str (required)

        :param enable: 是否开启告警，创建时默认为true
        :type enable: bool (optional)

        :param severity: 告警级别，notice/warning/major/critical
        :type severity: str (optional)

        :param labels: 自定义label键值对
        :type labels: Dict[str, str] (optional)

        :param annotations: 自定义注解键值对
        :type annotations: Dict[str, str] (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.alert_name = alert_name
        self.expr = expr
        self.cprom_for = cprom_for
        self.description = description
        self.notify_rule_id = notify_rule_id
        self.enable = enable
        self.severity = severity
        self.labels = labels
        self.annotations = annotations

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
        if self.alert_name is not None:
            result['alertName'] = self.alert_name
        if self.expr is not None:
            result['expr'] = self.expr
        if self.cprom_for is not None:
            result['for'] = self.cprom_for
        if self.description is not None:
            result['description'] = self.description
        if self.notify_rule_id is not None:
            result['notifyRuleId'] = self.notify_rule_id
        if self.enable is not None:
            result['enable'] = self.enable
        if self.severity is not None:
            result['severity'] = self.severity
        if self.labels is not None:
            result['labels'] = self.labels
        if self.annotations is not None:
            result['annotations'] = self.annotations
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateAlertRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('alertName') is not None:
            self.alert_name = m.get('alertName')
        if m.get('expr') is not None:
            self.expr = m.get('expr')
        if m.get('for') is not None:
            self.cprom_for = m.get('for')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('notifyRuleId') is not None:
            self.notify_rule_id = m.get('notifyRuleId')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('severity') is not None:
            self.severity = m.get('severity')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        return self
