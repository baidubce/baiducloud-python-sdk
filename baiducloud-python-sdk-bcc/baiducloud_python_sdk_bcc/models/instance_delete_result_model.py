"""
InstanceDeleteResultModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class InstanceDeleteResultModel(AbstractModel):
    """
    InstanceDeleteResultModel
    """

    def __init__(self, instance_id=None, eip=None, insnap_ids=None, snapshot_ids=None, volume_ids=None):
        """
        Initialize InstanceDeleteResultModel instance.

        :param instance_id: 实例id
        :type instance_id: str (optional)

        :param eip: eip
        :type eip: str (optional)

        :param insnap_ids: 实例快照id列表
        :type insnap_ids: List[str] (optional)

        :param snapshot_ids: 快照id列表
        :type snapshot_ids: List[str] (optional)

        :param volume_ids: 磁盘id列表
        :type volume_ids: List[str] (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.eip = eip
        self.insnap_ids = insnap_ids
        self.snapshot_ids = snapshot_ids
        self.volume_ids = volume_ids

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.eip is not None:
            result['eip'] = self.eip
        if self.insnap_ids is not None:
            result['insnapIds'] = self.insnap_ids
        if self.snapshot_ids is not None:
            result['snapshotIds'] = self.snapshot_ids
        if self.volume_ids is not None:
            result['volumeIds'] = self.volume_ids
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InstanceDeleteResultModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('insnapIds') is not None:
            self.insnap_ids = m.get('insnapIds')
        if m.get('snapshotIds') is not None:
            self.snapshot_ids = m.get('snapshotIds')
        if m.get('volumeIds') is not None:
            self.volume_ids = m.get('volumeIds')
        return self
