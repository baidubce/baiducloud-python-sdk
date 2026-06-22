"""
Request entity for ModifySnapshotAttributeRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModifySnapshotAttributeRequest(AbstractModel):
    """
    Request entity for ModifySnapshotAttributeRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, snapshot_id, snapshot_name=None, retention_in_days=None, desc=None):
        """
        Initialize ModifySnapshotAttributeRequest request entity.

        :param snapshot_id: snapshot_id parameter
        :type snapshot_id: str (required)

        :param snapshot_name: 修改后的快照名称，支持大小写字母、数字、中文以及-_ /.特殊字符，必须以字母开头，长度1-65。
        :type snapshot_name: str (optional)

        :param retention_in_days: 快照的保留时间，删除时间将从修改时间点开始重新计算。取值范围为1-10000天
        :type retention_in_days: int (optional)

        :param desc: 快照描述信息
        :type desc: str (optional)
        """
        super().__init__()
        self.snapshot_id = snapshot_id
        self.snapshot_name = snapshot_name
        self.retention_in_days = retention_in_days
        self.desc = desc

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
        if self.snapshot_name is not None:
            result['snapshotName'] = self.snapshot_name
        if self.retention_in_days is not None:
            result['retentionInDays'] = self.retention_in_days
        if self.desc is not None:
            result['desc'] = self.desc
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifySnapshotAttributeRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('snapshotId') is not None:
            self.snapshot_id = m.get('snapshotId')
        if m.get('snapshotName') is not None:
            self.snapshot_name = m.get('snapshotName')
        if m.get('retentionInDays') is not None:
            self.retention_in_days = m.get('retentionInDays')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        return self
