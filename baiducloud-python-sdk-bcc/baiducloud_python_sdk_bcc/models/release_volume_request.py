"""
Request entity for ReleaseVolumeRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ReleaseVolumeRequest(AbstractModel):
    """
    Request entity for ReleaseVolumeRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, volume_id, auto_snapshot=None, manual_snapshot=None, cds_attribute_active=None, recycle=None):
        """
        Initialize ReleaseVolumeRequest request entity.

        :param volume_id: volume_id parameter
        :type volume_id: str (required)

        :param auto_snapshot: 取值为\"on\"时，会删除磁盘关联的自动快照
        :type auto_snapshot: str (optional)

        :param manual_snapshot: 取值为\"on\"时，会删除磁盘关联的手动快照
        :type manual_snapshot: str (optional)

        :param cds_attribute_active: cds_attribute_active parameter
        :type cds_attribute_active: bool (optional)

        :param recycle: 取值为\"on\"时，数据盘进入回收站，取值为\"off\"时，立即删除。默认为\"on\"。
        :type recycle: str (optional)
        """
        super().__init__()
        self.volume_id = volume_id
        self.auto_snapshot = auto_snapshot
        self.manual_snapshot = manual_snapshot
        self.cds_attribute_active = cds_attribute_active
        self.recycle = recycle

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
        if self.auto_snapshot is not None:
            result['autoSnapshot'] = self.auto_snapshot
        if self.manual_snapshot is not None:
            result['manualSnapshot'] = self.manual_snapshot
        if self.cds_attribute_active is not None:
            result['cdsAttributeActive'] = self.cds_attribute_active
        if self.recycle is not None:
            result['recycle'] = self.recycle
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ReleaseVolumeRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('volumeId') is not None:
            self.volume_id = m.get('volumeId')
        if m.get('autoSnapshot') is not None:
            self.auto_snapshot = m.get('autoSnapshot')
        if m.get('manualSnapshot') is not None:
            self.manual_snapshot = m.get('manualSnapshot')
        if m.get('cdsAttributeActive') is not None:
            self.cds_attribute_active = m.get('cdsAttributeActive')
        if m.get('recycle') is not None:
            self.recycle = m.get('recycle')
        return self
