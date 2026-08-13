"""
Request entity for DeleteRouteResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_aigw.models.delete_route_result import DeleteRouteResult


class DeleteRouteResponse(BceResponse):
    """
    DeleteRouteResponse
    """

    def __init__(self, result=None, message=None):
        """
        Initialize DeleteRouteResponse response.

        :param result: result field
        :type result: DeleteRouteResult (optional)

        :param message: 错误信息，仅失败时返回
        :type message: str (optional)
        """
        super().__init__()
        self.result = result
        self.message = message

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
        if self.result is not None:
            result['result'] = self.result.to_dict()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteRouteResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('result') is not None:
            self.result = DeleteRouteResult().from_dict(m.get('result'))
        if m.get('message') is not None:
            self.message = m.get('message')
        return self
