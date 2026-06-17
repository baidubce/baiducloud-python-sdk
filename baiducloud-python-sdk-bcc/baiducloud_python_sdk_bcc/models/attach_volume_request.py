"""
Request entity for AttachVolumeRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AttachVolumeRequest(AbstractModel):
    """
    Request entity for AttachVolumeRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, volume_id, instance_id, delete_with_instance=None, delete_auto_snapshot=None):
        """
        Initialize AttachVolumeRequest request entity.

        :param volume_id: volume_id parameter
        :type volume_id: str (required)

        :param instance_id: 待挂载的虚拟机实例ID
        :type instance_id: str (required)

        :param delete_with_instance: 磁盘随实例删除，默认为false，仅后付费类型的数据盘支持配置该选项
        :type delete_with_instance: bool (optional)

        :param delete_auto_snapshot: 自动快照随磁盘删除，默认为false，所有类型的磁盘都支持配置该选项
        :type delete_auto_snapshot: bool (optional)
        """
        super().__init__()
        self.volume_id = volume_id
        self.instance_id = instance_id
        self.delete_with_instance = delete_with_instance
        self.delete_auto_snapshot = delete_auto_snapshot

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.delete_with_instance is not None:
            result['deleteWithInstance'] = self.delete_with_instance
        if self.delete_auto_snapshot is not None:
            result['deleteAutoSnapshot'] = self.delete_auto_snapshot
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AttachVolumeRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('volumeId') is not None:
            self.volume_id = m.get('volumeId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('deleteWithInstance') is not None:
            self.delete_with_instance = m.get('deleteWithInstance')
        if m.get('deleteAutoSnapshot') is not None:
            self.delete_auto_snapshot = m.get('deleteAutoSnapshot')
        return self
