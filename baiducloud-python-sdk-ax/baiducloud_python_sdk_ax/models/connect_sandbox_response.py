"""
ConnectSandboxResponse information
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class ConnectSandboxResponse(BceResponse):
    """
    ConnectSandboxResponse
    """

    def __init__(self, sandbox_id=None, template_id=None, envd_access_token=None, domain=None):
        """
        Initialize ConnectSandboxResponse instance.

        :param sandbox_id: 沙箱实例 ID。
        :type sandbox_id: str (optional)

        :param template_id: 模板 ID。
        :type template_id: str (optional)

        :param envd_access_token: envd 访问令牌。
        :type envd_access_token: str (optional)

        :param domain: 沙箱访问域名。
        :type domain: str (optional)
        """
        super().__init__()
        self.sandbox_id = sandbox_id
        self.template_id = template_id
        self.envd_access_token = envd_access_token
        self.domain = domain

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        Includes metadata from the parent BceResponse class.

        :return: Dictionary representation of the model
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
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ConnectSandboxResponse

        :raises TypeError: If input is not a dictionary type
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
        return self
