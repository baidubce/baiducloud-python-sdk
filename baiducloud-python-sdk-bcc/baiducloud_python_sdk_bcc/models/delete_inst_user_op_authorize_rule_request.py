"""
Request entity for DeleteInstUserOpAuthorizeRuleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteInstUserOpAuthorizeRuleRequest(AbstractModel):
    """
    Request entity for DeleteInstUserOpAuthorizeRuleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, action, rule_id):
        """
        Initialize DeleteInstUserOpAuthorizeRuleRequest request entity.

        :param action: action parameter
        :type action: str (required)

        :param rule_id: 预授权规则ID，只有在禁用状态DISABLED的规则才可以删除
        :type rule_id: str (required)
        """
        super().__init__()
        self.action = action
        self.rule_id = rule_id

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
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteInstUserOpAuthorizeRuleRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        return self
