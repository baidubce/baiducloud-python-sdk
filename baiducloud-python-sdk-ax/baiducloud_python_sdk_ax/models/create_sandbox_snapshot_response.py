"""
Request entity for CreateSandboxSnapshotResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateSandboxSnapshotResponse(BceResponse):
    """
    CreateSandboxSnapshotResponse
    """

    def __init__(self, snapshot_id=None, names=None):
        """
        Initialize CreateSandboxSnapshotResponse response.

        :param snapshot_id: 快照模板 ID。
        :type snapshot_id: str (optional)

        :param names: 快照模板名称列表。
        :type names: List[str] (optional)
        """
        super().__init__()
        self.snapshot_id = snapshot_id
        self.names = names

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
        if self.snapshot_id is not None:
            result['snapshotID'] = self.snapshot_id
        if self.names is not None:
            result['names'] = self.names
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateSandboxSnapshotResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('snapshotID') is not None:
            self.snapshot_id = m.get('snapshotID')
        if m.get('names') is not None:
            self.names = m.get('names')
        return self
