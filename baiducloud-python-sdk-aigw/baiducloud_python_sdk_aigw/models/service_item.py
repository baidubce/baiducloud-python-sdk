"""
ServiceItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ServiceItem(AbstractModel):
    """
    ServiceItem
    """

    def __init__(self, service_name=None, cluster_ids=None):
        """
        Initialize ServiceItem instance.

        :param service_name: 服务名称
        :type service_name: str (optional)

        :param cluster_ids: 服务绑定的集群 ID 列表
        :type cluster_ids: List[str] (optional)
        """
        super().__init__()
        self.service_name = service_name
        self.cluster_ids = cluster_ids

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
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.cluster_ids is not None:
            result['clusterIds'] = self.cluster_ids
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ServiceItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('clusterIds') is not None:
            self.cluster_ids = m.get('clusterIds')
        return self
