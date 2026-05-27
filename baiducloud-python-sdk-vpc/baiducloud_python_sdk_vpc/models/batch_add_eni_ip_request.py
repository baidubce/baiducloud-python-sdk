"""
Request entity for BatchAddEniIpRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BatchAddEniIpRequest(AbstractModel):
    """
    Request entity for BatchAddEniIpRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, eni_id, client_token=None, is_ipv6=None, private_ip_addresses=None, private_ip_address_count=None
    ):
        """
        Initialize BatchAddEniIpRequest request entity.

        :param eni_id: eni_id parameter
        :type eni_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param is_ipv6: 是否IPv6地址，true表示分配IPv6地址，默认false分配IPv4地址
        :type is_ipv6: bool (optional)

        :param private_ip_addresses: 指定的内网IP信息，单次最多指定10个，与privateIpAddressCount至少提供一个
        :type private_ip_addresses: List[str] (optional)

        :param private_ip_address_count: 新申请的内网IP地址个数，最大为10，与privateIpAddresses至少提供一个
        :type private_ip_address_count: int (optional)
        """
        super().__init__()
        self.eni_id = eni_id
        self.client_token = client_token
        self.is_ipv6 = is_ipv6
        self.private_ip_addresses = private_ip_addresses
        self.private_ip_address_count = private_ip_address_count

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
        if self.private_ip_addresses is not None:
            result['privateIpAddresses'] = self.private_ip_addresses
        if self.private_ip_address_count is not None:
            result['privateIpAddressCount'] = self.private_ip_address_count
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BatchAddEniIpRequest

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
        if m.get('privateIpAddresses') is not None:
            self.private_ip_addresses = m.get('privateIpAddresses')
        if m.get('privateIpAddressCount') is not None:
            self.private_ip_address_count = m.get('privateIpAddressCount')
        return self
