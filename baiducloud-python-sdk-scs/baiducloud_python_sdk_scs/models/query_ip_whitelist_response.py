"""
Request entity for QueryIpWhitelistResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class QueryIpWhitelistResponse(BceResponse):
    """
    QueryIpWhitelistResponse
    """

    def __init__(self, security_ips=None):
        """
        Initialize QueryIpWhitelistResponse response.

        :param security_ips: security_ips field
        :type security_ips: List[str] (optional)
        """
        super().__init__()
        self.security_ips = security_ips

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
        if self.security_ips is not None:
            result['securityIps'] = self.security_ips
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QueryIpWhitelistResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('securityIps') is not None:
            self.security_ips = m.get('securityIps')
        return self
