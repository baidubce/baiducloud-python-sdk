"""
Record information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Record(AbstractModel):
    """
    Record
    """

    def __init__(
        self,
        backup_record_id=None,
        backup_id=None,
        start_time=None,
        duration=None,
        object_size=None,
        backup_type=None,
        backup_status=None,
        shard_name=None,
        comment=None,
    ):
        """
        Initialize Record instance.

        :param backup_record_id: 备份记录ID。
        :type backup_record_id: str (optional)

        :param backup_id: 备份记录ID。
        :type backup_id: str (optional)

        :param start_time: 开始时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'
        :type start_time: str (optional)

        :param duration: 持续时间
        :type duration: int (optional)

        :param object_size: 文件大小
        :type object_size: int (optional)

        :param backup_type: 备份类型。 auto：自动备份；manual：手动备份
        :type backup_type: str (optional)

        :param backup_status: [备份状态](#BackupStatus)
        :type backup_status: str (optional)

        :param shard_name: 分片名称
        :type shard_name: str (optional)

        :param comment: 备注
        :type comment: str (optional)
        """
        super().__init__()
        self.backup_record_id = backup_record_id
        self.backup_id = backup_id
        self.start_time = start_time
        self.duration = duration
        self.object_size = object_size
        self.backup_type = backup_type
        self.backup_status = backup_status
        self.shard_name = shard_name
        self.comment = comment

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
        if self.backup_record_id is not None:
            result['backupRecordId'] = self.backup_record_id
        if self.backup_id is not None:
            result['backupId'] = self.backup_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.duration is not None:
            result['duration'] = self.duration
        if self.object_size is not None:
            result['objectSize'] = self.object_size
        if self.backup_type is not None:
            result['backupType'] = self.backup_type
        if self.backup_status is not None:
            result['backupStatus'] = self.backup_status
        if self.shard_name is not None:
            result['shardName'] = self.shard_name
        if self.comment is not None:
            result['comment'] = self.comment
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Record

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('backupRecordId') is not None:
            self.backup_record_id = m.get('backupRecordId')
        if m.get('backupId') is not None:
            self.backup_id = m.get('backupId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('objectSize') is not None:
            self.object_size = m.get('objectSize')
        if m.get('backupType') is not None:
            self.backup_type = m.get('backupType')
        if m.get('backupStatus') is not None:
            self.backup_status = m.get('backupStatus')
        if m.get('shardName') is not None:
            self.shard_name = m.get('shardName')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        return self
