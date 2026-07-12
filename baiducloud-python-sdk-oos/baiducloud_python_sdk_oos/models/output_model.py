"""
OutputModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class OutputModel(AbstractModel):
    """
    OutputModel
    """

    def __init__(self, name=None, type=None, description=None):
        """
        Initialize OutputModel instance.

        :param name: 输出名称
        :type name: str (optional)

        :param type: 输出类型
        :type type: str (optional)

        :param description: 输出描述
        :type description: str (optional)
        """
        super().__init__()
        self.name = name
        self.type = type
        self.description = description

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
        if self.type is not None:
            result['type'] = self.type
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: OutputModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
