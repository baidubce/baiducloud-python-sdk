"""
CdsInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CdsInfo(AbstractModel):
    """
    CdsInfo
    """

    def __init__(self, volume_type=None, size_in_gb=None, snapshot_id=None, snapshot_name=None):
        """
        Initialize CdsInfo instance.

        :param volume_type: 磁盘类型
        :type volume_type: str (optional)

        :param size_in_gb: 磁盘大小
        :type size_in_gb: int (optional)

        :param snapshot_id: 磁盘快照ID
        :type snapshot_id: str (optional)

        :param snapshot_name: 磁盘快照名称
        :type snapshot_name: str (optional)
        """
        super().__init__()
        self.volume_type = volume_type
        self.size_in_gb = size_in_gb
        self.snapshot_id = snapshot_id
        self.snapshot_name = snapshot_name

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
        if self.volume_type is not None:
            result['volumeType'] = self.volume_type
        if self.size_in_gb is not None:
            result['sizeInGB'] = self.size_in_gb
        if self.snapshot_id is not None:
            result['snapshotId'] = self.snapshot_id
        if self.snapshot_name is not None:
            result['snapshotName'] = self.snapshot_name
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CdsInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('volumeType') is not None:
            self.volume_type = m.get('volumeType')
        if m.get('sizeInGB') is not None:
            self.size_in_gb = m.get('sizeInGB')
        if m.get('snapshotId') is not None:
            self.snapshot_id = m.get('snapshotId')
        if m.get('snapshotName') is not None:
            self.snapshot_name = m.get('snapshotName')
        return self
