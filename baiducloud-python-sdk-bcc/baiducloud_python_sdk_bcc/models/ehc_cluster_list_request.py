"""
Request entity for EhcClusterListRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class EhcClusterListRequest(AbstractModel):
    """
    Request entity for EhcClusterListRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, ehc_cluster_id_list=None, name_list=None, zone_name=None):
        """
        Initialize EhcClusterListRequest request entity.

        :param ehc_cluster_id_list: EHC集群的ID列表
        :type ehc_cluster_id_list: List[str] (optional)

        :param name_list: EHC name列表
        :type name_list: List[str] (optional)

        :param zone_name: EHC集群的zoneName
        :type zone_name: str (optional)
        """
        super().__init__()
        self.ehc_cluster_id_list = ehc_cluster_id_list
        self.name_list = name_list
        self.zone_name = zone_name

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
        if self.name_list is not None:
            result['nameList'] = self.name_list
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EhcClusterListRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ehcClusterIdList') is not None:
            self.ehc_cluster_id_list = m.get('ehcClusterIdList')
        if m.get('nameList') is not None:
            self.name_list = m.get('nameList')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        return self
