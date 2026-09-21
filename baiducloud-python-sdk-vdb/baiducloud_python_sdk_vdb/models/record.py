"""
Record information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_vdb.models.batch_record import BatchRecord


class Record(AbstractModel):
    """
    Record
    """

    def __init__(
        self,
        backup_type=None,
        batch_id=None,
        batch_records=None,
        comment=None,
        end_time=None,
        recoverable=None,
        start_time=None,
        status=None,
        storage_type=None,
        total_size_bytes=None,
    ):
        """
        Initialize Record instance.

        :param backup_type:
        :type backup_type: str (optional)

        :param batch_id:
        :type batch_id: str (optional)

        :param batch_records:
        :type batch_records: List[BatchRecord] (optional)

        :param comment:
        :type comment: str (optional)

        :param end_time:
        :type end_time: str (optional)

        :param recoverable:
        :type recoverable: str (optional)

        :param start_time:
        :type start_time: str (optional)

        :param status:
        :type status: str (optional)

        :param storage_type:
        :type storage_type: str (optional)

        :param total_size_bytes:
        :type total_size_bytes: int (optional)
        """
        super().__init__()
        self.backup_type = backup_type
        self.batch_id = batch_id
        self.batch_records = batch_records
        self.comment = comment
        self.end_time = end_time
        self.recoverable = recoverable
        self.start_time = start_time
        self.status = status
        self.storage_type = storage_type
        self.total_size_bytes = total_size_bytes

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
        if self.backup_type is not None:
            result['backupType'] = self.backup_type
        if self.batch_id is not None:
            result['batchId'] = self.batch_id
        if self.batch_records is not None:
            result['batchRecords'] = [i.to_dict() for i in self.batch_records]
        if self.comment is not None:
            result['comment'] = self.comment
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.recoverable is not None:
            result['recoverable'] = self.recoverable
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.storage_type is not None:
            result['storageType'] = self.storage_type
        if self.total_size_bytes is not None:
            result['totalSizeBytes'] = self.total_size_bytes
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
        if m.get('backupType') is not None:
            self.backup_type = m.get('backupType')
        if m.get('batchId') is not None:
            self.batch_id = m.get('batchId')
        if m.get('batchRecords') is not None:
            self.batch_records = [BatchRecord().from_dict(i) for i in m.get('batchRecords')]
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('recoverable') is not None:
            self.recoverable = m.get('recoverable')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('storageType') is not None:
            self.storage_type = m.get('storageType')
        if m.get('totalSizeBytes') is not None:
            self.total_size_bytes = m.get('totalSizeBytes')
        return self
