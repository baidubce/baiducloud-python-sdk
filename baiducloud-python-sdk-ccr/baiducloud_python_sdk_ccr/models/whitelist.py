"""
Whitelist information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Whitelist(AbstractModel):
    """
    Whitelist
    """

    def __init__(self, ip_addr=None, description=None):
        """
        Initialize Whitelist instance.

        :param ip_addr: 白名单 IP 地址
        :type ip_addr: str (optional)

        :param description: 白名单描述信息
        :type description: str (optional)
        """
        super().__init__()
        self.ip_addr = ip_addr
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
        if self.ip_addr is not None:
            result['ipAddr'] = self.ip_addr
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
        :rtype: Whitelist

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ipAddr') is not None:
            self.ip_addr = m.get('ipAddr')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
