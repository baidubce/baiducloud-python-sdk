"""
Request entity for ListL3ClientsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_pfs.models.l3_client_model import L3ClientModel


class ListL3ClientsResponse(BceResponse):
    """
    ListL3ClientsResponse
    """

    def __init__(self, request_id=None, result=None, marker=None, max_keys=None, is_truncated=None, next_marker=None):
        """
        Initialize ListL3ClientsResponse response.

        :param request_id: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type request_id: str (optional)

        :param result: 返回的客户端列表，元素见下表
        :type result: List[L3ClientModel] (optional)

        :param marker: 本轮请求使用的 marker
        :type marker: str (optional)

        :param max_keys: 本轮请求生效的分页大小上限
        :type max_keys: int (optional)

        :param is_truncated: 是否被截断，false 表示本轮已返回全部数据
        :type is_truncated: bool (optional)

        :param next_marker: 下一轮请求应传入的 marker，未截断时为 null
        :type next_marker: str (optional)
        """
        super().__init__()
        self.request_id = request_id
        self.result = result
        self.marker = marker
        self.max_keys = max_keys
        self.is_truncated = is_truncated
        self.next_marker = next_marker

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
        if self.result is not None:
            result['result'] = [i.to_dict() for i in self.result]
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_keys is not None:
            result['maxKeys'] = self.max_keys
        if self.is_truncated is not None:
            result['isTruncated'] = self.is_truncated
        if self.next_marker is not None:
            result['nextMarker'] = self.next_marker
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListL3ClientsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = [L3ClientModel().from_dict(i) for i in m.get('result')]
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('isTruncated') is not None:
            self.is_truncated = m.get('isTruncated')
        if m.get('nextMarker') is not None:
            self.next_marker = m.get('nextMarker')
        return self
