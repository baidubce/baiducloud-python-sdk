"""
Request entity for SetEncryptionPolicyApiRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_rds.models.update_encrypt_policy_request import UpdateEncryptPolicyRequest


class SetEncryptionPolicyApiRequest(AbstractModel):
    """
    Request entity for SetEncryptionPolicyApiRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, backup_policy):
        """
        Initialize SetEncryptionPolicyApiRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param backup_policy: 加密策略请求体
        :type backup_policy: List[UpdateEncryptPolicyRequest] (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.backup_policy = backup_policy

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
        if self.backup_policy is not None:
            result['backupPolicy'] = [i.to_dict() for i in self.backup_policy]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SetEncryptionPolicyApiRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('backupPolicy') is not None:
            self.backup_policy = [UpdateEncryptPolicyRequest().from_dict(i) for i in m.get('backupPolicy')]
        return self
