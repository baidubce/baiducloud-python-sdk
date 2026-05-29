"""
Request entity for CreateFileSystemResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateFileSystemResponse(BceResponse):
    """
    CreateFileSystemResponse
    """

    def __init__(self, fs_id=None):
        """
        Initialize CreateFileSystemResponse response.

        :param fs_id: FileSystem的ID。后续针对该实例的操作，均需要在请求中带上此ID。
        :type fs_id: str (optional)
        """
        super().__init__()
        self.fs_id = fs_id

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
        if self.fs_id is not None:
            result['fsId'] = self.fs_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateFileSystemResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('fsId') is not None:
            self.fs_id = m.get('fsId')
        return self
