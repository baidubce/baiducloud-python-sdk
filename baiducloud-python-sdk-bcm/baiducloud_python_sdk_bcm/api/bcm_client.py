"""
Example for bcm client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_core.util import request_body_utils
from baiducloud_python_sdk_bcm.models.add_alarm_policy_actions_response import AddAlarmPolicyActionsResponse
from baiducloud_python_sdk_bcm.models.create_alarm_masking_response import CreateAlarmMaskingResponse
from baiducloud_python_sdk_bcm.models.create_alarm_policy_response import CreateAlarmPolicyResponse
from baiducloud_python_sdk_bcm.models.create_alarm_template_response import CreateAlarmTemplateResponse
from baiducloud_python_sdk_bcm.models.create_instance_group_response import CreateInstanceGroupResponse
from baiducloud_python_sdk_bcm.models.create_notify_template_response import CreateNotifyTemplateResponse
from baiducloud_python_sdk_bcm.models.delete_alarm_maskings_response import DeleteAlarmMaskingsResponse
from baiducloud_python_sdk_bcm.models.delete_alarm_policies_response import DeleteAlarmPoliciesResponse
from baiducloud_python_sdk_bcm.models.delete_alarm_policy_actions_response import DeleteAlarmPolicyActionsResponse
from baiducloud_python_sdk_bcm.models.delete_alarm_templates_response import DeleteAlarmTemplatesResponse
from baiducloud_python_sdk_bcm.models.delete_instance_group_response import DeleteInstanceGroupResponse
from baiducloud_python_sdk_bcm.models.delete_instance_group_instances_response import (
    DeleteInstanceGroupInstancesResponse,
)
from baiducloud_python_sdk_bcm.models.delete_notify_template_response import DeleteNotifyTemplateResponse
from baiducloud_python_sdk_bcm.models.describe_alarm_response import DescribeAlarmResponse
from baiducloud_python_sdk_bcm.models.describe_alarm_masking_response import DescribeAlarmMaskingResponse
from baiducloud_python_sdk_bcm.models.describe_alarm_maskings_response import DescribeAlarmMaskingsResponse
from baiducloud_python_sdk_bcm.models.describe_alarm_policies_response import DescribeAlarmPoliciesResponse
from baiducloud_python_sdk_bcm.models.describe_alarm_policy_response import DescribeAlarmPolicyResponse
from baiducloud_python_sdk_bcm.models.describe_alarm_template_response import DescribeAlarmTemplateResponse
from baiducloud_python_sdk_bcm.models.describe_alarm_templates_response import DescribeAlarmTemplatesResponse
from baiducloud_python_sdk_bcm.models.describe_alarms_response import DescribeAlarmsResponse
from baiducloud_python_sdk_bcm.models.describe_dimension_values_response import DescribeDimensionValuesResponse
from baiducloud_python_sdk_bcm.models.describe_instance_group_response import DescribeInstanceGroupResponse
from baiducloud_python_sdk_bcm.models.describe_instance_groups_response import DescribeInstanceGroupsResponse
from baiducloud_python_sdk_bcm.models.describe_metric_catalogs_response import DescribeMetricCatalogsResponse
from baiducloud_python_sdk_bcm.models.describe_metric_data_response import DescribeMetricDataResponse
from baiducloud_python_sdk_bcm.models.describe_metric_data_latest_response import DescribeMetricDataLatestResponse
from baiducloud_python_sdk_bcm.models.describe_metric_data_latest_top_response import (
    DescribeMetricDataLatestTopResponse,
)
from baiducloud_python_sdk_bcm.models.describe_notify_template_response import DescribeNotifyTemplateResponse
from baiducloud_python_sdk_bcm.models.describe_notify_templates_response import DescribeNotifyTemplatesResponse
from baiducloud_python_sdk_bcm.models.describe_receivers_response import DescribeReceiversResponse
from baiducloud_python_sdk_bcm.models.describe_resource_catalogs_response import DescribeResourceCatalogsResponse
from baiducloud_python_sdk_bcm.models.describe_system_template_rules_response import (
    DescribeSystemTemplateRulesResponse,
)
from baiducloud_python_sdk_bcm.models.export_alarm_templates_response import ExportAlarmTemplatesResponse
from baiducloud_python_sdk_bcm.models.import_alarm_templates_response import ImportAlarmTemplatesResponse
from baiducloud_python_sdk_bcm.models.update_alarm_masking_response import UpdateAlarmMaskingResponse
from baiducloud_python_sdk_bcm.models.update_alarm_masking_states_response import UpdateAlarmMaskingStatesResponse
from baiducloud_python_sdk_bcm.models.update_alarm_policy_response import UpdateAlarmPolicyResponse
from baiducloud_python_sdk_bcm.models.update_alarm_policy_notify_enabled_response import (
    UpdateAlarmPolicyNotifyEnabledResponse,
)
from baiducloud_python_sdk_bcm.models.update_alarm_policy_state_response import UpdateAlarmPolicyStateResponse
from baiducloud_python_sdk_bcm.models.update_alarm_template_response import UpdateAlarmTemplateResponse
from baiducloud_python_sdk_bcm.models.update_instance_group_response import UpdateInstanceGroupResponse
from baiducloud_python_sdk_bcm.models.update_notify_template_response import UpdateNotifyTemplateResponse

_logger = logging.getLogger(__name__)


class BcmClient(BceBaseClient):
    """
    bcm base sdk client
    """

    CONSTANT_V3 = b'v3'

    CONSTANT_BCM = b'bcm'

    CONSTANT_AH = b'ah'

    CONSTANT_QUERY = b'query'

    def __init__(self, config=None):
        """
        Initialize the bcm client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def add_alarm_policy_actions(self, request, config=None):
        """
        add_alarm_policy_actions

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing AddAlarmPolicyActionsResponse data
        :rtype: AddAlarmPolicyActionsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'AddAlarmPolicyActions'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=AddAlarmPolicyActionsResponse,
        )

    def create_alarm_masking(self, request, config=None):
        """
        create_alarm_masking

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateAlarmMaskingResponse data
        :rtype: CreateAlarmMaskingResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'CreateAlarmMasking'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateAlarmMaskingResponse,
        )

    def create_alarm_policy(self, request, config=None):
        """
        create_alarm_policy

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateAlarmPolicyResponse data
        :rtype: CreateAlarmPolicyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
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
            model=CreateAlarmPolicyResponse,
        )

    def create_alarm_template(self, request, config=None):
        """
        create_alarm_template

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateAlarmTemplateResponse data
        :rtype: CreateAlarmTemplateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'CreateAlarmTemplate'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateAlarmTemplateResponse,
        )

    def create_instance_group(self, request, config=None):
        """
        create_instance_group

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateInstanceGroupResponse data
        :rtype: CreateInstanceGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'CreateInstanceGroup'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateInstanceGroupResponse,
        )

    def create_notify_template(self, request, config=None):
        """
        create_notify_template

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateNotifyTemplateResponse data
        :rtype: CreateNotifyTemplateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'CreateNotifyTemplate'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateNotifyTemplateResponse,
        )

    def delete_alarm_maskings(self, request, config=None):
        """
        delete_alarm_maskings

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DeleteAlarmMaskingsResponse data
        :rtype: DeleteAlarmMaskingsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'DeleteAlarmMaskings'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DeleteAlarmMaskingsResponse,
        )

    def delete_alarm_policies(self, request, config=None):
        """
        delete_alarm_policies

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DeleteAlarmPoliciesResponse data
        :rtype: DeleteAlarmPoliciesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'DeleteAlarmPolicies'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DeleteAlarmPoliciesResponse,
        )

    def delete_alarm_policy_actions(self, request, config=None):
        """
        delete_alarm_policy_actions

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DeleteAlarmPolicyActionsResponse data
        :rtype: DeleteAlarmPolicyActionsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'DeleteAlarmPolicyActions'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DeleteAlarmPolicyActionsResponse,
        )

    def delete_alarm_templates(self, request, config=None):
        """
        delete_alarm_templates

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DeleteAlarmTemplatesResponse data
        :rtype: DeleteAlarmTemplatesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'DeleteAlarmTemplates'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DeleteAlarmTemplatesResponse,
        )

    def delete_instance_group(self, request, config=None):
        """
        delete_instance_group

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DeleteInstanceGroupResponse data
        :rtype: DeleteInstanceGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'DeleteInstanceGroup'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DeleteInstanceGroupResponse,
        )

    def delete_instance_group_instances(self, request, config=None):
        """
        delete_instance_group_instances

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DeleteInstanceGroupInstancesResponse data
        :rtype: DeleteInstanceGroupInstancesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'DeleteInstanceGroupInstances'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DeleteInstanceGroupInstancesResponse,
        )

    def delete_notify_template(self, request, config=None):
        """
        delete_notify_template

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DeleteNotifyTemplateResponse data
        :rtype: DeleteNotifyTemplateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'DeleteNotifyTemplate'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DeleteNotifyTemplateResponse,
        )

    def describe_alarm(self, request, config=None):
        """
        describe_alarm

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeAlarmResponse data
        :rtype: DescribeAlarmResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM, BcmClient.CONSTANT_AH)
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
            model=DescribeAlarmResponse,
        )

    def describe_alarm_masking(self, request, config=None):
        """
        describe_alarm_masking

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeAlarmMaskingResponse data
        :rtype: DescribeAlarmMaskingResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'DescribeAlarmMasking'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeAlarmMaskingResponse,
        )

    def describe_alarm_maskings(self, request, config=None):
        """
        describe_alarm_maskings

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeAlarmMaskingsResponse data
        :rtype: DescribeAlarmMaskingsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'DescribeAlarmMaskings'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeAlarmMaskingsResponse,
        )

    def describe_alarm_policies(self, request, config=None):
        """
        describe_alarm_policies

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeAlarmPoliciesResponse data
        :rtype: DescribeAlarmPoliciesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
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
            model=DescribeAlarmPoliciesResponse,
        )

    def describe_alarm_policy(self, request, config=None):
        """
        describe_alarm_policy

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeAlarmPolicyResponse data
        :rtype: DescribeAlarmPolicyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
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
            model=DescribeAlarmPolicyResponse,
        )

    def describe_alarm_template(self, request, config=None):
        """
        describe_alarm_template

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeAlarmTemplateResponse data
        :rtype: DescribeAlarmTemplateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'DescribeAlarmTemplate'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeAlarmTemplateResponse,
        )

    def describe_alarm_templates(self, request, config=None):
        """
        describe_alarm_templates

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeAlarmTemplatesResponse data
        :rtype: DescribeAlarmTemplatesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'DescribeAlarmTemplates'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeAlarmTemplatesResponse,
        )

    def describe_alarms(self, request, config=None):
        """
        describe_alarms

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeAlarmsResponse data
        :rtype: DescribeAlarmsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM, BcmClient.CONSTANT_AH)
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
            model=DescribeAlarmsResponse,
        )

    def describe_dimension_values(self, request, config=None):
        """
        describe_dimension_values

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeDimensionValuesResponse data
        :rtype: DescribeDimensionValuesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM, BcmClient.CONSTANT_QUERY)
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

    def describe_instance_group(self, request, config=None):
        """
        describe_instance_group

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeInstanceGroupResponse data
        :rtype: DescribeInstanceGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'DescribeInstanceGroup'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeInstanceGroupResponse,
        )

    def describe_instance_groups(self, request, config=None):
        """
        describe_instance_groups

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeInstanceGroupsResponse data
        :rtype: DescribeInstanceGroupsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'DescribeInstanceGroups'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeInstanceGroupsResponse,
        )

    def describe_metric_catalogs(self, request, config=None):
        """
        describe_metric_catalogs

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeMetricCatalogsResponse data
        :rtype: DescribeMetricCatalogsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'DescribeMetricCatalogs'
        params['locale'] = 'zh-cn'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeMetricCatalogsResponse,
        )

    def describe_metric_data(self, request, config=None):
        """
        describe_metric_data

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeMetricDataResponse data
        :rtype: DescribeMetricDataResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM, BcmClient.CONSTANT_QUERY)
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

    def describe_metric_data_latest(self, request, config=None):
        """
        describe_metric_data_latest

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeMetricDataLatestResponse data
        :rtype: DescribeMetricDataLatestResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM, BcmClient.CONSTANT_QUERY)
        headers = None
        params = {}
        params['action'] = 'DescribeMetricDataLatest'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeMetricDataLatestResponse,
        )

    def describe_metric_data_latest_top(self, request, config=None):
        """
        describe_metric_data_latest_top

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeMetricDataLatestTopResponse data
        :rtype: DescribeMetricDataLatestTopResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM, BcmClient.CONSTANT_QUERY)
        headers = None
        params = {}
        params['action'] = 'DescribeMetricDataLatestTop'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeMetricDataLatestTopResponse,
        )

    def describe_notify_template(self, request, config=None):
        """
        describe_notify_template

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeNotifyTemplateResponse data
        :rtype: DescribeNotifyTemplateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'DescribeNotifyTemplate'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeNotifyTemplateResponse,
        )

    def describe_notify_templates(self, request, config=None):
        """
        describe_notify_templates

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeNotifyTemplatesResponse data
        :rtype: DescribeNotifyTemplatesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'DescribeNotifyTemplates'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeNotifyTemplatesResponse,
        )

    def describe_receivers(self, request, config=None):
        """
        describe_receivers

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeReceiversResponse data
        :rtype: DescribeReceiversResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'DescribeReceivers'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeReceiversResponse,
        )

    def describe_resource_catalogs(self, request, config=None):
        """
        describe_resource_catalogs

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeResourceCatalogsResponse data
        :rtype: DescribeResourceCatalogsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'DescribeResourceCatalogs'
        params['locale'] = 'zh-cn'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, params=params, config=merged_config, model=DescribeResourceCatalogsResponse
        )

    def describe_system_template_rules(self, request, config=None):
        """
        describe_system_template_rules

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeSystemTemplateRulesResponse data
        :rtype: DescribeSystemTemplateRulesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'DescribeSystemTemplateRules'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=DescribeSystemTemplateRulesResponse,
        )

    def export_alarm_templates(self, request, config=None):
        """
        export_alarm_templates

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ExportAlarmTemplatesResponse data
        :rtype: ExportAlarmTemplatesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'ExportAlarmTemplates'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=ExportAlarmTemplatesResponse,
        )

    def import_alarm_templates(self, request, config=None):
        """
        import_alarm_templates

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ImportAlarmTemplatesResponse data
        :rtype: ImportAlarmTemplatesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'ImportAlarmTemplates'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=ImportAlarmTemplatesResponse,
        )

    def update_alarm_masking(self, request, config=None):
        """
        update_alarm_masking

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UpdateAlarmMaskingResponse data
        :rtype: UpdateAlarmMaskingResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'UpdateAlarmMasking'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=UpdateAlarmMaskingResponse,
        )

    def update_alarm_masking_states(self, request, config=None):
        """
        update_alarm_masking_states

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UpdateAlarmMaskingStatesResponse data
        :rtype: UpdateAlarmMaskingStatesResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'UpdateAlarmMaskingStates'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=UpdateAlarmMaskingStatesResponse,
        )

    def update_alarm_policy(self, request, config=None):
        """
        update_alarm_policy

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UpdateAlarmPolicyResponse data
        :rtype: UpdateAlarmPolicyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
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
            model=UpdateAlarmPolicyResponse,
        )

    def update_alarm_policy_notify_enabled(self, request, config=None):
        """
        update_alarm_policy_notify_enabled

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UpdateAlarmPolicyNotifyEnabledResponse data
        :rtype: UpdateAlarmPolicyNotifyEnabledResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'UpdateAlarmPolicyNotifyEnabled'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=UpdateAlarmPolicyNotifyEnabledResponse,
        )

    def update_alarm_policy_state(self, request, config=None):
        """
        update_alarm_policy_state

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UpdateAlarmPolicyStateResponse data
        :rtype: UpdateAlarmPolicyStateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
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
            model=UpdateAlarmPolicyStateResponse,
        )

    def update_alarm_template(self, request, config=None):
        """
        update_alarm_template

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UpdateAlarmTemplateResponse data
        :rtype: UpdateAlarmTemplateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'UpdateAlarmTemplate'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=UpdateAlarmTemplateResponse,
        )

    def update_instance_group(self, request, config=None):
        """
        update_instance_group

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UpdateInstanceGroupResponse data
        :rtype: UpdateInstanceGroupResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'UpdateInstanceGroup'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=UpdateInstanceGroupResponse,
        )

    def update_notify_template(self, request, config=None):
        """
        update_notify_template

        :param request: Request entity containing all parameters
        :type request: BcmClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UpdateNotifyTemplateResponse data
        :rtype: UpdateNotifyTemplateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(b'/', BcmClient.CONSTANT_V3, BcmClient.CONSTANT_BCM)
        headers = None
        params = {}
        params['action'] = 'UpdateNotifyTemplate'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=UpdateNotifyTemplateResponse,
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
        sign_fn, params = self._choose_signer(config, params)
        return bce_http_client.send_request(
            config, sign_fn, [handler.parse_error, body_parser], http_method, path, body, headers, params, model=model
        )
