"""
Request entity for CreateAuthorizationRuleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateAuthorizationRuleRequest(AbstractModel):
    """
    Request entity for CreateAuthorizationRuleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, action, authorize_maintenance_operations, rule_name, server_event_category, enable_rule=None):
        """
        Initialize CreateAuthorizationRuleRequest request entity.

        :param action: action parameter
        :type action: str (required)

        :param enable_rule: 是否启用立即启用预授权，默认为1，开启
        :type enable_rule: int (optional)

        :param authorize_maintenance_operations: 预授权方法（Repair / Reboot / TamAuthorize）
        :type authorize_maintenance_operations: List[str] (required)

        :param rule_name: 规则名称
        :type rule_name: str (required)

        :param server_event_category: server_event_category parameter
        :type server_event_category: str (required)
        """
        super().__init__()
        self.action = action
        self.enable_rule = enable_rule
        self.authorize_maintenance_operations = authorize_maintenance_operations
        self.rule_name = rule_name
        self.server_event_category = server_event_category

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
        if self.server_event_category is not None:
            result['serverEventCategory'] = self.server_event_category
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateAuthorizationRuleRequest

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
        if m.get('serverEventCategory') is not None:
            self.server_event_category = m.get('serverEventCategory')
        return self
