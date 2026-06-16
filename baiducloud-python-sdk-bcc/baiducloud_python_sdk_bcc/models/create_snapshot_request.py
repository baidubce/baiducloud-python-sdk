"""
Request entity for CreateSnapshotRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcc.models.tag_model import TagModel


class CreateSnapshotRequest(AbstractModel):
    """
    Request entity for CreateSnapshotRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, volume_id, snapshot_name, desc=None, tags=None, retention_in_days=None):
        """
        Initialize CreateSnapshotRequest request entity.

        :param volume_id: 用于创建快照的磁盘ID，系统盘则为实例ID
        :type volume_id: str (required)

        :param snapshot_name: 快照名称，支持大小写字母、数字、中文以及-_ /.特殊字符，必须以字母开头，长度1-65。
        :type snapshot_name: str (required)

        :param desc: desc parameter
        :type desc: str (optional)

        :param tags: 绑定标签信息
        :type tags: List[TagModel] (optional)

        :param retention_in_days: 快照的保留时间，默认-1永久保留，取值范围为1-10000天
        :type retention_in_days: int (optional)
        """
        super().__init__()
        self.volume_id = volume_id
        self.snapshot_name = snapshot_name
        self.desc = desc
        self.tags = tags
        self.retention_in_days = retention_in_days

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
        if self.volume_id is not None:
            result['volumeId'] = self.volume_id
        if self.snapshot_name is not None:
            result['snapshotName'] = self.snapshot_name
        if self.desc is not None:
            result['desc'] = self.desc
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.retention_in_days is not None:
            result['retentionInDays'] = self.retention_in_days
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateSnapshotRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('volumeId') is not None:
            self.volume_id = m.get('volumeId')
        if m.get('snapshotName') is not None:
            self.snapshot_name = m.get('snapshotName')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        if m.get('retentionInDays') is not None:
            self.retention_in_days = m.get('retentionInDays')
        return self
