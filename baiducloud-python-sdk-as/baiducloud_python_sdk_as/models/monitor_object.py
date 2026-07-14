"""
MonitorObject information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_as.models.policy_resource import PolicyResource


class MonitorObject(AbstractModel):
    """
    MonitorObject
    """

    def __init__(self, type=None, names=None, resources=None, type_name=None):
        """
        Initialize MonitorObject instance.

        :param type: 类型
        :type type: str (optional)

        :param names: 名称列表
        :type names: List[str] (optional)

        :param resources: 关联的策略资源列表
        :type resources: List[PolicyResource] (optional)

        :param type_name: 监控类型的可读名称
        :type type_name: str (optional)
        """
        super().__init__()
        self.type = type
        self.names = names
        self.resources = resources
        self.type_name = type_name

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
        if self.type is not None:
            result['type'] = self.type
        if self.names is not None:
            result['names'] = self.names
        if self.resources is not None:
            result['resources'] = [i.to_dict() for i in self.resources]
        if self.type_name is not None:
            result['typeName'] = self.type_name
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MonitorObject

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('names') is not None:
            self.names = m.get('names')
        if m.get('resources') is not None:
            self.resources = [PolicyResource().from_dict(i) for i in m.get('resources')]
        if m.get('typeName') is not None:
            self.type_name = m.get('typeName')
        return self
