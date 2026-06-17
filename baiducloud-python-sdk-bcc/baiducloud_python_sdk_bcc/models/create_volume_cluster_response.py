"""
Request entity for CreateVolumeClusterResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateVolumeClusterResponse(BceResponse):
    """
    CreateVolumeClusterResponse
    """

    def __init__(self, cluster_ids=None):
        """
        Initialize CreateVolumeClusterResponse response.

        :param cluster_ids: cluster_ids field
        :type cluster_ids: List[str] (optional)
        """
        super().__init__()
        self.cluster_ids = cluster_ids

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
        if self.cluster_ids is not None:
            result['clusterIds'] = self.cluster_ids
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateVolumeClusterResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clusterIds') is not None:
            self.cluster_ids = m.get('clusterIds')
        return self
