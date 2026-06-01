"""
StorageConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class StorageConfig(AbstractModel):
    """
    StorageConfig
    """

    def __init__(self, trace_retention_days=None, metric_retention_days=None, doris_retention_days=None):
        """
        Initialize StorageConfig instance.

        :param trace_retention_days: 链路数据保存时长，单位：天
        :type trace_retention_days: int (optional)

        :param metric_retention_days: 指标数据保存时长，单位：天
        :type metric_retention_days: int (optional)

        :param doris_retention_days: trace表数据保存时长，单位：天
        :type doris_retention_days: int (optional)
        """
        super().__init__()
        self.trace_retention_days = trace_retention_days
        self.metric_retention_days = metric_retention_days
        self.doris_retention_days = doris_retention_days

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
        if self.trace_retention_days is not None:
            result['traceRetentionDays'] = self.trace_retention_days
        if self.metric_retention_days is not None:
            result['metricRetentionDays'] = self.metric_retention_days
        if self.doris_retention_days is not None:
            result['dorisRetentionDays'] = self.doris_retention_days
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: StorageConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('traceRetentionDays') is not None:
            self.trace_retention_days = m.get('traceRetentionDays')
        if m.get('metricRetentionDays') is not None:
            self.metric_retention_days = m.get('metricRetentionDays')
        if m.get('dorisRetentionDays') is not None:
            self.doris_retention_days = m.get('dorisRetentionDays')
        return self
