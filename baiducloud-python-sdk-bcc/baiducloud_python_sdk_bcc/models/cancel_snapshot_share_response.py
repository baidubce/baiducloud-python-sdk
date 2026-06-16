"""
Request entity for CancelSnapshotShareResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CancelSnapshotShareResponse(BceResponse):
    """
    CancelSnapshotShareResponse
    """

    def __init__(self, source_snapshot_id=None, share_snapshot_id=None):
        """
        Initialize CancelSnapshotShareResponse response.

        :param source_snapshot_id: 源快照ID
        :type source_snapshot_id: str (optional)

        :param share_snapshot_id: 共享快照ID
        :type share_snapshot_id: str (optional)
        """
        super().__init__()
        self.source_snapshot_id = source_snapshot_id
        self.share_snapshot_id = share_snapshot_id

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
        if self.source_snapshot_id is not None:
            result['sourceSnapshotId'] = self.source_snapshot_id
        if self.share_snapshot_id is not None:
            result['shareSnapshotId'] = self.share_snapshot_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CancelSnapshotShareResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('sourceSnapshotId') is not None:
            self.source_snapshot_id = m.get('sourceSnapshotId')
        if m.get('shareSnapshotId') is not None:
            self.share_snapshot_id = m.get('shareSnapshotId')
        return self
