"""
Request entity for SynchronizeNodeMetadataV2Response information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class SynchronizeNodeMetadataV2Response(BceResponse):
    """
    SynchronizeNodeMetadataV2Response
    """

    def __init__(self, cluster_id=None, request_id=None):
        """
        Initialize SynchronizeNodeMetadataV2Response response.

        :param cluster_id: 请求的集群ID
        :type cluster_id: str (optional)

        :param request_id: 请求ID
        :type request_id: str (optional)
        """
        super().__init__()
        self.cluster_id = cluster_id
        self.request_id = request_id

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
        if self.cluster_id is not None:
            result['clusterID'] = self.cluster_id
        if self.request_id is not None:
            result['requestID'] = self.request_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SynchronizeNodeMetadataV2Response

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clusterID') is not None:
            self.cluster_id = m.get('clusterID')
        if m.get('requestID') is not None:
            self.request_id = m.get('requestID')
        return self
