"""
OpenApiBackup information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class OpenApiBackup(AbstractModel):
    """
    OpenApiBackup
    """

    def __init__(
        self,
        backup_id=None,
        backup_size=None,
        backup_type=None,
        backup_status=None,
        backup_start_time=None,
        backup_end_time=None,
        download_url=None,
        download_expires=None,
    ):
        """
        Initialize OpenApiBackup instance.

        :param backup_id: 备份 ID
        :type backup_id: str (optional)

        :param backup_size: 实例大小，单位MB
        :type backup_size: int (optional)

        :param backup_type: 备份类型 manual(手工创建)， automated(自动创建)
        :type backup_type: str (optional)

        :param backup_status: 备份状态。  creating(创建中) available(备份可用)   deleting(正在删除)
        :type backup_status: str (optional)

        :param backup_start_time: 备份开始时间
        :type backup_start_time: str (optional)

        :param backup_end_time: 备份结束时间
        :type backup_end_time: str (optional)

        :param download_url: 下载URL
        :type download_url: str (optional)

        :param download_expires: 下载有效期
        :type download_expires: str (optional)
        """
        super().__init__()
        self.backup_id = backup_id
        self.backup_size = backup_size
        self.backup_type = backup_type
        self.backup_status = backup_status
        self.backup_start_time = backup_start_time
        self.backup_end_time = backup_end_time
        self.download_url = download_url
        self.download_expires = download_expires

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
        if self.backup_id is not None:
            result['backupId'] = self.backup_id
        if self.backup_size is not None:
            result['backupSize'] = self.backup_size
        if self.backup_type is not None:
            result['backupType'] = self.backup_type
        if self.backup_status is not None:
            result['backupStatus'] = self.backup_status
        if self.backup_start_time is not None:
            result['backupStartTime'] = self.backup_start_time
        if self.backup_end_time is not None:
            result['backupEndTime'] = self.backup_end_time
        if self.download_url is not None:
            result['downloadUrl'] = self.download_url
        if self.download_expires is not None:
            result['downloadExpires'] = self.download_expires
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: OpenApiBackup

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('backupId') is not None:
            self.backup_id = m.get('backupId')
        if m.get('backupSize') is not None:
            self.backup_size = m.get('backupSize')
        if m.get('backupType') is not None:
            self.backup_type = m.get('backupType')
        if m.get('backupStatus') is not None:
            self.backup_status = m.get('backupStatus')
        if m.get('backupStartTime') is not None:
            self.backup_start_time = m.get('backupStartTime')
        if m.get('backupEndTime') is not None:
            self.backup_end_time = m.get('backupEndTime')
        if m.get('downloadUrl') is not None:
            self.download_url = m.get('downloadUrl')
        if m.get('downloadExpires') is not None:
            self.download_expires = m.get('downloadExpires')
        return self
