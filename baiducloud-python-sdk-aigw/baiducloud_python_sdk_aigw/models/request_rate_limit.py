"""
RequestRateLimit information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_aigw.models.rule_item import RuleItem


class RequestRateLimit(AbstractModel):
    """
    RequestRateLimit
    """

    def __init__(self, rule_name=None, enabled=None, rule_items=None):
        """
        Initialize RequestRateLimit instance.

        :param rule_name: 规则名称
        :type rule_name: str (optional)

        :param enabled: 是否启用
        :type enabled: bool (optional)

        :param rule_items: 请求次数限流规则；每项包含 match_condition 和 limit_config
        :type rule_items: List[RuleItem] (optional)
        """
        super().__init__()
        self.rule_name = rule_name
        self.enabled = enabled
        self.rule_items = rule_items

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
        if self.rule_name is not None:
            result['rule_name'] = self.rule_name
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.rule_items is not None:
            result['rule_items'] = [i.to_dict() for i in self.rule_items]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RequestRateLimit

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('rule_name') is not None:
            self.rule_name = m.get('rule_name')
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('rule_items') is not None:
            self.rule_items = [RuleItem().from_dict(i) for i in m.get('rule_items')]
        return self
