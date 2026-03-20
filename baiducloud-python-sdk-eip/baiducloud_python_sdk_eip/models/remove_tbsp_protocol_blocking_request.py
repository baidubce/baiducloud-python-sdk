"""
Request entity for RemoveTbspProtocolBlockingRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RemoveTbspProtocolBlockingRequest(AbstractModel):
    """
    Request entity for RemoveTbspProtocolBlockingRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, id, ip=None, client_token=None):
        """
        Initialize RemoveTbspProtocolBlockingRequest request entity.

        :param id: id parameter
        :type id: str (required)

        :param ip: ip parameter
        :type ip: str (optional)

        :param client_token: client_token parameter
        :type client_token: str (optional)
        """
        super().__init__()
        self.id = id
        self.ip = ip
        self.client_token = client_token

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RemoveTbspProtocolBlockingRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self
