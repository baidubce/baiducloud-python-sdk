"""
PodMetricsEndpoint information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class PodMetricsEndpoint(AbstractModel):
    """
    PodMetricsEndpoint
    """

    def __init__(self, interval=None, path=None, port=None):
        """
        Initialize PodMetricsEndpoint instance.

        :param interval: 采集间隔，如：15s，可不传，默认为 15s
        :type interval: str (optional)

        :param path: 采集路径，如：/metrics 可不传，默认为 /metrics
        :type path: str (optional)

        :param port: 对应 Pod 的 port name，注意不是端口号
        :type port: str (optional)
        """
        super().__init__()
        self.interval = interval
        self.path = path
        self.port = port

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
        if self.interval is not None:
            result['interval'] = self.interval
        if self.path is not None:
            result['path'] = self.path
        if self.port is not None:
            result['port'] = self.port
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PodMetricsEndpoint

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('interval') is not None:
            self.interval = m.get('interval')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('port') is not None:
            self.port = m.get('port')
        return self
