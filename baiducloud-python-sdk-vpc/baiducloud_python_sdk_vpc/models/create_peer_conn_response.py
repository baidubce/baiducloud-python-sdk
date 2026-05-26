"""
Request entity for CreatePeerConnResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreatePeerConnResponse(BceResponse):
    """
    CreatePeerConnResponse
    """

    def __init__(self, peer_conn_id=None):
        """
        Initialize CreatePeerConnResponse response.

        :param peer_conn_id: 创建的对等连接ID
        :type peer_conn_id: str (optional)
        """
        super().__init__()
        self.peer_conn_id = peer_conn_id

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
        if self.peer_conn_id is not None:
            result['peerConnId'] = self.peer_conn_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreatePeerConnResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('peerConnId') is not None:
            self.peer_conn_id = m.get('peerConnId')
        return self
