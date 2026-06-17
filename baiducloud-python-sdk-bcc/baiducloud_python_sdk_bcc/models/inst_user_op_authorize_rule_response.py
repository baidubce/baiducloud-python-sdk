"""
InstUserOpAuthorizeRuleResponse information
"""

from baiducloud_python_sdk_core.bce_response import BceResponse

from baiducloud_python_sdk_bcc.models.tag_model import TagModel


class InstUserOpAuthorizeRuleResponse(BceResponse):
    """
    InstUserOpAuthorizeRuleResponse
    """

    def __init__(
        self,
        rule_id=None,
        rule_name=None,
        server_event_category=None,
        effective_scope=None,
        status=None,
        tags=None,
        authorize_maintenance_operations=None,
        create_time=None,
    ):
        """
        Initialize InstUserOpAuthorizeRuleResponse instance.

        :param rule_id: 规则ID（获取授权规则列表接口返回）
        :type rule_id: str (optional)

        :param rule_name: 规则名称（获取授权规则列表接口返回）
        :type rule_name: str (optional)

        :param server_event_category: server_event_category attribute
        :type server_event_category: str (optional)

        :param effective_scope: 规则关联的范围（获取授权规则列表接口返回）
        :type effective_scope: str (optional)

        :param status: 规则状态（ DISABLED / ENABLED）（获取授权规则列表接口返回）
        :type status: str (optional)

        :param tags: 标签（获取授权规则列表接口返回）
        :type tags: List[TagModel] (optional)

        :param authorize_maintenance_operations: 授权方法（TamAuthorize / Repair / Reboot）（获取授权规则列表接口返回）
        :type authorize_maintenance_operations: List[str] (optional)

        :param create_time: 创建时间，符合BCE规范的日期格式（获取授权规则列表接口返回）
        :type create_time: str (optional)
        """
        super().__init__()
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.server_event_category = server_event_category
        self.effective_scope = effective_scope
        self.status = status
        self.tags = tags
        self.authorize_maintenance_operations = authorize_maintenance_operations
        self.create_time = create_time

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        Includes metadata from the parent BceResponse class.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.server_event_category is not None:
            result['serverEventCategory'] = self.server_event_category
        if self.effective_scope is not None:
            result['effectiveScope'] = self.effective_scope
        if self.status is not None:
            result['status'] = self.status
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.authorize_maintenance_operations is not None:
            result['authorizeMaintenanceOperations'] = self.authorize_maintenance_operations
        if self.create_time is not None:
            result['createTime'] = self.create_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InstUserOpAuthorizeRuleResponse

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('serverEventCategory') is not None:
            self.server_event_category = m.get('serverEventCategory')
        if m.get('effectiveScope') is not None:
            self.effective_scope = m.get('effectiveScope')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        if m.get('authorizeMaintenanceOperations') is not None:
            self.authorize_maintenance_operations = m.get('authorizeMaintenanceOperations')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        return self
