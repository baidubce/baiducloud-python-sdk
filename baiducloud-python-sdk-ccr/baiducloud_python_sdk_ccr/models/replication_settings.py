"""
ReplicationSettings information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ReplicationSettings(AbstractModel):
    """
    ReplicationSettings
    """

    def __init__(self, cron=None):
        """
        Initialize ReplicationSettings instance.

        :param cron: 当迁移规则触发类型为 `scheduled` 时，对应的触发规则表达式
        :type cron: str (optional)
        """
        super().__init__()
        self.cron = cron

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
        if self.cron is not None:
            result['cron'] = self.cron
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ReplicationSettings

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cron') is not None:
            self.cron = m.get('cron')
        return self
