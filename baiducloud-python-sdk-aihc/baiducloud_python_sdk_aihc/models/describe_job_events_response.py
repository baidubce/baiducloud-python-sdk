"""
Request entity for DescribeJobEventsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_aihc.models.event import Event


class DescribeJobEventsResponse(BceResponse):
    """
    DescribeJobEventsResponse
    """

    def __init__(self, request_id=None, events=None, total=None):
        """
        Initialize DescribeJobEventsResponse response.

        :param request_id: 请求ID，用于标译每个请求的唯一性
        :type request_id: str (optional)

        :param events: 事件列表
        :type events: List[Event] (optional)

        :param total: 事件的总数
        :type total: int (optional)
        """
        super().__init__()
        self.request_id = request_id
        self.events = events
        self.total = total

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.events is not None:
            result['events'] = [i.to_dict() for i in self.events]
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeJobEventsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('events') is not None:
            self.events = [Event().from_dict(i) for i in m.get('events')]
        if m.get('total') is not None:
            self.total = m.get('total')
        return self
