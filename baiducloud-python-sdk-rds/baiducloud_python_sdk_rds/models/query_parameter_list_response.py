"""
Request entity for QueryParameterListResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_rds.models.open_api_config_item import OpenApiConfigItem


class QueryParameterListResponse(BceResponse):
    """
    QueryParameterListResponse
    """

    def __init__(self, etag=None, parameters=None):
        """
        Initialize QueryParameterListResponse response.

        :param etag: 当前数据版本号，如：v1
        :type etag: str (optional)

        :param parameters: OpenApiConfigItem对象
        :type parameters: List[OpenApiConfigItem] (optional)
        """
        super().__init__()
        self.etag = etag
        self.parameters = parameters

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
        if self.etag is not None:
            result['etag'] = self.etag
        if self.parameters is not None:
            result['parameters'] = [i.to_dict() for i in self.parameters]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QueryParameterListResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('etag') is not None:
            self.etag = m.get('etag')
        if m.get('parameters') is not None:
            self.parameters = [OpenApiConfigItem().from_dict(i) for i in m.get('parameters')]
        return self
