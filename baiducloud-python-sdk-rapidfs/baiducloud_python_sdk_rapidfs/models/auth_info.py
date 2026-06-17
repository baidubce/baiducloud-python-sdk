"""
AuthInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AuthInfo(AbstractModel):
    """
    AuthInfo
    """

    def __init__(self, cidr=None, mode=None, description=None):
        """
        Initialize AuthInfo instance.

        :param cidr: 权限地址，ip/ip 段，请确保格式正确有效，如：127.0.0.1，127.0.0.0/28
        :type cidr: str (optional)

        :param mode: 权限类型，枚举值：ReadOnly：只读；ReadWrite：可读写；Forbid：禁止访问
        :type mode: str (optional)

        :param description: 权限描述信息
        :type description: str (optional)
        """
        super().__init__()
        self.cidr = cidr
        self.mode = mode
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
        if self.cidr is not None:
            result['cidr'] = self.cidr
        if self.mode is not None:
            result['mode'] = self.mode
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
        :rtype: AuthInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cidr') is not None:
            self.cidr = m.get('cidr')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
