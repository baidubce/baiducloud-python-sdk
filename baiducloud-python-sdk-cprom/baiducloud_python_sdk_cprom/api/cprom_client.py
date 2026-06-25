"""
Example for cprom client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.auth import bce_v1_signer
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_cprom.models.bind_cluster_response import BindClusterResponse
from baiducloud_python_sdk_cprom.models.claim_alert_event_response import ClaimAlertEventResponse
from baiducloud_python_sdk_cprom.models.create_alert_response import CreateAlertResponse
from baiducloud_python_sdk_cprom.models.create_custom_scrape_task_response import CreateCustomScrapeTaskResponse
from baiducloud_python_sdk_cprom.models.create_notification_policy_response import CreateNotificationPolicyResponse
from baiducloud_python_sdk_cprom.models.create_podmonitor_response import CreatePodmonitorResponse
from baiducloud_python_sdk_cprom.models.create_service_monitor_response import CreateServiceMonitorResponse
from baiducloud_python_sdk_cprom.models.get_alert_detail_response import GetAlertDetailResponse
from baiducloud_python_sdk_cprom.models.get_alert_event_detail_response import GetAlertEventDetailResponse
from baiducloud_python_sdk_cprom.models.get_cluster_bind_status_response import GetClusterBindStatusResponse
from baiducloud_python_sdk_cprom.models.get_notification_policy_response import GetNotificationPolicyResponse
from baiducloud_python_sdk_cprom.models.list_alert_events_response import ListAlertEventsResponse
from baiducloud_python_sdk_cprom.models.list_alert_templates_response import ListAlertTemplatesResponse
from baiducloud_python_sdk_cprom.models.list_alerts_response import ListAlertsResponse
from baiducloud_python_sdk_cprom.models.list_bindable_cloud_products_response import ListBindableCloudProductsResponse
from baiducloud_python_sdk_cprom.models.list_instances_response import ListInstancesResponse
from baiducloud_python_sdk_cprom.models.list_notification_policies_response import ListNotificationPoliciesResponse
from baiducloud_python_sdk_cprom.models.list_pod_monitors_response import ListPodMonitorsResponse
from baiducloud_python_sdk_cprom.models.list_related_cloud_products_response import ListRelatedCloudProductsResponse
from baiducloud_python_sdk_cprom.models.list_service_monitors_response import ListServiceMonitorsResponse
from baiducloud_python_sdk_cprom.models.remote_read_response import RemoteReadResponse

_logger = logging.getLogger(__name__)


class CpromClient(BceBaseClient):
    """
    cprom base sdk client
    """

    CONSTANT_V2 = b'v2'

    CONSTANT_NOTIFY_RULE = b'notify_rule'

    CONSTANT_BCM_SCOPES = b'bcm_scopes'

    CONSTANT_INSTANCE = b'instance'

    CONSTANT_SERVICE_MONITOR = b'service_monitor'

    CONSTANT_ALERTING_RULE = b'alerting_rule'

    CONSTANT_POD_MONITOR = b'pod_monitor'

    CONSTANT_SCRAPE_JOB = b'scrape_job'

    CONSTANT_BCM_JOB = b'bcm_job'

    CONSTANT_SCOPES = b'scopes'

    CONSTANT_POD_MONITOR_SERVICE = b'pod_monitor_service'

    CONSTANT_EVENT = b'event'

    CONSTANT_CLAIM = b'claim'

    CONSTANT_PROMETHEUS = b'prometheus'

    CONSTANT_API = b'api'

    CONSTANT_V1 = b'v1'

    CONSTANT_QUERY_RANGE = b'query_range'

    CONSTANT_TOKEN = b'token'

    CONSTANT_CLUSTER_BINDING = b'cluster_binding'

    CONSTANT_WRITE = b'write'

    CONSTANT_ALERTING_RULE_TEMPLATE = b'alerting_rule_template'

    def __init__(self, config=None):
        """
        Initialize the cprom client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def bind_cluster(self, request, config=None):
        """
        bind_cluster

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BindClusterResponse data
        :rtype: BindClusterResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_INSTANCE, request.instance_id)
        headers = None
        params = {}
        if request.action is not None:
            params['action'] = request.action
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=BindClusterResponse,
        )

    def claim_alert_event(self, request, config=None):
        """
        claim_alert_event

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ClaimAlertEventResponse data
        :rtype: ClaimAlertEventResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_EVENT, CpromClient.CONSTANT_CLAIM)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=ClaimAlertEventResponse,
        )

    def create_alert(self, request, config=None):
        """
        create_alert

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateAlertResponse data
        :rtype: CreateAlertResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_ALERTING_RULE)
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateAlertResponse,
        )

    def create_custom_scrape_task(self, request, config=None):
        """
        create_custom_scrape_task

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateCustomScrapeTaskResponse data
        :rtype: CreateCustomScrapeTaskResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_SCRAPE_JOB)
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.agent_id is not None:
            params['agentId'] = request.agent_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateCustomScrapeTaskResponse,
        )

    def create_instance(self, request, config=None):
        """
        create_instance

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_INSTANCE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, body=request.to_json_string(), config=merged_config)

    def create_notification_policy(self, request, config=None):
        """
        create_notification_policy

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateNotificationPolicyResponse data
        :rtype: CreateNotificationPolicyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_NOTIFY_RULE)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CreateNotificationPolicyResponse,
        )

    def create_podmonitor(self, request, config=None):
        """
        create_podmonitor

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreatePodmonitorResponse data
        :rtype: CreatePodmonitorResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_POD_MONITOR)
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.agent_id is not None:
            params['agentId'] = request.agent_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreatePodmonitorResponse,
        )

    def create_service_monitor(self, request, config=None):
        """
        create_service_monitor

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateServiceMonitorResponse data
        :rtype: CreateServiceMonitorResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_SERVICE_MONITOR)
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.agent_id is not None:
            params['agentId'] = request.agent_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateServiceMonitorResponse,
        )

    def delete_alert(self, request, config=None):
        """
        delete_alert

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_ALERTING_RULE, request.alerting_rule_id
        )
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_custom_scrape_task(self, request, config=None):
        """
        delete_custom_scrape_task

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_SCRAPE_JOB, request.scrape_job_id)
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.agent_id is not None:
            params['agentId'] = request.agent_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_instance(self, request, config=None):
        """
        delete_instance

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_INSTANCE, request.instance_id)
        headers = None
        params = {}
        if request.delete_grafana is not None:
            params['deleteGrafana'] = request.delete_grafana
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_notification_policy(self, request, config=None):
        """
        delete_notification_policy

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_NOTIFY_RULE, request.notify_rule_id
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, config=merged_config)

    def delete_podmonitor(self, request, config=None):
        """
        delete_podmonitor

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_POD_MONITOR, request.pod_monitor_name
        )
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.agent_id is not None:
            params['agentId'] = request.agent_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def delete_service_monitor(self, request, config=None):
        """
        delete_service_monitor

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_SERVICE_MONITOR, request.service_monitor_name
        )
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.agent_id is not None:
            params['agentId'] = request.agent_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.DELETE, path=path, params=params, config=merged_config)

    def generate_instance_token(self, request, config=None):
        """
        generate_instance_token

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CpromClient.CONSTANT_V2,
            CpromClient.CONSTANT_INSTANCE,
            request.instance_id,
            CpromClient.CONSTANT_TOKEN,
        )
        headers = None
        params = {}
        if request.action is not None:
            params['Action'] = request.action
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def get_alert_detail(self, request, config=None):
        """
        get_alert_detail

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetAlertDetailResponse data
        :rtype: GetAlertDetailResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_ALERTING_RULE, request.alerting_rule_id
        )
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetAlertDetailResponse
        )

    def get_alert_event_detail(self, request, config=None):
        """
        get_alert_event_detail

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetAlertEventDetailResponse data
        :rtype: GetAlertEventDetailResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_EVENT, request.event_id)
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.GET, path=path, config=merged_config, model=GetAlertEventDetailResponse)

    def get_cluster_bind_status(self, request, config=None):
        """
        get_cluster_bind_status

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetClusterBindStatusResponse data
        :rtype: GetClusterBindStatusResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_CLUSTER_BINDING)
        headers = None
        params = {}
        if request.cluster_id is not None:
            params['clusterId'] = request.cluster_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetClusterBindStatusResponse
        )

    def get_notification_policy(self, request, config=None):
        """
        get_notification_policy

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetNotificationPolicyResponse data
        :rtype: GetNotificationPolicyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_NOTIFY_RULE, request.notify_rule_id
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, config=merged_config, model=GetNotificationPolicyResponse
        )

    def list_alert_events(self, request, config=None):
        """
        list_alert_events

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListAlertEventsResponse data
        :rtype: ListAlertEventsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_EVENT)
        headers = None
        params = {}
        if request.start_time is not None:
            params['startTime'] = request.start_time
        if request.end_time is not None:
            params['endTime'] = request.end_time
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        if request.monitor_instance_id is not None:
            params['monitorInstanceId'] = request.monitor_instance_id
        if request.alerting_rule_id is not None:
            params['alertingRuleId'] = request.alerting_rule_id
        if request.alerting_rule_name is not None:
            params['alertingRuleName'] = request.alerting_rule_name
        if request.notify_rule_id is not None:
            params['notifyRuleId'] = request.notify_rule_id
        if request.notify_rule_name is not None:
            params['notifyRuleName'] = request.notify_rule_name
        if request.severity is not None:
            params['severity'] = request.severity
        if request.status is not None:
            params['status'] = request.status
        if request.expr is not None:
            params['expr'] = request.expr
        if request.order_by is not None:
            params['orderBy'] = request.order_by
        if request.order is not None:
            params['order'] = request.order
        if request.alarm_tags is not None:
            params['alarmTags'] = request.alarm_tags
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListAlertEventsResponse
        )

    def list_alert_templates(self, config=None):
        """
        list_alert_templates
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListAlertTemplatesResponse data
        :rtype: ListAlertTemplatesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_ALERTING_RULE_TEMPLATE)
        headers = None
        return self._send_request(http_methods.GET, path=path, config=config, model=ListAlertTemplatesResponse)

    def list_alerts(self, request, config=None):
        """
        list_alerts

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListAlertsResponse data
        :rtype: ListAlertsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_ALERTING_RULE)
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.keyword_type is not None:
            params['keywordType'] = request.keyword_type
        if request.keyword is not None:
            params['keyword'] = request.keyword
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListAlertsResponse
        )

    def list_bindable_cloud_products(self, config=None):
        """
        list_bindable_cloud_products
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListBindableCloudProductsResponse data
        :rtype: ListBindableCloudProductsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_BCM_SCOPES)
        headers = None
        return self._send_request(http_methods.GET, path=path, config=config, model=ListBindableCloudProductsResponse)

    def list_instances(self, request, config=None):
        """
        list_instances

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListInstancesResponse data
        :rtype: ListInstancesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_INSTANCE)
        headers = None
        params = {}
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.order_by is not None:
            params['orderBy'] = request.order_by
        if request.order is not None:
            params['order'] = request.order
        if request.phase is not None:
            params['phase'] = request.phase
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListInstancesResponse
        )

    def list_notification_policies(self, request, config=None):
        """
        list_notification_policies

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListNotificationPoliciesResponse data
        :rtype: ListNotificationPoliciesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_NOTIFY_RULE)
        headers = None
        params = {}
        params['pageNo'] = '1'
        params['pageSize'] = '10'
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.keyword_type is not None:
            params['keywordType'] = request.keyword_type
        if request.keyword is not None:
            params['keyword'] = request.keyword
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListNotificationPoliciesResponse
        )

    def list_pod_monitors(self, request, config=None):
        """
        list_pod_monitors

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListPodMonitorsResponse data
        :rtype: ListPodMonitorsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_POD_MONITOR)
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.agent_id is not None:
            params['agentId'] = request.agent_id
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        if request.keyword_type is not None:
            params['keywordType'] = request.keyword_type
        if request.keyword is not None:
            params['keyword'] = request.keyword
        if request.order_by is not None:
            params['orderBy'] = request.order_by
        if request.order is not None:
            params['order'] = request.order
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListPodMonitorsResponse
        )

    def list_related_cloud_products(self, request, config=None):
        """
        list_related_cloud_products

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListRelatedCloudProductsResponse data
        :rtype: ListRelatedCloudProductsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_BCM_JOB, CpromClient.CONSTANT_SCOPES
        )
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListRelatedCloudProductsResponse
        )

    def list_service_monitors(self, request, config=None):
        """
        list_service_monitors

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ListServiceMonitorsResponse data
        :rtype: ListServiceMonitorsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_SERVICE_MONITOR)
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.agent_id is not None:
            params['agentId'] = request.agent_id
        if request.page_no is not None:
            params['pageNo'] = request.page_no
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        if request.keyword_type is not None:
            params['keywordType'] = request.keyword_type
        if request.keyword is not None:
            params['keyword'] = request.keyword
        if request.order_by is not None:
            params['orderBy'] = request.order_by
        if request.order is not None:
            params['order'] = request.order
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=ListServiceMonitorsResponse
        )

    def remote_read(self, request, config=None):
        """
        remote_read

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing RemoteReadResponse data
        :rtype: RemoteReadResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CpromClient.CONSTANT_PROMETHEUS,
            CpromClient.CONSTANT_API,
            CpromClient.CONSTANT_V1,
            CpromClient.CONSTANT_QUERY_RANGE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), config=merged_config, model=RemoteReadResponse
        )

    def remote_write(self, request, config=None):
        """
        remote_write

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            CpromClient.CONSTANT_PROMETHEUS,
            CpromClient.CONSTANT_API,
            CpromClient.CONSTANT_V1,
            CpromClient.CONSTANT_WRITE,
        )
        headers = {}
        if request.content_type is not None:
            headers[b'Content-Type'] = str(request.content_type).encode('utf-8')
        if request.content_encoding is not None:
            headers[b'Content-Encoding'] = str(request.content_encoding).encode('utf-8')
        if request.instance_id is not None:
            headers[b'InstanceId'] = str(request.instance_id).encode('utf-8')
        if request.authorization is not None:
            headers[b'Authorization'] = str(request.authorization).encode('utf-8')
        body_stream = request.body
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=body_stream, headers=headers, config=merged_config
        )

    def toggle_pod_monitor_service(self, request, config=None):
        """
        toggle_pod_monitor_service

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_POD_MONITOR_SERVICE)
        headers = None
        params = {}
        if request.action is not None:
            params['action'] = request.action
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.agent_id is not None:
            params['agentId'] = request.agent_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def toggle_service_monitor_service(self, request, config=None):
        """
        toggle_service_monitor_service

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_SERVICE_MONITOR)
        headers = None
        params = {}
        if request.action is not None:
            params['action'] = request.action
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.agent_id is not None:
            params['agentId'] = request.agent_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, params=params, config=merged_config)

    def update_alert(self, request, config=None):
        """
        update_alert

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_ALERTING_RULE, request.alerting_rule_id
        )
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_notification_policy(self, request, config=None):
        """
        update_notification_policy

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_NOTIFY_RULE, request.notify_rule_id
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.PUT, path=path, body=request.to_json_string(), config=merged_config)

    def update_pod_monitor(self, request, config=None):
        """
        update_pod_monitor

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_POD_MONITOR, request.pod_monitor_name
        )
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.agent_id is not None:
            params['agentId'] = request.agent_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_related_cloud_products(self, request, config=None):
        """
        update_related_cloud_products

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_BCM_JOB, CpromClient.CONSTANT_SCOPES
        )
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def update_service_monitor(self, request, config=None):
        """
        update_service_monitor

        :param request: Request entity containing all parameters
        :type request: CpromClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/', CpromClient.CONSTANT_V2, CpromClient.CONSTANT_SERVICE_MONITOR, request.service_monitor_name
        )
        headers = None
        params = {}
        if request.instance_id is not None:
            params['instanceId'] = request.instance_id
        if request.agent_id is not None:
            params['agentId'] = request.agent_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.PUT, path=path, body=request.to_json_string(), params=params, config=merged_config
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
