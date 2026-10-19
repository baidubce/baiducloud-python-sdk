"""
Request entity for ReleaseInstanceResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class ReleaseInstanceResponse(BceResponse):
    """
    ReleaseInstanceResponse
    """

    def __init__(self, success=None, message=None, release_failed_instance_ids=None):
        """
        Initialize ReleaseInstanceResponse response.

        :param success: 释放是否成功。true：成功，false：失败
        :type success: bool (optional)

        :param message: 提示信息，成功时为 null
        :type message: str (optional)

        :param release_failed_instance_ids: 释放失败的实例ID列表，全部成功时为空数组
        :type release_failed_instance_ids: List[str] (optional)
        """
        super().__init__()
        self.success = success
        self.message = message
        self.release_failed_instance_ids = release_failed_instance_ids

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
        if self.release_failed_instance_ids is not None:
            result['releaseFailedInstanceIds'] = self.release_failed_instance_ids
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ReleaseInstanceResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('releaseFailedInstanceIds') is not None:
            self.release_failed_instance_ids = m.get('releaseFailedInstanceIds')
        return self
