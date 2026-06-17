"""
AppBackendServerForCreate information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AppBackendServerForCreate(AbstractModel):
    """
    AppBackendServerForCreate
    """

    def __init__(self, instance_id=None, weight=None):
        """
        Initialize AppBackendServerForCreate instance.

        :param instance_id: 后端服务器标识符
        :type instance_id: str (optional)

        :param weight: 后端服务器权重，取值范围0-100
        :type weight: int (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.weight = weight

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
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AppBackendServerForCreate

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self
