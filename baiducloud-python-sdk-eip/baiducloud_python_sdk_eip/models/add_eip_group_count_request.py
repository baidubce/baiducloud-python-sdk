"""
Request entity for AddEipGroupCountRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AddEipGroupCountRequest(AbstractModel):
    """
    Request entity for AddEipGroupCountRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, id, client_token=None, eip_add_count=None, eipv6_add_count=None):
        """
        Initialize AddEipGroupCountRequest request entity.

        :param id: id parameter
        :type id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param eip_add_count: 共享带宽包新增IPv4 EIP的数量。该值大于0，公网IP数量最多可以包括n个（n\\*5Mbps小于共享带宽包总量）。
        :type eip_add_count: int (optional)

        :param eipv6_add_count: 共享带宽包新增IPv6 EIP的数量。该值大于0，公网IP数量最多受配额控制，默认是256。
        :type eipv6_add_count: int (optional)
        """
        super().__init__()
        self.id = id
        self.client_token = client_token
        self.eip_add_count = eip_add_count
        self.eipv6_add_count = eipv6_add_count

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
        if self.eip_add_count is not None:
            result['eipAddCount'] = self.eip_add_count
        if self.eipv6_add_count is not None:
            result['eipv6AddCount'] = self.eipv6_add_count
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AddEipGroupCountRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('eipAddCount') is not None:
            self.eip_add_count = m.get('eipAddCount')
        if m.get('eipv6AddCount') is not None:
            self.eipv6_add_count = m.get('eipv6AddCount')
        return self
