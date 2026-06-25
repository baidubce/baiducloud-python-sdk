"""
PodMonitor information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_cprom.models.object_meta import ObjectMeta

from baiducloud_python_sdk_cprom.models.pod_monitor_spec import PodMonitorSpec


class PodMonitor(AbstractModel):
    """
    PodMonitor
    """

    def __init__(self, api_version=None, kind=None, metadata=None, spec=None):
        """
        Initialize PodMonitor instance.

        :param api_version: 固定值：monitoring.coreos.com/v1
        :type api_version: str (optional)

        :param kind: 固定值：PodMonitor
        :type kind: str (optional)

        :param metadata: metadata attribute
        :type metadata: ObjectMeta (optional)

        :param spec: spec attribute
        :type spec: PodMonitorSpec (optional)
        """
        super().__init__()
        self.api_version = api_version
        self.kind = kind
        self.metadata = metadata
        self.spec = spec

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
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_dict()
        if self.spec is not None:
            result['spec'] = self.spec.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PodMonitor

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            self.metadata = ObjectMeta().from_dict(m.get('metadata'))
        if m.get('spec') is not None:
            self.spec = PodMonitorSpec().from_dict(m.get('spec'))
        return self
