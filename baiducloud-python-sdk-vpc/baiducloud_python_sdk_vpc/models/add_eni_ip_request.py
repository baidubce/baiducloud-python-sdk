"""
Request entity for AddEniIpRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AddEniIpRequest(AbstractModel):
    """
    Request entity for AddEniIpRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, eni_id, private_ip_address, client_token=None, is_ipv6=None):
        """
        Initialize AddEniIpRequest request entity.

        :param eni_id: eni_id parameter
        :type eni_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param is_ipv6: 是否IPv6地址，true表示分配IPv6地址，默认false分配IPv4地址
        :type is_ipv6: bool (optional)

        :param private_ip_address: 新增的内网IP地址
        :type private_ip_address: str (required)
        """
        super().__init__()
        self.eni_id = eni_id
        self.client_token = client_token
        self.is_ipv6 = is_ipv6
        self.private_ip_address = private_ip_address

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.is_ipv6 is not None:
            result['isIpv6'] = self.is_ipv6
        if self.private_ip_address is not None:
            result['privateIpAddress'] = self.private_ip_address
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AddEniIpRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('eniId') is not None:
            self.eni_id = m.get('eniId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('isIpv6') is not None:
            self.is_ipv6 = m.get('isIpv6')
        if m.get('privateIpAddress') is not None:
            self.private_ip_address = m.get('privateIpAddress')
        return self
