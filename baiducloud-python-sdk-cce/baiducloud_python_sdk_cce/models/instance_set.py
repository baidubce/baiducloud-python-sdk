"""
InstanceSet information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class InstanceSet(AbstractModel):
    """
    InstanceSet
    """

    def __init__(self, instance_spec=None, count=None):
        """
        Initialize InstanceSet instance.

        :param instance_spec: 节点规格配置
        :type instance_spec: object (optional)

        :param count: 节点数量
        :type count: int (optional)
        """
        super().__init__()
        self.instance_spec = instance_spec
        self.count = count

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
        if self.instance_spec is not None:
            result['instanceSpec'] = self.instance_spec
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InstanceSet

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceSpec') is not None:
            self.instance_spec = m.get('instanceSpec')
        if m.get('count') is not None:
            self.count = m.get('count')
        return self
