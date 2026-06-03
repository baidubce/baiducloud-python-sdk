"""
CCECacheNodeInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CCECacheNodeInfo(AbstractModel):
    """
    CCECacheNodeInfo
    """

    def __init__(
        self, cache_deploy_group=None, cce_cluster_id=None, host_bcc_id=None, host_bcc_name=None, host_zone=None
    ):
        """
        Initialize CCECacheNodeInfo instance.

        :param cache_deploy_group: 缓存部署组
        :type cache_deploy_group: str (optional)

        :param cce_cluster_id: CCE 集群 ID
        :type cce_cluster_id: str (optional)

        :param host_bcc_id: 容器所在 BCC ID
        :type host_bcc_id: str (optional)

        :param host_bcc_name: 容器所在 BCC 名称
        :type host_bcc_name: str (optional)

        :param host_zone: 容器所在 BCC 可用区
        :type host_zone: str (optional)
        """
        super().__init__()
        self.cache_deploy_group = cache_deploy_group
        self.cce_cluster_id = cce_cluster_id
        self.host_bcc_id = host_bcc_id
        self.host_bcc_name = host_bcc_name
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
        if self.cce_cluster_id is not None:
            result['cceClusterId'] = self.cce_cluster_id
        if self.host_bcc_id is not None:
            result['hostBccId'] = self.host_bcc_id
        if self.host_bcc_name is not None:
            result['hostBccName'] = self.host_bcc_name
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
        :rtype: CCECacheNodeInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cacheDeployGroup') is not None:
            self.cache_deploy_group = m.get('cacheDeployGroup')
        if m.get('cceClusterId') is not None:
            self.cce_cluster_id = m.get('cceClusterId')
        if m.get('hostBccId') is not None:
            self.host_bcc_id = m.get('hostBccId')
        if m.get('hostBccName') is not None:
            self.host_bcc_name = m.get('hostBccName')
        if m.get('hostZone') is not None:
            self.host_zone = m.get('hostZone')
        return self
