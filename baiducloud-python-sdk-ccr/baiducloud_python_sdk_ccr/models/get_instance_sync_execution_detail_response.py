"""
Request entity for GetInstanceSyncExecutionDetailResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class GetInstanceSyncExecutionDetailResponse(BceResponse):
    """
    GetInstanceSyncExecutionDetailResponse
    """

    def __init__(
        self,
        end_time=None,
        failed=None,
        id=None,
        in_progress=None,
        policy_id=None,
        start_time=None,
        status=None,
        status_text=None,
        stopped=None,
        succeed=None,
        total=None,
        trigger=None,
    ):
        """
        Initialize GetInstanceSyncExecutionDetailResponse response.

        :param end_time: 结束时间
        :type end_time: str (optional)

        :param failed: 执行失败的次数
        :type failed: int (optional)

        :param id: 执行任务ID
        :type id: int (optional)

        :param in_progress: 正在进行的任务数量
        :type in_progress: int (optional)

        :param policy_id: 执行任务所属的规则ID
        :type policy_id: int (optional)

        :param start_time: 开始时间
        :type start_time: str (optional)

        :param status: 执行状态
        :type status: str (optional)

        :param status_text: 状态文本
        :type status_text: str (optional)

        :param stopped: 停止执行的计数
        :type stopped: int (optional)

        :param succeed: 成功执行的计数
        :type succeed: int (optional)

        :param total: 所有执行的计数
        :type total: int (optional)

        :param trigger: 触发方式
        :type trigger: str (optional)
        """
        super().__init__()
        self.end_time = end_time
        self.failed = failed
        self.id = id
        self.in_progress = in_progress
        self.policy_id = policy_id
        self.start_time = start_time
        self.status = status
        self.status_text = status_text
        self.stopped = stopped
        self.succeed = succeed
        self.total = total
        self.trigger = trigger

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
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.failed is not None:
            result['failed'] = self.failed
        if self.id is not None:
            result['id'] = self.id
        if self.in_progress is not None:
            result['inProgress'] = self.in_progress
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.status_text is not None:
            result['statusText'] = self.status_text
        if self.stopped is not None:
            result['stopped'] = self.stopped
        if self.succeed is not None:
            result['succeed'] = self.succeed
        if self.total is not None:
            result['total'] = self.total
        if self.trigger is not None:
            result['trigger'] = self.trigger
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetInstanceSyncExecutionDetailResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('failed') is not None:
            self.failed = m.get('failed')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('inProgress') is not None:
            self.in_progress = m.get('inProgress')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusText') is not None:
            self.status_text = m.get('statusText')
        if m.get('stopped') is not None:
            self.stopped = m.get('stopped')
        if m.get('succeed') is not None:
            self.succeed = m.get('succeed')
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('trigger') is not None:
            self.trigger = m.get('trigger')
        return self
