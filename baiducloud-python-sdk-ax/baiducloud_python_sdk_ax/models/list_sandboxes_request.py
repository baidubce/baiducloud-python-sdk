"""
Request entity for ListSandboxesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListSandboxesRequest(AbstractModel):
    """
    Request entity for ListSandboxesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, metadata=None):
        """
        Initialize ListSandboxesRequest request entity.

        :param metadata: metadata parameter
        :type metadata: str (optional)
        """
        super().__init__()
        self.metadata = metadata

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
        :rtype: ListSandboxesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')
        return self
