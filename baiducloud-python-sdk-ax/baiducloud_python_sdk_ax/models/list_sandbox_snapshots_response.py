"""
Request entity for ListSandboxSnapshotsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_ax.models.snapshot_info import SnapshotInfo


class ListSandboxSnapshotsResponse(BceResponse):
    """
    ListSandboxSnapshotsResponse
    """

    def __init__(self, sandbox_id=None, snapshots=None):
        """
        Initialize ListSandboxSnapshotsResponse response.

        :param sandbox_id: 沙箱实例 ID。
        :type sandbox_id: str (optional)

        :param snapshots: 快照列表。
        :type snapshots: List[SnapshotInfo] (optional)
        """
        super().__init__()
        self.sandbox_id = sandbox_id
        self.snapshots = snapshots

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
        if self.sandbox_id is not None:
            result['sandboxId'] = self.sandbox_id
        if self.snapshots is not None:
            result['snapshots'] = [i.to_dict() for i in self.snapshots]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListSandboxSnapshotsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('sandboxId') is not None:
            self.sandbox_id = m.get('sandboxId')
        if m.get('snapshots') is not None:
            self.snapshots = [SnapshotInfo().from_dict(i) for i in m.get('snapshots')]
        return self
