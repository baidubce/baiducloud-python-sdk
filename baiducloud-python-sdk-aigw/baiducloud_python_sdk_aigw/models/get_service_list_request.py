"""
Request entity for GetServiceListRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetServiceListRequest(AbstractModel):
    """
    Request entity for GetServiceListRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, x_region, service_source=None):
        """
        Initialize GetServiceListRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param service_source: service_source parameter
        :type service_source: str (optional)

        :param x_region: x_region parameter
        :type x_region: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.service_source = service_source
        self.x_region = x_region

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
        :rtype: GetServiceListRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('serviceSource') is not None:
            self.service_source = m.get('serviceSource')
        if m.get('X-Region') is not None:
            self.x_region = m.get('X-Region')
        return self
