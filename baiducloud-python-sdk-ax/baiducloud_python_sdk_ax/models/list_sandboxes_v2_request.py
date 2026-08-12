"""
Request entity for ListSandboxesV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListSandboxesV2Request(AbstractModel):
    """
    Request entity for ListSandboxesV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, limit=None, next_token=None, metadata=None, state=None):
        """
        Initialize ListSandboxesV2Request request entity.

        :param limit: limit parameter
        :type limit: int (optional)

        :param next_token: next_token parameter
        :type next_token: str (optional)

        :param metadata: metadata parameter
        :type metadata: str (optional)

        :param state: state parameter
        :type state: str (optional)
        """
        super().__init__()
        self.limit = limit
        self.next_token = next_token
        self.metadata = metadata
        self.state = state

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
        :rtype: ListSandboxesV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self
