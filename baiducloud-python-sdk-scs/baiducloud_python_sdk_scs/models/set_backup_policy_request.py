"""
Request entity for SetBackupPolicyRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SetBackupPolicyRequest(AbstractModel):
    """
    Request entity for SetBackupPolicyRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, backup_days, expire_day, is_encrypt, backup_time=None):
        """
        Initialize SetBackupPolicyRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param backup_time: 备份时间。<li>未填写该参数时，备份时间默认修改为1:05:00。
        :type backup_time: str (optional)

        :param backup_days: 备份周期。
        :type backup_days: str (required)

        :param expire_day: 备份文件保留时长，可选范围： 1-15天
        :type expire_day: int (required)

        :param is_encrypt: 是否开启加密 no 不开启 yes 开启
        :type is_encrypt: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.backup_time = backup_time
        self.backup_days = backup_days
        self.expire_day = expire_day
        self.is_encrypt = is_encrypt

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
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SetBackupPolicyRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('backupTime') is not None:
            self.backup_time = m.get('backupTime')
        if m.get('backupDays') is not None:
            self.backup_days = m.get('backupDays')
        if m.get('expireDay') is not None:
            self.expire_day = m.get('expireDay')
        if m.get('isEncrypt') is not None:
            self.is_encrypt = m.get('isEncrypt')
        return self
