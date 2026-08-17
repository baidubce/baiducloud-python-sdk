"""
Request entity for GetConsumerListResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_aigw.models.consumer_summary import ConsumerSummary


class GetConsumerListResponse(BceResponse):
    """
    GetConsumerListResponse
    """

    def __init__(self, success=None, status=None, total=None, consumers=None, next_token=None):
        """
        Initialize GetConsumerListResponse response.

        :param success: 是否成功
        :type success: bool (optional)

        :param status: HTTP 状态码
        :type status: int (optional)

        :param total: 消费者总数
        :type total: int (optional)

        :param consumers: 消费者摘要列表
        :type consumers: List[ConsumerSummary] (optional)

        :param next_token: 下一页令牌
        :type next_token: str (optional)
        """
        super().__init__()
        self.success = success
        self.status = status
        self.total = total
        self.consumers = consumers
        self.next_token = next_token

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
        if self.total is not None:
            result['total'] = self.total
        if self.consumers is not None:
            result['consumers'] = [i.to_dict() for i in self.consumers]
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetConsumerListResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('consumers') is not None:
            self.consumers = [ConsumerSummary().from_dict(i) for i in m.get('consumers')]
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self
