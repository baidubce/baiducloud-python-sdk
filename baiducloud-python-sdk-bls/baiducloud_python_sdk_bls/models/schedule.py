"""
Schedule information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Schedule(AbstractModel):
    """
    Schedule
    """

    def __init__(self, interval_minute=None, fix_time_minute=None, day_of_week=None):
        """
        Initialize Schedule instance.

        :param interval_minute: 固定间隔，单位：分钟，取值范围[1, 1440]
        :type interval_minute: int (optional)

        :param fix_time_minute: 指定时刻，一天中的第几分钟，取值范围[0, 1440)
        :type fix_time_minute: int (optional)

        :param day_of_week: 固定时间频率; 0: 每天 1~7 一周的某天
        :type day_of_week: int (optional)
        """
        super().__init__()
        self.interval_minute = interval_minute
        self.fix_time_minute = fix_time_minute
        self.day_of_week = day_of_week

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
        if self.interval_minute is not None:
            result['intervalMinute'] = self.interval_minute
        if self.fix_time_minute is not None:
            result['fixTimeMinute'] = self.fix_time_minute
        if self.day_of_week is not None:
            result['dayOfWeek'] = self.day_of_week
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Schedule

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('intervalMinute') is not None:
            self.interval_minute = m.get('intervalMinute')
        if m.get('fixTimeMinute') is not None:
            self.fix_time_minute = m.get('fixTimeMinute')
        if m.get('dayOfWeek') is not None:
            self.day_of_week = m.get('dayOfWeek')
        return self
