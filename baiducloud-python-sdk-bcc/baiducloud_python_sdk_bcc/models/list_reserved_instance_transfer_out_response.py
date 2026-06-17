"""
Request entity for ListReservedInstanceTransferOutResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcc.models.transfer_out_record import TransferOutRecord


class ListReservedInstanceTransferOutResponse(BceResponse):
    """
    ListReservedInstanceTransferOutResponse
    """

    def __init__(
        self, marker=None, is_truncated=None, next_marker=None, max_keys=None, total_count=None, transfer_records=None
    ):
        """
        Initialize ListReservedInstanceTransferOutResponse response.

        :param marker: 当前页标记
        :type marker: str (optional)

        :param is_truncated: 是否还有下一页
        :type is_truncated: bool (optional)

        :param next_marker: 下一页标记
        :type next_marker: str (optional)

        :param max_keys: 每页最大数量
        :type max_keys: int (optional)

        :param total_count: 预留实例券转移记录总数
        :type total_count: int (optional)

        :param transfer_records: 预留实例券转移记录详情
        :type transfer_records: List[TransferOutRecord] (optional)
        """
        super().__init__()
        self.marker = marker
        self.is_truncated = is_truncated
        self.next_marker = next_marker
        self.max_keys = max_keys
        self.total_count = total_count
        self.transfer_records = transfer_records

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
        if self.marker is not None:
            result['marker'] = self.marker
        if self.is_truncated is not None:
            result['isTruncated'] = self.is_truncated
        if self.next_marker is not None:
            result['nextMarker'] = self.next_marker
        if self.max_keys is not None:
            result['maxKeys'] = self.max_keys
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.transfer_records is not None:
            result['transferRecords'] = [i.to_dict() for i in self.transfer_records]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListReservedInstanceTransferOutResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('isTruncated') is not None:
            self.is_truncated = m.get('isTruncated')
        if m.get('nextMarker') is not None:
            self.next_marker = m.get('nextMarker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('transferRecords') is not None:
            self.transfer_records = [TransferOutRecord().from_dict(i) for i in m.get('transferRecords')]
        return self
