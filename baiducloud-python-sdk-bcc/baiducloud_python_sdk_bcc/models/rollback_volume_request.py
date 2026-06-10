"""
Request entity for RollbackVolumeRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RollbackVolumeRequest(AbstractModel):
    """
    Request entity for RollbackVolumeRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, volume_id, snapshot_id):
        """
        Initialize RollbackVolumeRequest request entity.

        :param volume_id: volume_id parameter
        :type volume_id: str (required)

        :param snapshot_id: 用于回滚指定磁盘的快照ID，必须为 volumeId 所创建的快照
        :type snapshot_id: str (required)
        """
        super().__init__()
        self.volume_id = volume_id
        self.snapshot_id = snapshot_id

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
        if self.snapshot_id is not None:
            result['snapshotId'] = self.snapshot_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RollbackVolumeRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('volumeId') is not None:
            self.volume_id = m.get('volumeId')
        if m.get('snapshotId') is not None:
            self.snapshot_id = m.get('snapshotId')
        return self
