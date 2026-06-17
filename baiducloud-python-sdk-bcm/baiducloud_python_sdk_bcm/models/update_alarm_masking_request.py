"""
Request entity for UpdateAlarmMaskingRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcm.models.target_instance import TargetInstance


class UpdateAlarmMaskingRequest(AbstractModel):
    """
    Request entity for UpdateAlarmMaskingRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        id,
        state,
        name,
        scope,
        resource_type,
        instances,
        region,
        policy_id=None,
        metric_names=None,
        period_type=None,
        begin_time=None,
        end_time=None,
        tz=None,
        daily_begin_timestamp=None,
        daily_end_timestamp=None,
    ):
        """
        Initialize UpdateAlarmMaskingRequest request entity.

        :param id: 屏蔽规则ID
        :type id: str (required)

        :param state: 屏蔽规则状态，可选ENABLED/DISABLED
        :type state: str (required)

        :param name: 屏蔽规则名称
        :type name: str (required)

        :param scope: 云产品命名空间
        :type scope: str (required)

        :param resource_type: 资源类型
        :type resource_type: str (required)

        :param policy_id: 报警策略ID
        :type policy_id: str (optional)

        :param instances: 屏蔽的实例列表
        :type instances: List[TargetInstance] (required)

        :param region: 地域
        :type region: str (required)

        :param metric_names: 屏蔽的指标名称列表
        :type metric_names: List[str] (optional)

        :param period_type: 屏蔽时间类型，默认FOREVER，可选FOREVER/FIXED/RELATIVE
        :type period_type: str (optional)

        :param begin_time: 屏蔽开始时间，periodType为FIXED时必填
        :type begin_time: str (optional)

        :param end_time: 屏蔽结束时间，periodType为FIXED时必填
        :type end_time: str (optional)

        :param tz: 时区
        :type tz: str (optional)

        :param daily_begin_timestamp: 每日屏蔽开始时间戳，periodType为RELATIVE时必填
        :type daily_begin_timestamp: int (optional)

        :param daily_end_timestamp: 每日屏蔽结束时间戳，periodType为RELATIVE时必填
        :type daily_end_timestamp: int (optional)
        """
        super().__init__()
        self.id = id
        self.state = state
        self.name = name
        self.scope = scope
        self.resource_type = resource_type
        self.policy_id = policy_id
        self.instances = instances
        self.region = region
        self.metric_names = metric_names
        self.period_type = period_type
        self.begin_time = begin_time
        self.end_time = end_time
        self.tz = tz
        self.daily_begin_timestamp = daily_begin_timestamp
        self.daily_end_timestamp = daily_end_timestamp

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
        if self.id is not None:
            result['id'] = self.id
        if self.state is not None:
            result['state'] = self.state
        if self.name is not None:
            result['name'] = self.name
        if self.scope is not None:
            result['scope'] = self.scope
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        if self.instances is not None:
            result['instances'] = [i.to_dict() for i in self.instances]
        if self.region is not None:
            result['region'] = self.region
        if self.metric_names is not None:
            result['metricNames'] = self.metric_names
        if self.period_type is not None:
            result['periodType'] = self.period_type
        if self.begin_time is not None:
            result['beginTime'] = self.begin_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.tz is not None:
            result['tz'] = self.tz
        if self.daily_begin_timestamp is not None:
            result['dailyBeginTimestamp'] = self.daily_begin_timestamp
        if self.daily_end_timestamp is not None:
            result['dailyEndTimestamp'] = self.daily_end_timestamp
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateAlarmMaskingRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('instances') is not None:
            self.instances = [TargetInstance().from_dict(i) for i in m.get('instances')]
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('metricNames') is not None:
            self.metric_names = m.get('metricNames')
        if m.get('periodType') is not None:
            self.period_type = m.get('periodType')
        if m.get('beginTime') is not None:
            self.begin_time = m.get('beginTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('tz') is not None:
            self.tz = m.get('tz')
        if m.get('dailyBeginTimestamp') is not None:
            self.daily_begin_timestamp = m.get('dailyBeginTimestamp')
        if m.get('dailyEndTimestamp') is not None:
            self.daily_end_timestamp = m.get('dailyEndTimestamp')
        return self
