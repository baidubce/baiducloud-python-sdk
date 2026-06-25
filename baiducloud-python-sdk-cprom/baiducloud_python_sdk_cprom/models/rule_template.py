"""
RuleTemplate information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RuleTemplate(AbstractModel):
    """
    RuleTemplate
    """

    def __init__(self, alert_name=None, expr=None, cprom_for=None, description=None):
        """
        Initialize RuleTemplate instance.

        :param alert_name: 告警名称
        :type alert_name: str (optional)

        :param expr: 告警规则，promQL查询语句
        :type expr: str (optional)

        :param cprom_for: 告警持续时间
        :type cprom_for: str (optional)

        :param description: 告警内容
        :type description: str (optional)
        """
        super().__init__()
        self.alert_name = alert_name
        self.expr = expr
        self.cprom_for = cprom_for
        self.description = description

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
        if self.alert_name is not None:
            result['alertName'] = self.alert_name
        if self.expr is not None:
            result['expr'] = self.expr
        if self.cprom_for is not None:
            result['for'] = self.cprom_for
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RuleTemplate

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('alertName') is not None:
            self.alert_name = m.get('alertName')
        if m.get('expr') is not None:
            self.expr = m.get('expr')
        if m.get('for') is not None:
            self.cprom_for = m.get('for')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
