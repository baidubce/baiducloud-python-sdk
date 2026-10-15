"""
InitialDataReference information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class InitialDataReference(AbstractModel):
    """
    InitialDataReference
    """

    def __init__(self, instance_id=None, reference_type=None, datetime=None, snapshot_id=None):
        """
        Initialize InitialDataReference instance.

        :param instance_id: 数据源的InstanceId
        :type instance_id: str (optional)

        :param reference_type: 仅限两种取值：datetime, snapshot
        :type reference_type: str (optional)

        :param datetime: datetime attribute
        :type datetime: str (optional)

        :param snapshot_id: referenceType为snapshot时必须，初始数据导入的目标备份集，取备份集ID
        :type snapshot_id: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.reference_type = reference_type
        self.datetime = datetime
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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.reference_type is not None:
            result['referenceType'] = self.reference_type
        if self.datetime is not None:
            result['datetime'] = self.datetime
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
        :rtype: InitialDataReference

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('referenceType') is not None:
            self.reference_type = m.get('referenceType')
        if m.get('datetime') is not None:
            self.datetime = m.get('datetime')
        if m.get('snapshotId') is not None:
            self.snapshot_id = m.get('snapshotId')
        return self
