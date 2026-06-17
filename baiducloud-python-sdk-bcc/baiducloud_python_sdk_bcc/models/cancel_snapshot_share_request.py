"""
Request entity for CancelSnapshotShareRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CancelSnapshotShareRequest(AbstractModel):
    """
    Request entity for CancelSnapshotShareRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, source_snapshot_id, share_snapshot_id, account_ids=None):
        """
        Initialize CancelSnapshotShareRequest request entity.

        :param source_snapshot_id: 源快照需取消共享ID，共享方取消快照共享时必填。
        :type source_snapshot_id: str (required)

        :param account_ids: 共享方可指定取消共享的接收方账号ID，不填时默认取消全部共享。
        :type account_ids: List[str] (optional)

        :param share_snapshot_id: 已接收需取消共享的快照ID，接收方必填。
        :type share_snapshot_id: str (required)
        """
        super().__init__()
        self.source_snapshot_id = source_snapshot_id
        self.account_ids = account_ids
        self.share_snapshot_id = share_snapshot_id

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
        if self.source_snapshot_id is not None:
            result['sourceSnapshotId'] = self.source_snapshot_id
        if self.account_ids is not None:
            result['accountIds'] = self.account_ids
        if self.share_snapshot_id is not None:
            result['shareSnapshotId'] = self.share_snapshot_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CancelSnapshotShareRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('sourceSnapshotId') is not None:
            self.source_snapshot_id = m.get('sourceSnapshotId')
        if m.get('accountIds') is not None:
            self.account_ids = m.get('accountIds')
        if m.get('shareSnapshotId') is not None:
            self.share_snapshot_id = m.get('shareSnapshotId')
        return self
