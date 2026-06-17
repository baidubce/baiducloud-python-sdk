"""
RemoteCopySnapshot information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RemoteCopySnapshot(AbstractModel):
    """
    RemoteCopySnapshot
    """

    def __init__(self, region=None, snapshot_id=None):
        """
        Initialize RemoteCopySnapshot instance.

        :param region: 目标区域
        :type region: str (optional)

        :param snapshot_id: 成功复制到目标区域快照的快照ID
        :type snapshot_id: str (optional)
        """
        super().__init__()
        self.region = region
        self.snapshot_id = snapshot_id

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
        if self.region is not None:
            result['region'] = self.region
        if self.snapshot_id is not None:
            result['snapshotId'] = self.snapshot_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RemoteCopySnapshot

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('snapshotId') is not None:
            self.snapshot_id = m.get('snapshotId')
        return self
