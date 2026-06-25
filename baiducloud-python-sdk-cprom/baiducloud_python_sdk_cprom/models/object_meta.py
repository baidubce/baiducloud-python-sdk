"""
ObjectMeta information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ObjectMeta(AbstractModel):
    """
    ObjectMeta
    """

    def __init__(self, name=None, namespace=None):
        """
        Initialize ObjectMeta instance.

        :param name: 资源名称
        :type name: str (optional)

        :param namespace: 命名空间
        :type namespace: str (optional)
        """
        super().__init__()
        self.name = name
        self.namespace = namespace

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
        if self.name is not None:
            result['name'] = self.name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ObjectMeta

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        return self
