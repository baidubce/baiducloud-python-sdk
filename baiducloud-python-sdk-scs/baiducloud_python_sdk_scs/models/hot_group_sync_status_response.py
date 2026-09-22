"""
Request entity for HotGroupSyncStatusResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_scs.models.followers import Followers


class HotGroupSyncStatusResponse(BceResponse):
    """
    HotGroupSyncStatusResponse
    """

    def __init__(self, followers=None):
        """
        Initialize HotGroupSyncStatusResponse response.

        :param followers: 热活实例组ID
        :type followers: List[Followers] (optional)
        """
        super().__init__()
        self.followers = followers

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
        if self.followers is not None:
            result['followers'] = [i.to_dict() for i in self.followers]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HotGroupSyncStatusResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('followers') is not None:
            self.followers = [Followers().from_dict(i) for i in m.get('followers')]
        return self
