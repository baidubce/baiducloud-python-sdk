"""
Resource information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Resource(AbstractModel):
    """
    Resource
    """

    def __init__(self, type=None, id=None):
        """
        Initialize Resource instance.

        :param type: 资源类型
        :type type: str (optional)

        :param id: 资源标识，结构由资源类型决定
        :type id: object (optional)
        """
        super().__init__()
        self.type = type
        self.id = id

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
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Resource

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self
