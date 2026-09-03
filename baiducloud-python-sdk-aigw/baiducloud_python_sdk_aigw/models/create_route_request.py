"""
Request entity for CreateRouteRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_aigw.models.match_rule import MatchRule
from baiducloud_python_sdk_aigw.models.target_service import TargetService
from baiducloud_python_sdk_aigw.models.rewrite import Rewrite
from baiducloud_python_sdk_aigw.models.regex_rewrite import RegexRewrite
from baiducloud_python_sdk_aigw.models.custom_header import CustomHeader
from baiducloud_python_sdk_aigw.models.token_rate_limit import TokenRateLimit
from baiducloud_python_sdk_aigw.models.request_rate_limit import RequestRateLimit
from baiducloud_python_sdk_aigw.models.timeout_policy import TimeoutPolicy
from baiducloud_python_sdk_aigw.models.retry_policy import RetryPolicy
from baiducloud_python_sdk_aigw.models.cors_policy import CorsPolicy
from baiducloud_python_sdk_aigw.models.response_headers import ResponseHeaders
from baiducloud_python_sdk_aigw.models.fallback_config import FallbackConfig


class CreateRouteRequest(AbstractModel):
    """
    Request entity for CreateRouteRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        instance_id,
        cluster_id,
        route_name,
        match_rules,
        target_service,
        x_region,
        src_product=None,
        access_mode=None,
        web_subdomain=None,
        service_path=None,
        domains=None,
        multi_service=None,
        traffic_distribution_strategy=None,
        enable_weight_adjust=None,
        rewrite=None,
        regex_rewrite=None,
        custom_headers=None,
        skip_set_host_header=None,
        auth_enabled=None,
        allowed_consumers=None,
        token_rate_limit=None,
        request_rate_limit=None,
        timeout_policy=None,
        retry_policy=None,
        cors_policy=None,
        response_headers=None,
        fallback_config=None,
    ):
        """
        Initialize CreateRouteRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param cluster_id: cluster_id parameter
        :type cluster_id: str (required)

        :param route_name: 路由名称，长度为 2～64 个字符，在同一实例内唯一
        :type route_name: str (required)

        :param src_product: 来源产品标识，外部用户无需填写
        :type src_product: str (optional)

        :param access_mode: 访问模式，取值为 API 或 Web，默认为 API
        :type access_mode: str (optional)

        :param web_subdomain: Web 模式的独立子域名，accessMode 为 Web 时必需
        :type web_subdomain: str (optional)

        :param service_path: Web 模式的后端服务路径，accessMode 为 Web 时必需，必须以 `/` 开头
        :type service_path: str (optional)

        :param domains: API 模式绑定的自定义域名列表；为空时使用实例默认域名
        :type domains: List[str] (optional)

        :param match_rules: match_rules parameter
        :type match_rules: MatchRule (required)

        :param multi_service: 是否启用多服务，默认为 false；Web 模式不支持多服务
        :type multi_service: bool (optional)

        :param traffic_distribution_strategy: 多服务流量分发策略，取值为 ratio 或 model_name，multiService 为 true 时必需
        :type traffic_distribution_strategy: str (optional)

        :param enable_weight_adjust: 是否启用动态权重调节，仅多服务 ratio 策略生效，默认为 false
        :type enable_weight_adjust: bool (optional)

        :param target_service: target_service parameter
        :type target_service: TargetService (required)

        :param rewrite: rewrite parameter
        :type rewrite: Rewrite (optional)

        :param regex_rewrite: regex_rewrite parameter
        :type regex_rewrite: RegexRewrite (optional)

        :param custom_headers: 转发请求时设置的自定义请求头
        :type custom_headers: List[CustomHeader] (optional)

        :param skip_set_host_header: FIXED_IP 或 DNS_DOMAIN 服务是否跳过自动设置 Host 请求头
        :type skip_set_host_header: bool (optional)

        :param auth_enabled: 是否启用消费者认证，默认为 false
        :type auth_enabled: bool (optional)

        :param allowed_consumers: 允许访问的消费者 ID 列表，authEnabled 为 true 时至少传一项
        :type allowed_consumers: List[str] (optional)

        :param token_rate_limit: token_rate_limit parameter
        :type token_rate_limit: TokenRateLimit (optional)

        :param request_rate_limit: request_rate_limit parameter
        :type request_rate_limit: RequestRateLimit (optional)

        :param timeout_policy: timeout_policy parameter
        :type timeout_policy: TimeoutPolicy (optional)

        :param retry_policy: retry_policy parameter
        :type retry_policy: RetryPolicy (optional)

        :param cors_policy: cors_policy parameter
        :type cors_policy: CorsPolicy (optional)

        :param response_headers: response_headers parameter
        :type response_headers: ResponseHeaders (optional)

        :param fallback_config: fallback_config parameter
        :type fallback_config: FallbackConfig (optional)

        :param x_region: x_region parameter
        :type x_region: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.cluster_id = cluster_id
        self.route_name = route_name
        self.src_product = src_product
        self.access_mode = access_mode
        self.web_subdomain = web_subdomain
        self.service_path = service_path
        self.domains = domains
        self.match_rules = match_rules
        self.multi_service = multi_service
        self.traffic_distribution_strategy = traffic_distribution_strategy
        self.enable_weight_adjust = enable_weight_adjust
        self.target_service = target_service
        self.rewrite = rewrite
        self.regex_rewrite = regex_rewrite
        self.custom_headers = custom_headers
        self.skip_set_host_header = skip_set_host_header
        self.auth_enabled = auth_enabled
        self.allowed_consumers = allowed_consumers
        self.token_rate_limit = token_rate_limit
        self.request_rate_limit = request_rate_limit
        self.timeout_policy = timeout_policy
        self.retry_policy = retry_policy
        self.cors_policy = cors_policy
        self.response_headers = response_headers
        self.fallback_config = fallback_config
        self.x_region = x_region

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
        if self.route_name is not None:
            result['routeName'] = self.route_name
        if self.src_product is not None:
            result['srcProduct'] = self.src_product
        if self.access_mode is not None:
            result['accessMode'] = self.access_mode
        if self.web_subdomain is not None:
            result['webSubdomain'] = self.web_subdomain
        if self.service_path is not None:
            result['servicePath'] = self.service_path
        if self.domains is not None:
            result['domains'] = self.domains
        if self.match_rules is not None:
            result['matchRules'] = self.match_rules.to_dict()
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
        if self.skip_set_host_header is not None:
            result['skipSetHostHeader'] = self.skip_set_host_header
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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateRouteRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('routeName') is not None:
            self.route_name = m.get('routeName')
        if m.get('srcProduct') is not None:
            self.src_product = m.get('srcProduct')
        if m.get('accessMode') is not None:
            self.access_mode = m.get('accessMode')
        if m.get('webSubdomain') is not None:
            self.web_subdomain = m.get('webSubdomain')
        if m.get('servicePath') is not None:
            self.service_path = m.get('servicePath')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        if m.get('matchRules') is not None:
            self.match_rules = MatchRule().from_dict(m.get('matchRules'))
        if m.get('multiService') is not None:
            self.multi_service = m.get('multiService')
        if m.get('trafficDistributionStrategy') is not None:
            self.traffic_distribution_strategy = m.get('trafficDistributionStrategy')
        if m.get('enableWeightAdjust') is not None:
            self.enable_weight_adjust = m.get('enableWeightAdjust')
        if m.get('targetService') is not None:
            self.target_service = TargetService().from_dict(m.get('targetService'))
        if m.get('rewrite') is not None:
            self.rewrite = Rewrite().from_dict(m.get('rewrite'))
        if m.get('regexRewrite') is not None:
            self.regex_rewrite = RegexRewrite().from_dict(m.get('regexRewrite'))
        if m.get('customHeaders') is not None:
            self.custom_headers = [CustomHeader().from_dict(i) for i in m.get('customHeaders')]
        if m.get('skipSetHostHeader') is not None:
            self.skip_set_host_header = m.get('skipSetHostHeader')
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
        if m.get('X-Region') is not None:
            self.x_region = m.get('X-Region')
        return self
