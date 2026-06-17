"""
Request entity for AutoRenewVolumeClusterRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AutoRenewVolumeClusterRequest(AbstractModel):
    """
    Request entity for AutoRenewVolumeClusterRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, cluster_id, renew_time_unit, renew_time):
        """
        Initialize AutoRenewVolumeClusterRequest request entity.

        :param cluster_id: 专属集群ID
        :type cluster_id: str (required)

        :param renew_time_unit: 按月付费或者按年付费，月是month，年是year
        :type renew_time_unit: str (required)

        :param renew_time: 自动续费的时间，按月是1-9，按年是1-3
        :type renew_time: int (required)
        """
        super().__init__()
        self.cluster_id = cluster_id
        self.renew_time_unit = renew_time_unit
        self.renew_time = renew_time

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
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.renew_time_unit is not None:
            result['renewTimeUnit'] = self.renew_time_unit
        if self.renew_time is not None:
            result['renewTime'] = self.renew_time
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AutoRenewVolumeClusterRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('renewTimeUnit') is not None:
            self.renew_time_unit = m.get('renewTimeUnit')
        if m.get('renewTime') is not None:
            self.renew_time = m.get('renewTime')
        return self
