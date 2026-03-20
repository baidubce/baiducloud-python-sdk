"""
Request entity for CreateIpReservedRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateIpReservedRequest(AbstractModel):
    """
    Request entity for CreateIpReservedRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, subnet_id, ip_cidr, ip_version, client_token=None, description=None):
        """
        Initialize CreateIpReservedRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param subnet_id: 预留网段所属的子网ID
        :type subnet_id: str (required)

        :param ip_cidr: 预留网段的ip或cidr
        :type ip_cidr: str (required)

        :param ip_version: IP版本，支持IPv4和IPv6
        :type ip_version: int (required)

        :param description: 预留网段描述
        :type description: str (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.subnet_id = subnet_id
        self.ip_cidr = ip_cidr
        self.ip_version = ip_version
        self.description = description

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
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.ip_cidr is not None:
            result['ipCidr'] = self.ip_cidr
        if self.ip_version is not None:
            result['ipVersion'] = self.ip_version
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateIpReservedRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('ipCidr') is not None:
            self.ip_cidr = m.get('ipCidr')
        if m.get('ipVersion') is not None:
            self.ip_version = m.get('ipVersion')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
