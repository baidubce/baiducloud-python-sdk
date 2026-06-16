"""
Request entity for GetSnapshotResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcc.models.snapshot_model import SnapshotModel


class GetSnapshotResponse(BceResponse):
    """
    GetSnapshotResponse
    """

    def __init__(self, snapshot=None):
        """
        Initialize GetSnapshotResponse response.

        :param snapshot: snapshot field
        :type snapshot: SnapshotModel (optional)
        """
        super().__init__()
        self.snapshot = snapshot

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
        if self.snapshot is not None:
            result['snapshot'] = self.snapshot.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetSnapshotResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('snapshot') is not None:
            self.snapshot = SnapshotModel().from_dict(m.get('snapshot'))
        return self
