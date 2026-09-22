"""
SyncFlowItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SyncFlowItem(AbstractModel):
    """
    SyncFlowItem
    """

    def __init__(self, target_blbip=None, target_blb_port=None, target_cluster_show_id=None):
        """
        Initialize SyncFlowItem instance.

        :param target_blbip: 同步流目标端BLBIP。
        :type target_blbip: str (optional)

        :param target_blb_port: 同步流目标端BLB端口。
        :type target_blb_port: str (optional)

        :param target_cluster_show_id: 同步流目标端集群ID。
        :type target_cluster_show_id: str (optional)
        """
        super().__init__()
        self.target_blbip = target_blbip
        self.target_blb_port = target_blb_port
        self.target_cluster_show_id = target_cluster_show_id

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
        if self.target_blbip is not None:
            result['targetBLBIp'] = self.target_blbip
        if self.target_blb_port is not None:
            result['targetBLBPort'] = self.target_blb_port
        if self.target_cluster_show_id is not None:
            result['targetClusterShowId'] = self.target_cluster_show_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SyncFlowItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('targetBLBIp') is not None:
            self.target_blbip = m.get('targetBLBIp')
        if m.get('targetBLBPort') is not None:
            self.target_blb_port = m.get('targetBLBPort')
        if m.get('targetClusterShowId') is not None:
            self.target_cluster_show_id = m.get('targetClusterShowId')
        return self
