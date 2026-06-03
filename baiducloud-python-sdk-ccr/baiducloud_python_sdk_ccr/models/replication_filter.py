"""
ReplicationFilter information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ReplicationFilter(AbstractModel):
    """
    ReplicationFilter
    """

    def __init__(self, type=None, value=None):
        """
        Initialize ReplicationFilter instance.

        :param type: 迁移规则资源筛选种类
        :type type: str (optional)

        :param value: 迁移规则资源筛选种类对应值
        :type value: str (optional)
        """
        super().__init__()
        self.type = type
        self.value = value

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
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ReplicationFilter

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self
