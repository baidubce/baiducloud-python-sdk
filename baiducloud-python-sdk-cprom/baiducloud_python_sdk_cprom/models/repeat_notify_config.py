"""
RepeatNotifyConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RepeatNotifyConfig(AbstractModel):
    """
    RepeatNotifyConfig
    """

    def __init__(self, enabled=None, interval_hour=None, interval_min=None, max_count=None, strategy=None):
        """
        Initialize RepeatNotifyConfig instance.

        :param enabled: 是否开启重复通知
        :type enabled: bool (optional)

        :param interval_hour: 重复通知间隔小时数
        :type interval_hour: int (optional)

        :param interval_min: 重复通知间隔分钟数
        :type interval_min: int (optional)

        :param max_count: 最大重复通知次数
        :type max_count: int (optional)

        :param strategy: 重复通知策略
        :type strategy: str (optional)
        """
        super().__init__()
        self.enabled = enabled
        self.interval_hour = interval_hour
        self.interval_min = interval_min
        self.max_count = max_count
        self.strategy = strategy

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
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.interval_hour is not None:
            result['intervalHour'] = self.interval_hour
        if self.interval_min is not None:
            result['intervalMin'] = self.interval_min
        if self.max_count is not None:
            result['maxCount'] = self.max_count
        if self.strategy is not None:
            result['strategy'] = self.strategy
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RepeatNotifyConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('intervalHour') is not None:
            self.interval_hour = m.get('intervalHour')
        if m.get('intervalMin') is not None:
            self.interval_min = m.get('intervalMin')
        if m.get('maxCount') is not None:
            self.max_count = m.get('maxCount')
        if m.get('strategy') is not None:
            self.strategy = m.get('strategy')
        return self
