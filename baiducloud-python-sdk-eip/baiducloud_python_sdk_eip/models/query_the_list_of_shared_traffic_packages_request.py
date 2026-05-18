"""
Request entity for QueryTheListOfSharedTrafficPackagesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class QueryTheListOfSharedTrafficPackagesRequest(AbstractModel):
    """
    Request entity for QueryTheListOfSharedTrafficPackagesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, marker=None, max_keys=None, id=None, status=None, deduct_policy=None):
        """
        Initialize QueryTheListOfSharedTrafficPackagesRequest request entity.

        :param marker: marker parameter
        :type marker: str (optional)

        :param max_keys: max_keys parameter
        :type max_keys: int (optional)

        :param id: id parameter
        :type id: str (optional)

        :param status: status parameter
        :type status: str (optional)

        :param deduct_policy: deduct_policy parameter
        :type deduct_policy: str (optional)
        """
        super().__init__()
        self.marker = marker
        self.max_keys = max_keys
        self.id = id
        self.status = status
        self.deduct_policy = deduct_policy

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
        :rtype: QueryTheListOfSharedTrafficPackagesRequest

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
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('deductPolicy') is not None:
            self.deduct_policy = m.get('deductPolicy')
        return self
