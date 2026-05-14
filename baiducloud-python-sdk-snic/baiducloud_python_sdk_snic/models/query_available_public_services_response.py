"""
Request entity for QueryAvailablePublicServicesResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class QueryAvailablePublicServicesResponse(BceResponse):
    """
    QueryAvailablePublicServicesResponse
    """

    def __init__(self, services=None):
        """
        Initialize QueryAvailablePublicServicesResponse response.

        :param services: 公共服务的域名列表
        :type services: List[str] (optional)
        """
        super().__init__()
        self.services = services

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.services is not None:
            result['services'] = self.services
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QueryAvailablePublicServicesResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('services') is not None:
            self.services = m.get('services')
        return self
