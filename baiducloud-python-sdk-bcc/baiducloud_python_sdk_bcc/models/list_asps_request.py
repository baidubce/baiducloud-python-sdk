"""
Request entity for ListAspsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListAspsRequest(AbstractModel):
    """
    Request entity for ListAspsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, marker=None, max_keys=None, asp_name=None, volume_name=None):
        """
        Initialize ListAspsRequest request entity.

        :param marker: marker parameter
        :type marker: str (optional)

        :param max_keys: max_keys parameter
        :type max_keys: int (optional)

        :param asp_name: asp_name parameter
        :type asp_name: str (optional)

        :param volume_name: volume_name parameter
        :type volume_name: str (optional)
        """
        super().__init__()
        self.marker = marker
        self.max_keys = max_keys
        self.asp_name = asp_name
        self.volume_name = volume_name

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
        :rtype: ListAspsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('aspName') is not None:
            self.asp_name = m.get('aspName')
        if m.get('volumeName') is not None:
            self.volume_name = m.get('volumeName')
        return self
