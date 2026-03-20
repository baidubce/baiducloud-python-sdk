"""
Request entity for ListTbspIpWhitelistRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListTbspIpWhitelistRequest(AbstractModel):
    """
    Request entity for ListTbspIpWhitelistRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, id, ip=None, ip_cidr=None, marker=None, max_keys=None):
        """
        Initialize ListTbspIpWhitelistRequest request entity.

        :param id: id parameter
        :type id: str (required)

        :param ip: ip parameter
        :type ip: str (optional)

        :param ip_cidr: ip_cidr parameter
        :type ip_cidr: str (optional)

        :param marker: marker parameter
        :type marker: str (optional)

        :param max_keys: max_keys parameter
        :type max_keys: int (optional)
        """
        super().__init__()
        self.id = id
        self.ip = ip
        self.ip_cidr = ip_cidr
        self.marker = marker
        self.max_keys = max_keys

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListTbspIpWhitelistRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('ipCidr') is not None:
            self.ip_cidr = m.get('ipCidr')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        return self
