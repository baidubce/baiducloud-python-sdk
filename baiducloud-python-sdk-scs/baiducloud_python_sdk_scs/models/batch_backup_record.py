"""
BatchBackupRecord information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_scs.models.record import Record


class BatchBackupRecord(AbstractModel):
    """
    BatchBackupRecord
    """

    def __init__(self, batch_id=None, backup_type=None, comment=None, start_time=None, recoverable=None, records=None):
        """
        Initialize BatchBackupRecord instance.

        :param batch_id: 备份ID
        :type batch_id: str (optional)

        :param backup_type: 备份类型。auto表示自动备份；manual表示手动产生的备份
        :type backup_type: str (optional)

        :param comment: 备注
        :type comment: str (optional)

        :param start_time: 开始时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'
        :type start_time: str (optional)

        :param recoverable: 是否可用于备份恢复。recoverable - 可用；non-recoverable - 不可用
        :type recoverable: str (optional)

        :param records: 按分片备份的列表。
        :type records: List[Record] (optional)
        """
        super().__init__()
        self.batch_id = batch_id
        self.backup_type = backup_type
        self.comment = comment
        self.start_time = start_time
        self.recoverable = recoverable
        self.records = records

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
        if self.batch_id is not None:
            result['batchId'] = self.batch_id
        if self.backup_type is not None:
            result['backupType'] = self.backup_type
        if self.comment is not None:
            result['comment'] = self.comment
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.recoverable is not None:
            result['recoverable'] = self.recoverable
        if self.records is not None:
            result['records'] = [i.to_dict() for i in self.records]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BatchBackupRecord

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('batchId') is not None:
            self.batch_id = m.get('batchId')
        if m.get('backupType') is not None:
            self.backup_type = m.get('backupType')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('recoverable') is not None:
            self.recoverable = m.get('recoverable')
        if m.get('records') is not None:
            self.records = [Record().from_dict(i) for i in m.get('records')]
        return self
