"""
EmptyDirVolume information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class EmptyDirVolume(AbstractModel):
    """
    EmptyDirVolume
    """

    def __init__(self, name=None, medium=None, size_limit=None):
        """
        Initialize EmptyDirVolume instance.

        :param name: EmptyDirVolume名称
        :type name: str (optional)

        :param medium: 存储媒介，默认空（node文件系统），支持memory
        :type medium: str (optional)

        :param size_limit: 大小（GiB）
        :type size_limit: float (optional)
        """
        super().__init__()
        self.name = name
        self.medium = medium
        self.size_limit = size_limit

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
        if self.medium is not None:
            result['medium'] = self.medium
        if self.size_limit is not None:
            result['sizeLimit'] = self.size_limit
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EmptyDirVolume

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('medium') is not None:
            self.medium = m.get('medium')
        if m.get('sizeLimit') is not None:
            self.size_limit = m.get('sizeLimit')
        return self
