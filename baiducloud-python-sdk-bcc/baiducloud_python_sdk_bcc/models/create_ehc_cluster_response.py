"""
Request entity for CreateEhcClusterResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateEhcClusterResponse(BceResponse):
    """
    CreateEhcClusterResponse
    """

    def __init__(self, ehc_cluster_id=None):
        """
        Initialize CreateEhcClusterResponse response.

        :param ehc_cluster_id: 返回EHC集群ID
        :type ehc_cluster_id: str (optional)
        """
        super().__init__()
        self.ehc_cluster_id = ehc_cluster_id

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
        if self.ehc_cluster_id is not None:
            result['ehcClusterId'] = self.ehc_cluster_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateEhcClusterResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ehcClusterId') is not None:
            self.ehc_cluster_id = m.get('ehcClusterId')
        return self
