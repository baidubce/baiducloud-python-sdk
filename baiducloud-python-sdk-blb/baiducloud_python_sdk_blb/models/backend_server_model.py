"""
BackendServerModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BackendServerModel(AbstractModel):
    """
    BackendServerModel
    """

    def __init__(self, instance_id=None, weight=None, desc=None):
        """
        Initialize BackendServerModel instance.

        :param instance_id: 后端服务器标识符
        :type instance_id: str (optional)

        :param weight: 后端服务器权重，取值范围[0, 100]，权重为0表示不要把流量转发到该后端服务器上
        :type weight: int (optional)

        :param desc: 描述
        :type desc: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.weight = weight
        self.desc = desc

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
        if self.desc is not None:
            result['desc'] = self.desc
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BackendServerModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        return self
