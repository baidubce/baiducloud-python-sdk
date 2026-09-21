"""
Request entity for CreateRedisBigKeyAnalysisTaskRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateRedisBigKeyAnalysisTaskRequest(AbstractModel):
    """
    Request entity for CreateRedisBigKeyAnalysisTaskRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, app_id, cluster_id, backup_type, backup_id=None):
        """
        Initialize CreateRedisBigKeyAnalysisTaskRequest request entity.

        :param app_id: 集群ID
        :type app_id: str (required)

        :param cluster_id: 分片ID
        :type cluster_id: str (required)

        :param backup_type: BackupType 使用的备份方式1：新建备份 2.：使用历史备份
        :type backup_type: int (required)

        :param backup_id: 备份ID，当BackupType为2时，必须指定该字段
        :type backup_id: str (optional)
        """
        super().__init__()
        self.app_id = app_id
        self.cluster_id = cluster_id
        self.backup_type = backup_type
        self.backup_id = backup_id

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
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.backup_type is not None:
            result['backupType'] = self.backup_type
        if self.backup_id is not None:
            result['backupId'] = self.backup_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateRedisBigKeyAnalysisTaskRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('backupType') is not None:
            self.backup_type = m.get('backupType')
        if m.get('backupId') is not None:
            self.backup_id = m.get('backupId')
        return self
