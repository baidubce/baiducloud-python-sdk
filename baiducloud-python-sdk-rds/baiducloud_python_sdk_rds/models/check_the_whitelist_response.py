"""
Request entity for CheckTheWhitelistResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CheckTheWhitelistResponse(BceResponse):
    """
    CheckTheWhitelistResponse
    """

    def __init__(self, etag=None, security_ips=None, security_ip_group=None, tag=None):
        """
        Initialize CheckTheWhitelistResponse response.

        :param etag: 数据修改的版本号，如：\"v0\"。当前字段仅在 version 取值为1时返回
        :type etag: str (optional)

        :param security_ips: 白名单IP地址列表
        :type security_ips: List[str] (optional)

        :param security_ip_group: 当前字段为保留字段，固定取值 console。仅在version 取值为2时返回
        :type security_ip_group: str (optional)

        :param tag: 白名单分组名称。仅在version 取值为2时返回
        :type tag: str (optional)
        """
        super().__init__()
        self.etag = etag
        self.security_ips = security_ips
        self.security_ip_group = security_ip_group
        self.tag = tag

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
        if self.etag is not None:
            result['etag'] = self.etag
        if self.security_ips is not None:
            result['securityIps'] = self.security_ips
        if self.security_ip_group is not None:
            result['securityIpGroup'] = self.security_ip_group
        if self.tag is not None:
            result['tag'] = self.tag
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CheckTheWhitelistResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('etag') is not None:
            self.etag = m.get('etag')
        if m.get('securityIps') is not None:
            self.security_ips = m.get('securityIps')
        if m.get('securityIpGroup') is not None:
            self.security_ip_group = m.get('securityIpGroup')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        return self
