"""
Request entity for RemoteReadRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RemoteReadRequest(AbstractModel):
    """
    Request entity for RemoteReadRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, remote_read_url, query, step, start, end):
        """
        Initialize RemoteReadRequest request entity.

        :param remote_read_url: remote_read_url parameter
        :type remote_read_url: str (required)

        :param query: query parameter
        :type query: str (required)

        :param step: step parameter
        :type step: int (required)

        :param start: start parameter
        :type start: int (required)

        :param end: end parameter
        :type end: int (required)
        """
        super().__init__()
        self.remote_read_url = remote_read_url
        self.query = query
        self.step = step
        self.start = start
        self.end = end

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
        if self.query is not None:
            result['query'] = self.query
        if self.step is not None:
            result['step'] = self.step
        if self.start is not None:
            result['start'] = self.start
        if self.end is not None:
            result['end'] = self.end
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RemoteReadRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('remoteReadUrl') is not None:
            self.remote_read_url = m.get('remoteReadUrl')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('step') is not None:
            self.step = m.get('step')
        if m.get('start') is not None:
            self.start = m.get('start')
        if m.get('end') is not None:
            self.end = m.get('end')
        return self
