"""
K8SCacheNodeInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class K8SCacheNodeInfo(AbstractModel):
    """
    K8SCacheNodeInfo
    """

    def __init__(self, cache_deploy_group=None, k8s_controller_id=None):
        """
        Initialize K8SCacheNodeInfo instance.

        :param cache_deploy_group: 缓存部署组
        :type cache_deploy_group: str (optional)

        :param k8s_controller_id: 容器控制器 ID
        :type k8s_controller_id: str (optional)
        """
        super().__init__()
        self.cache_deploy_group = cache_deploy_group
        self.k8s_controller_id = k8s_controller_id

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
        if self.k8s_controller_id is not None:
            result['k8sControllerId'] = self.k8s_controller_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: K8SCacheNodeInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cacheDeployGroup') is not None:
            self.cache_deploy_group = m.get('cacheDeployGroup')
        if m.get('k8sControllerId') is not None:
            self.k8s_controller_id = m.get('k8sControllerId')
        return self
