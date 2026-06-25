"""
Request entity for ListAlertTemplatesResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_cprom.models.rule_template import RuleTemplate


class ListAlertTemplatesResponse(BceResponse):
    """
    ListAlertTemplatesResponse
    """

    def __init__(self, rule_templates=None):
        """
        Initialize ListAlertTemplatesResponse response.

        :param rule_templates: 告警模板列表
        :type rule_templates: List[RuleTemplate] (optional)
        """
        super().__init__()
        self.rule_templates = rule_templates

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
        if self.rule_templates is not None:
            result['ruleTemplates'] = [i.to_dict() for i in self.rule_templates]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListAlertTemplatesResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ruleTemplates') is not None:
            self.rule_templates = [RuleTemplate().from_dict(i) for i in m.get('ruleTemplates')]
        return self
