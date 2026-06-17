"""
Request entity for ModifyInstUserOpAuthorizeRuleAttributeResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class ModifyInstUserOpAuthorizeRuleAttributeResponse(BceResponse):
    """
    ModifyInstUserOpAuthorizeRuleAttributeResponse
    """

    def __init__(self, request_id=None):
        """
        Initialize ModifyInstUserOpAuthorizeRuleAttributeResponse response.

        :param request_id: 请求Id
        :type request_id: str (optional)
        """
        super().__init__()
        self.request_id = request_id

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyInstUserOpAuthorizeRuleAttributeResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self
