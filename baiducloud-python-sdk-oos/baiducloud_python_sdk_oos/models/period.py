"""
Period information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Period(AbstractModel):
    """
    Period
    """

    def __init__(self, frequency=None, days_of_week=None, dates=None, last_date_of_month=None, hour=None, minute=None):
        """
        Initialize Period instance.

        :param frequency: 频率
        :type frequency: str (optional)

        :param days_of_week: 周几
        :type days_of_week: List[int] (optional)

        :param dates: 几号
        :type dates: List[int] (optional)

        :param last_date_of_month: 是否每月最后一天
        :type last_date_of_month: bool (optional)

        :param hour: 小时（0-23）
        :type hour: int (optional)

        :param minute: 分钟（0-59）
        :type minute: int (optional)
        """
        super().__init__()
        self.frequency = frequency
        self.days_of_week = days_of_week
        self.dates = dates
        self.last_date_of_month = last_date_of_month
        self.hour = hour
        self.minute = minute

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
        if self.frequency is not None:
            result['frequency'] = self.frequency
        if self.days_of_week is not None:
            result['daysOfWeek'] = self.days_of_week
        if self.dates is not None:
            result['dates'] = self.dates
        if self.last_date_of_month is not None:
            result['lastDateOfMonth'] = self.last_date_of_month
        if self.hour is not None:
            result['hour'] = self.hour
        if self.minute is not None:
            result['minute'] = self.minute
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Period

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('frequency') is not None:
            self.frequency = m.get('frequency')
        if m.get('daysOfWeek') is not None:
            self.days_of_week = m.get('daysOfWeek')
        if m.get('dates') is not None:
            self.dates = m.get('dates')
        if m.get('lastDateOfMonth') is not None:
            self.last_date_of_month = m.get('lastDateOfMonth')
        if m.get('hour') is not None:
            self.hour = m.get('hour')
        if m.get('minute') is not None:
            self.minute = m.get('minute')
        return self
