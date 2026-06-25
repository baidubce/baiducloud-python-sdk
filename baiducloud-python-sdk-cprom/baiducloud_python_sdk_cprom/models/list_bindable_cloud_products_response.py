"""
Request entity for ListBindableCloudProductsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_cprom.models.scope_detail import ScopeDetail


class ListBindableCloudProductsResponse(BceResponse):
    """
    ListBindableCloudProductsResponse
    """

    def __init__(self, scopes=None):
        """
        Initialize ListBindableCloudProductsResponse response.

        :param scopes: BCM 支持的云产品列表
        :type scopes: List[ScopeDetail] (optional)
        """
        super().__init__()
        self.scopes = scopes

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
        if self.scopes is not None:
            result['scopes'] = [i.to_dict() for i in self.scopes]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListBindableCloudProductsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('scopes') is not None:
            self.scopes = [ScopeDetail().from_dict(i) for i in m.get('scopes')]
        return self
