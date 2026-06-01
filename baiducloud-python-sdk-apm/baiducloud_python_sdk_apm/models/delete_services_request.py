"""
Request entity for DeleteServicesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteServicesRequest(AbstractModel):
    """
    Request entity for DeleteServicesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, service_names):
        """
        Initialize DeleteServicesRequest request entity.

        :param service_names: 应用名列表，支持批量删除
        :type service_names: List[str] (required)
        """
        super().__init__()
        self.service_names = service_names

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
        if self.service_names is not None:
            result['serviceNames'] = self.service_names
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteServicesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('serviceNames') is not None:
            self.service_names = m.get('serviceNames')
        return self
