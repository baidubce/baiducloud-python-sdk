"""
Request entity for CreateSnapshotShareRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateSnapshotShareRequest(AbstractModel):
    """
    Request entity for CreateSnapshotShareRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, snapshot_id, account_ids):
        """
        Initialize CreateSnapshotShareRequest request entity.

        :param snapshot_id: 需要操作共享的快照
        :type snapshot_id: str (required)

        :param account_ids: account_ids parameter
        :type account_ids: List[str] (required)
        """
        super().__init__()
        self.snapshot_id = snapshot_id
        self.account_ids = account_ids

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.snapshot_id is not None:
            result['snapshotId'] = self.snapshot_id
        if self.account_ids is not None:
            result['accountIds'] = self.account_ids
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateSnapshotShareRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('snapshotId') is not None:
            self.snapshot_id = m.get('snapshotId')
        if m.get('accountIds') is not None:
            self.account_ids = m.get('accountIds')
        return self
