"""
AlarmRule information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AlarmRule(AbstractModel):
    """
    AlarmRule
    """

    def __init__(
        self,
        operator=None,
        rules=None,
        metric=None,
        window_in_seconds=None,
        aggregate=None,
        display_value=None,
        display_unit=None,
    ):
        """
        Initialize AlarmRule instance.

        :param operator: 逻辑运算符，可选项：`and` - 且，`or` - 或。作为逻辑组合节点时必填
        :type operator: str (optional)

        :param rules: 子规则列表，当operator为and/or时必填
        :type rules: List[AlarmRule] (optional)

        :param metric: 指标名，作为叶子节点（指标表达式）时必填
        :type metric: str (optional)

        :param window_in_seconds: 聚合窗口，单位：秒，不可小于60
        :type window_in_seconds: int (optional)

        :param aggregate: aggregate attribute
        :type aggregate: str (optional)

        :param display_value: 阈值（显示值）
        :type display_value: float (optional)

        :param display_unit: 阈值单位
        :type display_unit: str (optional)
        """
        super().__init__()
        self.operator = operator
        self.rules = rules
        self.metric = metric
        self.window_in_seconds = window_in_seconds
        self.aggregate = aggregate
        self.display_value = display_value
        self.display_unit = display_unit

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
        if self.operator is not None:
            result['operator'] = self.operator
        if self.rules is not None:
            result['rules'] = [i.to_dict() for i in self.rules]
        if self.metric is not None:
            result['metric'] = self.metric
        if self.window_in_seconds is not None:
            result['windowInSeconds'] = self.window_in_seconds
        if self.aggregate is not None:
            result['aggregate'] = self.aggregate
        if self.display_value is not None:
            result['displayValue'] = self.display_value
        if self.display_unit is not None:
            result['displayUnit'] = self.display_unit
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AlarmRule

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('rules') is not None:
            self.rules = [AlarmRule().from_dict(i) for i in m.get('rules')]
        if m.get('metric') is not None:
            self.metric = m.get('metric')
        if m.get('windowInSeconds') is not None:
            self.window_in_seconds = m.get('windowInSeconds')
        if m.get('aggregate') is not None:
            self.aggregate = m.get('aggregate')
        if m.get('displayValue') is not None:
            self.display_value = m.get('displayValue')
        if m.get('displayUnit') is not None:
            self.display_unit = m.get('displayUnit')
        return self
