"""
Request entity for SetCommentUsingPOSTRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SetCommentUsingPOSTRequest(AbstractModel):
    """
    Request entity for SetCommentUsingPOSTRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, engine_type=None, backup_id=None, batch_id=None, comment=None):
        """
        Initialize SetCommentUsingPOSTRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param engine_type: engine_type parameter
        :type engine_type: str (optional)

        :param backup_id: backup_id parameter
        :type backup_id: str (optional)

        :param batch_id: batch_id parameter
        :type batch_id: str (optional)

        :param comment: comment parameter
        :type comment: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.engine_type = engine_type
        self.backup_id = backup_id
        self.batch_id = batch_id
        self.comment = comment

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
        if self.backup_id is not None:
            result['backupId'] = self.backup_id
        if self.batch_id is not None:
            result['batchId'] = self.batch_id
        if self.comment is not None:
            result['comment'] = self.comment
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SetCommentUsingPOSTRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('engineType') is not None:
            self.engine_type = m.get('engineType')
        if m.get('backupId') is not None:
            self.backup_id = m.get('backupId')
        if m.get('batchId') is not None:
            self.batch_id = m.get('batchId')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        return self
