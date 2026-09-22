"""
DelayInfoConsoleItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DelayInfoConsoleItem(AbstractModel):
    """
    DelayInfoConsoleItem
    """

    def __init__(self, source_cluster=None, dest_cluster=None, delay_result=None, time_result=None):
        """
        Initialize DelayInfoConsoleItem instance.

        :param source_cluster: 源端集群
        :type source_cluster: str (optional)

        :param dest_cluster: 目标端集群
        :type dest_cluster: str (optional)

        :param delay_result: 延迟信息
        :type delay_result: int (optional)

        :param time_result: 延迟时间
        :type time_result: int (optional)
        """
        super().__init__()
        self.source_cluster = source_cluster
        self.dest_cluster = dest_cluster
        self.delay_result = delay_result
        self.time_result = time_result

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
        if self.source_cluster is not None:
            result['sourceCluster'] = self.source_cluster
        if self.dest_cluster is not None:
            result['destCluster'] = self.dest_cluster
        if self.delay_result is not None:
            result['delayResult'] = self.delay_result
        if self.time_result is not None:
            result['timeResult'] = self.time_result
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DelayInfoConsoleItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('sourceCluster') is not None:
            self.source_cluster = m.get('sourceCluster')
        if m.get('destCluster') is not None:
            self.dest_cluster = m.get('destCluster')
        if m.get('delayResult') is not None:
            self.delay_result = m.get('delayResult')
        if m.get('timeResult') is not None:
            self.time_result = m.get('timeResult')
        return self
