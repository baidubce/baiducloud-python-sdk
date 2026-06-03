"""
Request entity for ListL2PolicyResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_pfs.models.policy_info import PolicyInfo


class ListL2PolicyResponse(BceResponse):
    """
    ListL2PolicyResponse
    """

    def __init__(self, request_id=None, is_truncated=None, max_keys=None, marker=None, next_marker=None, result=None):
        """
        Initialize ListL2PolicyResponse response.

        :param request_id: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type request_id: str (optional)

        :param is_truncated: <li>True表示数据未全部返回<br><li>False表示数据全部返回
        :type is_truncated: bool (optional)

        :param max_keys: 请求返回的result个数
        :type max_keys: int (optional)

        :param marker: 本次请求的起始位置
        :type marker: str (optional)

        :param next_marker: 下次请求的起始位置
        :type next_marker: str (optional)

        :param result: policy任务的详细列表
        :type result: List[PolicyInfo] (optional)
        """
        super().__init__()
        self.request_id = request_id
        self.is_truncated = is_truncated
        self.max_keys = max_keys
        self.marker = marker
        self.next_marker = next_marker
        self.result = result

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
        if self.is_truncated is not None:
            result['isTruncated'] = self.is_truncated
        if self.max_keys is not None:
            result['maxKeys'] = self.max_keys
        if self.marker is not None:
            result['marker'] = self.marker
        if self.next_marker is not None:
            result['nextMarker'] = self.next_marker
        if self.result is not None:
            result['result'] = [i.to_dict() for i in self.result]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListL2PolicyResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('isTruncated') is not None:
            self.is_truncated = m.get('isTruncated')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('nextMarker') is not None:
            self.next_marker = m.get('nextMarker')
        if m.get('result') is not None:
            self.result = [PolicyInfo().from_dict(i) for i in m.get('result')]
        return self
