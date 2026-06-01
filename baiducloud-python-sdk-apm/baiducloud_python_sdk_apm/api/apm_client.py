"""
Example for apm client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.auth import bce_v1_signer
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_apm.models.apm_create_alarm_policy_response import ApmCreateAlarmPolicyResponse
from baiducloud_python_sdk_apm.models.apm_delete_alarm_policy_response import ApmDeleteAlarmPolicyResponse
from baiducloud_python_sdk_apm.models.apm_describe_alarm_response import ApmDescribeAlarmResponse
from baiducloud_python_sdk_apm.models.apm_describe_alarm_policies_response import ApmDescribeAlarmPoliciesResponse
from baiducloud_python_sdk_apm.models.apm_describe_alarm_policy_response import ApmDescribeAlarmPolicyResponse
from baiducloud_python_sdk_apm.models.apm_describe_alarms_response import ApmDescribeAlarmsResponse
from baiducloud_python_sdk_apm.models.apm_update_alarm_policy_response import ApmUpdateAlarmPolicyResponse
from baiducloud_python_sdk_apm.models.apm_update_alarm_policy_action_response import ApmUpdateAlarmPolicyActionResponse
from baiducloud_python_sdk_apm.models.apm_update_alarm_policy_state_response import ApmUpdateAlarmPolicyStateResponse
from baiducloud_python_sdk_apm.models.bind_service_tag_response import BindServiceTagResponse
from baiducloud_python_sdk_apm.models.delete_services_response import DeleteServicesResponse
from baiducloud_python_sdk_apm.models.describe_db_statement_response import DescribeDbStatementResponse
from baiducloud_python_sdk_apm.models.describe_default_config_response import DescribeDefaultConfigResponse
from baiducloud_python_sdk_apm.models.describe_dimension_values_response import DescribeDimensionValuesResponse
from baiducloud_python_sdk_apm.models.describe_env_response import DescribeEnvResponse
from baiducloud_python_sdk_apm.models.describe_exceptions_response import DescribeExceptionsResponse
from baiducloud_python_sdk_apm.models.describe_llm_dimension_values_response import DescribeLLMDimensionValuesResponse
from baiducloud_python_sdk_apm.models.describe_llm_metric_data_response import DescribeLLMMetricDataResponse
from baiducloud_python_sdk_apm.models.describe_llm_services_response import DescribeLLMServicesResponse
from baiducloud_python_sdk_apm.models.describe_llm_session_response import DescribeLLMSessionResponse
from baiducloud_python_sdk_apm.models.describe_llm_sessions_response import DescribeLLMSessionsResponse
from baiducloud_python_sdk_apm.models.describe_llm_sessions_statistics_response import (
    DescribeLLMSessionsStatisticsResponse,
)
from baiducloud_python_sdk_apm.models.describe_llm_spans_response import DescribeLLMSpansResponse
from baiducloud_python_sdk_apm.models.describe_llm_trace_response import DescribeLLMTraceResponse
from baiducloud_python_sdk_apm.models.describe_llm_traces_response import DescribeLLMTracesResponse
from baiducloud_python_sdk_apm.models.describe_llm_traces_statistics_response import (
    DescribeLLMTracesStatisticsResponse,
)
from baiducloud_python_sdk_apm.models.describe_metric_data_response import DescribeMetricDataResponse
from baiducloud_python_sdk_apm.models.describe_retention_limit_response import DescribeRetentionLimitResponse
from baiducloud_python_sdk_apm.models.describe_service_config_response import DescribeServiceConfigResponse
from baiducloud_python_sdk_apm.models.describe_services_metrics_response import DescribeServicesMetricsResponse
from baiducloud_python_sdk_apm.models.describe_services_names_response import DescribeServicesNamesResponse
from baiducloud_python_sdk_apm.models.describe_span_field_values_response import DescribeSpanFieldValuesResponse
from baiducloud_python_sdk_apm.models.describe_spans_response import DescribeSpansResponse
from baiducloud_python_sdk_apm.models.describe_topology_response import DescribeTopologyResponse
from baiducloud_python_sdk_apm.models.describe_trace_response import DescribeTraceResponse
from baiducloud_python_sdk_apm.models.describe_trace_metric_data_response import DescribeTraceMetricDataResponse
from baiducloud_python_sdk_apm.models.update_service_config_response import UpdateServiceConfigResponse

_logger = logging.getLogger(__name__)


class ApmClient(BceBaseClient):
    """
    apm base sdk client
    """

    VERSION_V1 = b'/v1'

    CONSTANT_V1 = b'v1'

    CONSTANT_APM = b'apm'

    CONSTANT_QUERY = b'query'

    CONSTANT_ALARM = b'alarm'

    def __init__(self, config=None):
        """
        Initialize the apm client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def apm_create_alarm_policy(self, request, config=None):
        """
        apm_create_alarm_policy

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ApmCreateAlarmPolicyResponse data
        :rtype: ApmCreateAlarmPolicyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM)
        headers = None
        params = {}
        params['action'] = 'CreateAlarmPolicy'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=ApmCreateAlarmPolicyResponse,
        )

    def apm_delete_alarm_policy(self, request, config=None):
        """
        apm_delete_alarm_policy

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ApmDeleteAlarmPolicyResponse data
        :rtype: ApmDeleteAlarmPolicyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM)
        headers = None
        params = {}
        params['action'] = 'DeleteAlarmPolicy'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=ApmDeleteAlarmPolicyResponse,
        )

    def apm_describe_alarm(self, request, config=None):
        """
        apm_describe_alarm

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ApmDescribeAlarmResponse data
        :rtype: ApmDescribeAlarmResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM, ApmClient.CONSTANT_ALARM)
        headers = None
        params = {}
        params['action'] = 'DescribeAlarm'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=ApmDescribeAlarmResponse,
        )

    def apm_describe_alarm_policies(self, request, config=None):
        """
        apm_describe_alarm_policies

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ApmDescribeAlarmPoliciesResponse data
        :rtype: ApmDescribeAlarmPoliciesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM)
        headers = None
        params = {}
        params['action'] = 'DescribeAlarmPolicies'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=ApmDescribeAlarmPoliciesResponse,
        )

    def apm_describe_alarm_policy(self, request, config=None):
        """
        apm_describe_alarm_policy

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ApmDescribeAlarmPolicyResponse data
        :rtype: ApmDescribeAlarmPolicyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM)
        headers = None
        params = {}
        params['action'] = 'DescribeAlarmPolicy'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=ApmDescribeAlarmPolicyResponse,
        )

    def apm_describe_alarms(self, request, config=None):
        """
        apm_describe_alarms

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ApmDescribeAlarmsResponse data
        :rtype: ApmDescribeAlarmsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM, ApmClient.CONSTANT_ALARM)
        headers = None
        params = {}
        params['action'] = 'DescribeAlarms'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=ApmDescribeAlarmsResponse,
        )

    def apm_update_alarm_policy(self, request, config=None):
        """
        apm_update_alarm_policy

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ApmUpdateAlarmPolicyResponse data
        :rtype: ApmUpdateAlarmPolicyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM)
        headers = None
        params = {}
        params['action'] = 'UpdateAlarmPolicy'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=ApmUpdateAlarmPolicyResponse,
        )

    def apm_update_alarm_policy_action(self, request, config=None):
        """
        apm_update_alarm_policy_action

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ApmUpdateAlarmPolicyActionResponse data
        :rtype: ApmUpdateAlarmPolicyActionResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM)
        headers = None
        params = {}
        params['action'] = 'UpdateAlarmPolicyAction'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=ApmUpdateAlarmPolicyActionResponse,
        )

    def apm_update_alarm_policy_state(self, request, config=None):
        """
        apm_update_alarm_policy_state

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ApmUpdateAlarmPolicyStateResponse data
        :rtype: ApmUpdateAlarmPolicyStateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM)
        headers = None
        params = {}
        params['action'] = 'UpdateAlarmPolicyState'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=ApmUpdateAlarmPolicyStateResponse,
        )

    def bind_service_tag(self, request, config=None):
        """
        bind_service_tag

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BindServiceTagResponse data
        :rtype: BindServiceTagResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM)
        headers = None
        params = {}
        params['action'] = 'BindServiceTag'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=BindServiceTagResponse,
        )

    def delete_services(self, request, config=None):
        """
        delete_services

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DeleteServicesResponse data
        :rtype: DeleteServicesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM)
        headers = None
        params = {}
        params['action'] = 'DeleteServices'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DeleteServicesResponse,
        )

    def describe_db_statement(self, request, config=None):
        """
        describe_db_statement

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeDbStatementResponse data
        :rtype: DescribeDbStatementResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM, ApmClient.CONSTANT_QUERY)
        headers = None
        params = {}
        params['action'] = 'DescribeDbStatement'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeDbStatementResponse,
        )

    def describe_default_config(self, config=None):
        """
        describe_default_config
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeDefaultConfigResponse data
        :rtype: DescribeDefaultConfigResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM)
        headers = None
        params = {}
        params['action'] = 'DescribeDefaultConfig'
        return self._send_request(
            http_methods.POST, path=path, params=params, config=config, model=DescribeDefaultConfigResponse
        )

    def describe_dimension_values(self, request, config=None):
        """
        describe_dimension_values

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeDimensionValuesResponse data
        :rtype: DescribeDimensionValuesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM, ApmClient.CONSTANT_QUERY)
        headers = None
        params = {}
        params['action'] = 'DescribeDimensionValues'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeDimensionValuesResponse,
        )

    def describe_env(self, config=None):
        """
        describe_env
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeEnvResponse data
        :rtype: DescribeEnvResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM, ApmClient.CONSTANT_QUERY)
        headers = None
        params = {}
        params['action'] = 'DescribeEnv'
        return self._send_request(
            http_methods.POST, path=path, params=params, config=config, model=DescribeEnvResponse
        )

    def describe_exceptions(self, request, config=None):
        """
        describe_exceptions

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeExceptionsResponse data
        :rtype: DescribeExceptionsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM, ApmClient.CONSTANT_QUERY)
        headers = None
        params = {}
        params['action'] = 'DescribeExceptions'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeExceptionsResponse,
        )

    def describe_llm_dimension_values(self, request, config=None):
        """
        describe_llm_dimension_values

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeLLMDimensionValuesResponse data
        :rtype: DescribeLLMDimensionValuesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM, ApmClient.CONSTANT_QUERY)
        headers = None
        params = {}
        params['action'] = 'DescribeLLMDimensionValues'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeLLMDimensionValuesResponse,
        )

    def describe_llm_metric_data(self, request, config=None):
        """
        describe_llm_metric_data

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeLLMMetricDataResponse data
        :rtype: DescribeLLMMetricDataResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM, ApmClient.CONSTANT_QUERY)
        headers = None
        params = {}
        params['action'] = 'DescribeLLMMetricData'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeLLMMetricDataResponse,
        )

    def describe_llm_services(self, request, config=None):
        """
        describe_llm_services

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeLLMServicesResponse data
        :rtype: DescribeLLMServicesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM, ApmClient.CONSTANT_QUERY)
        headers = None
        params = {}
        params['action'] = 'DescribeLLMServices'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeLLMServicesResponse,
        )

    def describe_llm_session(self, request, config=None):
        """
        describe_llm_session

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeLLMSessionResponse data
        :rtype: DescribeLLMSessionResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM, ApmClient.CONSTANT_QUERY)
        headers = None
        params = {}
        params['action'] = 'DescribeLLMSession'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeLLMSessionResponse,
        )

    def describe_llm_sessions(self, request, config=None):
        """
        describe_llm_sessions

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeLLMSessionsResponse data
        :rtype: DescribeLLMSessionsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM, ApmClient.CONSTANT_QUERY)
        headers = None
        params = {}
        params['action'] = 'DescribeLLMSessions'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeLLMSessionsResponse,
        )

    def describe_llm_sessions_statistics(self, request, config=None):
        """
        describe_llm_sessions_statistics

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeLLMSessionsStatisticsResponse data
        :rtype: DescribeLLMSessionsStatisticsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM, ApmClient.CONSTANT_QUERY)
        headers = None
        params = {}
        params['action'] = 'DescribeLLMSessionsStatistics'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeLLMSessionsStatisticsResponse,
        )

    def describe_llm_spans(self, request, config=None):
        """
        describe_llm_spans

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeLLMSpansResponse data
        :rtype: DescribeLLMSpansResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM, ApmClient.CONSTANT_QUERY)
        headers = None
        params = {}
        params['action'] = 'DescribeLLMSpans'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeLLMSpansResponse,
        )

    def describe_llm_trace(self, request, config=None):
        """
        describe_llm_trace

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeLLMTraceResponse data
        :rtype: DescribeLLMTraceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM, ApmClient.CONSTANT_QUERY)
        headers = None
        params = {}
        params['action'] = 'DescribeLLMTrace'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeLLMTraceResponse,
        )

    def describe_llm_traces(self, request, config=None):
        """
        describe_llm_traces

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeLLMTracesResponse data
        :rtype: DescribeLLMTracesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM, ApmClient.CONSTANT_QUERY)
        headers = None
        params = {}
        params['action'] = 'DescribeLLMTraces'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeLLMTracesResponse,
        )

    def describe_llm_traces_statistics(self, request, config=None):
        """
        describe_llm_traces_statistics

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeLLMTracesStatisticsResponse data
        :rtype: DescribeLLMTracesStatisticsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM, ApmClient.CONSTANT_QUERY)
        headers = None
        params = {}
        params['action'] = 'DescribeLLMTracesStatistics'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeLLMTracesStatisticsResponse,
        )

    def describe_metric_data(self, request, config=None):
        """
        describe_metric_data

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeMetricDataResponse data
        :rtype: DescribeMetricDataResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM, ApmClient.CONSTANT_QUERY)
        headers = None
        params = {}
        params['action'] = 'DescribeMetricData'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeMetricDataResponse,
        )

    def describe_retention_limit(self, config=None):
        """
        describe_retention_limit
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeRetentionLimitResponse data
        :rtype: DescribeRetentionLimitResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM)
        headers = None
        params = {}
        params['action'] = 'DescribeRetentionLimit'
        return self._send_request(
            http_methods.POST, path=path, params=params, config=config, model=DescribeRetentionLimitResponse
        )

    def describe_service_config(self, request, config=None):
        """
        describe_service_config

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeServiceConfigResponse data
        :rtype: DescribeServiceConfigResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM)
        headers = None
        params = {}
        params['action'] = 'DescribeServiceConfig'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeServiceConfigResponse,
        )

    def describe_services_metrics(self, request, config=None):
        """
        describe_services_metrics

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeServicesMetricsResponse data
        :rtype: DescribeServicesMetricsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM, ApmClient.CONSTANT_QUERY)
        headers = None
        params = {}
        params['action'] = 'DescribeServicesMetrics'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeServicesMetricsResponse,
        )

    def describe_services_names(self, request, config=None):
        """
        describe_services_names

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeServicesNamesResponse data
        :rtype: DescribeServicesNamesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM, ApmClient.CONSTANT_QUERY)
        headers = None
        params = {}
        params['action'] = 'DescribeServicesNames'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeServicesNamesResponse,
        )

    def describe_span_field_values(self, request, config=None):
        """
        describe_span_field_values

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeSpanFieldValuesResponse data
        :rtype: DescribeSpanFieldValuesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM, ApmClient.CONSTANT_QUERY)
        headers = None
        params = {}
        params['action'] = 'DescribeSpanFieldValues'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeSpanFieldValuesResponse,
        )

    def describe_spans(self, request, config=None):
        """
        describe_spans

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeSpansResponse data
        :rtype: DescribeSpansResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM, ApmClient.CONSTANT_QUERY)
        headers = None
        params = {}
        params['action'] = 'DescribeSpans'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeSpansResponse,
        )

    def describe_topology(self, request, config=None):
        """
        describe_topology

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeTopologyResponse data
        :rtype: DescribeTopologyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM, ApmClient.CONSTANT_QUERY)
        headers = None
        params = {}
        params['action'] = 'DescribeTopology'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeTopologyResponse,
        )

    def describe_trace(self, request, config=None):
        """
        describe_trace

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeTraceResponse data
        :rtype: DescribeTraceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM, ApmClient.CONSTANT_QUERY)
        headers = None
        params = {}
        params['action'] = 'DescribeTrace'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeTraceResponse,
        )

    def describe_trace_metric_data(self, request, config=None):
        """
        describe_trace_metric_data

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeTraceMetricDataResponse data
        :rtype: DescribeTraceMetricDataResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM, ApmClient.CONSTANT_QUERY)
        headers = None
        params = {}
        params['action'] = 'DescribeTraceMetricData'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeTraceMetricDataResponse,
        )

    def update_service_config(self, request, config=None):
        """
        update_service_config

        :param request: Request entity containing all parameters
        :type request: ApmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UpdateServiceConfigResponse data
        :rtype: UpdateServiceConfigResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', ApmClient.CONSTANT_V1, ApmClient.CONSTANT_APM)
        headers = None
        params = {}
        params['action'] = 'UpdateServiceConfig'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=UpdateServiceConfigResponse,
        )

    def _merge_config(self, config=None):
        """
        :param config:
        :type config: baiducloud_python_sdk_core.BceClientConfiguration
        """
        if config is None:
            return self.config
        else:
            new_config = copy.copy(self.config)
            new_config.merge_non_none_values(config)
            return new_config

    def _send_request(
        self, http_method, path, body=None, headers=None, params=None, config=None, body_parser=None, model=None
    ):
        """
        Send an HTTP request to the service endpoint.

        :param http_method: HTTP method (GET, POST, PUT, DELETE, etc.)
        :type http_method: bytes
        :param path: Request path
        :type path: bytes
        :param body: Optional request body
        :type body: str or bytes
        :param headers: Optional HTTP headers
        :type headers: dict
        :param params: Optional query parameters
        :type params: dict
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration
        :param body_parser: Optional custom body parser function
        :type body_parser: callable
        :param model: Optional response model class for deserialization
        :type model: class

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network connection failure, SSL errors, etc.)
        :raises BceServerError: Server returned error response
        """
        config = self._merge_config(config)
        if body_parser is None:
            body_parser = handler.parse_json
        if headers is None:
            headers = {b'Accept': b'*/*', b'Content-Type': b'application/json;charset=utf-8'}
        return bce_http_client.send_request(
            config,
            bce_v1_signer.sign,
            [handler.parse_error, body_parser],
            http_method,
            path,
            body,
            headers,
            params,
            model=model,
        )
