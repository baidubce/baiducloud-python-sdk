"""
Request entity for InstanceDeletionProtectionRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class InstanceDeletionProtectionRequest(AbstractModel):
    """
    Request entity for InstanceDeletionProtectionRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, deletion_protection):
        """
        Initialize InstanceDeletionProtectionRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param deletion_protection: 删除保护策略，默认0，不设置
        :type deletion_protection: int (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.deletion_protection = deletion_protection

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
        if self.deletion_protection is not None:
            result['deletionProtection'] = self.deletion_protection
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InstanceDeletionProtectionRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('deletionProtection') is not None:
            self.deletion_protection = m.get('deletionProtection')
        return self
