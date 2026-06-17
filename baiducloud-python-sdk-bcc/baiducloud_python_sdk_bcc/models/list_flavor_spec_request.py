"""
Request entity for ListFlavorSpecRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListFlavorSpecRequest(AbstractModel):
    """
    Request entity for ListFlavorSpecRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, zone_name=None, specs=None, spec_ids=None):
        """
        Initialize ListFlavorSpecRequest request entity.

        :param zone_name: zone_name parameter
        :type zone_name: str (optional)

        :param specs: specs parameter
        :type specs: str (optional)

        :param spec_ids: spec_ids parameter
        :type spec_ids: str (optional)
        """
        super().__init__()
        self.zone_name = zone_name
        self.specs = specs
        self.spec_ids = spec_ids

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
        :rtype: ListFlavorSpecRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('specs') is not None:
            self.specs = m.get('specs')
        if m.get('specIds') is not None:
            self.spec_ids = m.get('specIds')
        return self
