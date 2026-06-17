"""
ExecutionStats information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bls.models.log_store import LogStore

from baiducloud_python_sdk_bls.models.notice import Notice


class ExecutionStats(AbstractModel):
    """
    ExecutionStats
    """

    def __init__(
        self,
        policy_id=None,
        policy_name=None,
        objects=None,
        pending_count=None,
        repeat_interval_minute=None,
        notices=None,
        total_count=None,
        fail_count=None,
        notice_total_count=None,
        notice_fail_count=None,
    ):
        """
        Initialize ExecutionStats instance.

        :param policy_id: 报警策略ID
        :type policy_id: str (optional)

        :param policy_name: 报警策略名称
        :type policy_name: str (optional)

        :param objects: 监控对象
        :type objects: List[LogStore] (optional)

        :param pending_count: 连续触发阈值，连续多少次触发阈值则报警
        :type pending_count: int (optional)

        :param repeat_interval_minute: 重复报警间隔，单位：分钟，默认值：0，表示关闭重复报警
        :type repeat_interval_minute: int (optional)

        :param notices: notices attribute
        :type notices: List[Notice] (optional)

        :param total_count: 执行次数
        :type total_count: int (optional)

        :param fail_count: 执行失败次数
        :type fail_count: int (optional)

        :param notice_total_count: 通知次数
        :type notice_total_count: int (optional)

        :param notice_fail_count: 通知失败次数
        :type notice_fail_count: int (optional)
        """
        super().__init__()
        self.policy_id = policy_id
        self.policy_name = policy_name
        self.objects = objects
        self.pending_count = pending_count
        self.repeat_interval_minute = repeat_interval_minute
        self.notices = notices
        self.total_count = total_count
        self.fail_count = fail_count
        self.notice_total_count = notice_total_count
        self.notice_fail_count = notice_fail_count

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
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.objects is not None:
            result['objects'] = [i.to_dict() for i in self.objects]
        if self.pending_count is not None:
            result['pendingCount'] = self.pending_count
        if self.repeat_interval_minute is not None:
            result['repeatIntervalMinute'] = self.repeat_interval_minute
        if self.notices is not None:
            result['notices'] = [i.to_dict() for i in self.notices]
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.fail_count is not None:
            result['failCount'] = self.fail_count
        if self.notice_total_count is not None:
            result['noticeTotalCount'] = self.notice_total_count
        if self.notice_fail_count is not None:
            result['noticeFailCount'] = self.notice_fail_count
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ExecutionStats

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('objects') is not None:
            self.objects = [LogStore().from_dict(i) for i in m.get('objects')]
        if m.get('pendingCount') is not None:
            self.pending_count = m.get('pendingCount')
        if m.get('repeatIntervalMinute') is not None:
            self.repeat_interval_minute = m.get('repeatIntervalMinute')
        if m.get('notices') is not None:
            self.notices = [Notice().from_dict(i) for i in m.get('notices')]
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('failCount') is not None:
            self.fail_count = m.get('failCount')
        if m.get('noticeTotalCount') is not None:
            self.notice_total_count = m.get('noticeTotalCount')
        if m.get('noticeFailCount') is not None:
            self.notice_fail_count = m.get('noticeFailCount')
        return self
