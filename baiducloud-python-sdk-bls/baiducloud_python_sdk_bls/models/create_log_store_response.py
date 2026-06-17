"""
CreateLogStoreResponse information
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateLogStoreResponse(BceResponse):
    """
    CreateLogStoreResponse
    """

    def __init__(self, success=None, code=None):
        """
        Initialize CreateLogStoreResponse instance.

        :param success: 请求是否成功
        :type success: bool (optional)

        :param code: 请求码，成功为OK，错误为具体的错误码
        :type code: str (optional)
        """
        super().__init__()
        self.success = success
        self.code = code

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        Includes metadata from the parent BceResponse class.

        :return: Dictionary representation of the model
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
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateLogStoreResponse

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('code') is not None:
            self.code = m.get('code')
        return self
