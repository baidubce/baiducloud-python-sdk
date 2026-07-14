"""
HealthCheckConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class HealthCheckConfig(AbstractModel):
    """
    HealthCheckConfig
    """

    def __init__(self, health_check_interval=None, grace_time=None):
        """
        Initialize HealthCheckConfig instance.

        :param health_check_interval: 健康检查间隔
        :type health_check_interval: int (optional)

        :param grace_time: 健康检查时间
        :type grace_time: int (optional)
        """
        super().__init__()
        self.health_check_interval = health_check_interval
        self.grace_time = grace_time

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
        if self.health_check_interval is not None:
            result['healthCheckInterval'] = self.health_check_interval
        if self.grace_time is not None:
            result['graceTime'] = self.grace_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HealthCheckConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('healthCheckInterval') is not None:
            self.health_check_interval = m.get('healthCheckInterval')
        if m.get('graceTime') is not None:
            self.grace_time = m.get('graceTime')
        return self
