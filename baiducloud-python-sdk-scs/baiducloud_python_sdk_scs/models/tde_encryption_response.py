"""
Request entity for TdeEncryptionResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class TdeEncryptionResponse(BceResponse):
    """
    TdeEncryptionResponse
    """

    def __init__(self, operate_status=None, error_message=None):
        """
        Initialize TdeEncryptionResponse response.

        :param operate_status: 操作状态。仅成功时返回success
        :type operate_status: str (optional)

        :param error_message: 操作失败原因。该值为空，无实际意义。
        :type error_message: str (optional)
        """
        super().__init__()
        self.operate_status = operate_status
        self.error_message = error_message

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
        if self.operate_status is not None:
            result['operateStatus'] = self.operate_status
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TdeEncryptionResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('operateStatus') is not None:
            self.operate_status = m.get('operateStatus')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        return self
