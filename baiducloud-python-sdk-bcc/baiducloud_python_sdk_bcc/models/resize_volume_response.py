"""
Request entity for ResizeVolumeResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class ResizeVolumeResponse(BceResponse):
    """
    ResizeVolumeResponse
    """

    def __init__(self, warning_list=None):
        """
        Initialize ResizeVolumeResponse response.

        :param warning_list: 磁盘扩容变更产生的warning信息
        :type warning_list: List[str] (optional)
        """
        super().__init__()
        self.warning_list = warning_list

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
        if self.warning_list is not None:
            result['warningList'] = self.warning_list
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ResizeVolumeResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('warningList') is not None:
            self.warning_list = m.get('warningList')
        return self
