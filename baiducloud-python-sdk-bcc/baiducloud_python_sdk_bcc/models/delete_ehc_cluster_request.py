"""
Request entity for DeleteEhcClusterRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteEhcClusterRequest(AbstractModel):
    """
    Request entity for DeleteEhcClusterRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, ehc_cluster_id_list):
        """
        Initialize DeleteEhcClusterRequest request entity.

        :param ehc_cluster_id_list: 删除的EHC集群id列表
        :type ehc_cluster_id_list: List[str] (required)
        """
        super().__init__()
        self.ehc_cluster_id_list = ehc_cluster_id_list

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
        if self.ehc_cluster_id_list is not None:
            result['ehcClusterIdList'] = self.ehc_cluster_id_list
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteEhcClusterRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ehcClusterIdList') is not None:
            self.ehc_cluster_id_list = m.get('ehcClusterIdList')
        return self
