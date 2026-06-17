"""
Request entity for ModifyInstUserOpAuthorizeRuleAttributeRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModifyInstUserOpAuthorizeRuleAttributeRequest(AbstractModel):
    """
    Request entity for ModifyInstUserOpAuthorizeRuleAttributeRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, action, rule_id, enable_rule=None, authorize_maintenance_operations=None, rule_name=None):
        """
        Initialize ModifyInstUserOpAuthorizeRuleAttributeRequest request entity.

        :param action: action parameter
        :type action: str (required)

        :param enable_rule: 是否启用立即启用预授权，默认为1，开启
        :type enable_rule: int (optional)

        :param authorize_maintenance_operations: 预授权方法（Repair / Reboot / TamAuthorize）
        :type authorize_maintenance_operations: List[str] (optional)

        :param rule_name: 规则名称
        :type rule_name: str (optional)

        :param rule_id: 规则ID
        :type rule_id: str (required)
        """
        super().__init__()
        self.action = action
        self.enable_rule = enable_rule
        self.authorize_maintenance_operations = authorize_maintenance_operations
        self.rule_name = rule_name
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
        if self.enable_rule is not None:
            result['enableRule'] = self.enable_rule
        if self.authorize_maintenance_operations is not None:
            result['authorizeMaintenanceOperations'] = self.authorize_maintenance_operations
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
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
        :rtype: ModifyInstUserOpAuthorizeRuleAttributeRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('enableRule') is not None:
            self.enable_rule = m.get('enableRule')
        if m.get('authorizeMaintenanceOperations') is not None:
            self.authorize_maintenance_operations = m.get('authorizeMaintenanceOperations')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        return self
