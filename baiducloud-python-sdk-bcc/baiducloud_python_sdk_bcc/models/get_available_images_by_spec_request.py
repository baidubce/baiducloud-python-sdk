"""
Request entity for GetAvailableImagesBySpecRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetAvailableImagesBySpecRequest(AbstractModel):
    """
    Request entity for GetAvailableImagesBySpecRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, spec, marker=None, max_keys=None, os_name=None):
        """
        Initialize GetAvailableImagesBySpecRequest request entity.

        :param spec: spec parameter
        :type spec: str (required)

        :param marker: marker parameter
        :type marker: str (optional)

        :param max_keys: max_keys parameter
        :type max_keys: int (optional)

        :param os_name: os_name parameter
        :type os_name: str (optional)
        """
        super().__init__()
        self.spec = spec
        self.marker = marker
        self.max_keys = max_keys
        self.os_name = os_name

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
        :rtype: GetAvailableImagesBySpecRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('osName') is not None:
            self.os_name = m.get('osName')
        return self
