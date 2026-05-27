"""
Request entity for ListEgressOnlyRuleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListEgressOnlyRuleRequest(AbstractModel):
    """
    Request entity for ListEgressOnlyRuleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, gateway_id, marker=None, max_keys=None):
        """
        Initialize ListEgressOnlyRuleRequest request entity.

        :param gateway_id: gateway_id parameter
        :type gateway_id: str (required)

        :param marker: marker parameter
        :type marker: str (optional)

        :param max_keys: max_keys parameter
        :type max_keys: int (optional)
        """
        super().__init__()
        self.gateway_id = gateway_id
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
        :rtype: ListEgressOnlyRuleRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        return self
