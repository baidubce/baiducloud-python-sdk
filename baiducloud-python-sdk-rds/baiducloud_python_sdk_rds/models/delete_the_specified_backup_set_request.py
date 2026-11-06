"""
Request entity for DeleteTheSpecifiedBackupSetRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteTheSpecifiedBackupSetRequest(AbstractModel):
    """
    Request entity for DeleteTheSpecifiedBackupSetRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, snapshot_id):
        """
        Initialize DeleteTheSpecifiedBackupSetRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param snapshot_id: snapshot_id parameter
        :type snapshot_id: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.snapshot_id = snapshot_id

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteTheSpecifiedBackupSetRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('snapshotId') is not None:
            self.snapshot_id = m.get('snapshotId')
        return self
