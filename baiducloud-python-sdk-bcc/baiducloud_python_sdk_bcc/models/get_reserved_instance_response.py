"""
Request entity for GetReservedInstanceResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcc.models.reserved_instance_info import ReservedInstanceInfo


class GetReservedInstanceResponse(BceResponse):
    """
    GetReservedInstanceResponse
    """

    def __init__(
        self,
        total_count=None,
        marker=None,
        max_keys=None,
        next_marker=None,
        is_truncated=None,
        reserved_instances=None,
    ):
        """
        Initialize GetReservedInstanceResponse response.

        :param total_count: 预留实例券的总数量
        :type total_count: int (optional)

        :param marker: 标记查询的起始位置
        :type marker: str (optional)

        :param max_keys: 每页包含的最大数量
        :type max_keys: int (optional)

        :param next_marker: 获取下一页所需要传递的marker值。当isTruncated为false时，该域不出现
        :type next_marker: str (optional)

        :param is_truncated: true表示后面还有数据，false表示已经是最后一页
        :type is_truncated: bool (optional)

        :param reserved_instances: 预留实例券信息，由 ReservedInstanceInfo 组成的集合
        :type reserved_instances: List[ReservedInstanceInfo] (optional)
        """
        super().__init__()
        self.total_count = total_count
        self.marker = marker
        self.max_keys = max_keys
        self.next_marker = next_marker
        self.is_truncated = is_truncated
        self.reserved_instances = reserved_instances

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
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_keys is not None:
            result['maxKeys'] = self.max_keys
        if self.next_marker is not None:
            result['nextMarker'] = self.next_marker
        if self.is_truncated is not None:
            result['isTruncated'] = self.is_truncated
        if self.reserved_instances is not None:
            result['reservedInstances'] = [i.to_dict() for i in self.reserved_instances]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetReservedInstanceResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('nextMarker') is not None:
            self.next_marker = m.get('nextMarker')
        if m.get('isTruncated') is not None:
            self.is_truncated = m.get('isTruncated')
        if m.get('reservedInstances') is not None:
            self.reserved_instances = [ReservedInstanceInfo().from_dict(i) for i in m.get('reservedInstances')]
        return self
