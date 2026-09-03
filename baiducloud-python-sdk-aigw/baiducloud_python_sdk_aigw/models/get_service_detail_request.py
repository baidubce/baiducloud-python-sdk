"""
Request entity for GetServiceDetailRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetServiceDetailRequest(AbstractModel):
    """
    Request entity for GetServiceDetailRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, service_name, x_region):
        """
        Initialize GetServiceDetailRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param service_name: service_name parameter
        :type service_name: str (required)

        :param x_region: x_region parameter
        :type x_region: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.service_name = service_name
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
        :rtype: GetServiceDetailRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('X-Region') is not None:
            self.x_region = m.get('X-Region')
        return self
