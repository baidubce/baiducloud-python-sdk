"""
InstanceDict information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class InstanceDict(AbstractModel):
    """
    InstanceDict
    """

    def __init__(self, port=None, vnet_ip=None, inet_ip=None, address=None):
        """
        Initialize InstanceDict instance.

        :param port: 端口。
        :type port: int (optional)

        :param vnet_ip: 内网IP。
        :type vnet_ip: str (optional)

        :param inet_ip: 外网IP。
        :type inet_ip: str (optional)

        :param address: 域名。
        :type address: str (optional)
        """
        super().__init__()
        self.port = port
        self.vnet_ip = vnet_ip
        self.inet_ip = inet_ip
        self.address = address

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
        if self.port is not None:
            result['port'] = self.port
        if self.vnet_ip is not None:
            result['vnetIp'] = self.vnet_ip
        if self.inet_ip is not None:
            result['inetIp'] = self.inet_ip
        if self.address is not None:
            result['address'] = self.address
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InstanceDict

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('vnetIp') is not None:
            self.vnet_ip = m.get('vnetIp')
        if m.get('inetIp') is not None:
            self.inet_ip = m.get('inetIp')
        if m.get('address') is not None:
            self.address = m.get('address')
        return self
