"""
BackendServerStatus information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BackendServerStatus(AbstractModel):
    """
    BackendServerStatus
    """

    def __init__(self, instance_id=None, weight=None, status=None):
        """
        Initialize BackendServerStatus instance.

        :param instance_id: 后端服务器标识符
        :type instance_id: str (optional)

        :param weight: 后端服务器权重
        :type weight: int (optional)

        :param status: 后端服务器健康状态，值为\"Alive\"/\"Dead\"/\"Unknown\"
        :type status: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.weight = weight
        self.status = status

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
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BackendServerStatus

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self
