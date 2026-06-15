"""
InstancePassRoleFailModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class InstancePassRoleFailModel(AbstractModel):
    """
    InstancePassRoleFailModel
    """

    def __init__(self, instance_id=None, fail_message=None):
        """
        Initialize InstancePassRoleFailModel instance.

        :param instance_id: 实例ID
        :type instance_id: str (optional)

        :param fail_message: 失败信息
        :type fail_message: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.fail_message = fail_message

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
        if self.fail_message is not None:
            result['failMessage'] = self.fail_message
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InstancePassRoleFailModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('failMessage') is not None:
            self.fail_message = m.get('failMessage')
        return self
