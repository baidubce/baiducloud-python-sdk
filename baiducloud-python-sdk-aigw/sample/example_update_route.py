"""
Example for aigw update_route method.
"""

from baiducloud_python_sdk_core import exception
from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_aigw.api.aigw_client import AigwClient
from baiducloud_python_sdk_aigw import models as aigw_models

if __name__ == '__main__':
    try:
        endpoint = ""

        # ==== AK/SK 鉴权 ====
        access_key_id = "Your Ak"
        secret_access_key = "Your Sk"
        bce_client_config = BceClientConfiguration(
            credentials=BceCredentials(access_key_id, secret_access_key), endpoint=endpoint
        )

        client = AigwClient(bce_client_config)

        path_rule = aigw_models.PathRule(match_type="", value="", case_sensitive=False)
        match_rules = aigw_models.MatchRule(path_rule=path_rule, methods=[], headers=[], var_query_params=[])
        target_service = aigw_models.TargetService(
            service_source="",
            service_name="",
            namespace="",
            service_port=0,
            load_balance_algorithm="",
            hash_type="",
            hash_key="",
            request_ratio=0,
            model_name="",
            weight_factor=0,
            model_name_mode="",
            specified_model_name="",
        )
        rewrite = aigw_models.Rewrite(enabled=False, path="")
        regex_rewrite = aigw_models.RegexRewrite(match="", rewrite="")
        token_rate_limit = aigw_models.TokenRateLimit(
            rule_name="",
            enabled=False,
            pre_reserve_remaining_ratio=0.0,
            pre_reserve_history_window_seconds=0,
            pre_reserve_safety_factor=0.0,
            pre_reserve_estimation_mode="",
            pre_reserve_initial_tokens=None,
            sliding_window_bucket_count=0,
            pre_reserve_admission_mode="",
            pre_reserve_admission_burst_seconds=0,
            pre_reserve_retry_jitter_ms=0,
            rule_items=[],
        )
        request_rate_limit = aigw_models.RequestRateLimit(rule_name="", enabled=False, rule_items=[])
        timeout_policy = aigw_models.TimeoutPolicy(enabled=False, timeout=0)
        retry_policy = aigw_models.RetryPolicy(enabled=False, retry_conditions="", num_retries=0)
        cors_policy = aigw_models.CorsPolicy(
            enabled=False,
            allow_origins=[],
            allow_methods=[],
            allow_headers=[],
            expose_headers=[],
            max_age=0,
            allow_credentials=False,
        )
        response_headers = aigw_models.ResponseHeaders(enabled=False, headers=[])
        fallback_config = aigw_models.FallbackConfig(
            enabled=False, service_name="", model_name_mode="", specified_model_name=""
        )
        request = aigw_models.UpdateRouteRequest(
            instance_id="",
            route_name="",
            x_region="",
            match_rules=match_rules,
            target_service=target_service,
            src_product="",
            access_mode="",
            web_subdomain="",
            service_path="",
            domains=[],
            multi_service=False,
            traffic_distribution_strategy="",
            enable_weight_adjust=False,
            rewrite=rewrite,
            regex_rewrite=regex_rewrite,
            custom_headers=[],
            skip_set_host_header=False,
            auth_enabled=False,
            allowed_consumers=[],
            token_rate_limit=token_rate_limit,
            request_rate_limit=request_rate_limit,
            timeout_policy=timeout_policy,
            retry_policy=retry_policy,
            cors_policy=cors_policy,
            response_headers=response_headers,
            fallback_config=fallback_config,
        )
        res = client.update_route(request)
        print(res.to_json_string())
    except exception.BceHttpClientError as e:
        # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
        print(e.last_error)
        print(e.request_id)
        print(e.code)
