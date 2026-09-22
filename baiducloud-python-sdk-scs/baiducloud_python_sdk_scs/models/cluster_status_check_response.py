"""
Request entity for ClusterStatusCheckResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_scs.models.check_list import CheckList


class ClusterStatusCheckResponse(BceResponse):
    """
    ClusterStatusCheckResponse
    """

    def __init__(self, cluster_status=None, check_list=None):
        """
        Initialize ClusterStatusCheckResponse response.

        :param cluster_status: 用于描述集群状态，有两种取值。normal 集群状态正常；abnormal 集群状态不正常。
        :type cluster_status: str (optional)

        :param check_list: check_list field
        :type check_list: CheckList (optional)
        """
        super().__init__()
        self.cluster_status = cluster_status
        self.check_list = check_list

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
        if self.cluster_status is not None:
            result['clusterStatus'] = self.cluster_status
        if self.check_list is not None:
            result['checkList'] = self.check_list.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ClusterStatusCheckResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clusterStatus') is not None:
            self.cluster_status = m.get('clusterStatus')
        if m.get('checkList') is not None:
            self.check_list = CheckList().from_dict(m.get('checkList'))
        return self
