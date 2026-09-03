"""
Request entity for DeleteAIGatewayResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class DeleteAIGatewayResponse(BceResponse):
    """
    DeleteAIGatewayResponse
    """

    def __init__(self, result=None):
        """
        Initialize DeleteAIGatewayResponse response.

        :param result: 删除成功时为空，实际响应为 null
        :type result: str (optional)
        """
        super().__init__()
        self.result = result

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
            result['result'] = self.result
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteAIGatewayResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        return self
