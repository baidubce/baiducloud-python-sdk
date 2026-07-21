"""
Request entity for CreateRuleV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_as.models.as_alarm_rule import AsAlarmRule


class CreateRuleV2Request(AbstractModel):
    """
    Request entity for CreateRuleV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        rule_name,
        group_id,
        state,
        type,
        action_type,
        action_num,
        cooldown_in_sec,
        cron_time=None,
        period_type=None,
        period_value=None,
        period_start_time=None,
        period_end_time=None,
        as_alarm_rule=None,
    ):
        """
        Initialize CreateRuleV2Request request entity.

        :param rule_name: 规则名称
        :type rule_name: str (required)

        :param group_id: 伸缩组id
        :type group_id: str (required)

        :param state: 创建后的规则状态。包括：ENABLE(启用),DISABLE(禁用)
        :type state: str (required)

        :param type: 规则类型。包括：CRONTAB(定时伸缩),ALARM(报警触发伸缩),PERIOD(周期伸缩)
        :type type: str (required)

        :param action_type: 动作类型。包括：INCREASE(扩容),DECREASE(缩容),ADJUST(调整至)
        :type action_type: str (required)

        :param action_num: 动作数量
        :type action_num: int (required)

        :param cron_time: 定时规则或周期规则：当日执行时间。如12:30。
        :type cron_time: str (optional)

        :param cooldown_in_sec: 冷却时间（秒）
        :type cooldown_in_sec: int (required)

        :param period_type: 周期规则：周期单位，可选值为DAY/WEEK/MONTH/CronExpression
        :type period_type: str (optional)

        :param period_value: 周期规则：周期触发日期，1-7标识周1-周日，1-31表示1号到31号，与periodType相关
        :type period_value: int (optional)

        :param period_start_time: 周期规则：周期有效期开始时间。如：2023-12-10T12:00:00Z
        :type period_start_time: str (optional)

        :param period_end_time: 周期规则：周期有效期结束时间。如：2023-12-11T12:00:00Z
        :type period_end_time: str (optional)

        :param as_alarm_rule: as_alarm_rule parameter
        :type as_alarm_rule: AsAlarmRule (optional)
        """
        super().__init__()
        self.rule_name = rule_name
        self.group_id = group_id
        self.state = state
        self.type = type
        self.action_type = action_type
        self.action_num = action_num
        self.cron_time = cron_time
        self.cooldown_in_sec = cooldown_in_sec
        self.period_type = period_type
        self.period_value = period_value
        self.period_start_time = period_start_time
        self.period_end_time = period_end_time
        self.as_alarm_rule = as_alarm_rule

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
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.state is not None:
            result['state'] = self.state
        if self.type is not None:
            result['type'] = self.type
        if self.action_type is not None:
            result['actionType'] = self.action_type
        if self.action_num is not None:
            result['actionNum'] = self.action_num
        if self.cron_time is not None:
            result['cronTime'] = self.cron_time
        if self.cooldown_in_sec is not None:
            result['cooldownInSec'] = self.cooldown_in_sec
        if self.period_type is not None:
            result['periodType'] = self.period_type
        if self.period_value is not None:
            result['periodValue'] = self.period_value
        if self.period_start_time is not None:
            result['periodStartTime'] = self.period_start_time
        if self.period_end_time is not None:
            result['periodEndTime'] = self.period_end_time
        if self.as_alarm_rule is not None:
            result['asAlarmRule'] = self.as_alarm_rule.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateRuleV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('actionType') is not None:
            self.action_type = m.get('actionType')
        if m.get('actionNum') is not None:
            self.action_num = m.get('actionNum')
        if m.get('cronTime') is not None:
            self.cron_time = m.get('cronTime')
        if m.get('cooldownInSec') is not None:
            self.cooldown_in_sec = m.get('cooldownInSec')
        if m.get('periodType') is not None:
            self.period_type = m.get('periodType')
        if m.get('periodValue') is not None:
            self.period_value = m.get('periodValue')
        if m.get('periodStartTime') is not None:
            self.period_start_time = m.get('periodStartTime')
        if m.get('periodEndTime') is not None:
            self.period_end_time = m.get('periodEndTime')
        if m.get('asAlarmRule') is not None:
            self.as_alarm_rule = AsAlarmRule().from_dict(m.get('asAlarmRule'))
        return self
