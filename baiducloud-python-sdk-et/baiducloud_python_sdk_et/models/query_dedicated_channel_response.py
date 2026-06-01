"""
Request entity for QueryDedicatedChannelResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_et.models.et_channel import EtChannel


class QueryDedicatedChannelResponse(BceResponse):
    """
    QueryDedicatedChannelResponse
    """

    def __init__(self, et_channels=None):
        """
        Initialize QueryDedicatedChannelResponse response.

        :param et_channels: 专线通道列表
        :type et_channels: List[EtChannel] (optional)
        """
        super().__init__()
        self.et_channels = et_channels

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
        if self.et_channels is not None:
            result['etChannels'] = [i.to_dict() for i in self.et_channels]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QueryDedicatedChannelResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('etChannels') is not None:
            self.et_channels = [EtChannel().from_dict(i) for i in m.get('etChannels')]
        return self
