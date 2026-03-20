"""
Request entity for ListRecycleEipsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListRecycleEipsRequest(AbstractModel):
    """
    Request entity for ListRecycleEipsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, eip=None, name=None, marker=None, max_keys=None):
        """
        Initialize ListRecycleEipsRequest request entity.

        :param eip: eip parameter
        :type eip: str (optional)

        :param name: name parameter
        :type name: str (optional)

        :param marker: marker parameter
        :type marker: str (optional)

        :param max_keys: max_keys parameter
        :type max_keys: int (optional)
        """
        super().__init__()
        self.eip = eip
        self.name = name
        self.marker = marker
        self.max_keys = max_keys

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
        :rtype: ListRecycleEipsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        return self
