"""
Request entity for GetBackupStrategyResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class GetBackupStrategyResponse(BceResponse):
    """
    GetBackupStrategyResponse
    """

    def __init__(self, backup_time=None, backup_days=None, expire_day=None, is_encrypt=None):
        """
        Initialize GetBackupStrategyResponse response.

        :param backup_time: 备份时间。
        :type backup_time: str (optional)

        :param backup_days: 备份周期。
        :type backup_days: str (optional)

        :param expire_day: 备份文件保留时长，可选范围： 1-15天
        :type expire_day: int (optional)

        :param is_encrypt: 是否开启加密 <li>no 不开启 <li> yes 开启
        :type is_encrypt: str (optional)
        """
        super().__init__()
        self.backup_time = backup_time
        self.backup_days = backup_days
        self.expire_day = expire_day
        self.is_encrypt = is_encrypt

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
        if self.backup_time is not None:
            result['backupTime'] = self.backup_time
        if self.backup_days is not None:
            result['backupDays'] = self.backup_days
        if self.expire_day is not None:
            result['expireDay'] = self.expire_day
        if self.is_encrypt is not None:
            result['isEncrypt'] = self.is_encrypt
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetBackupStrategyResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('backupTime') is not None:
            self.backup_time = m.get('backupTime')
        if m.get('backupDays') is not None:
            self.backup_days = m.get('backupDays')
        if m.get('expireDay') is not None:
            self.expire_day = m.get('expireDay')
        if m.get('isEncrypt') is not None:
            self.is_encrypt = m.get('isEncrypt')
        return self
