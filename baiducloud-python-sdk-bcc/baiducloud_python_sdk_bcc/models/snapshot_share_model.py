"""
SnapshotShareModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SnapshotShareModel(AbstractModel):
    """
    SnapshotShareModel
    """

    def __init__(
        self,
        source_snapshot_id=None,
        source_snapshot_uuid=None,
        snapshot_id=None,
        source_account_id=None,
        account_id=None,
        snapshot_type=None,
        name=None,
        size_in_gb=None,
        share_time=None,
        desc=None,
        share_status=None,
        encrypt_key=None,
        is_source_deleted=None,
    ):
        """
        Initialize SnapshotShareModel instance.

        :param source_snapshot_id: 源快照ID
        :type source_snapshot_id: str (optional)

        :param source_snapshot_uuid: 源快照uuid
        :type source_snapshot_uuid: str (optional)

        :param snapshot_id: 共享快照ID
        :type snapshot_id: str (optional)

        :param source_account_id: 共享方用户ID
        :type source_account_id: str (optional)

        :param account_id: 接收方用户ID
        :type account_id: str (optional)

        :param snapshot_type: 快照类型
        :type snapshot_type: str (optional)

        :param name: 共享快照名称
        :type name: str (optional)

        :param size_in_gb: 快照大小
        :type size_in_gb: int (optional)

        :param share_time: 快照共享时间
        :type share_time: str (optional)

        :param desc: 共享快照描述
        :type desc: str (optional)

        :param share_status: 共享状态
        :type share_status: str (optional)

        :param encrypt_key: 加密的密钥对
        :type encrypt_key: str (optional)

        :param is_source_deleted: 源快照是否已被删除
        :type is_source_deleted: bool (optional)
        """
        super().__init__()
        self.source_snapshot_id = source_snapshot_id
        self.source_snapshot_uuid = source_snapshot_uuid
        self.snapshot_id = snapshot_id
        self.source_account_id = source_account_id
        self.account_id = account_id
        self.snapshot_type = snapshot_type
        self.name = name
        self.size_in_gb = size_in_gb
        self.share_time = share_time
        self.desc = desc
        self.share_status = share_status
        self.encrypt_key = encrypt_key
        self.is_source_deleted = is_source_deleted

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.source_snapshot_id is not None:
            result['sourceSnapshotId'] = self.source_snapshot_id
        if self.source_snapshot_uuid is not None:
            result['sourceSnapshotUuid'] = self.source_snapshot_uuid
        if self.snapshot_id is not None:
            result['snapshotId'] = self.snapshot_id
        if self.source_account_id is not None:
            result['sourceAccountId'] = self.source_account_id
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.snapshot_type is not None:
            result['snapshotType'] = self.snapshot_type
        if self.name is not None:
            result['name'] = self.name
        if self.size_in_gb is not None:
            result['sizeInGB'] = self.size_in_gb
        if self.share_time is not None:
            result['shareTime'] = self.share_time
        if self.desc is not None:
            result['desc'] = self.desc
        if self.share_status is not None:
            result['shareStatus'] = self.share_status
        if self.encrypt_key is not None:
            result['encryptKey'] = self.encrypt_key
        if self.is_source_deleted is not None:
            result['isSourceDeleted'] = self.is_source_deleted
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SnapshotShareModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('sourceSnapshotId') is not None:
            self.source_snapshot_id = m.get('sourceSnapshotId')
        if m.get('sourceSnapshotUuid') is not None:
            self.source_snapshot_uuid = m.get('sourceSnapshotUuid')
        if m.get('snapshotId') is not None:
            self.snapshot_id = m.get('snapshotId')
        if m.get('sourceAccountId') is not None:
            self.source_account_id = m.get('sourceAccountId')
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('snapshotType') is not None:
            self.snapshot_type = m.get('snapshotType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sizeInGB') is not None:
            self.size_in_gb = m.get('sizeInGB')
        if m.get('shareTime') is not None:
            self.share_time = m.get('shareTime')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('shareStatus') is not None:
            self.share_status = m.get('shareStatus')
        if m.get('encryptKey') is not None:
            self.encrypt_key = m.get('encryptKey')
        if m.get('isSourceDeleted') is not None:
            self.is_source_deleted = m.get('isSourceDeleted')
        return self
