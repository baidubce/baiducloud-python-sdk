"""
Request entity for CreateServiceResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateServiceResponse(BceResponse):
    """
    CreateServiceResponse
    """

    def __init__(self, service=None):
        """
        Initialize CreateServiceResponse response.

        :param service: 服务发布点的域名，使用此域名绑定服务网卡
        :type service: str (optional)
        """
        super().__init__()
        self.service = service

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
        if self.service is not None:
            result['service'] = self.service
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateServiceResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('service') is not None:
            self.service = m.get('service')
        return self
