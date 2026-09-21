"""
BatchRecord information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BatchRecord(AbstractModel):
    """
    BatchRecord
    """

    def __init__(
        self,
        backup_id=None,
        backup_status=None,
        backup_type=None,
        comment=None,
        duration=None,
        node_info=None,
        object_size=None,
        start_time=None,
    ):
        """
        Initialize BatchRecord instance.

        :param backup_id:
        :type backup_id: int (optional)

        :param backup_status:
        :type backup_status: str (optional)

        :param backup_type:
        :type backup_type: str (optional)

        :param comment:
        :type comment: str (optional)

        :param duration:
        :type duration: int (optional)

        :param node_info:
        :type node_info: str (optional)

        :param object_size:
        :type object_size: int (optional)

        :param start_time:
        :type start_time: str (optional)
        """
        super().__init__()
        self.backup_id = backup_id
        self.backup_status = backup_status
        self.backup_type = backup_type
        self.comment = comment
        self.duration = duration
        self.node_info = node_info
        self.object_size = object_size
        self.start_time = start_time

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
        if self.backup_id is not None:
            result['backupId'] = self.backup_id
        if self.backup_status is not None:
            result['backupStatus'] = self.backup_status
        if self.backup_type is not None:
            result['backupType'] = self.backup_type
        if self.comment is not None:
            result['comment'] = self.comment
        if self.duration is not None:
            result['duration'] = self.duration
        if self.node_info is not None:
            result['nodeInfo'] = self.node_info
        if self.object_size is not None:
            result['objectSize'] = self.object_size
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BatchRecord

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('backupId') is not None:
            self.backup_id = m.get('backupId')
        if m.get('backupStatus') is not None:
            self.backup_status = m.get('backupStatus')
        if m.get('backupType') is not None:
            self.backup_type = m.get('backupType')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('nodeInfo') is not None:
            self.node_info = m.get('nodeInfo')
        if m.get('objectSize') is not None:
            self.object_size = m.get('objectSize')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self
