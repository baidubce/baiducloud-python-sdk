"""
RouteResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_aigw.models.target_service import TargetService

from baiducloud_python_sdk_aigw.models.rewrite_config import RewriteConfig

from baiducloud_python_sdk_aigw.models.regex_rewrite_config import RegexRewriteConfig

from baiducloud_python_sdk_aigw.models.custom_header import CustomHeader

from baiducloud_python_sdk_aigw.models.token_rate_limit import TokenRateLimit

from baiducloud_python_sdk_aigw.models.request_rate_limit import RequestRateLimit

from baiducloud_python_sdk_aigw.models.timeout_policy import TimeoutPolicy

from baiducloud_python_sdk_aigw.models.retry_policy import RetryPolicy

from baiducloud_python_sdk_aigw.models.cors_policy import CorsPolicy

from baiducloud_python_sdk_aigw.models.response_headers import ResponseHeaders

from baiducloud_python_sdk_aigw.models.fallback_config import FallbackConfig

from baiducloud_python_sdk_aigw.models.match_rules import MatchRules


class RouteResult(AbstractModel):
    """
    RouteResult
    """

    def __init__(
        self,
        route_name=None,
        src_product=None,
        access_mode=None,
        domains=None,
        web_domains=None,
        web_subdomain=None,
        service_path=None,
        create_time=None,
        update_time=None,
        multi_service=None,
        traffic_distribution_strategy=None,
        enable_weight_adjust=None,
        target_service=None,
        rewrite=None,
        regex_rewrite=None,
        custom_headers=None,
        auth_enabled=None,
        allowed_consumers=None,
        token_rate_limit=None,
        request_rate_limit=None,
        timeout_policy=None,
        retry_policy=None,
        cors_policy=None,
        response_headers=None,
        fallback_config=None,
        match_rules=None,
    ):
        """
        Initialize RouteResult instance.

        :param route_name: 路由名称
        :type route_name: str (optional)

        :param src_product: 来源产品标识
        :type src_product: str (optional)

        :param access_mode: 访问模式：API、Web
        :type access_mode: str (optional)

        :param domains: API 模式绑定的自定义域名
        :type domains: List[str] (optional)

        :param web_domains: Web 模式自动绑定的公网、内网域名
        :type web_domains: List[str] (optional)

        :param web_subdomain: Web 模式的独立子域名
        :type web_subdomain: str (optional)

        :param service_path: Web 模式的后端服务路径
        :type service_path: str (optional)

        :param create_time: 创建时间，格式为 `YYYY-MM-DD HH:mm:ss`
        :type create_time: str (optional)

        :param update_time: 更新时间，格式为 `YYYY-MM-DD HH:mm:ss`
        :type update_time: str (optional)

        :param multi_service: 是否启用多服务
        :type multi_service: bool (optional)

        :param traffic_distribution_strategy: 多服务流量分发策略：ratio、model_name
        :type traffic_distribution_strategy: str (optional)

        :param enable_weight_adjust: 是否启用动态权重调节
        :type enable_weight_adjust: bool (optional)

        :param target_service: target_service attribute
        :type target_service: TargetService (optional)

        :param rewrite: rewrite attribute
        :type rewrite: RewriteConfig (optional)

        :param regex_rewrite: regex_rewrite attribute
        :type regex_rewrite: RegexRewriteConfig (optional)

        :param custom_headers: 自定义请求头，每项包含 key、value
        :type custom_headers: List[CustomHeader] (optional)

        :param auth_enabled: 是否启用消费者认证
        :type auth_enabled: bool (optional)

        :param allowed_consumers: 允许访问的消费者 ID
        :type allowed_consumers: List[str] (optional)

        :param token_rate_limit: token_rate_limit attribute
        :type token_rate_limit: TokenRateLimit (optional)

        :param request_rate_limit: request_rate_limit attribute
        :type request_rate_limit: RequestRateLimit (optional)

        :param timeout_policy: timeout_policy attribute
        :type timeout_policy: TimeoutPolicy (optional)

        :param retry_policy: retry_policy attribute
        :type retry_policy: RetryPolicy (optional)

        :param cors_policy: cors_policy attribute
        :type cors_policy: CorsPolicy (optional)

        :param response_headers: response_headers attribute
        :type response_headers: ResponseHeaders (optional)

        :param fallback_config: fallback_config attribute
        :type fallback_config: FallbackConfig (optional)

        :param match_rules: match_rules attribute
        :type match_rules: MatchRules (optional)
        """
        super().__init__()
        self.route_name = route_name
        self.src_product = src_product
        self.access_mode = access_mode
        self.domains = domains
        self.web_domains = web_domains
        self.web_subdomain = web_subdomain
        self.service_path = service_path
        self.create_time = create_time
        self.update_time = update_time
        self.multi_service = multi_service
        self.traffic_distribution_strategy = traffic_distribution_strategy
        self.enable_weight_adjust = enable_weight_adjust
        self.target_service = target_service
        self.rewrite = rewrite
        self.regex_rewrite = regex_rewrite
        self.custom_headers = custom_headers
        self.auth_enabled = auth_enabled
        self.allowed_consumers = allowed_consumers
        self.token_rate_limit = token_rate_limit
        self.request_rate_limit = request_rate_limit
        self.timeout_policy = timeout_policy
        self.retry_policy = retry_policy
        self.cors_policy = cors_policy
        self.response_headers = response_headers
        self.fallback_config = fallback_config
        self.match_rules = match_rules

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
        if self.route_name is not None:
            result['routeName'] = self.route_name
        if self.src_product is not None:
            result['srcProduct'] = self.src_product
        if self.access_mode is not None:
            result['accessMode'] = self.access_mode
        if self.domains is not None:
            result['domains'] = self.domains
        if self.web_domains is not None:
            result['webDomains'] = self.web_domains
        if self.web_subdomain is not None:
            result['webSubdomain'] = self.web_subdomain
        if self.service_path is not None:
            result['servicePath'] = self.service_path
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.multi_service is not None:
            result['multiService'] = self.multi_service
        if self.traffic_distribution_strategy is not None:
            result['trafficDistributionStrategy'] = self.traffic_distribution_strategy
        if self.enable_weight_adjust is not None:
            result['enableWeightAdjust'] = self.enable_weight_adjust
        if self.target_service is not None:
            result['targetService'] = self.target_service.to_dict()
        if self.rewrite is not None:
            result['rewrite'] = self.rewrite.to_dict()
        if self.regex_rewrite is not None:
            result['regexRewrite'] = self.regex_rewrite.to_dict()
        if self.custom_headers is not None:
            result['customHeaders'] = [i.to_dict() for i in self.custom_headers]
        if self.auth_enabled is not None:
            result['authEnabled'] = self.auth_enabled
        if self.allowed_consumers is not None:
            result['allowedConsumers'] = self.allowed_consumers
        if self.token_rate_limit is not None:
            result['tokenRateLimit'] = self.token_rate_limit.to_dict()
        if self.request_rate_limit is not None:
            result['requestRateLimit'] = self.request_rate_limit.to_dict()
        if self.timeout_policy is not None:
            result['timeoutPolicy'] = self.timeout_policy.to_dict()
        if self.retry_policy is not None:
            result['retryPolicy'] = self.retry_policy.to_dict()
        if self.cors_policy is not None:
            result['corsPolicy'] = self.cors_policy.to_dict()
        if self.response_headers is not None:
            result['responseHeaders'] = self.response_headers.to_dict()
        if self.fallback_config is not None:
            result['fallbackConfig'] = self.fallback_config.to_dict()
        if self.match_rules is not None:
            result['matchRules'] = self.match_rules.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RouteResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('routeName') is not None:
            self.route_name = m.get('routeName')
        if m.get('srcProduct') is not None:
            self.src_product = m.get('srcProduct')
        if m.get('accessMode') is not None:
            self.access_mode = m.get('accessMode')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        if m.get('webDomains') is not None:
            self.web_domains = m.get('webDomains')
        if m.get('webSubdomain') is not None:
            self.web_subdomain = m.get('webSubdomain')
        if m.get('servicePath') is not None:
            self.service_path = m.get('servicePath')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('multiService') is not None:
            self.multi_service = m.get('multiService')
        if m.get('trafficDistributionStrategy') is not None:
            self.traffic_distribution_strategy = m.get('trafficDistributionStrategy')
        if m.get('enableWeightAdjust') is not None:
            self.enable_weight_adjust = m.get('enableWeightAdjust')
        if m.get('targetService') is not None:
            self.target_service = TargetService().from_dict(m.get('targetService'))
        if m.get('rewrite') is not None:
            self.rewrite = RewriteConfig().from_dict(m.get('rewrite'))
        if m.get('regexRewrite') is not None:
            self.regex_rewrite = RegexRewriteConfig().from_dict(m.get('regexRewrite'))
        if m.get('customHeaders') is not None:
            self.custom_headers = [CustomHeader().from_dict(i) for i in m.get('customHeaders')]
        if m.get('authEnabled') is not None:
            self.auth_enabled = m.get('authEnabled')
        if m.get('allowedConsumers') is not None:
            self.allowed_consumers = m.get('allowedConsumers')
        if m.get('tokenRateLimit') is not None:
            self.token_rate_limit = TokenRateLimit().from_dict(m.get('tokenRateLimit'))
        if m.get('requestRateLimit') is not None:
            self.request_rate_limit = RequestRateLimit().from_dict(m.get('requestRateLimit'))
        if m.get('timeoutPolicy') is not None:
            self.timeout_policy = TimeoutPolicy().from_dict(m.get('timeoutPolicy'))
        if m.get('retryPolicy') is not None:
            self.retry_policy = RetryPolicy().from_dict(m.get('retryPolicy'))
        if m.get('corsPolicy') is not None:
            self.cors_policy = CorsPolicy().from_dict(m.get('corsPolicy'))
        if m.get('responseHeaders') is not None:
            self.response_headers = ResponseHeaders().from_dict(m.get('responseHeaders'))
        if m.get('fallbackConfig') is not None:
            self.fallback_config = FallbackConfig().from_dict(m.get('fallbackConfig'))
        if m.get('matchRules') is not None:
            self.match_rules = MatchRules().from_dict(m.get('matchRules'))
        return self
