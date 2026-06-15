"""
InstancePassRoleModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class InstancePassRoleModel(AbstractModel):
    """
    InstancePassRoleModel
    """

    def __init__(self, instance_id=None):
        """
        Initialize InstancePassRoleModel instance.

        :param instance_id: 实例ID
        :type instance_id: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id

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
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InstancePassRoleModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self
