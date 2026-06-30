"""
ImageRegistryCredential information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ImageRegistryCredential(AbstractModel):
    """
    ImageRegistryCredential
    """

    def __init__(self, server=None, user_name=None, password=None):
        """
        Initialize ImageRegistryCredential instance.

        :param server: 镜像仓库注册地址
        :type server: str (optional)

        :param user_name: 镜像仓库用户名
        :type user_name: str (optional)

        :param password: 镜像仓库密码
        :type password: str (optional)
        """
        super().__init__()
        self.server = server
        self.user_name = user_name
        self.password = password

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
        if self.server is not None:
            result['server'] = self.server
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.password is not None:
            result['password'] = self.password
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ImageRegistryCredential

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('server') is not None:
            self.server = m.get('server')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('password') is not None:
            self.password = m.get('password')
        return self
