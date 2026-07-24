"""
Request entity for RemoteCopySnapshotRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcc.models.remote_copy_request import RemoteCopyRequest


class RemoteCopySnapshotRequest(AbstractModel):
    """
    Request entity for RemoteCopySnapshotRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, snapshot_id, dest_region_infos=None):
        """
        Initialize RemoteCopySnapshotRequest request entity.

        :param snapshot_id: snapshot_id parameter
        :type snapshot_id: str (required)

        :param dest_region_infos: 待复制到目标区域列表
        :type dest_region_infos: List[RemoteCopyRequest] (optional)
        """
        super().__init__()
        self.snapshot_id = snapshot_id
        self.dest_region_infos = dest_region_infos

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
        if self.dest_region_infos is not None:
            result['destRegionInfos'] = [i.to_dict() for i in self.dest_region_infos]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RemoteCopySnapshotRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('snapshotId') is not None:
            self.snapshot_id = m.get('snapshotId')
        if m.get('destRegionInfos') is not None:
            self.dest_region_infos = [RemoteCopyRequest().from_dict(i) for i in m.get('destRegionInfos')]
        return self
