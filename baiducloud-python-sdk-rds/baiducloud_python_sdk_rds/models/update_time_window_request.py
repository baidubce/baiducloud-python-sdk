"""
Request entity for UpdateTimeWindowRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateTimeWindowRequest(AbstractModel):
    """
    Request entity for UpdateTimeWindowRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, maintain_start_time, maintain_duration):
        """
        Initialize UpdateTimeWindowRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param maintain_start_time: 实例维护时间窗口的开始时间，local时间，如17:00:00
        :type maintain_start_time: str (required)

        :param maintain_duration: 实例维护时间窗口的持续时间，单位是小时，如：1；每1个小时为一个时间段，开始时间+持续时间不可跨天
        :type maintain_duration: int (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.maintain_start_time = maintain_start_time
        self.maintain_duration = maintain_duration

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
        if self.maintain_start_time is not None:
            result['maintainStartTime'] = self.maintain_start_time
        if self.maintain_duration is not None:
            result['maintainDuration'] = self.maintain_duration
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateTimeWindowRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('maintainStartTime') is not None:
            self.maintain_start_time = m.get('maintainStartTime')
        if m.get('maintainDuration') is not None:
            self.maintain_duration = m.get('maintainDuration')
        return self
