"""
Request entity for EhcClusterListResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcc.models.ehc_cluster import EhcCluster


class EhcClusterListResponse(BceResponse):
    """
    EhcClusterListResponse
    """

    def __init__(self, total_count=None, ehc_clusters=None):
        """
        Initialize EhcClusterListResponse response.

        :param total_count: EHC集群总数
        :type total_count: int (optional)

        :param ehc_clusters: EHC集群信息列表
        :type ehc_clusters: List[EhcCluster] (optional)
        """
        super().__init__()
        self.total_count = total_count
        self.ehc_clusters = ehc_clusters

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.ehc_clusters is not None:
            result['ehcClusters'] = [i.to_dict() for i in self.ehc_clusters]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EhcClusterListResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('ehcClusters') is not None:
            self.ehc_clusters = [EhcCluster().from_dict(i) for i in m.get('ehcClusters')]
        return self
