"""
NfsVolume information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class NfsVolume(AbstractModel):
    """
    NfsVolume
    """

    def __init__(self, name=None, server=None, path=None, read_only=None):
        """
        Initialize NfsVolume instance.

        :param name: NFS服务器名称
        :type name: str (optional)

        :param server: NFS服务器地址
        :type server: str (optional)

        :param path: NFS数据卷路径
        :type path: str (optional)

        :param read_only: 是否只读，默认false
        :type read_only: bool (optional)
        """
        super().__init__()
        self.name = name
        self.server = server
        self.path = path
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
        if self.name is not None:
            result['name'] = self.name
        if self.server is not None:
            result['server'] = self.server
        if self.path is not None:
            result['path'] = self.path
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
        :rtype: NfsVolume

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('server') is not None:
            self.server = m.get('server')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('readOnly') is not None:
            self.read_only = m.get('readOnly')
        return self
