"""
Autoscaler information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_cce.models.ca_config import CAConfig


class Autoscaler(AbstractModel):
    """
    Autoscaler
    """

    def __init__(self, cluster_id=None, cluster_name=None, ca_config=None):
        """
        Initialize Autoscaler instance.

        :param cluster_id: 集群 ID
        :type cluster_id: str (optional)

        :param cluster_name: 集群名称
        :type cluster_name: str (optional)

        :param ca_config: ca_config attribute
        :type ca_config: CAConfig (optional)
        """
        super().__init__()
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.ca_config = ca_config

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
            result['clusterID'] = self.cluster_id
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.ca_config is not None:
            result['caConfig'] = self.ca_config.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Autoscaler

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clusterID') is not None:
            self.cluster_id = m.get('clusterID')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('caConfig') is not None:
            self.ca_config = CAConfig().from_dict(m.get('caConfig'))
        return self
