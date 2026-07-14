"""
ScaleCondition information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ScaleCondition(AbstractModel):
    """
    ScaleCondition
    """

    def __init__(
        self,
        target_type=None,
        target_id=None,
        indicator=None,
        threshold=None,
        unit=None,
        comparison_operator=None,
        cron_time=None,
        trigger_time=None,
        type=None,
        period_type=None,
        period_value=None,
        alarm_rule=None,
    ):
        """
        Initialize ScaleCondition instance.

        :param target_type: 指标类型，如伸缩组指标为ASG
        :type target_type: str (optional)

        :param target_id: 报警监控实例，如伸缩组ID：asg-CClxxxxx
        :type target_id: str (optional)

        :param indicator: 监控指标。如伸缩组CPU使用率均值为CPUUsagePercent_Average
        :type indicator: str (optional)

        :param threshold: 阈值
        :type threshold: str (optional)

        :param unit: 单位
        :type unit: str (optional)

        :param comparison_operator: 比较运算符，支持'>'，'<'，'='
        :type comparison_operator: str (optional)

        :param cron_time: 定时规则或周期规则：当日执行时间。如12:30
        :type cron_time: str (optional)

        :param trigger_time: 不重复触发时间
        :type trigger_time: str (optional)

        :param type: 包括：CRONTAB(定时伸缩),ALARM(报警触发伸缩),PERIOD(周期伸缩)
        :type type: str (optional)

        :param period_type: 周期单位，可选值为DAY/WEEK/MONTH/CronExpression
        :type period_type: str (optional)

        :param period_value: 周期触发日期，1-7标识周1-周日，1-31表示1号到31号，与periodType相关
        :type period_value: int (optional)

        :param alarm_rule: 报警类规则
        :type alarm_rule: str (optional)
        """
        super().__init__()
        self.target_type = target_type
        self.target_id = target_id
        self.indicator = indicator
        self.threshold = threshold
        self.unit = unit
        self.comparison_operator = comparison_operator
        self.cron_time = cron_time
        self.trigger_time = trigger_time
        self.type = type
        self.period_type = period_type
        self.period_value = period_value
        self.alarm_rule = alarm_rule

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
        if self.target_type is not None:
            result['targetType'] = self.target_type
        if self.target_id is not None:
            result['targetId'] = self.target_id
        if self.indicator is not None:
            result['indicator'] = self.indicator
        if self.threshold is not None:
            result['threshold'] = self.threshold
        if self.unit is not None:
            result['unit'] = self.unit
        if self.comparison_operator is not None:
            result['comparisonOperator'] = self.comparison_operator
        if self.cron_time is not None:
            result['cronTime'] = self.cron_time
        if self.trigger_time is not None:
            result['triggerTime'] = self.trigger_time
        if self.type is not None:
            result['type'] = self.type
        if self.period_type is not None:
            result['periodType'] = self.period_type
        if self.period_value is not None:
            result['periodValue'] = self.period_value
        if self.alarm_rule is not None:
            result['alarmRule'] = self.alarm_rule
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ScaleCondition

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')
        if m.get('targetId') is not None:
            self.target_id = m.get('targetId')
        if m.get('indicator') is not None:
            self.indicator = m.get('indicator')
        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        if m.get('comparisonOperator') is not None:
            self.comparison_operator = m.get('comparisonOperator')
        if m.get('cronTime') is not None:
            self.cron_time = m.get('cronTime')
        if m.get('triggerTime') is not None:
            self.trigger_time = m.get('triggerTime')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('periodType') is not None:
            self.period_type = m.get('periodType')
        if m.get('periodValue') is not None:
            self.period_value = m.get('periodValue')
        if m.get('alarmRule') is not None:
            self.alarm_rule = m.get('alarmRule')
        return self
