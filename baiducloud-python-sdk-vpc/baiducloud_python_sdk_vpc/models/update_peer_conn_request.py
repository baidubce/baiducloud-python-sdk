"""
Request entity for UpdatePeerConnRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdatePeerConnRequest(AbstractModel):
    """
    Request entity for UpdatePeerConnRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, peer_conn_id, local_if_id, client_token=None, description=None, local_if_name=None):
        """
        Initialize UpdatePeerConnRequest request entity.

        :param peer_conn_id: peer_conn_id parameter
        :type peer_conn_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param local_if_id: 对等连接的接口ID 不可更改
        :type local_if_id: str (required)

        :param description: 备注
        :type description: str (optional)

        :param local_if_name: 本端接口名称
        :type local_if_name: str (optional)
        """
        super().__init__()
        self.peer_conn_id = peer_conn_id
        self.client_token = client_token
        self.local_if_id = local_if_id
        self.description = description
        self.local_if_name = local_if_name

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
        if self.local_if_id is not None:
            result['localIfId'] = self.local_if_id
        if self.description is not None:
            result['description'] = self.description
        if self.local_if_name is not None:
            result['localIfName'] = self.local_if_name
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdatePeerConnRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('peerConnId') is not None:
            self.peer_conn_id = m.get('peerConnId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('localIfId') is not None:
            self.local_if_id = m.get('localIfId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('localIfName') is not None:
            self.local_if_name = m.get('localIfName')
        return self
