"""
AIHCCacheNodeInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AIHCCacheNodeInfo(AbstractModel):
    """
    AIHCCacheNodeInfo
    """

    def __init__(
        self,
        cache_deploy_group=None,
        aihc_resource_pool_id=None,
        host_node_id=None,
        host_node_name=None,
        host_zone=None,
    ):
        """
        Initialize AIHCCacheNodeInfo instance.

        :param cache_deploy_group: 缓存部署组
        :type cache_deploy_group: str (optional)

        :param aihc_resource_pool_id: 百舸资源池 ID
        :type aihc_resource_pool_id: str (optional)

        :param host_node_id: 容器所在百舸节点 ID
        :type host_node_id: str (optional)

        :param host_node_name: 容器所在百舸节点名称
        :type host_node_name: str (optional)

        :param host_zone: 容器所在节点可用区
        :type host_zone: str (optional)
        """
        super().__init__()
        self.cache_deploy_group = cache_deploy_group
        self.aihc_resource_pool_id = aihc_resource_pool_id
        self.host_node_id = host_node_id
        self.host_node_name = host_node_name
        self.host_zone = host_zone

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
        if self.cache_deploy_group is not None:
            result['cacheDeployGroup'] = self.cache_deploy_group
        if self.aihc_resource_pool_id is not None:
            result['aihcResourcePoolId'] = self.aihc_resource_pool_id
        if self.host_node_id is not None:
            result['hostNodeId'] = self.host_node_id
        if self.host_node_name is not None:
            result['hostNodeName'] = self.host_node_name
        if self.host_zone is not None:
            result['hostZone'] = self.host_zone
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AIHCCacheNodeInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cacheDeployGroup') is not None:
            self.cache_deploy_group = m.get('cacheDeployGroup')
        if m.get('aihcResourcePoolId') is not None:
            self.aihc_resource_pool_id = m.get('aihcResourcePoolId')
        if m.get('hostNodeId') is not None:
            self.host_node_id = m.get('hostNodeId')
        if m.get('hostNodeName') is not None:
            self.host_node_name = m.get('hostNodeName')
        if m.get('hostZone') is not None:
            self.host_zone = m.get('hostZone')
        return self
