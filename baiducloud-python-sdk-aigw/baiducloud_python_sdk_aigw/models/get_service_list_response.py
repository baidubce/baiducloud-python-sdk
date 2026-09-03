"""
GetServiceListResponse information
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class GetServiceListResponse(BceResponse):
    """
    GetServiceListResponse
    """

    def __init__(self, service_name=None, namespace=None, cluster_id=None):
        """
        Initialize GetServiceListResponse instance.

        :param service_name: 服务名称
        :type service_name: str (optional)

        :param namespace: 服务命名空间
        :type namespace: str (optional)

        :param cluster_id: 关联集群 ID；非 CCE 服务可能为空
        :type cluster_id: str (optional)
        """
        super().__init__()
        self.service_name = service_name
        self.namespace = namespace
        self.cluster_id = cluster_id

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        Includes metadata from the parent BceResponse class.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetServiceListResponse

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        return self
