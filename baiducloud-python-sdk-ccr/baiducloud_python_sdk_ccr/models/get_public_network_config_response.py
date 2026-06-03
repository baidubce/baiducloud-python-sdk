"""
Request entity for GetPublicNetworkConfigResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_ccr.models.whitelist import Whitelist


class GetPublicNetworkConfigResponse(BceResponse):
    """
    GetPublicNetworkConfigResponse
    """

    def __init__(self, domain=None, status=None, whitelist=None):
        """
        Initialize GetPublicNetworkConfigResponse response.

        :param domain: 公网访问域名
        :type domain: str (optional)

        :param status: 公网访问入口状态，取值包含：opened、opening、closing、closed
        :type status: str (optional)

        :param whitelist: 白名单列表
        :type whitelist: List[Whitelist] (optional)
        """
        super().__init__()
        self.domain = domain
        self.status = status
        self.whitelist = whitelist

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
        if self.domain is not None:
            result['domain'] = self.domain
        if self.status is not None:
            result['status'] = self.status
        if self.whitelist is not None:
            result['whitelist'] = [i.to_dict() for i in self.whitelist]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetPublicNetworkConfigResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('whitelist') is not None:
            self.whitelist = [Whitelist().from_dict(i) for i in m.get('whitelist')]
        return self
