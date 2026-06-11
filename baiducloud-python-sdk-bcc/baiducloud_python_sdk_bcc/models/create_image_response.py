"""
Request entity for CreateImageResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateImageResponse(BceResponse):
    """
    CreateImageResponse
    """

    def __init__(self, image_id=None, cds_snapshot_ids=None):
        """
        Initialize CreateImageResponse response.

        :param image_id: 已创建的镜像的ID
        :type image_id: str (optional)

        :param cds_snapshot_ids: 关联CDS磁盘的快照ID列表
        :type cds_snapshot_ids: List[str] (optional)
        """
        super().__init__()
        self.image_id = image_id
        self.cds_snapshot_ids = cds_snapshot_ids

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.image_id is not None:
            result['imageId'] = self.image_id
        if self.cds_snapshot_ids is not None:
            result['cdsSnapshotIds'] = self.cds_snapshot_ids
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateImageResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')
        if m.get('cdsSnapshotIds') is not None:
            self.cds_snapshot_ids = m.get('cdsSnapshotIds')
        return self
