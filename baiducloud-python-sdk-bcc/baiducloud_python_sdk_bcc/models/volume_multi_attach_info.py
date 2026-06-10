"""
VolumeMultiAttachInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class VolumeMultiAttachInfo(AbstractModel):
    """
    VolumeMultiAttachInfo
    """

    def __init__(self, volume_id=None, serial=None, instance_id=None, status=None):
        """
        Initialize VolumeMultiAttachInfo instance.

        :param volume_id: 磁盘ID
        :type volume_id: str (optional)

        :param serial: 磁盘序列号
        :type serial: str (optional)

        :param instance_id: 实例ID
        :type instance_id: str (optional)

        :param status: 状态
        :type status: str (optional)
        """
        super().__init__()
        self.volume_id = volume_id
        self.serial = serial
        self.instance_id = instance_id
        self.status = status

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
        if self.volume_id is not None:
            result['volumeId'] = self.volume_id
        if self.serial is not None:
            result['serial'] = self.serial
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: VolumeMultiAttachInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('volumeId') is not None:
            self.volume_id = m.get('volumeId')
        if m.get('serial') is not None:
            self.serial = m.get('serial')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self
