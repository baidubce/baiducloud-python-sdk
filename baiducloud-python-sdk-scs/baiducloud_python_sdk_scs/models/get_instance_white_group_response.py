"""
Request entity for GetInstanceWhiteGroupResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_scs.models.cluster_ip import ClusterIP


class GetInstanceWhiteGroupResponse(BceResponse):
    """
    GetInstanceWhiteGroupResponse
    """

    def __init__(self, cluster_ip_groups=None):
        """
        Initialize GetInstanceWhiteGroupResponse response.

        :param cluster_ip_groups: 白名单分组列表
        :type cluster_ip_groups: List[ClusterIP] (optional)
        """
        super().__init__()
        self.cluster_ip_groups = cluster_ip_groups

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
        if self.cluster_ip_groups is not None:
            result['clusterIPGroups'] = [i.to_dict() for i in self.cluster_ip_groups]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetInstanceWhiteGroupResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clusterIPGroups') is not None:
            self.cluster_ip_groups = [ClusterIP().from_dict(i) for i in m.get('clusterIPGroups')]
        return self
