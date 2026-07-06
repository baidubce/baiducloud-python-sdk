"""
ImageConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ImageConfig(AbstractModel):
    """
    ImageConfig
    """

    def __init__(self, username=None, password=None):
        """
        Initialize ImageConfig instance.

        :param username: 私有镜像仓库用户名
        :type username: str (optional)

        :param password: 私有镜像仓库密码
        :type password: str (optional)
        """
        super().__init__()
        self.username = username
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
        if self.username is not None:
            result['username'] = self.username
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
        :rtype: ImageConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('username') is not None:
            self.username = m.get('username')
        if m.get('password') is not None:
            self.password = m.get('password')
        return self
