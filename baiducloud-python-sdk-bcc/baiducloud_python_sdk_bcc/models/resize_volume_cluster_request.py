"""
Request entity for ResizeVolumeClusterRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ResizeVolumeClusterRequest(AbstractModel):
    """
    Request entity for ResizeVolumeClusterRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, cluster_id, new_cluster_size_in_gb):
        """
        Initialize ResizeVolumeClusterRequest request entity.

        :param cluster_id: cluster_id parameter
        :type cluster_id: str (required)

        :param new_cluster_size_in_gb: 新扩容专属集群容量大小，必须为大于当前专属集群容量的整数，单位为GB，大小为87040~1039360的正整数。
        :type new_cluster_size_in_gb: int (required)
        """
        super().__init__()
        self.cluster_id = cluster_id
        self.new_cluster_size_in_gb = new_cluster_size_in_gb

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
        if self.new_cluster_size_in_gb is not None:
            result['newClusterSizeInGB'] = self.new_cluster_size_in_gb
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ResizeVolumeClusterRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('newClusterSizeInGB') is not None:
            self.new_cluster_size_in_gb = m.get('newClusterSizeInGB')
        return self
