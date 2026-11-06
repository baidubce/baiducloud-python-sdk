"""
Request entity for ErrorLogListResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_rds.models.openapi_errorlog import OpenapiErrorlog


class ErrorLogListResponse(BceResponse):
    """
    ErrorLogListResponse
    """

    def __init__(self, errorlogs=None):
        """
        Initialize ErrorLogListResponse response.

        :param errorlogs: 错误日志对象
        :type errorlogs: List[OpenapiErrorlog] (optional)
        """
        super().__init__()
        self.errorlogs = errorlogs

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
        if self.errorlogs is not None:
            result['errorlogs'] = [i.to_dict() for i in self.errorlogs]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ErrorLogListResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('errorlogs') is not None:
            self.errorlogs = [OpenapiErrorlog().from_dict(i) for i in m.get('errorlogs')]
        return self
