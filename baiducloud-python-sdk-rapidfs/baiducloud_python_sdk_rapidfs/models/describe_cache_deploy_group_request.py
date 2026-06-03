"""
Request entity for DescribeCacheDeployGroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescribeCacheDeployGroupRequest(AbstractModel):
    """
    Request entity for DescribeCacheDeployGroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, cache_deploy_group_name, cache_deploy_group_ns):
        """
        Initialize DescribeCacheDeployGroupRequest request entity.

        :param instance_id: RapidFS 实例 ID
        :type instance_id: str (required)

        :param cache_deploy_group_name: 缓存部署组名称
        :type cache_deploy_group_name: str (required)

        :param cache_deploy_group_ns: K8s 集群的命名空间
        :type cache_deploy_group_ns: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.cache_deploy_group_name = cache_deploy_group_name
        self.cache_deploy_group_ns = cache_deploy_group_ns

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.cache_deploy_group_name is not None:
            result['cacheDeployGroupName'] = self.cache_deploy_group_name
        if self.cache_deploy_group_ns is not None:
            result['cacheDeployGroupNS'] = self.cache_deploy_group_ns
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeCacheDeployGroupRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('cacheDeployGroupName') is not None:
            self.cache_deploy_group_name = m.get('cacheDeployGroupName')
        if m.get('cacheDeployGroupNS') is not None:
            self.cache_deploy_group_ns = m.get('cacheDeployGroupNS')
        return self
