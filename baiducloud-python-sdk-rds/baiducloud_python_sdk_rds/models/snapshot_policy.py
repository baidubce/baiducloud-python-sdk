"""
SnapshotPolicy information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_rds.models.data_backup_retain_strategy import DataBackupRetainStrategy

from baiducloud_python_sdk_rds.models.encrypt_strategy import EncryptStrategy


class SnapshotPolicy(AbstractModel):
    """
    SnapshotPolicy
    """

    def __init__(
        self,
        backup_time=None,
        backup_days=None,
        persistent=None,
        expire_in_days=None,
        log_backup_retain_days=None,
        free_space_in_gb=None,
        data_backup_type=None,
        free_space=None,
        incremental_data_backup_enable=None,
        time_unit=None,
        data_backup_copy_enable=None,
        incremental_data_backup_interval=None,
        latest_data_backup_retain_days=None,
        retention_period=None,
        data_backup_retain_strategys=None,
        encrypt_strategy=None,
    ):
        """
        Initialize SnapshotPolicy instance.

        :param backup_time: 备份时间. 时:分:秒Z。
        :type backup_time: str (optional)

        :param backup_days: 以英文半角逗号分隔的备份时日间，周日为第一天。
        :type backup_days: str (optional)

        :param persistent: 是否启用备份数据持久化。 true：是 ，false：否。
        :type persistent: bool (optional)

        :param expire_in_days: 持久化天数（单位:天数）。
        :type expire_in_days: int (optional)

        :param log_backup_retain_days: 日志备份保留时长（单位:天数）。
        :type log_backup_retain_days: int (optional)

        :param free_space_in_gb: 空闲空间大小（单位:GB）。
        :type free_space_in_gb: int (optional)

        :param data_backup_type: 备份类型，支持physical/snapshot， 取值为：snapshot，磁盘类型为ssd将不支持快照备份。
        :type data_backup_type: str (optional)

        :param free_space: 空闲空间大小（单位:MB）。
        :type free_space: int (optional)

        :param incremental_data_backup_enable: 是否开启高频备份，默认为 false。
        :type incremental_data_backup_enable: bool (optional)

        :param time_unit: 增量备份保留策略时长单位，取值为 week、month，默认为 week。
        :type time_unit: str (optional)

        :param data_backup_copy_enable: 是否开启备份跨区域复制。true：是，false：否。
        :type data_backup_copy_enable: bool (optional)

        :param incremental_data_backup_interval: 增量数据备份间隔（秒）最小粒度是小时级别。
        :type incremental_data_backup_interval: int (optional)

        :param latest_data_backup_retain_days: 最新数据备份保留天数（实例删除后），天级别。
        :type latest_data_backup_retain_days: int (optional)

        :param retention_period: 增量备份保留时长。
        :type retention_period: int (optional)

        :param data_backup_retain_strategys: 数据备份保留策略列表。
        :type data_backup_retain_strategys: List[DataBackupRetainStrategy] (optional)

        :param encrypt_strategy: encrypt_strategy attribute
        :type encrypt_strategy: EncryptStrategy (optional)
        """
        super().__init__()
        self.backup_time = backup_time
        self.backup_days = backup_days
        self.persistent = persistent
        self.expire_in_days = expire_in_days
        self.log_backup_retain_days = log_backup_retain_days
        self.free_space_in_gb = free_space_in_gb
        self.data_backup_type = data_backup_type
        self.free_space = free_space
        self.incremental_data_backup_enable = incremental_data_backup_enable
        self.time_unit = time_unit
        self.data_backup_copy_enable = data_backup_copy_enable
        self.incremental_data_backup_interval = incremental_data_backup_interval
        self.latest_data_backup_retain_days = latest_data_backup_retain_days
        self.retention_period = retention_period
        self.data_backup_retain_strategys = data_backup_retain_strategys
        self.encrypt_strategy = encrypt_strategy

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
        if self.backup_time is not None:
            result['backupTime'] = self.backup_time
        if self.backup_days is not None:
            result['backupDays'] = self.backup_days
        if self.persistent is not None:
            result['persistent'] = self.persistent
        if self.expire_in_days is not None:
            result['expireInDays'] = self.expire_in_days
        if self.log_backup_retain_days is not None:
            result['logBackupRetainDays'] = self.log_backup_retain_days
        if self.free_space_in_gb is not None:
            result['freeSpaceInGB'] = self.free_space_in_gb
        if self.data_backup_type is not None:
            result['dataBackupType'] = self.data_backup_type
        if self.free_space is not None:
            result['freeSpace'] = self.free_space
        if self.incremental_data_backup_enable is not None:
            result['incrementalDataBackupEnable'] = self.incremental_data_backup_enable
        if self.time_unit is not None:
            result['timeUnit'] = self.time_unit
        if self.data_backup_copy_enable is not None:
            result['dataBackupCopyEnable'] = self.data_backup_copy_enable
        if self.incremental_data_backup_interval is not None:
            result['incrementalDataBackupInterval'] = self.incremental_data_backup_interval
        if self.latest_data_backup_retain_days is not None:
            result['latestDataBackupRetainDays'] = self.latest_data_backup_retain_days
        if self.retention_period is not None:
            result['retentionPeriod'] = self.retention_period
        if self.data_backup_retain_strategys is not None:
            result['dataBackupRetainStrategys'] = [i.to_dict() for i in self.data_backup_retain_strategys]
        if self.encrypt_strategy is not None:
            result['encryptStrategy'] = self.encrypt_strategy.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SnapshotPolicy

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('backupTime') is not None:
            self.backup_time = m.get('backupTime')
        if m.get('backupDays') is not None:
            self.backup_days = m.get('backupDays')
        if m.get('persistent') is not None:
            self.persistent = m.get('persistent')
        if m.get('expireInDays') is not None:
            self.expire_in_days = m.get('expireInDays')
        if m.get('logBackupRetainDays') is not None:
            self.log_backup_retain_days = m.get('logBackupRetainDays')
        if m.get('freeSpaceInGB') is not None:
            self.free_space_in_gb = m.get('freeSpaceInGB')
        if m.get('dataBackupType') is not None:
            self.data_backup_type = m.get('dataBackupType')
        if m.get('freeSpace') is not None:
            self.free_space = m.get('freeSpace')
        if m.get('incrementalDataBackupEnable') is not None:
            self.incremental_data_backup_enable = m.get('incrementalDataBackupEnable')
        if m.get('timeUnit') is not None:
            self.time_unit = m.get('timeUnit')
        if m.get('dataBackupCopyEnable') is not None:
            self.data_backup_copy_enable = m.get('dataBackupCopyEnable')
        if m.get('incrementalDataBackupInterval') is not None:
            self.incremental_data_backup_interval = m.get('incrementalDataBackupInterval')
        if m.get('latestDataBackupRetainDays') is not None:
            self.latest_data_backup_retain_days = m.get('latestDataBackupRetainDays')
        if m.get('retentionPeriod') is not None:
            self.retention_period = m.get('retentionPeriod')
        if m.get('dataBackupRetainStrategys') is not None:
            self.data_backup_retain_strategys = [
                DataBackupRetainStrategy().from_dict(i) for i in m.get('dataBackupRetainStrategys')
            ]
        if m.get('encryptStrategy') is not None:
            self.encrypt_strategy = EncryptStrategy().from_dict(m.get('encryptStrategy'))
        return self
