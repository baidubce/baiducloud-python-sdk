"""
Request entity for ListOsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcc.models.os_model import OsModel


class ListOsResponse(BceResponse):
    """
    ListOsResponse
    """

    def __init__(self, os_info=None):
        """
        Initialize ListOsResponse response.

        :param os_info: 返回的OS列表
        :type os_info: List[OsModel] (optional)
        """
        super().__init__()
        self.os_info = os_info

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
        if self.os_info is not None:
            result['osInfo'] = [i.to_dict() for i in self.os_info]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListOsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('osInfo') is not None:
            self.os_info = [OsModel().from_dict(i) for i in m.get('osInfo')]
        return self
