"""
Request entity for SyncGroupDelayInfoResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_scs.models.delay_info_console_item import DelayInfoConsoleItem


class SyncGroupDelayInfoResponse(BceResponse):
    """
    SyncGroupDelayInfoResponse
    """

    def __init__(self, delay_info=None):
        """
        Initialize SyncGroupDelayInfoResponse response.

        :param delay_info: 延迟信息列表
        :type delay_info: List[DelayInfoConsoleItem] (optional)
        """
        super().__init__()
        self.delay_info = delay_info

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
        if self.delay_info is not None:
            result['delayInfo'] = [i.to_dict() for i in self.delay_info]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SyncGroupDelayInfoResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('delayInfo') is not None:
            self.delay_info = [DelayInfoConsoleItem().from_dict(i) for i in m.get('delayInfo')]
        return self
