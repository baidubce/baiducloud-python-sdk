"""
Request entity for GetTaskDetailV2Response information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_oos.models.task import Task


class GetTaskDetailV2Response(BceResponse):
    """
    GetTaskDetailV2Response
    """

    def __init__(self, success=None, msg=None, code=None, result=None):
        """
        Initialize GetTaskDetailV2Response response.

        :param success: 请求是否成功
        :type success: bool (optional)

        :param msg: 失败时返回失败原因，成功时为空字符串
        :type msg: str (optional)

        :param code: 状态码
        :type code: int (optional)

        :param result: result field
        :type result: Task (optional)
        """
        super().__init__()
        self.success = success
        self.msg = msg
        self.code = code
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.code is not None:
            result['code'] = self.code
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
        :rtype: GetTaskDetailV2Response

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('result') is not None:
            self.result = Task().from_dict(m.get('result'))
        return self
