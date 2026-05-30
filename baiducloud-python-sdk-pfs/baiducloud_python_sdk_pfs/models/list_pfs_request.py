"""
Request entity for ListPfsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListPfsRequest(AbstractModel):
    """
    Request entity for ListPfsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, max_keys=None, marker=None, filter_tag=None):
        """
        Initialize ListPfsRequest request entity.

        :param max_keys: max_keys parameter
        :type max_keys: int (optional)

        :param marker: marker parameter
        :type marker: str (optional)

        :param filter_tag: filter_tag parameter
        :type filter_tag: str (optional)
        """
        super().__init__()
        self.max_keys = max_keys
        self.marker = marker
        self.filter_tag = filter_tag

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
        :rtype: ListPfsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('filterTag') is not None:
            self.filter_tag = m.get('filterTag')
        return self
