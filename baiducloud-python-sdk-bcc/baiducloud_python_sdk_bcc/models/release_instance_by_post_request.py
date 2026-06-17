"""
Request entity for ReleaseInstanceByPostRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ReleaseInstanceByPostRequest(AbstractModel):
    """
    Request entity for ReleaseInstanceByPostRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        instance_id,
        related_release_flag,
        delete_cds_snapshot_flag,
        delete_related_enis_flag=None,
        bcc_recycle_flag=None,
        cds_attribute_active=None,
    ):
        """
        Initialize ReleaseInstanceByPostRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param related_release_flag: related_release_flag parameter
        :type related_release_flag: bool (required)

        :param delete_cds_snapshot_flag: delete_cds_snapshot_flag parameter
        :type delete_cds_snapshot_flag: bool (required)

        :param delete_related_enis_flag: 实例释放时是否删除关联的ENI
        :type delete_related_enis_flag: bool (optional)

        :param bcc_recycle_flag: 实例释放时是否进入回收站
        :type bcc_recycle_flag: bool (optional)

        :param cds_attribute_active: cds_attribute_active parameter
        :type cds_attribute_active: bool (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.related_release_flag = related_release_flag
        self.delete_cds_snapshot_flag = delete_cds_snapshot_flag
        self.delete_related_enis_flag = delete_related_enis_flag
        self.bcc_recycle_flag = bcc_recycle_flag
        self.cds_attribute_active = cds_attribute_active

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
        if self.related_release_flag is not None:
            result['relatedReleaseFlag'] = self.related_release_flag
        if self.delete_cds_snapshot_flag is not None:
            result['deleteCdsSnapshotFlag'] = self.delete_cds_snapshot_flag
        if self.delete_related_enis_flag is not None:
            result['deleteRelatedEnisFlag'] = self.delete_related_enis_flag
        if self.bcc_recycle_flag is not None:
            result['bccRecycleFlag'] = self.bcc_recycle_flag
        if self.cds_attribute_active is not None:
            result['cdsAttributeActive'] = self.cds_attribute_active
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ReleaseInstanceByPostRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('relatedReleaseFlag') is not None:
            self.related_release_flag = m.get('relatedReleaseFlag')
        if m.get('deleteCdsSnapshotFlag') is not None:
            self.delete_cds_snapshot_flag = m.get('deleteCdsSnapshotFlag')
        if m.get('deleteRelatedEnisFlag') is not None:
            self.delete_related_enis_flag = m.get('deleteRelatedEnisFlag')
        if m.get('bccRecycleFlag') is not None:
            self.bcc_recycle_flag = m.get('bccRecycleFlag')
        if m.get('cdsAttributeActive') is not None:
            self.cds_attribute_active = m.get('cdsAttributeActive')
        return self
