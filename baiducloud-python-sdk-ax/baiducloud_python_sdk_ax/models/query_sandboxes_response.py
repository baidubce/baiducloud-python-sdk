"""
Request entity for QuerySandboxesResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_ax.models.queried_sandbox import QueriedSandbox


class QuerySandboxesResponse(BceResponse):
    """
    QuerySandboxesResponse
    """

    def __init__(self, sandboxes=None, next_token=None):
        """
        Initialize QuerySandboxesResponse response.

        :param sandboxes: 满足过滤条件的沙箱实例列表。
        :type sandboxes: List[QueriedSandbox] (optional)

        :param next_token: 下一页游标。为空表示没有更多数据。
        :type next_token: str (optional)
        """
        super().__init__()
        self.sandboxes = sandboxes
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
        if self.sandboxes is not None:
            result['sandboxes'] = [i.to_dict() for i in self.sandboxes]
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
        :rtype: QuerySandboxesResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('sandboxes') is not None:
            self.sandboxes = [QueriedSandbox().from_dict(i) for i in m.get('sandboxes')]
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self
