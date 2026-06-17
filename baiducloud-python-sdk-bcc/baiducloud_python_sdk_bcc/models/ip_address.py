"""
IpAddress information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class IpAddress(AbstractModel):
    """
    IpAddress
    """

    def __init__(self, primary=None, public_ip_address=None, private_ip_address=None, ipv6_address=None):
        """
        Initialize IpAddress instance.

        :param primary: 是否为主IP
        :type primary: bool (optional)

        :param public_ip_address: 公网IP
        :type public_ip_address: str (optional)

        :param private_ip_address: 内网IP
        :type private_ip_address: str (optional)

        :param ipv6_address: IPV6地址
        :type ipv6_address: str (optional)
        """
        super().__init__()
        self.primary = primary
        self.public_ip_address = public_ip_address
        self.private_ip_address = private_ip_address
        self.ipv6_address = ipv6_address

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
        if self.primary is not None:
            result['primary'] = self.primary
        if self.public_ip_address is not None:
            result['publicIpAddress'] = self.public_ip_address
        if self.private_ip_address is not None:
            result['privateIpAddress'] = self.private_ip_address
        if self.ipv6_address is not None:
            result['ipv6Address'] = self.ipv6_address
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: IpAddress

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('primary') is not None:
            self.primary = m.get('primary')
        if m.get('publicIpAddress') is not None:
            self.public_ip_address = m.get('publicIpAddress')
        if m.get('privateIpAddress') is not None:
            self.private_ip_address = m.get('privateIpAddress')
        if m.get('ipv6Address') is not None:
            self.ipv6_address = m.get('ipv6Address')
        return self
