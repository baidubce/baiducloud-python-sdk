"""
Request entity for GetParameterTemplateDetailsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_rds.models.result import Result


class GetParameterTemplateDetailsResponse(BceResponse):
    """
    GetParameterTemplateDetailsResponse
    """

    def __init__(self, success=None, message=None, status=None, result=None):
        """
        Initialize GetParameterTemplateDetailsResponse response.

        :param success: 见示例
        :type success: bool (optional)

        :param message: 见示例
        :type message: object (optional)

        :param status: 见示例
        :type status: int (optional)

        :param result: result field
        :type result: Result (optional)
        """
        super().__init__()
        self.success = success
        self.message = message
        self.status = status
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
        if self.success is not None:
            result['success'] = self.success
        if self.message is not None:
            result['message'] = self.message
        if self.status is not None:
            result['status'] = self.status
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
        :rtype: GetParameterTemplateDetailsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('result') is not None:
            self.result = Result().from_dict(m.get('result'))
        return self
