"""
CorsPolicy information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_aigw.models.origin_match import OriginMatch


class CorsPolicy(AbstractModel):
    """
    CorsPolicy
    """

    def __init__(
        self,
        enabled=None,
        allow_origins=None,
        allow_methods=None,
        allow_headers=None,
        expose_headers=None,
        max_age=None,
        allow_credentials=None,
    ):
        """
        Initialize CorsPolicy instance.

        :param enabled: 是否启用跨域策略
        :type enabled: bool (optional)

        :param allow_origins: 允许的来源，每项包含 matchType、value
        :type allow_origins: List[OriginMatch] (optional)

        :param allow_methods: 允许的 HTTP 方法
        :type allow_methods: List[str] (optional)

        :param allow_headers: 允许的请求头
        :type allow_headers: List[str] (optional)

        :param expose_headers: 暴露的响应头
        :type expose_headers: List[str] (optional)

        :param max_age: 预检请求缓存时间，单位为秒
        :type max_age: int (optional)

        :param allow_credentials: 是否允许携带凭证
        :type allow_credentials: bool (optional)
        """
        super().__init__()
        self.enabled = enabled
        self.allow_origins = allow_origins
        self.allow_methods = allow_methods
        self.allow_headers = allow_headers
        self.expose_headers = expose_headers
        self.max_age = max_age
        self.allow_credentials = allow_credentials

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.allow_origins is not None:
            result['allowOrigins'] = [i.to_dict() for i in self.allow_origins]
        if self.allow_methods is not None:
            result['allowMethods'] = self.allow_methods
        if self.allow_headers is not None:
            result['allowHeaders'] = self.allow_headers
        if self.expose_headers is not None:
            result['exposeHeaders'] = self.expose_headers
        if self.max_age is not None:
            result['maxAge'] = self.max_age
        if self.allow_credentials is not None:
            result['allowCredentials'] = self.allow_credentials
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CorsPolicy

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('allowOrigins') is not None:
            self.allow_origins = [OriginMatch().from_dict(i) for i in m.get('allowOrigins')]
        if m.get('allowMethods') is not None:
            self.allow_methods = m.get('allowMethods')
        if m.get('allowHeaders') is not None:
            self.allow_headers = m.get('allowHeaders')
        if m.get('exposeHeaders') is not None:
            self.expose_headers = m.get('exposeHeaders')
        if m.get('maxAge') is not None:
            self.max_age = m.get('maxAge')
        if m.get('allowCredentials') is not None:
            self.allow_credentials = m.get('allowCredentials')
        return self
