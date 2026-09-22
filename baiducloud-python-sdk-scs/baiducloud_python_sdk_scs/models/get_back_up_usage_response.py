"""
Request entity for GetBackUpUsageResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class GetBackUpUsageResponse(BceResponse):
    """
    GetBackUpUsageResponse
    """

    def __init__(
        self,
        logical_log_backup_billing_size_bytes=None,
        snapshot_data_backup_size_bytes=None,
        physical_data_backup_size_bytes=None,
        logical_log_backup_size_bytes=None,
        logical_data_backup_size_bytes=None,
        physical_log_backup_size_bytes=None,
        data_type=None,
    ):
        """
        Initialize GetBackUpUsageResponse response.

        :param logical_log_backup_billing_size_bytes: 逻辑日志备份计费大小Bytes（备份到bos的rdb/aof）
        :type logical_log_backup_billing_size_bytes: int (optional)

        :param snapshot_data_backup_size_bytes: 快照数据备份总大小Bytes
        :type snapshot_data_backup_size_bytes: int (optional)

        :param physical_data_backup_size_bytes: 物理数据备份总大小Bytes（备份到bos的rdb）
        :type physical_data_backup_size_bytes: int (optional)

        :param logical_log_backup_size_bytes: 逻辑日志备份总大小Bytes（备份到bos的rdb/aof）
        :type logical_log_backup_size_bytes: int (optional)

        :param logical_data_backup_size_bytes: 逻辑数据备份总大小
        :type logical_data_backup_size_bytes: int (optional)

        :param physical_log_backup_size_bytes: 物理日志备份总大小
        :type physical_log_backup_size_bytes: int (optional)

        :param data_type: 固定为Redis
        :type data_type: str (optional)
        """
        super().__init__()
        self.logical_log_backup_billing_size_bytes = logical_log_backup_billing_size_bytes
        self.snapshot_data_backup_size_bytes = snapshot_data_backup_size_bytes
        self.physical_data_backup_size_bytes = physical_data_backup_size_bytes
        self.logical_log_backup_size_bytes = logical_log_backup_size_bytes
        self.logical_data_backup_size_bytes = logical_data_backup_size_bytes
        self.physical_log_backup_size_bytes = physical_log_backup_size_bytes
        self.data_type = data_type

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
        if self.logical_log_backup_billing_size_bytes is not None:
            result['logicalLogBackupBillingSizeBytes'] = self.logical_log_backup_billing_size_bytes
        if self.snapshot_data_backup_size_bytes is not None:
            result['snapshotDataBackupSizeBytes'] = self.snapshot_data_backup_size_bytes
        if self.physical_data_backup_size_bytes is not None:
            result['physicalDataBackupSizeBytes'] = self.physical_data_backup_size_bytes
        if self.logical_log_backup_size_bytes is not None:
            result['logicalLogBackupSizeBytes'] = self.logical_log_backup_size_bytes
        if self.logical_data_backup_size_bytes is not None:
            result['logicalDataBackupSizeBytes'] = self.logical_data_backup_size_bytes
        if self.physical_log_backup_size_bytes is not None:
            result['physicalLogBackupSizeBytes'] = self.physical_log_backup_size_bytes
        if self.data_type is not None:
            result['dataType'] = self.data_type
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetBackUpUsageResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('logicalLogBackupBillingSizeBytes') is not None:
            self.logical_log_backup_billing_size_bytes = m.get('logicalLogBackupBillingSizeBytes')
        if m.get('snapshotDataBackupSizeBytes') is not None:
            self.snapshot_data_backup_size_bytes = m.get('snapshotDataBackupSizeBytes')
        if m.get('physicalDataBackupSizeBytes') is not None:
            self.physical_data_backup_size_bytes = m.get('physicalDataBackupSizeBytes')
        if m.get('logicalLogBackupSizeBytes') is not None:
            self.logical_log_backup_size_bytes = m.get('logicalLogBackupSizeBytes')
        if m.get('logicalDataBackupSizeBytes') is not None:
            self.logical_data_backup_size_bytes = m.get('logicalDataBackupSizeBytes')
        if m.get('physicalLogBackupSizeBytes') is not None:
            self.physical_log_backup_size_bytes = m.get('physicalLogBackupSizeBytes')
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        return self
