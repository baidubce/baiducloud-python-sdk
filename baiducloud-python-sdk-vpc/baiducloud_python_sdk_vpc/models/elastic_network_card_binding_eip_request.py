"""
Request entity for ElasticNetworkCardBindingEipRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ElasticNetworkCardBindingEipRequest(AbstractModel):
    """
    Request entity for ElasticNetworkCardBindingEipRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, eni_id, private_ip_address, public_ip_address, client_token=None):
        """
        Initialize ElasticNetworkCardBindingEipRequest request entity.

        :param eni_id: eni_id parameter
        :type eni_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param private_ip_address: 弹性网卡的内网IP地址
        :type private_ip_address: str (required)

        :param public_ip_address: EIP的地址
        :type public_ip_address: str (required)
        """
        super().__init__()
        self.eni_id = eni_id
        self.client_token = client_token
        self.private_ip_address = private_ip_address
        self.public_ip_address = public_ip_address

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
        if self.private_ip_address is not None:
            result['privateIpAddress'] = self.private_ip_address
        if self.public_ip_address is not None:
            result['publicIpAddress'] = self.public_ip_address
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ElasticNetworkCardBindingEipRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('eniId') is not None:
            self.eni_id = m.get('eniId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('privateIpAddress') is not None:
            self.private_ip_address = m.get('privateIpAddress')
        if m.get('publicIpAddress') is not None:
            self.public_ip_address = m.get('publicIpAddress')
        return self
