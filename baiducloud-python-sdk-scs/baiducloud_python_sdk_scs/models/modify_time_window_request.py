"""
Request entity for ModifyTimeWindowRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModifyTimeWindowRequest(AbstractModel):
    """
    Request entity for ModifyTimeWindowRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, start_time, duration, period):
        """
        Initialize ModifyTimeWindowRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param start_time: 开始时间。示例：04:00（即凌晨4点）
        :type start_time: str (required)

        :param duration: 持续时间。取值范围：1-8（单位：小时）
        :type duration: int (required)

        :param period: 维护周期。1-6分别代表周一到周六。0代表周日。
        :type period: List[int] (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.start_time = start_time
        self.duration = duration
        self.period = period

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
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.duration is not None:
            result['duration'] = self.duration
        if self.period is not None:
            result['period'] = self.period
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyTimeWindowRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('period') is not None:
            self.period = m.get('period')
        return self
