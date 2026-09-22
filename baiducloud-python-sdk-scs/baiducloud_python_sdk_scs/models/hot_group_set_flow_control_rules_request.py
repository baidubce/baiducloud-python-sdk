"""
Request entity for HotGroupSetFlowControlRulesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class HotGroupSetFlowControlRulesRequest(AbstractModel):
    """
    Request entity for HotGroupSetFlowControlRulesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, group_id, cluster_show_id, qps_write=None, qps_read=None):
        """
        Initialize HotGroupSetFlowControlRulesRequest request entity.

        :param group_id: group_id parameter
        :type group_id: str (required)

        :param cluster_show_id: 集群ID
        :type cluster_show_id: str (required)

        :param qps_write: 写流量限制。（读写流量限制至少传一个）
        :type qps_write: int (optional)

        :param qps_read: 读流量限制。（读写流量限制至少传一个）
        :type qps_read: int (optional)
        """
        super().__init__()
        self.group_id = group_id
        self.cluster_show_id = cluster_show_id
        self.qps_write = qps_write
        self.qps_read = qps_read

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
        if self.cluster_show_id is not None:
            result['clusterShowId'] = self.cluster_show_id
        if self.qps_write is not None:
            result['qpsWrite'] = self.qps_write
        if self.qps_read is not None:
            result['qpsRead'] = self.qps_read
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HotGroupSetFlowControlRulesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('clusterShowId') is not None:
            self.cluster_show_id = m.get('clusterShowId')
        if m.get('qpsWrite') is not None:
            self.qps_write = m.get('qpsWrite')
        if m.get('qpsRead') is not None:
            self.qps_read = m.get('qpsRead')
        return self
