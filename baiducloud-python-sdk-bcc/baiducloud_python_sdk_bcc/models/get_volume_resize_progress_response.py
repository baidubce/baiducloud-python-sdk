"""
Request entity for GetVolumeResizeProgressResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class GetVolumeResizeProgressResponse(BceResponse):
    """
    GetVolumeResizeProgressResponse
    """

    def __init__(self, progress=None):
        """
        Initialize GetVolumeResizeProgressResponse response.

        :param progress: 磁盘变配进度
        :type progress: int (optional)
        """
        super().__init__()
        self.progress = progress

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
        if self.progress is not None:
            result['progress'] = self.progress
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetVolumeResizeProgressResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        return self
