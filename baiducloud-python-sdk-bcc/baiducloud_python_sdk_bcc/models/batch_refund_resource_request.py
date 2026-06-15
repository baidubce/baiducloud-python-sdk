"""
Request entity for BatchRefundResourceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BatchRefundResourceRequest(AbstractModel):
    """
    Request entity for BatchRefundResourceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, instance_ids, related_release_flag=None, delete_cds_snapshot_flag=None, delete_related_enis_flag=None
    ):
        """
        Initialize BatchRefundResourceRequest request entity.

        :param instance_ids: 实例id列表，单次操作最多支持20个实例
        :type instance_ids: List[str] (required)

        :param related_release_flag: related_release_flag parameter
        :type related_release_flag: bool (optional)

        :param delete_cds_snapshot_flag: 是否释放云磁盘快照。默认值：false，不关联释放
        :type delete_cds_snapshot_flag: bool (optional)

        :param delete_related_enis_flag: 实例释放时是否删除关联的ENI。默认值：false，不关联释放
        :type delete_related_enis_flag: bool (optional)
        """
        super().__init__()
        self.instance_ids = instance_ids
        self.related_release_flag = related_release_flag
        self.delete_cds_snapshot_flag = delete_cds_snapshot_flag
        self.delete_related_enis_flag = delete_related_enis_flag

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
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids
        if self.related_release_flag is not None:
            result['relatedReleaseFlag'] = self.related_release_flag
        if self.delete_cds_snapshot_flag is not None:
            result['deleteCdsSnapshotFlag'] = self.delete_cds_snapshot_flag
        if self.delete_related_enis_flag is not None:
            result['deleteRelatedEnisFlag'] = self.delete_related_enis_flag
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BatchRefundResourceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        if m.get('relatedReleaseFlag') is not None:
            self.related_release_flag = m.get('relatedReleaseFlag')
        if m.get('deleteCdsSnapshotFlag') is not None:
            self.delete_cds_snapshot_flag = m.get('deleteCdsSnapshotFlag')
        if m.get('deleteRelatedEnisFlag') is not None:
            self.delete_related_enis_flag = m.get('deleteRelatedEnisFlag')
        return self
