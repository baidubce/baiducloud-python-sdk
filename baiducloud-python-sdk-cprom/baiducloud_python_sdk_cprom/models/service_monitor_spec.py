"""
ServiceMonitorSpec information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_cprom.models.service_monitor_endpoint import ServiceMonitorEndpoint

from baiducloud_python_sdk_cprom.models.namespace_selector import NamespaceSelector

from baiducloud_python_sdk_cprom.models.label_selector import LabelSelector


class ServiceMonitorSpec(AbstractModel):
    """
    ServiceMonitorSpec
    """

    def __init__(self, endpoints=None, namespace_selector=None, selector=None):
        """
        Initialize ServiceMonitorSpec instance.

        :param endpoints: 采集端点配置列表
        :type endpoints: List[ServiceMonitorEndpoint] (optional)

        :param namespace_selector: namespace_selector attribute
        :type namespace_selector: NamespaceSelector (optional)

        :param selector: selector attribute
        :type selector: LabelSelector (optional)
        """
        super().__init__()
        self.endpoints = endpoints
        self.namespace_selector = namespace_selector
        self.selector = selector

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
        if self.endpoints is not None:
            result['endpoints'] = [i.to_dict() for i in self.endpoints]
        if self.namespace_selector is not None:
            result['namespaceSelector'] = self.namespace_selector.to_dict()
        if self.selector is not None:
            result['selector'] = self.selector.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ServiceMonitorSpec

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('endpoints') is not None:
            self.endpoints = [ServiceMonitorEndpoint().from_dict(i) for i in m.get('endpoints')]
        if m.get('namespaceSelector') is not None:
            self.namespace_selector = NamespaceSelector().from_dict(m.get('namespaceSelector'))
        if m.get('selector') is not None:
            self.selector = LabelSelector().from_dict(m.get('selector'))
        return self
