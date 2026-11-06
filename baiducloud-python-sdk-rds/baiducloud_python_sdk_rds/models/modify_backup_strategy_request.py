"""
Request entity for ModifyBackupStrategyRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModifyBackupStrategyRequest(AbstractModel):
    """
    Request entity for ModifyBackupStrategyRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        instance_id,
        backup_days,
        backup_time,
        persistent,
        expire_in_days=None,
        log_backup_retain_days=None,
        data_backup_type=None,
        incremental_data_backup_enable=None,
        incremental_data_backup_interval=None,
        latest_data_backup_retain_days=None,
        retention_period=None,
        time_unit=None,
        data_backup_copy_enable=None,
        data_backup_copy_storages_regions=None,
        data_backup_copy_retain_days=None,
    ):
        """
        Initialize ModifyBackupStrategyRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param backup_days: 以英文半角逗号分隔的备份时日间，周日为第一天，取值0 举例：\"0,1,2,3,5,6\"
        :type backup_days: str (required)

        :param backup_time: 备份开始时间,这里的时间是用的UTC时间
        :type backup_time: str (required)

        :param persistent: 是否启用备份数据持久化
        :type persistent: bool (required)

        :param expire_in_days: 数据备份保留时长，范围1-730天；未启用则为0或不填
        :type expire_in_days: int (optional)

        :param log_backup_retain_days: 日志备份保留时长，范围1-730天；未启用则为0或不填
        :type log_backup_retain_days: int (optional)

        :param data_backup_type: 类型：physical（物理）、snapshot（快照），仅支持MySQL
        :type data_backup_type: str (optional)

        :param incremental_data_backup_enable: 是否开启高频备份，默认为 false
        :type incremental_data_backup_enable: bool (optional)

        :param incremental_data_backup_interval: 增量数据备份间隔（秒）最小粒度是小时级别，开启高频备份后必传，值需要可以被3600整除
        :type incremental_data_backup_interval: int (optional)

        :param latest_data_backup_retain_days: 最新数据备份保留天数（实例删除后），天级别，不传默认0天
        :type latest_data_backup_retain_days: int (optional)

        :param retention_period: 增量备份保留时长
        :type retention_period: int (optional)

        :param time_unit: 增量备份保留策略时长单位，取值为 week、month，默认为 week
        :type time_unit: str (optional)

        :param data_backup_copy_enable: 标识是否开启跨地域备份，默认为false
        :type data_backup_copy_enable: bool (optional)

        :param data_backup_copy_storages_regions: data_backup_copy_storages_regions parameter
        :type data_backup_copy_storages_regions: List[str] (optional)

        :param data_backup_copy_retain_days: 跨地域备份保留时长支持1-730天
        :type data_backup_copy_retain_days: int (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.backup_days = backup_days
        self.backup_time = backup_time
        self.persistent = persistent
        self.expire_in_days = expire_in_days
        self.log_backup_retain_days = log_backup_retain_days
        self.data_backup_type = data_backup_type
        self.incremental_data_backup_enable = incremental_data_backup_enable
        self.incremental_data_backup_interval = incremental_data_backup_interval
        self.latest_data_backup_retain_days = latest_data_backup_retain_days
        self.retention_period = retention_period
        self.time_unit = time_unit
        self.data_backup_copy_enable = data_backup_copy_enable
        self.data_backup_copy_storages_regions = data_backup_copy_storages_regions
        self.data_backup_copy_retain_days = data_backup_copy_retain_days

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
        if self.backup_days is not None:
            result['backupDays'] = self.backup_days
        if self.backup_time is not None:
            result['backupTime'] = self.backup_time
        if self.persistent is not None:
            result['persistent'] = self.persistent
        if self.expire_in_days is not None:
            result['expireInDays'] = self.expire_in_days
        if self.log_backup_retain_days is not None:
            result['logBackupRetainDays'] = self.log_backup_retain_days
        if self.data_backup_type is not None:
            result['dataBackupType'] = self.data_backup_type
        if self.incremental_data_backup_enable is not None:
            result['incrementalDataBackupEnable'] = self.incremental_data_backup_enable
        if self.incremental_data_backup_interval is not None:
            result['incrementalDataBackupInterval'] = self.incremental_data_backup_interval
        if self.latest_data_backup_retain_days is not None:
            result['latestDataBackupRetainDays'] = self.latest_data_backup_retain_days
        if self.retention_period is not None:
            result['retentionPeriod'] = self.retention_period
        if self.time_unit is not None:
            result['timeUnit'] = self.time_unit
        if self.data_backup_copy_enable is not None:
            result['dataBackupCopyEnable'] = self.data_backup_copy_enable
        if self.data_backup_copy_storages_regions is not None:
            result['dataBackupCopyStoragesRegions'] = self.data_backup_copy_storages_regions
        if self.data_backup_copy_retain_days is not None:
            result['dataBackupCopyRetainDays'] = self.data_backup_copy_retain_days
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyBackupStrategyRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('backupDays') is not None:
            self.backup_days = m.get('backupDays')
        if m.get('backupTime') is not None:
            self.backup_time = m.get('backupTime')
        if m.get('persistent') is not None:
            self.persistent = m.get('persistent')
        if m.get('expireInDays') is not None:
            self.expire_in_days = m.get('expireInDays')
        if m.get('logBackupRetainDays') is not None:
            self.log_backup_retain_days = m.get('logBackupRetainDays')
        if m.get('dataBackupType') is not None:
            self.data_backup_type = m.get('dataBackupType')
        if m.get('incrementalDataBackupEnable') is not None:
            self.incremental_data_backup_enable = m.get('incrementalDataBackupEnable')
        if m.get('incrementalDataBackupInterval') is not None:
            self.incremental_data_backup_interval = m.get('incrementalDataBackupInterval')
        if m.get('latestDataBackupRetainDays') is not None:
            self.latest_data_backup_retain_days = m.get('latestDataBackupRetainDays')
        if m.get('retentionPeriod') is not None:
            self.retention_period = m.get('retentionPeriod')
        if m.get('timeUnit') is not None:
            self.time_unit = m.get('timeUnit')
        if m.get('dataBackupCopyEnable') is not None:
            self.data_backup_copy_enable = m.get('dataBackupCopyEnable')
        if m.get('dataBackupCopyStoragesRegions') is not None:
            self.data_backup_copy_storages_regions = m.get('dataBackupCopyStoragesRegions')
        if m.get('dataBackupCopyRetainDays') is not None:
            self.data_backup_copy_retain_days = m.get('dataBackupCopyRetainDays')
        return self
