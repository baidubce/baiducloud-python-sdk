"""
RegistryCredential information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RegistryCredential(AbstractModel):
    """
    RegistryCredential
    """

    def __init__(self, access_key=None, access_secret=None, type=None):
        """
        Initialize RegistryCredential instance.

        :param access_key: Access key，当凭据类型为 `basic` 时，`accessKey` 为用户名
        :type access_key: str (optional)

        :param access_secret: Access secret，当凭据类型为 `oauth` 时，`accessSecret` 为用户密码
        :type access_secret: str (optional)

        :param type: Registry 访问凭据，可选值：`basic`、`oauth`
        :type type: str (optional)
        """
        super().__init__()
        self.access_key = access_key
        self.access_secret = access_secret
        self.type = type

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
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.access_secret is not None:
            result['accessSecret'] = self.access_secret
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RegistryCredential

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('accessSecret') is not None:
            self.access_secret = m.get('accessSecret')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self
