"""
Request entity for ListEipBpRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListEipBpRequest(AbstractModel):
    """
    Request entity for ListEipBpRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, marker=None, max_keys=None, id=None, name=None, bind_type=None, type=None):
        """
        Initialize ListEipBpRequest request entity.

        :param marker: marker parameter
        :type marker: str (optional)

        :param max_keys: max_keys parameter
        :type max_keys: int (optional)

        :param id: id parameter
        :type id: str (optional)

        :param name: name parameter
        :type name: str (optional)

        :param bind_type: bind_type parameter
        :type bind_type: str (optional)

        :param type: type parameter
        :type type: str (optional)
        """
        super().__init__()
        self.marker = marker
        self.max_keys = max_keys
        self.id = id
        self.name = name
        self.bind_type = bind_type
        self.type = type

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
        :rtype: ListEipBpRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('bindType') is not None:
            self.bind_type = m.get('bindType')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self
