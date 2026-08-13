"""
Rewrite information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Rewrite(AbstractModel):
    """
    Rewrite
    """

    def __init__(self, enabled=None, path=None):
        """
        Initialize Rewrite instance.

        :param enabled: 是否启用普通路径重写
        :type enabled: bool (optional)

        :param path: 重写后的路径，enabled 为 true 时必需
        :type path: str (optional)
        """
        super().__init__()
        self.enabled = enabled
        self.path = path

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
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.path is not None:
            result['path'] = self.path
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Rewrite

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('path') is not None:
            self.path = m.get('path')
        return self
