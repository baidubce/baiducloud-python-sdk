"""
Request entity for DeleteApikeyPermanentlyValidResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class DeleteApikeyPermanentlyValidResponse(BceResponse):
    """
    DeleteApikeyPermanentlyValidResponse
    """

    def __init__(self, success=None, status=None):
        """
        Initialize DeleteApikeyPermanentlyValidResponse response.

        :param success: 标识
        :type success: bool (optional)

        :param status: 状态吗
        :type status: int (optional)
        """
        super().__init__()
        self.success = success
        self.status = status

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
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteApikeyPermanentlyValidResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self
