"""
PrivateIP information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class PrivateIP(AbstractModel):
    """
    PrivateIP
    """

    def __init__(self, public_ip_address=None, primary=None, private_ip_address=None):
        """
        Initialize PrivateIP instance.

        :param public_ip_address: 弹性网卡的公网IP地址，即EIP地址
        :type public_ip_address: str (optional)

        :param primary: 是否是主IP
        :type primary: bool (optional)

        :param private_ip_address: 弹性网卡的内网Ip地址
        :type private_ip_address: str (optional)
        """
        super().__init__()
        self.public_ip_address = public_ip_address
        self.primary = primary
        self.private_ip_address = private_ip_address

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
        if self.public_ip_address is not None:
            result['publicIpAddress'] = self.public_ip_address
        if self.primary is not None:
            result['primary'] = self.primary
        if self.private_ip_address is not None:
            result['privateIpAddress'] = self.private_ip_address
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PrivateIP

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('publicIpAddress') is not None:
            self.public_ip_address = m.get('publicIpAddress')
        if m.get('primary') is not None:
            self.primary = m.get('primary')
        if m.get('privateIpAddress') is not None:
            self.private_ip_address = m.get('privateIpAddress')
        return self
