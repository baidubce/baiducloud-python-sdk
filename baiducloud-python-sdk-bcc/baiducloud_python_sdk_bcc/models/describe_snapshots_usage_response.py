"""
Request entity for DescribeSnapshotsUsageResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class DescribeSnapshotsUsageResponse(BceResponse):
    """
    DescribeSnapshotsUsageResponse
    """

    def __init__(
        self, snapshot_count=None, auto_snapshot_count=None, manual_snapshot_count=None, snapshot_capacity=None
    ):
        """
        Initialize DescribeSnapshotsUsageResponse response.

        :param snapshot_count: 该地域下创建的所有快照数量
        :type snapshot_count: int (optional)

        :param auto_snapshot_count: 该地域下创建的自动快照数量
        :type auto_snapshot_count: int (optional)

        :param manual_snapshot_count: 该地域下创建的手动快照数量
        :type manual_snapshot_count: int (optional)

        :param snapshot_capacity: 该地域下快照占用的容量（GB）
        :type snapshot_capacity: float (optional)
        """
        super().__init__()
        self.snapshot_count = snapshot_count
        self.auto_snapshot_count = auto_snapshot_count
        self.manual_snapshot_count = manual_snapshot_count
        self.snapshot_capacity = snapshot_capacity

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
        if self.snapshot_count is not None:
            result['snapshotCount'] = self.snapshot_count
        if self.auto_snapshot_count is not None:
            result['autoSnapshotCount'] = self.auto_snapshot_count
        if self.manual_snapshot_count is not None:
            result['manualSnapshotCount'] = self.manual_snapshot_count
        if self.snapshot_capacity is not None:
            result['snapshotCapacity'] = self.snapshot_capacity
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeSnapshotsUsageResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('snapshotCount') is not None:
            self.snapshot_count = m.get('snapshotCount')
        if m.get('autoSnapshotCount') is not None:
            self.auto_snapshot_count = m.get('autoSnapshotCount')
        if m.get('manualSnapshotCount') is not None:
            self.manual_snapshot_count = m.get('manualSnapshotCount')
        if m.get('snapshotCapacity') is not None:
            self.snapshot_capacity = m.get('snapshotCapacity')
        return self
