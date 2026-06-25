"""
ServiceMonitorItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_cprom.models.endpoint import Endpoint


class ServiceMonitorItem(AbstractModel):
    """
    ServiceMonitorItem
    """

    def __init__(self, service_monitor_name=None, namespace=None, enable=None, create_time=None, endpoints=None):
        """
        Initialize ServiceMonitorItem instance.

        :param service_monitor_name: Service Monitor名称
        :type service_monitor_name: str (optional)

        :param namespace: Service Monitor命名空间
        :type namespace: str (optional)

        :param enable: 是否启用：true/false
        :type enable: str (optional)

        :param create_time: 创建时间
        :type create_time: str (optional)

        :param endpoints: 端点信息
        :type endpoints: List[Endpoint] (optional)
        """
        super().__init__()
        self.service_monitor_name = service_monitor_name
        self.namespace = namespace
        self.enable = enable
        self.create_time = create_time
        self.endpoints = endpoints

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
        if self.service_monitor_name is not None:
            result['serviceMonitorName'] = self.service_monitor_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.enable is not None:
            result['enable'] = self.enable
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.endpoints is not None:
            result['endpoints'] = [i.to_dict() for i in self.endpoints]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ServiceMonitorItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('serviceMonitorName') is not None:
            self.service_monitor_name = m.get('serviceMonitorName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('endpoints') is not None:
            self.endpoints = [Endpoint().from_dict(i) for i in m.get('endpoints')]
        return self
