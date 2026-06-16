"""
Request entity for GetDownloadTaskLinkResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bls.models.download_link_result import DownloadLinkResult


class GetDownloadTaskLinkResponse(BceResponse):
    """
    GetDownloadTaskLinkResponse
    """

    def __init__(self, success=None, code=None, message=None, result=None):
        """
        Initialize GetDownloadTaskLinkResponse response.

        :param success: 请求是否成功
        :type success: bool (optional)

        :param code: 请求码，成功为OK，错误为具体的错误码
        :type code: str (optional)

        :param message: 请求成功为空，失败为具体的错误信息
        :type message: str (optional)

        :param result: result field
        :type result: DownloadLinkResult (optional)
        """
        super().__init__()
        self.success = success
        self.code = code
        self.message = message
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
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
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
        :rtype: GetDownloadTaskLinkResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('result') is not None:
            self.result = DownloadLinkResult().from_dict(m.get('result'))
        return self
