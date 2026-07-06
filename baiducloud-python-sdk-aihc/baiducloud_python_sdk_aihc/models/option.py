"""
Option information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Option(AbstractModel):
    """
    Option
    """

    def __init__(self, read_only=None):
        """
        Initialize Option instance.

        :param read_only: 是否以只读模式挂载到容器中
        :type read_only: bool (optional)
        """
        super().__init__()
        self.read_only = read_only

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
        if self.read_only is not None:
            result['readOnly'] = self.read_only
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Option

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('readOnly') is not None:
            self.read_only = m.get('readOnly')
        return self
