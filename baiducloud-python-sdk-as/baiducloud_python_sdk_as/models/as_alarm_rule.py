"""
AsAlarmRule information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_as.models.monitor_object import MonitorObject


class AsAlarmRule(AbstractModel):
    """
    AsAlarmRule
    """

    def __init__(
        self,
        id=None,
        scope=None,
        monitor_object=None,
        rules=None,
        alarm_name=None,
        alias_name=None,
        insufficient_cycle=None,
        policy_enabled=None,
        rule_contents=None,
        rule_contents_en=None,
        source=None,
        component_type=None,
        alarm_actions=None,
        ok_actions=None,
        insufficient_actions=None,
    ):
        """
        Initialize AsAlarmRule instance.

        :param id: 策略ID
        :type id: int (optional)

        :param scope: 策略归属产品
        :type scope: str (optional)

        :param monitor_object: monitor_object attribute
        :type monitor_object: MonitorObject (optional)

        :param rules: 创建伸缩组的规则时，传入具体的判断规则，支持且规则、或规则。
        :type rules: List[List[AlarmRule]] (optional)

        :param alarm_name: BCM策略ID，使用BCM已有策略时候，传入对应策略的唯一id
        :type alarm_name: str (optional)

        :param alias_name: BCM策略别名
        :type alias_name: str (optional)

        :param insufficient_cycle: 无数据状态触发的持续时间，单位s
        :type insufficient_cycle: int (optional)

        :param policy_enabled: 策略状态
        :type policy_enabled: bool (optional)

        :param rule_contents: 报警规则的内容描述
        :type rule_contents: List[str] (optional)

        :param rule_contents_en: 报警规则的英文描述
        :type rule_contents_en: List[str] (optional)

        :param source: 报警策略创建来源
        :type source: str (optional)

        :param component_type: 表示报警策略来自于哪个业务组件
        :type component_type: str (optional)

        :param alarm_actions: 报警动作
        :type alarm_actions: List[str] (optional)

        :param ok_actions: 当报警恢复时执行的动作列表
        :type ok_actions: List[str] (optional)

        :param insufficient_actions: 当数据不足时执行的动作列表
        :type insufficient_actions: List[str] (optional)
        """
        super().__init__()
        self.id = id
        self.scope = scope
        self.monitor_object = monitor_object
        self.rules = rules
        self.alarm_name = alarm_name
        self.alias_name = alias_name
        self.insufficient_cycle = insufficient_cycle
        self.policy_enabled = policy_enabled
        self.rule_contents = rule_contents
        self.rule_contents_en = rule_contents_en
        self.source = source
        self.component_type = component_type
        self.alarm_actions = alarm_actions
        self.ok_actions = ok_actions
        self.insufficient_actions = insufficient_actions

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
        if self.id is not None:
            result['id'] = self.id
        if self.scope is not None:
            result['scope'] = self.scope
        if self.monitor_object is not None:
            result['monitorObject'] = self.monitor_object.to_dict()
        if self.rules is not None:
            result['rules'] = self.rules
        if self.alarm_name is not None:
            result['alarmName'] = self.alarm_name
        if self.alias_name is not None:
            result['aliasName'] = self.alias_name
        if self.insufficient_cycle is not None:
            result['insufficientCycle'] = self.insufficient_cycle
        if self.policy_enabled is not None:
            result['policyEnabled'] = self.policy_enabled
        if self.rule_contents is not None:
            result['ruleContents'] = self.rule_contents
        if self.rule_contents_en is not None:
            result['ruleContentsEn'] = self.rule_contents_en
        if self.source is not None:
            result['source'] = self.source
        if self.component_type is not None:
            result['componentType'] = self.component_type
        if self.alarm_actions is not None:
            result['alarmActions'] = self.alarm_actions
        if self.ok_actions is not None:
            result['okActions'] = self.ok_actions
        if self.insufficient_actions is not None:
            result['insufficientActions'] = self.insufficient_actions
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AsAlarmRule

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('monitorObject') is not None:
            self.monitor_object = MonitorObject().from_dict(m.get('monitorObject'))
        if m.get('rules') is not None:
            self.rules = m.get('rules')
        if m.get('alarmName') is not None:
            self.alarm_name = m.get('alarmName')
        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')
        if m.get('insufficientCycle') is not None:
            self.insufficient_cycle = m.get('insufficientCycle')
        if m.get('policyEnabled') is not None:
            self.policy_enabled = m.get('policyEnabled')
        if m.get('ruleContents') is not None:
            self.rule_contents = m.get('ruleContents')
        if m.get('ruleContentsEn') is not None:
            self.rule_contents_en = m.get('ruleContentsEn')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('componentType') is not None:
            self.component_type = m.get('componentType')
        if m.get('alarmActions') is not None:
            self.alarm_actions = m.get('alarmActions')
        if m.get('okActions') is not None:
            self.ok_actions = m.get('okActions')
        if m.get('insufficientActions') is not None:
            self.insufficient_actions = m.get('insufficientActions')
        return self
