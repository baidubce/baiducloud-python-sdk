"""
CceClusterInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CceClusterInfo(AbstractModel):
    """
    CceClusterInfo
    """

    def __init__(self, cluster_id=None, cluster_name=None, zones=None):
        """
        Initialize CceClusterInfo instance.

        :param cluster_id: CCE 集群 ID
        :type cluster_id: str (optional)

        :param cluster_name: 集群名称（排序键）
        :type cluster_name: str (optional)

        :param zones: 集群关联的可用区列表
        :type zones: List[str] (optional)
        """
        super().__init__()
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.zones = zones

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
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.zones is not None:
            result['zones'] = self.zones
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CceClusterInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('zones') is not None:
            self.zones = m.get('zones')
        return self
