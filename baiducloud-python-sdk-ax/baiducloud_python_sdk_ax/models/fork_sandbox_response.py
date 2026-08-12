"""
Request entity for ForkSandboxResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class ForkSandboxResponse(BceResponse):
    """
    ForkSandboxResponse
    """

    def __init__(
        self,
        sandbox_id=None,
        template_id=None,
        envd_access_token=None,
        domain=None,
        alias=None,
        client_id=None,
        envd_version=None,
        vpc_domain=None,
    ):
        """
        Initialize ForkSandboxResponse response.

        :param sandbox_id: 新派生沙箱实例 ID。
        :type sandbox_id: str (optional)

        :param template_id: 模板 ID。
        :type template_id: str (optional)

        :param envd_access_token: envd 访问令牌。
        :type envd_access_token: str (optional)

        :param domain: 沙箱访问域名。
        :type domain: str (optional)

        :param alias: 模板别名。
        :type alias: str (optional)

        :param client_id: 客户端 ID。
        :type client_id: str (optional)

        :param envd_version: envd 版本号。
        :type envd_version: str (optional)

        :param vpc_domain: 沙箱 VPC 访问域名。
        :type vpc_domain: str (optional)
        """
        super().__init__()
        self.sandbox_id = sandbox_id
        self.template_id = template_id
        self.envd_access_token = envd_access_token
        self.domain = domain
        self.alias = alias
        self.client_id = client_id
        self.envd_version = envd_version
        self.vpc_domain = vpc_domain

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
        if self.sandbox_id is not None:
            result['sandboxID'] = self.sandbox_id
        if self.template_id is not None:
            result['templateID'] = self.template_id
        if self.envd_access_token is not None:
            result['envdAccessToken'] = self.envd_access_token
        if self.domain is not None:
            result['domain'] = self.domain
        if self.alias is not None:
            result['alias'] = self.alias
        if self.client_id is not None:
            result['clientID'] = self.client_id
        if self.envd_version is not None:
            result['envdVersion'] = self.envd_version
        if self.vpc_domain is not None:
            result['vpcDomain'] = self.vpc_domain
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ForkSandboxResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('sandboxID') is not None:
            self.sandbox_id = m.get('sandboxID')
        if m.get('templateID') is not None:
            self.template_id = m.get('templateID')
        if m.get('envdAccessToken') is not None:
            self.envd_access_token = m.get('envdAccessToken')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('clientID') is not None:
            self.client_id = m.get('clientID')
        if m.get('envdVersion') is not None:
            self.envd_version = m.get('envdVersion')
        if m.get('vpcDomain') is not None:
            self.vpc_domain = m.get('vpcDomain')
        return self
