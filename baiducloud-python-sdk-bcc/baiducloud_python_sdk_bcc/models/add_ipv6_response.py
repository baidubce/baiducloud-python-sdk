"""
Request entity for AddIpv6Response information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class AddIpv6Response(BceResponse):
    """
    AddIpv6Response
    """

    def __init__(self, ipv6_address=None):
        """
        Initialize AddIpv6Response response.

        :param ipv6_address: 主网卡全量的ipv6
        :type ipv6_address: str (optional)
        """
        super().__init__()
        self.ipv6_address = ipv6_address

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.ipv6_address is not None:
            result['ipv6Address'] = self.ipv6_address
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AddIpv6Response

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ipv6Address') is not None:
            self.ipv6_address = m.get('ipv6Address')
        return self
