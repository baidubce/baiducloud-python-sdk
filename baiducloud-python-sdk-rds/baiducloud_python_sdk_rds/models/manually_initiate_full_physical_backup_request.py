"""
Request entity for ManuallyInitiateFullPhysicalBackupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ManuallyInitiateFullPhysicalBackupRequest(AbstractModel):
    """
    Request entity for ManuallyInitiateFullPhysicalBackupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, effective_time=None, data_backup_type=None):
        """
        Initialize ManuallyInitiateFullPhysicalBackupRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param effective_time: effective_time parameter
        :type effective_time: str (optional)

        :param data_backup_type: 备份类型，支持physical/snapshot， 取值为：snapshot，磁盘类型为ssd将不支持快照备份
        :type data_backup_type: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.effective_time = effective_time
        self.data_backup_type = data_backup_type

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
        if self.effective_time is not None:
            result['effectiveTime'] = self.effective_time
        if self.data_backup_type is not None:
            result['dataBackupType'] = self.data_backup_type
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ManuallyInitiateFullPhysicalBackupRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('effectiveTime') is not None:
            self.effective_time = m.get('effectiveTime')
        if m.get('dataBackupType') is not None:
            self.data_backup_type = m.get('dataBackupType')
        return self
