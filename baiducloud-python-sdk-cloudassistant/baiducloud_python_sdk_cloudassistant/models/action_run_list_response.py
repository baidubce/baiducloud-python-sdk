"""
Request entity for ActionRunListResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_cloudassistant.models.action_run_page import ActionRunPage


class ActionRunListResponse(BceResponse):
    """
    ActionRunListResponse
    """

    def __init__(self, request_id=None, code=None, message=None, success=None, result=None):
        """
        Initialize ActionRunListResponse response.

        :param request_id: 请求id
        :type request_id: str (optional)

        :param code: 响应状态，成功为success
        :type code: str (optional)

        :param message: 错误信息
        :type message: str (optional)

        :param success: 请求是否处理成功
        :type success: bool (optional)

        :param result: result field
        :type result: ActionRunPage (optional)
        """
        super().__init__()
        self.request_id = request_id
        self.code = code
        self.message = message
        self.success = success
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.success is not None:
            result['success'] = self.success
        if self.result is not None:
            result['result'] = self.result.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ActionRunListResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('result') is not None:
            self.result = ActionRunPage().from_dict(m.get('result'))
        return self
