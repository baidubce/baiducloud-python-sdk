"""
ConfigFileDetail information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ConfigFileDetail(AbstractModel):
    """
    ConfigFileDetail
    """

    def __init__(self, path=None, file=None):
        """
        Initialize ConfigFileDetail instance.

        :param path: ConfigFile文件路径
        :type path: str (optional)

        :param file: ConfigFile文件名
        :type file: str (optional)
        """
        super().__init__()
        self.path = path
        self.file = file

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
        if self.path is not None:
            result['path'] = self.path
        if self.file is not None:
            result['file'] = self.file
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ConfigFileDetail

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('file') is not None:
            self.file = m.get('file')
        return self
