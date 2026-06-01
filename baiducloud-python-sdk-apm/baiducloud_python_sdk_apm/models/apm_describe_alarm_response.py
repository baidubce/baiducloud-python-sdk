"""
Request entity for ApmDescribeAlarmResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_apm.models.alarm_policy_detail import AlarmPolicyDetail


class ApmDescribeAlarmResponse(BceResponse):
    """
    ApmDescribeAlarmResponse
    """

    def __init__(
        self,
        success=None,
        code=None,
        message=None,
        id=None,
        start_time=None,
        end_time=None,
        duration=None,
        init_state=None,
        state=None,
        close_reason=None,
        current_value=None,
        monitor_object=None,
        policy=None,
    ):
        """
        Initialize ApmDescribeAlarmResponse response.

        :param success: 请求是否成功
        :type success: bool (optional)

        :param code: 状态码
        :type code: str (optional)

        :param message: 错误信息
        :type message: str (optional)

        :param id: 报警ID
        :type id: str (optional)

        :param start_time: 报警开始时间，UTC时间
        :type start_time: str (optional)

        :param end_time: 报警关闭时间，UTC时间，若报警未关闭该值为空字符串
        :type end_time: str (optional)

        :param duration: 报警持续时间，单位：分钟
        :type duration: int (optional)

        :param init_state: 初始报警状态，可选值：ALERT-报警中，NODATA-无数据报警
        :type init_state: str (optional)

        :param state: 报警状态，可选值：OK-已恢复，ALERT-报警中，NODATA-无数据报警，CLOSED-已关闭
        :type state: str (optional)

        :param close_reason: 报警关闭原因，可选值：POLICY_MODIFIED-报警策略更新
        :type close_reason: str (optional)

        :param current_value: 报警异常值
        :type current_value: str (optional)

        :param monitor_object: 异常资源信息
        :type monitor_object: str (optional)

        :param policy: policy field
        :type policy: AlarmPolicyDetail (optional)
        """
        super().__init__()
        self.success = success
        self.code = code
        self.message = message
        self.id = id
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration
        self.init_state = init_state
        self.state = state
        self.close_reason = close_reason
        self.current_value = current_value
        self.monitor_object = monitor_object
        self.policy = policy

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
        if self.success is not None:
            result['success'] = self.success
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.id is not None:
            result['id'] = self.id
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.duration is not None:
            result['duration'] = self.duration
        if self.init_state is not None:
            result['initState'] = self.init_state
        if self.state is not None:
            result['state'] = self.state
        if self.close_reason is not None:
            result['closeReason'] = self.close_reason
        if self.current_value is not None:
            result['currentValue'] = self.current_value
        if self.monitor_object is not None:
            result['monitorObject'] = self.monitor_object
        if self.policy is not None:
            result['policy'] = self.policy.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ApmDescribeAlarmResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('initState') is not None:
            self.init_state = m.get('initState')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('closeReason') is not None:
            self.close_reason = m.get('closeReason')
        if m.get('currentValue') is not None:
            self.current_value = m.get('currentValue')
        if m.get('monitorObject') is not None:
            self.monitor_object = m.get('monitorObject')
        if m.get('policy') is not None:
            self.policy = AlarmPolicyDetail().from_dict(m.get('policy'))
        return self
