"""
Rule information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_as.models.as_alarm_rule import AsAlarmRule


class Rule(AbstractModel):
    """
    Rule
    """

    def __init__(
        self,
        rule_id=None,
        rule_name=None,
        group_id=None,
        account_id=None,
        state=None,
        type=None,
        cron_time=None,
        action_type=None,
        action_num=None,
        cooldown_in_sec=None,
        create_time=None,
        last_execution_time=None,
        last_schedule_time=None,
        period_start_time=None,
        period_end_time=None,
        period_type=None,
        period_value=None,
        as_alarm_rule=None,
    ):
        """
        Initialize Rule instance.

        :param rule_id: 规则ID
        :type rule_id: str (optional)

        :param rule_name: 规则名称
        :type rule_name: str (optional)

        :param group_id: 伸缩组ID
        :type group_id: str (optional)

        :param account_id: 用户ID
        :type account_id: str (optional)

        :param state: 规则的状态
        :type state: str (optional)

        :param type: 规则的类型
        :type type: str (optional)

        :param cron_time: 定时规则或周期规则：当日执行时间。如12:30。
        :type cron_time: str (optional)

        :param action_type: 动作类型。包括：INCREASE(扩容),DECREASE(缩容),ADJUST(调整至)
        :type action_type: str (optional)

        :param action_num: 动作数量
        :type action_num: int (optional)

        :param cooldown_in_sec: 冷却时间（秒）
        :type cooldown_in_sec: int (optional)

        :param create_time: 规则创建时间
        :type create_time: str (optional)

        :param last_execution_time: 规则最后修改时间
        :type last_execution_time: str (optional)

        :param last_schedule_time: 规则最后执行时间
        :type last_schedule_time: str (optional)

        :param period_start_time: 周期规则：周期有效期开始时间。如：2023-12-10T12:00:00Z
        :type period_start_time: str (optional)

        :param period_end_time: 周期规则：周期有效期结束时间。如：2023-12-11T12:00:00Z
        :type period_end_time: str (optional)

        :param period_type: 周期规则：周期单位，可选值为DAY/WEEK/MONTH/CronExpression
        :type period_type: str (optional)

        :param period_value: 周期规则：周期触发日期，1-7标识周1-周日，1-31表示1号到31号，与periodType相关
        :type period_value: int (optional)

        :param as_alarm_rule: as_alarm_rule attribute
        :type as_alarm_rule: AsAlarmRule (optional)
        """
        super().__init__()
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.group_id = group_id
        self.account_id = account_id
        self.state = state
        self.type = type
        self.cron_time = cron_time
        self.action_type = action_type
        self.action_num = action_num
        self.cooldown_in_sec = cooldown_in_sec
        self.create_time = create_time
        self.last_execution_time = last_execution_time
        self.last_schedule_time = last_schedule_time
        self.period_start_time = period_start_time
        self.period_end_time = period_end_time
        self.period_type = period_type
        self.period_value = period_value
        self.as_alarm_rule = as_alarm_rule

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
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.state is not None:
            result['state'] = self.state
        if self.type is not None:
            result['type'] = self.type
        if self.cron_time is not None:
            result['cronTime'] = self.cron_time
        if self.action_type is not None:
            result['actionType'] = self.action_type
        if self.action_num is not None:
            result['actionNum'] = self.action_num
        if self.cooldown_in_sec is not None:
            result['cooldownInSec'] = self.cooldown_in_sec
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.last_execution_time is not None:
            result['lastExecutionTime'] = self.last_execution_time
        if self.last_schedule_time is not None:
            result['lastScheduleTime'] = self.last_schedule_time
        if self.period_start_time is not None:
            result['periodStartTime'] = self.period_start_time
        if self.period_end_time is not None:
            result['periodEndTime'] = self.period_end_time
        if self.period_type is not None:
            result['periodType'] = self.period_type
        if self.period_value is not None:
            result['periodValue'] = self.period_value
        if self.as_alarm_rule is not None:
            result['asAlarmRule'] = self.as_alarm_rule.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Rule

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('cronTime') is not None:
            self.cron_time = m.get('cronTime')
        if m.get('actionType') is not None:
            self.action_type = m.get('actionType')
        if m.get('actionNum') is not None:
            self.action_num = m.get('actionNum')
        if m.get('cooldownInSec') is not None:
            self.cooldown_in_sec = m.get('cooldownInSec')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('lastExecutionTime') is not None:
            self.last_execution_time = m.get('lastExecutionTime')
        if m.get('lastScheduleTime') is not None:
            self.last_schedule_time = m.get('lastScheduleTime')
        if m.get('periodStartTime') is not None:
            self.period_start_time = m.get('periodStartTime')
        if m.get('periodEndTime') is not None:
            self.period_end_time = m.get('periodEndTime')
        if m.get('periodType') is not None:
            self.period_type = m.get('periodType')
        if m.get('periodValue') is not None:
            self.period_value = m.get('periodValue')
        if m.get('asAlarmRule') is not None:
            self.as_alarm_rule = AsAlarmRule().from_dict(m.get('asAlarmRule'))
        return self
