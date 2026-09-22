"""
MaintainTime information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MaintainTime(AbstractModel):
    """
    MaintainTime
    """

    def __init__(self, start_time=None, duration=None, period=None):
        """
        Initialize MaintainTime instance.

        :param start_time: 开始时间
        :type start_time: str (optional)

        :param duration: 持续时间
        :type duration: int (optional)

        :param period: 时间周期。0代表周日，1-6分别代表周一到周六。
        :type period: List[str] (optional)
        """
        super().__init__()
        self.start_time = start_time
        self.duration = duration
        self.period = period

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
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.duration is not None:
            result['duration'] = self.duration
        if self.period is not None:
            result['period'] = self.period
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MaintainTime

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('period') is not None:
            self.period = m.get('period')
        return self
