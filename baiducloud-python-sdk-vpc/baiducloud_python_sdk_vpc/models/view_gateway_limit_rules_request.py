"""
Request entity for ViewGatewayLimitRulesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ViewGatewayLimitRulesRequest(AbstractModel):
    """
    Request entity for ViewGatewayLimitRulesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, service_type=None, name=None, glr_id=None, resource_id=None, marker=None, max_keys=None):
        """
        Initialize ViewGatewayLimitRulesRequest request entity.

        :param service_type: service_type parameter
        :type service_type: str (optional)

        :param name: name parameter
        :type name: str (optional)

        :param glr_id: glr_id parameter
        :type glr_id: str (optional)

        :param resource_id: resource_id parameter
        :type resource_id: str (optional)

        :param marker: marker parameter
        :type marker: str (optional)

        :param max_keys: max_keys parameter
        :type max_keys: str (optional)
        """
        super().__init__()
        self.service_type = service_type
        self.name = name
        self.glr_id = glr_id
        self.resource_id = resource_id
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
        :rtype: ViewGatewayLimitRulesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('glrId') is not None:
            self.glr_id = m.get('glrId')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        return self
