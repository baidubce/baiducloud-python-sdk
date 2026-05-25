"""
Request entity for BatchDeleteElasticNetworkCardIntranetIpRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BatchDeleteElasticNetworkCardIntranetIpRequest(AbstractModel):
    """
    Request entity for BatchDeleteElasticNetworkCardIntranetIpRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, eni_id, private_ip_addresses, client_token=None):
        """
        Initialize BatchDeleteElasticNetworkCardIntranetIpRequest request entity.

        :param eni_id: eni_id parameter
        :type eni_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param private_ip_addresses: 指定的内网IP信息，可指定IPv4或IPv6地址，单次最多指定10个
        :type private_ip_addresses: List[str] (required)
        """
        super().__init__()
        self.eni_id = eni_id
        self.client_token = client_token
        self.private_ip_addresses = private_ip_addresses

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
        if self.private_ip_addresses is not None:
            result['privateIpAddresses'] = self.private_ip_addresses
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BatchDeleteElasticNetworkCardIntranetIpRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('eniId') is not None:
            self.eni_id = m.get('eniId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('privateIpAddresses') is not None:
            self.private_ip_addresses = m.get('privateIpAddresses')
        return self
